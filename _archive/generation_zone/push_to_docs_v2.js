const fs = require('fs');
const { google } = require('googleapis');
const readline = require('readline');

const CREDENTIALS_PATH = '/Users/farricecain/Downloads/client_secret_65050601772-5shkqvc6nphonjelkk388lmq30t7hoce.apps.googleusercontent.com.json';
const SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive'];
const FILE_PATH = '/Users/farricecain/.gemini/antigravity/brain/14d123a9-aeb7-46b4-8bea-913a7084b80a/Josh_Banday_Fellowship_Complete_Strategy_Final.md';
const DOC_TITLE = 'Josh Banday: Fellowship Strategy 2026';

async function main() {
    const content = fs.readFileSync(CREDENTIALS_PATH);
    const credentials = JSON.parse(content);
    const { client_secret, client_id, redirect_uris } = credentials.installed;
    const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);
    getNewToken(oAuth2Client, createFormattedDoc);
}

function getNewToken(oAuth2Client, callback) {
    const authUrl = oAuth2Client.generateAuthUrl({ access_type: 'offline', scope: SCOPES });
    console.log('AUTHORIZE_URL_START');
    console.log(authUrl);
    console.log('AUTHORIZE_URL_END');
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    rl.question('Enter the code: ', (code) => {
        rl.close();
        oAuth2Client.getToken(code, (err, token) => {
            if (err) return console.error('Error:', err);
            oAuth2Client.setCredentials(token);
            callback(oAuth2Client);
        });
    });
}

// Comprehensive markdown to clean text + formatting requests
function convertMarkdownToDocsFormat(markdown) {
    const lines = markdown.split('\n');
    let cleanText = '';
    const formattingRequests = [];
    let currentIndex = 1;

    for (let line of lines) {
        // Skip horizontal rules
        if (line.trim() === '---') {
            cleanText += '\n';
            currentIndex += 1;
            continue;
        }

        let headingType = null;
        let isBlockquote = false;
        let isBullet = false;

        // Handle headings
        if (line.startsWith('# ')) {
            line = line.substring(2);
            headingType = 'HEADING_1';
        } else if (line.startsWith('## ')) {
            line = line.substring(3);
            headingType = 'HEADING_2';
        } else if (line.startsWith('### ')) {
            line = line.substring(4);
            headingType = 'HEADING_3';
        } else if (line.startsWith('> ')) {
            line = line.substring(2);
            isBlockquote = true;
        } else if (line.startsWith('*   ') || line.startsWith('-   ')) {
            line = '• ' + line.substring(4);
            isBullet = true;
        } else if (line.startsWith('1.  ')) {
            // Keep numbered lists as-is
        }

        // Find bold (**text**) and italics (*text*) positions BEFORE stripping
        const boldMatches = [];
        const italicMatches = [];

        // Find all **bold** segments
        let boldRegex = /\*\*(.+?)\*\*/g;
        let match;
        let processedLine = line;
        let offset = 0;

        // First pass: collect bold ranges
        while ((match = boldRegex.exec(line)) !== null) {
            const startInLine = match.index - offset;
            const innerText = match[1];
            boldMatches.push({
                start: currentIndex + startInLine,
                end: currentIndex + startInLine + innerText.length,
                text: innerText
            });
            offset += 4; // Remove 4 characters (** **)
        }

        // Strip bold markers
        processedLine = processedLine.replace(/\*\*(.+?)\*\*/g, '$1');

        // Find all *italic* segments (single asterisk, not inside bold)
        let italicRegex = /\*([^*]+?)\*/g;
        offset = 0;
        while ((match = italicRegex.exec(processedLine)) !== null) {
            const startInLine = match.index - offset;
            const innerText = match[1];
            italicMatches.push({
                start: currentIndex + startInLine,
                end: currentIndex + startInLine + innerText.length,
                text: innerText
            });
            offset += 2; // Remove 2 characters (* *)
        }

        // Strip italic markers
        processedLine = processedLine.replace(/\*([^*]+?)\*/g, '$1');

        // Add newline
        processedLine += '\n';

        const lineStart = currentIndex;
        const lineEnd = currentIndex + processedLine.length;

        // Add to clean text
        cleanText += processedLine;

        // Store heading formatting
        if (headingType) {
            formattingRequests.push({
                type: 'heading',
                start: lineStart,
                end: lineEnd,
                style: headingType
            });
        }

        // Store blockquote formatting
        if (isBlockquote) {
            formattingRequests.push({
                type: 'blockquote',
                start: lineStart,
                end: lineEnd
            });
        }

        // Store bullet formatting
        if (isBullet) {
            formattingRequests.push({
                type: 'indent',
                start: lineStart,
                end: lineEnd
            });
        }

        // Store bold formatting
        for (const b of boldMatches) {
            formattingRequests.push({
                type: 'bold',
                start: b.start,
                end: b.end
            });
        }

        // Store italic formatting (adjusted for bold removal)
        for (const i of italicMatches) {
            formattingRequests.push({
                type: 'italic',
                start: i.start,
                end: i.end
            });
        }

        currentIndex = lineEnd;
    }

    return { cleanText, formattingRequests };
}

function buildDocsApiRequests(cleanText, formattingRequests) {
    const requests = [];

    // First: insert all the clean text
    requests.push({
        insertText: {
            location: { index: 1 },
            text: cleanText
        }
    });

    // Then: apply formatting in reverse order (so indices stay valid)
    const sortedFormatting = formattingRequests.sort((a, b) => b.start - a.start);

    for (const fmt of sortedFormatting) {
        if (fmt.type === 'heading') {
            requests.push({
                updateParagraphStyle: {
                    range: { startIndex: fmt.start, endIndex: fmt.end },
                    paragraphStyle: { namedStyleType: fmt.style },
                    fields: 'namedStyleType'
                }
            });
        } else if (fmt.type === 'bold') {
            requests.push({
                updateTextStyle: {
                    range: { startIndex: fmt.start, endIndex: fmt.end },
                    textStyle: { bold: true },
                    fields: 'bold'
                }
            });
        } else if (fmt.type === 'italic') {
            requests.push({
                updateTextStyle: {
                    range: { startIndex: fmt.start, endIndex: fmt.end },
                    textStyle: { italic: true },
                    fields: 'italic'
                }
            });
        } else if (fmt.type === 'blockquote') {
            requests.push({
                updateParagraphStyle: {
                    range: { startIndex: fmt.start, endIndex: fmt.end },
                    paragraphStyle: {
                        indentFirstLine: { magnitude: 36, unit: 'PT' },
                        indentStart: { magnitude: 36, unit: 'PT' }
                    },
                    fields: 'indentFirstLine,indentStart'
                }
            });
            requests.push({
                updateTextStyle: {
                    range: { startIndex: fmt.start, endIndex: fmt.end - 1 },
                    textStyle: { italic: true },
                    fields: 'italic'
                }
            });
        } else if (fmt.type === 'indent') {
            requests.push({
                updateParagraphStyle: {
                    range: { startIndex: fmt.start, endIndex: fmt.end },
                    paragraphStyle: {
                        indentStart: { magnitude: 18, unit: 'PT' }
                    },
                    fields: 'indentStart'
                }
            });
        }
    }

    return requests;
}

async function createFormattedDoc(auth) {
    const docs = google.docs({ version: 'v1', auth });
    const markdownContent = fs.readFileSync(FILE_PATH, 'utf8');

    try {
        console.log('Creating document...');
        const createResponse = await docs.documents.create({
            requestBody: { title: DOC_TITLE }
        });
        const documentId = createResponse.data.documentId;
        console.log(`Created: ${documentId}`);

        console.log('Converting markdown...');
        const { cleanText, formattingRequests } = convertMarkdownToDocsFormat(markdownContent);

        console.log('Building API requests...');
        const requests = buildDocsApiRequests(cleanText, formattingRequests);

        console.log('Applying formatting...');
        await docs.documents.batchUpdate({
            documentId: documentId,
            requestBody: { requests }
        });

        console.log(`\nSUCCESS: https://docs.google.com/document/d/${documentId}/edit`);
    } catch (error) {
        console.error('Error:', error.message);
        if (error.errors) console.error(JSON.stringify(error.errors, null, 2));
    }
}

main();
