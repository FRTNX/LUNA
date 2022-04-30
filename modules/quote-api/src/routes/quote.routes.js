const express = require('express');
const quoteCtrl = require('../controllers/quote.controller');

const router = express.Router();

// router.route('/')
//     .post(quoteCtrl.create);
router.route('/quote')
    .get(quoteCtrl.read);

module.exports = router;
