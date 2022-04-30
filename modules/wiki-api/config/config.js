module.exports.config = {
    env: process.env.NODE_ENV || 'development',
    port: process.env.PORT || 4004,
    dbWikipediaUrl: 'http://127.0.0.1:5000/dbwiki',
    dbWikiSearchUrl: 'http://localhost:5000/wikisearch',
    dbWikiRandomListUrl:  'http://localhost:5000/wikirandomlist',
    request: { limit: '20mb' }
};
