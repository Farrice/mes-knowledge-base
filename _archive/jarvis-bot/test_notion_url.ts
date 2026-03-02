import { getNotionClient } from './src/integrations/notion.js';

async function test() {
    console.log("Testing Notion URL...");
    const notion = getNotionClient();
    if (!notion) return console.error("No client");

    const id = "21949875a8978036b06bed778786bd61";

    try {
        const db = await notion.databases.retrieve({ database_id: id });
        console.log("It is a DATABASE!");
        console.log(db.title);
        return;
    } catch (e: any) {
        console.log("Not a database:", e.message);
    }

    try {
        const page = await notion.pages.retrieve({ page_id: id });
        console.log("It is a PAGE!");
        console.log((page as any).properties);
    } catch (e: any) {
        console.log("Not a page either:", e.message);
    }
}

test().catch(console.error);
