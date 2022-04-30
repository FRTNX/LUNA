const { config } = require('./../config/config');
const app = require('./express');
const callApi = require('request-promise');

// const mongoose = require('mongoose');

// mongoose.Promise = global.Promise;
// mongoose.connect(config.mongoUri, { useNewUrlParser: true, useUnifiedTopology: true });

// mongoose.connection.on('error', () => {
//     throw new Error(`Unable to connect to database: ${config.mongoUri}`)
// });

const server = app.listen(config.port, (error) => {
    if (error) {
        console.log(error);
    }

    else {
        console.log(`Server running on http://localhost:${config.port}/`);
    }
});

const checkCommandApiStatus = async () => {
    try {
        await callApi({ uri: 'http://localhost:4001/', method: 'GET' });
    } catch (error) {
        server.close();
        process.exit(0)
    }
};


setInterval(checkCommandApiStatus, 60000);