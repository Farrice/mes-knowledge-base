const fs = require('fs');
const { google } = require('googleapis');
const readline = require('readline');

// Credential File Path
const CREDENTIALS_PATH = '/Users/farricecain/Downloads/client_secret_65050601772-5shkqvc6nphonjelkk388lmq30t7hoce.apps.googleusercontent.com.json';
// Using only Drive scope since Docs API is disabled
const SCOPES = ['https://www.googleapis.com/auth/drive.file'];

// File to Upload (The .docx file we created earlier)
const FILE_PATH = '/Users/farricecain/.gemini/antigravity/brain/14d123a9-aeb7-46b4-8bea-913a7084b80a/Josh_Banday_Fellowship_Complete_Strategy.docx';
const DOC_TITLE = 'Josh Banday: Fellowship Strategy 2026';

async function main() {
    const content = fs.readFileSync(CREDENTIALS_PATH);
    const credentials = JSON.parse(content);
    const { client_secret, client_id, redirect_uris } = credentials.installed;
    const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);

    getNewToken(oAuth2Client, uploadFile);
}

function getNewToken(oAuth2Client, callback) {
    const authUrl = oAuth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: SCOPES,
    });
    console.log('AUTHORIZE_URL_START');
    console.log(authUrl);
    console.log('AUTHORIZE_URL_END');

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    rl.question('Enter the code from that page here: ', (code) => {
        rl.close();
        oAuth2Client.getToken(code, (err, token) => {
            if (err) return console.error('Error retrieving access token', err);
            oAuth2Client.setCredentials(token);
            callback(oAuth2Client);
        });
    });
}

async function uploadFile(auth) {
    const drive = google.drive({ version: 'v3', auth });

    // Upload the .docx and ask Drive to convert it to a native Google Doc
    try {
        const res = await drive.files.create({
            requestBody: {
                name: DOC_TITLE,
                mimeType: 'application/vnd.google-apps.document', // Convert to Google Doc
            },
            media: {
                mimeType: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                body: fs.createReadStream(FILE_PATH),
            },
        });
        console.log(`UPLOAD_SUCCESS: https://docs.google.com/document/d/${res.data.id}/edit`);
    } catch (error) {
        console.error('Upload Failed', error);
    }
}

main();
