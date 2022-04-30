const mongoose = require('mongoose');

const WikipediaSchema = new mongoose.Schema({
    text: String,
    images: {
        type: Array,
        default: []
    },
    created: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('Wikipedia', WikipediaSchema);
