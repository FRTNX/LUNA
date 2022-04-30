const { config } = require('./../../config/config');
const request = require('request-promise');

const read = async (req, response) => {
    try {
        const cmd = req.query.cmd;
        const documentTitle = cmd.split(' ').slice(1).reduce((str, word) => str + ' ' + word);
        // if (documentTitle.includes('-f')) {
        //     documentTitle.pop('-f');
        //     // set display setting
        // }
        const result = await request({
            uri: `${config.dbWikipediaUrl}?title=${documentTitle}`,
            method: 'GET'
        });

        return response.json(result);
    } catch (error) {
        console.log(error)
        return response.status('400').json({
            error: "Error processing request"
        });
    }
};

const searchLocalWiki = async (req, response) => {
    try {
        const cmd = req.query.cmd;
        const searchTerm = cmd.split(' ').slice(1).reduce((str, word) => str + ' ' + word);
        const result = await request({
            uri: `${config.dbWikiSearchUrl}?searchTerm=${searchTerm}`,
            method: 'GET'
        });

        return response.json(JSON.parse(result).message);
    } catch (error) {
        console.log(error)
        return response.status('400').json({
            error: "Error processing request"
        });
    }
};

const randomList = async (req, response) => {
    try {
        const result = await request({ uri: `${config.dbWikiRandomListUrl}`, method: 'GET' });
        return response.json(JSON.parse(result).message);
    } catch (error) {
        console.log(error)
        return response.status('400').json({
            error: "Error processing request"
        });
    }
};

module.exports = {
    read,
    searchLocalWiki,
    randomList
};
