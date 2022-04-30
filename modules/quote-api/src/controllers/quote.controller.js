const { config } = require('./../../config/config');
const request = require('request-promise');

const read = async (req, response) => {
    try {
        const result = await request({ uri: config.coreDbServerUrl, method: 'GET' });
        return response.json(result);
    } catch (error) {
        console.log(error)
        return response.status('400').json({
            error: "Could not retrieve user"
        });
    }
};

module.exports = {
    read
};
