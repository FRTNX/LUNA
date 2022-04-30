const mongoose = require('mongoose');

const QuoteShema = new mongoose.Schema({
    text: String,
    created: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('Quote', QuoteShema);
