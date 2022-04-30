const express = require('express');
const wikiCtrl = require('../controllers/wikipedia.controller');

const router = express.Router();

router.route('/wikipedia')
    .get(wikiCtrl.read);
    // implement post (and put)?

router.route('/wikisearch')
    .get(wikiCtrl.searchLocalWiki);

router.route('/wikirandomlist')
    .get(wikiCtrl.randomList)

router.route('/')
    .get((request, response) => {
        return response.json('OK');
    });

module.exports = router;
