module.exports.config = {
    env: process.env.NODE_ENV || 'development',
    port: process.env.PORT || 4001,
    request: { limit: '20mb' }
};
