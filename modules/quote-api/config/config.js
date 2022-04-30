module.exports.config = {
    env: process.env.NODE_ENV || 'development',
    port: process.env.PORT || 4003,
    coreDbServerUrl: 'http://127.0.0.1:5000/dbquote',
    request: { limit: '20mb' }
};
