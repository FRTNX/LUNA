const express = require('express');
const { config } = require('./../config/config');

const cookieParser = require('cookie-parser');
const compress = require('compression');
const cors = require('cors');
const helmet = require('helmet');

const quoteRoutes = require('./routes/quote.routes');

const app = express();

const logit = (request, response, next) => {
    console.log('Request recieved: ', request.method, request.url);
    next();
};

app.use(logit);

app.use(express.json({ limit: config.request.limit }));
app.use(express.urlencoded());

// app.use(bodyParser.json())
// app.use(bodyParser.urlencoded({ extended: true }))
app.use(cookieParser())
app.use(compress())
app.use(helmet())
app.use(cors())

app.use('/', quoteRoutes);



app.use('*', (request, response) => {
    response.status(404).json({ message: 'Resource not found'});
});

module.exports = app;
