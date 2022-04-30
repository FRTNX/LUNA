const { Client } = require('whatsapp-web.js');
const qrcode = require('qrcode');
const { exec } = require('child_process');

const client = new Client();

const displayImage = () => {
    exec("xdg-open image.png", (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });
}

client.on('qr', (qr) => {
    // Generate and scan this code with your phone
    console.log('QR RECEIVED', qr);
    qrcode.toFile('image.png', qr, {
        width: 300,
        height: 300
    }, function (err) {
        if (err) throw err;
        console.log('done');
    });
    displayImage();
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('message', msg => {
    if (msg.body == '!ping') {
        msg.reply('pong');
    }
});

client.initialize();
