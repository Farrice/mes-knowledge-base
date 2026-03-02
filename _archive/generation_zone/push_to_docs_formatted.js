const fs = require('fs');
const { google } = require('googleapis');
const readline = require('readline');

// Credential File Path
const CREDENTIALS_PATH = '/Users/farricecain/Downloads/client_secret_65050601772-5shkqvc6nphonjelkk388lmq30t7hoce.apps.googleusercontent.com.json';
const SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive'];

// File to read content from
const FILE_PATH = '/Users/farricecain/.gemini/antigravity/brain/14d123a9-aeb7-46b4-8bea-913a7084b80a/Josh_Banday_Fellowship_Complete_Strategy_Final.md';
const DOC_TITLE = 'Josh Banday: Fellowship Strategy 2026 (Complete)';

async function main() {
    const content = fs.readFileSync(CREDENTIALS_PATH);
    const credentials = JSON.parse(content);
    const { client_secret, client_id, redirect_uris } = credentials.installed;
    const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);

    getNewToken(oAuth2Client, createFormattedDoc);
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

// Parse markdown and create formatting requests
function parseMarkdownToRequests(markdown) {
    const lines = markdown.split('\n');
    const requests = [];
    let currentIndex = 1; // Docs API uses 1-based index

    for (const line of lines) {
        if (line.trim() === '' || line.trim() === '---') {
            // Add empty line
            const text = '\n';
            requests.push({
                insertText: {
                    location: { index: currentIndex },
                    text: text
                }
            });
            currentIndex += text.length;
            continue;
        }

        let text = line;
        let headingType = null;
        let isBold = false;
        let isItalic = false;
        let isBlockquote = false;

        // Detect heading level
        if (line.startsWith('# ')) {
            text = line.substring(2) + '\n';
            headingType = 'HEADING_1';
        } else if (line.startsWith('## ')) {
            text = line.substring(3) + '\n';
            headingType = 'HEADING_2';
        } else if (line.startsWith('### ')) {
            text = line.substring(4) + '\n';
            headingType = 'HEADING_3';
        } else if (line.startsWith('> ')) {
            text = line.substring(2) + '\n';
            isBlockquote = true;
        } else if (line.startsWith('|')) {
            // Table row - just insert as text for now
            text = line + '\n';
        } else {
            text = line + '\n';
        }

        // Insert the text
        requests.push({
            insertText: {
                location: { index: currentIndex },
                text: text
            }
        });

        const startIndex = currentIndex;
        const endIndex = currentIndex + text.length;

        // Apply heading style
        if (headingType) {
            requests.push({
                updateParagraphStyle: {
                    range: { startIndex, endIndex },
                    paragraphStyle: { namedStyleType: headingType },
                    fields: 'namedStyleType'
                }
            });
        }

        // Apply blockquote style (indent + italic)
        if (isBlockquote) {
            requests.push({
                updateParagraphStyle: {
                    range: { startIndex, endIndex },
                    paragraphStyle: {
                        indentFirstLine: { magnitude: 36, unit: 'PT' },
                        indentStart: { magnitude: 36, unit: 'PT' }
                    },
                    fields: 'indentFirstLine,indentStart'
                }
            });
            requests.push({
                updateTextStyle: {
                    range: { startIndex, endIndex: endIndex - 1 },
                    textStyle: { italic: true },
                    fields: 'italic'
                }
            });
        }

        // Find and format **bold** text
        const boldRegex = /\*\*(.+?)\*\*/g;
        let match;
        let cleanText = text;
        let offset = 0;

        // We need to track bold segments for later formatting
        // For simplicity in this version, we'll handle inline formatting in a second pass

        currentIndex = endIndex;
    }

    return requests;
}

async function createFormattedDoc(auth) {
    const docs = google.docs({ version: 'v1', auth });

    // Read the full markdown content
    const markdownContent = fs.readFileSync(FILE_PATH, 'utf8');

    try {
        // 1. Create a blank doc
        console.log('Creating document...');
        const createResponse = await docs.documents.create({
            requestBody: {
                title: DOC_TITLE,
            },
        });
        const documentId = createResponse.data.documentId;
        console.log(`Created Document ID: ${documentId}`);

        // 2. Parse markdown and build requests
        console.log('Parsing content...');
        const requests = parseMarkdownToRequests(markdownContent);

        // 3. Apply all formatting in batch
        console.log('Applying formatting...');
        await docs.documents.batchUpdate({
            documentId: documentId,
            requestBody: { requests },
        });

        console.log(`\nUPLOAD_SUCCESS: https://docs.google.com/document/d/${documentId}/edit`);
    } catch (error) {
        console.error('Error:', error.message);
        if (error.errors) {
            console.error('Details:', JSON.stringify(error.errors, null, 2));
        }
    }
}

main();
