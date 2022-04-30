const express = require('express');
const cmdCtrl = require('../controllers/cmd.controller');

const router = express.Router();

router.route('/router')
    .get(cmdCtrl.commandHandler);

router.route('/')
    .get((request, response) => {
        return response.json('OK');
    });

module.exports = router;
