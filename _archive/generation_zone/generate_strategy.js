const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, BorderStyle } = require('docx');

const doc = new Document({
    sections: [{
        properties: {},
        children: [
            // TITLE
            new Paragraph({
                text: "Josh Banday: Fellowship Strategy 2026",
                heading: HeadingLevel.TITLE,
                spacing: { after: 200 },
            }),
            new Paragraph({
                text: "Complete Strategic Toolkit",
                style: "Subtitle",
                spacing: { after: 400 },
            }),

            // SECTION 1: HANDOFF GUIDE
            new Paragraph({
                text: "1. Handoff Guide",
                heading: HeadingLevel.HEADING_1,
                spacing: { before: 400, after: 200 },
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Josh, ", bold: true }),
                    new TextRun("Most people applying for these fellowships are 'Emerging Writers' (unknowns). "),
                    new TextRun({ text: "You are not.", bold: true }),
                ],
                spacing: { after: 200 },
            }),
            new Paragraph({
                children: [
                    new TextRun("You are "),
                    new TextRun({ text: "De-Risked Talent", bold: true }),
                    new TextRun(". You are a Series Regular ("),
                    new TextRun({ text: "Upload, Not Dead Yet", italics: true }),
                    new TextRun(") with Second City/Groundlings training. You have already survived the two hardest things in this town: casting and network production."),
                ],
                spacing: { after: 200 },
            }),
            new Paragraph({
                text: "This strategy is designed to weaponize your resume. We aren't asking them to 'give you a shot'; we are showing them you are already a pro, and this fellowship is just the formal certification of your transition to Showrunner.",
                spacing: { after: 200 },
            }),

            // SECTION 2: MANIFESTO
            new Paragraph({
                text: "2. Strategic Manifesto: The Unfair Advantage",
                heading: HeadingLevel.HEADING_1,
                pageBreakBefore: true,
                spacing: { before: 400, after: 200 },
            }),
            new Paragraph({
                text: "Why You Will Win the 2026 Fellowship Cycle",
                heading: HeadingLevel.HEADING_2,
                spacing: { after: 200 },
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Core Thesis: ", bold: true }),
                    new TextRun("You are not an emerging writer. You are an "),
                    new TextRun({ text: "Emerging Showrunner.", bold: true }),
                ],
                spacing: { after: 200 },
            }),
            new Paragraph({
                text: "The Judge's Psychology:",
                heading: HeadingLevel.HEADING_3,
            }),
            new Paragraph({
                text: "They fear buying a 'great voice' who freezes in a room. You are the relief. You are Proven, Safe, and Ready. Your dialogue is already actor-proof because an actor wrote it.",
                spacing: { after: 200 },
            }),
            new Paragraph({
                text: "Your Pivot:",
                heading: HeadingLevel.HEADING_3,
            }),
            new Paragraph({
                text: "You are not asking for a chance to learn; you are demonstrating that you have already learned the hardest parts of the job.",
                spacing: { after: 200 },
            }),

            // SECTION 3: WRITER AVATAR
            new Paragraph({
                text: "3. The Writer Avatar (Identity Architecture)",
                heading: HeadingLevel.HEADING_1,
                pageBreakBefore: true,
                spacing: { before: 400, after: 200 },
            }),
            new Paragraph({
                text: "Based on the Dai Media Framework",
                heading: HeadingLevel.HEADING_2,
                spacing: { after: 200 },
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Occupation: The Set-Tested Pro. ", bold: true }),
                    new TextRun("Most applicants haven't stepped on a soundstage. Josh lives there. He knows the rhythm of a table read."),
                ],
                spacing: { after: 200 },
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Activity: The Improv Pivot. ", bold: true }),
                    new TextRun("Trained at Second City, he writes with an improviser's brain. He 'Yes, Ands' his own characters."),
                ],
                spacing: { after: 200 },
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Thought Process: Internal Logic. ", bold: true }),
                    new TextRun("He plays the 'Main Character' even when he has few lines. He centers the B-plot stories."),
                ],
                spacing: { after: 200 },
            }),

            // SECTION 4: FELLOWSHIP MATRIX
            new Paragraph({
                text: "4. Insider Fellowship Matrix",
                heading: HeadingLevel.HEADING_1,
                pageBreakBefore: true,
                spacing: { before: 400, after: 200 },
            }),
            new Paragraph({
                text: "Disney Entertainment (May-June)",
                heading: HeadingLevel.HEADING_2,
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Leverage: ", bold: true }),
                    new TextRun("Home Team Advantage (Not Dead Yet)."),
                ],
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Action: ", bold: true }),
                    new TextRun("Mention NDY as a masterclass in ABC tone."),
                ],
                spacing: { after: 200 },
            }),
            new Paragraph({
                text: "NBC Launch (Aug-Sept)",
                heading: HeadingLevel.HEADING_2,
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Leverage: ", bold: true }),
                    new TextRun("Improv DNA (Second City/Groundlings)."),
                ],
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Action: ", bold: true }),
                    new TextRun("Highlight Improv roots. Submit ensemble sample."),
                ],
                spacing: { after: 200 },
            }),

            // SECTION 5: TEMPLATES
            new Paragraph({
                text: "5. Master Class Templates",
                heading: HeadingLevel.HEADING_1,
                pageBreakBefore: true,
                spacing: { before: 400, after: 200 },
            }),
            new Paragraph({
                text: "Personal Statement Hook (Drafting The Scene):",
                heading: HeadingLevel.HEADING_3,
            }),
            new Paragraph({
                text: "\"I am standing on the set of Upload, watching my co-star do a take. The line is funny. The crew is laughing. But in my head, I'm rewriting the scene. Not because it's bad—Greg Daniels is a genius—but because there is a specific, nuanced joke about the Black/Filipino intersection that only I know is missing. And I realized: I can spend my life selling the joke, or I can start building the world where the joke lives.\"",
                style: "Quote",
                spacing: { after: 200 },
            }),
            new Paragraph({
                children: [
                    new TextRun({ text: "Psychological Trigger: ", bold: true }),
                    new TextRun("Social Proof. You dropped 'Upload' and 'Greg Daniels' in the first 3 lines."),
                ],
                spacing: { after: 200 },
            }),

            // SECTION 6: BIOS
            new Paragraph({
                text: "6. Industry-Ready Bios",
                heading: HeadingLevel.HEADING_1,
                pageBreakBefore: true,
                spacing: { before: 400, after: 200 },
            }),
            new Paragraph({
                text: "The Fellowship Bio:",
                heading: HeadingLevel.HEADING_2,
            }),
            new Paragraph({
                text: "Josh Banday is a writer, actor, and improviser known for his series regular roles as 'Ivan' on Amazon’s Upload and 'Dennis' on ABC’s Not Dead Yet. A Second City and Groundlings alum, Josh has spent his career bringing warmth and timing to other people’s words—now, he’s writing his own. Born Black, Filipino, Mexican, and Jewish, and raised in the LGBTQ+ community, Josh writes 'Code-Switching Comedy'—stories that explore the hilarious friction of belonging everywhere and nowhere.",
                spacing: { after: 200 },
            }),
        ],
    }],
});

Packer.toBuffer(doc).then((buffer) => {
    fs.writeFileSync("Josh_Banday_Strategy.docx", buffer);
});
