const fs = require('fs');

const fetchCommandPool = () => {
    let commandPool = {};

    const modules = fs.readdirSync('../');

    // ignore these modules. read from config in future
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
                            method: moduleConfig.commands[cmd].httpMethod,
                            displayStyle: moduleConfig.commands[cmd].displayStyle
                        }}
                    })
                });
            }
        }
    });

    console.log(commandPool)
    return commandPool;
}

createCmdFile();