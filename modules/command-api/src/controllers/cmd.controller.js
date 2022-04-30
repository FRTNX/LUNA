const request = require('request-promise');
const fs = require('fs');

const fetchCommandPool = () => {
    let commandPool = {};

    const modules = fs.readdirSync('../');

    // ignore these modules. read from config in future
    // apis that fail to meet performance benchmark will be ignored in future.
    const ignore = ['command-api'];
    modules.map((mod) => {
        if (!ignore.includes(mod)) {
            const moduleFiles = fs.readdirSync(`../${mod}/`);
            if (moduleFiles.includes('config.json')) {
                const moduleConfig = JSON.parse(fs.readFileSync(`../${mod}/config.json`));
                const commands = Object.keys(moduleConfig.commands);
                commands.map((cmd) => {
                    let triggers = moduleConfig.commands[cmd].triggers;
                    if (!triggers) triggers = []
                    triggers.push(cmd)
                    triggers.map((trigger) => {
                        commandPool = { ...commandPool, [trigger]: {
                            url: moduleConfig.base_url + moduleConfig.commands[cmd].endpoint,
                            httpMethod: moduleConfig.commands[cmd].httpMethod,
                            displayStyle: moduleConfig.commands[cmd].displayStyle,
                            displayIcon: moduleConfig.commands[cmd].displayIcon
                        }}
                    })
                });
            }
        }
    });

    return commandPool;
};


const commandHandler = async (req, response) => {
    try {
        const text = req.query.cmd;
        const cmd = text.split(' ')[0];
        const commandPool = fetchCommandPool();
        const commands = Object.keys(commandPool);

        if (commands.includes(cmd)) {
            const result = await request({ uri: `${commandPool[cmd].url}?cmd=${text}`, method: 'GET' });

            const responseObject = {
                text: JSON.parse(result),
                displayStyle: commandPool[cmd].displayStyle
            };

            if (commandPool[cmd].displayIcon) {
                responseObject.displayIcon = commandPool[cmd].displayIcon;
            }

            return response.json(responseObject);
        }
    
        const result = await request({
            uri: `${commandPool.aiml_converse.url}?text=${text}`,
            method: 'GET'
        });

        return response.json({ text: JSON.parse(result), displayStyle: 'matrix' });
    } catch (error) {
        console.log(error)
        return response.status('400').json({
            error: "Could not process command"
        });
    }
};

module.exports = {
    commandHandler
};
