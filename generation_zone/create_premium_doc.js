const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
    AlignmentType, HeadingLevel, BorderStyle, WidthType, LevelFormat,
    ShadingType, VerticalAlign, PageBreak, Header, Footer, PageNumber,
    TableOfContents } = require('docx');

const SCOPES = ['https://www.googleapis.com/auth/drive.file'];
const CREDENTIALS_PATH = '/Users/farricecain/Downloads/client_secret_65050601772-5shkqvc6nphonjelkk388lmq30t7hoce.apps.googleusercontent.com.json';

// === COLOR PALETTE ===
const COLORS = {
    navy: "1a1a2e",      // Primary - Authority
    gold: "d4af37",      // Accent - Achievement  
    darkGold: "b8860b",  // Darker gold for text
    lightNavy: "16213e", // Lighter navy for H1
    slate: "4a5568",     // Supporting text
    lightGray: "f7f7f7", // Alternating rows
    white: "FFFFFF"
};

const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noCellBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

// Callout box helper
function createCalloutBox(title, content, accentColor = COLORS.gold) {
    return new Table({
        columnWidths: [9360],
        rows: [
            new TableRow({
                children: [
                    new TableCell({
                        borders: {
                            top: { style: BorderStyle.SINGLE, size: 1, color: accentColor },
                            bottom: { style: BorderStyle.SINGLE, size: 1, color: accentColor },
                            left: { style: BorderStyle.SINGLE, size: 24, color: accentColor },
                            right: { style: BorderStyle.SINGLE, size: 1, color: accentColor }
                        },
                        shading: { fill: "FFFDF5", type: ShadingType.CLEAR },
                        margins: { top: 150, bottom: 150, left: 200, right: 200 },
                        children: [
                            new Paragraph({
                                spacing: { after: 80 }, children: [
                                    new TextRun({ text: title, bold: true, color: COLORS.navy, size: 24, font: "Arial" })
                                ]
                            }),
                            new Paragraph({
                                children: [
                                    new TextRun({ text: content, color: COLORS.slate, size: 22, font: "Arial" })
                                ]
                            })
                        ]
                    })
                ]
            })
        ]
    });
}

// Pull quote helper
function createPullQuote(quote) {
    return new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 300, after: 300 },
        indent: { left: 720, right: 720 },
        children: [
            new TextRun({ text: '"', color: COLORS.gold, size: 48, font: "Georgia" }),
            new TextRun({ text: quote, italics: true, color: COLORS.navy, size: 28, font: "Georgia" }),
            new TextRun({ text: '"', color: COLORS.gold, size: 48, font: "Georgia" })
        ]
    });
}

function createDocument() {
    return new Document({
        styles: {
            default: { document: { run: { font: "Arial", size: 22 } } },
            paragraphStyles: [
                {
                    id: "Title", name: "Title", basedOn: "Normal",
                    run: { size: 72, bold: true, color: COLORS.navy, font: "Arial" },
                    paragraph: { spacing: { before: 0, after: 100 }, alignment: AlignmentType.CENTER }
                },
                {
                    id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
                    run: { size: 36, bold: true, color: COLORS.lightNavy, font: "Arial" },
                    paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 }
                },
                {
                    id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
                    run: { size: 28, bold: true, color: COLORS.navy, font: "Arial" },
                    paragraph: { spacing: { before: 300, after: 150 }, outlineLevel: 1 }
                },
                {
                    id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
                    run: { size: 24, bold: true, color: COLORS.slate, font: "Arial" },
                    paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 }
                },
                {
                    id: "Subtitle", name: "Subtitle", basedOn: "Normal",
                    run: { italics: true, color: COLORS.slate, size: 28 },
                    paragraph: { alignment: AlignmentType.CENTER, spacing: { after: 200 } }
                },
                {
                    id: "Tagline", name: "Tagline", basedOn: "Normal",
                    run: { color: COLORS.gold, size: 32, font: "Georgia", italics: true },
                    paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 400, after: 400 } }
                }
            ]
        },
        numbering: {
            config: [
                {
                    reference: "main-bullets",
                    levels: [{
                        level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
                        style: { paragraph: { indent: { left: 720, hanging: 360 } } }
                    }]
                },
                {
                    reference: "sub-bullets",
                    levels: [{
                        level: 0, format: LevelFormat.BULLET, text: "◦", alignment: AlignmentType.LEFT,
                        style: { paragraph: { indent: { left: 1080, hanging: 360 } } }
                    }]
                },
                {
                    reference: "toolkit-list",
                    levels: [{
                        level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
                        style: { paragraph: { indent: { left: 720, hanging: 360 } } }
                    }]
                }
            ]
        },
        sections: [{
            properties: {
                page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } }
            },
            headers: {
                default: new Header({
                    children: [new Paragraph({
                        alignment: AlignmentType.RIGHT,
                        children: [new TextRun({ text: "JOSH BANDAY | FELLOWSHIP STRATEGY 2026", color: COLORS.slate, size: 18, font: "Arial" })]
                    })]
                })
            },
            footers: {
                default: new Footer({
                    children: [new Paragraph({
                        alignment: AlignmentType.CENTER,
                        children: [
                            new TextRun({ text: "CONFIDENTIAL  •  ", color: COLORS.slate, size: 16 }),
                            new TextRun({ text: "Page ", color: COLORS.slate, size: 16 }),
                            new TextRun({ children: [PageNumber.CURRENT], color: COLORS.slate, size: 16 }),
                            new TextRun({ text: " of ", color: COLORS.slate, size: 16 }),
                            new TextRun({ children: [PageNumber.TOTAL_PAGES], color: COLORS.slate, size: 16 })
                        ]
                    })]
                })
            },
            children: [
                // === TITLE PAGE ===
                new Paragraph({ spacing: { before: 2000 } }),
                new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun("JOSH BANDAY")] }),
                new Paragraph({ style: "Subtitle", children: [new TextRun("Fellowship Strategy 2026")] }),
                new Paragraph({ style: "Tagline", children: [new TextRun("From Series Regular to Showrunner")] }),

                // Executive Summary Box
                new Paragraph({ spacing: { before: 600 } }),
                new Table({
                    columnWidths: [9360],
                    rows: [new TableRow({
                        children: [new TableCell({
                            borders: {
                                top: { style: BorderStyle.SINGLE, size: 2, color: COLORS.navy },
                                bottom: { style: BorderStyle.SINGLE, size: 2, color: COLORS.navy },
                                left: { style: BorderStyle.SINGLE, size: 2, color: COLORS.navy },
                                right: { style: BorderStyle.SINGLE, size: 2, color: COLORS.navy }
                            },
                            shading: { fill: "F8F9FA", type: ShadingType.CLEAR },
                            margins: { top: 200, bottom: 200, left: 300, right: 300 },
                            children: [
                                new Paragraph({
                                    alignment: AlignmentType.CENTER, spacing: { after: 150 }, children: [
                                        new TextRun({ text: "THE CORE THESIS", bold: true, color: COLORS.navy, size: 24, smallCaps: true })
                                    ]
                                }),
                                new Paragraph({
                                    alignment: AlignmentType.CENTER, children: [
                                        new TextRun({ text: "You are ", size: 24 }),
                                        new TextRun({ text: "De-Risked Talent", bold: true, color: COLORS.darkGold, size: 24 }),
                                        new TextRun({ text: ". The fellowship is not a chance to learn—it's the certification of what you've already mastered.", size: 24 })
                                    ]
                                })
                            ]
                        })]
                    })]
                }),

                // Three Hooks
                new Paragraph({
                    spacing: { before: 400, after: 200 }, alignment: AlignmentType.CENTER, children: [
                        new TextRun({ text: "YOUR THREE HOOKS", bold: true, color: COLORS.navy, size: 22, smallCaps: true })
                    ]
                }),
                new Table({
                    columnWidths: [3120, 3120, 3120],
                    rows: [new TableRow({
                        children: [
                            new TableCell({
                                borders: noCellBorders,
                                margins: { top: 100, bottom: 100, left: 100, right: 100 },
                                children: [
                                    new Paragraph({
                                        alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [
                                            new TextRun({ text: "STRATEGIC", bold: true, color: COLORS.gold, size: 20 })
                                        ]
                                    }),
                                    new Paragraph({
                                        alignment: AlignmentType.CENTER, children: [
                                            new TextRun({ text: '"The Series Regular who wants to run the show."', italics: true, size: 20, color: COLORS.slate })
                                        ]
                                    })
                                ]
                            }),
                            new TableCell({
                                borders: { left: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" }, right: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" }, top: noBorder, bottom: noBorder },
                                margins: { top: 100, bottom: 100, left: 100, right: 100 },
                                children: [
                                    new Paragraph({
                                        alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [
                                            new TextRun({ text: "EMOTIONAL", bold: true, color: COLORS.gold, size: 20 })
                                        ]
                                    }),
                                    new Paragraph({
                                        alignment: AlignmentType.CENTER, children: [
                                            new TextRun({ text: '"The Code-Switcher who found his true voice."', italics: true, size: 20, color: COLORS.slate })
                                        ]
                                    })
                                ]
                            }),
                            new TableCell({
                                borders: noCellBorders,
                                margins: { top: 100, bottom: 100, left: 100, right: 100 },
                                children: [
                                    new Paragraph({
                                        alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [
                                            new TextRun({ text: "TACTICAL", bold: true, color: COLORS.gold, size: 20 })
                                        ]
                                    }),
                                    new Paragraph({
                                        alignment: AlignmentType.CENTER, children: [
                                            new TextRun({ text: '"The De-Risked Hire ready for Day 1."', italics: true, size: 20, color: COLORS.slate })
                                        ]
                                    })
                                ]
                            })
                        ]
                    })]
                }),

                // Fellowship Deadlines Preview
                new Paragraph({
                    spacing: { before: 400, after: 200 }, alignment: AlignmentType.CENTER, children: [
                        new TextRun({ text: "2026 FELLOWSHIP TIMELINE", bold: true, color: COLORS.navy, size: 22, smallCaps: true })
                    ]
                }),
                new Table({
                    columnWidths: [2340, 2340, 2340, 2340],
                    rows: [new TableRow({
                        children: [
                            createTimelineCell("APR-MAY", "Paramount", COLORS.slate),
                            createTimelineCell("MAY-JUN", "Disney", COLORS.gold),
                            createTimelineCell("JUN-JUL", "WB", COLORS.slate),
                            createTimelineCell("AUG-SEP", "NBC", COLORS.gold)
                        ]
                    })]
                }),

                // === PAGE BREAK ===
                new Paragraph({ children: [new PageBreak()] }),

                // === TABLE OF CONTENTS ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Contents")] }),
                new TableOfContents("Table of Contents", { hyperlink: true, headingStyleRange: "1-2" }),

                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 1: STRATEGY OVERVIEW ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("1. Strategy Overview")] }),

                createCalloutBox(
                    "THE DE-RISKED FELLOW STRATEGY",
                    "Most applicants are 'Emerging Writers' (unknowns). You are De-Risked Talent—a Series Regular with Second City/Groundlings training who has survived the two hardest things in Hollywood: casting and network production."
                ),

                new Paragraph({
                    spacing: { before: 200 }, children: [
                        new TextRun("This strategy is designed to "),
                        new TextRun({ text: "weaponize your resume", bold: true }),
                        new TextRun(". We aren't asking them to \"give you a shot\"—we're showing them you're already a pro, and this fellowship is just the formal certification of your transition to Showrunner.")
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Your Toolkit")] }),
                new Paragraph({
                    numbering: { reference: "toolkit-list", level: 0 }, children: [
                        new TextRun({ text: "The Strategic Manifesto: ", bold: true }),
                        new TextRun("The high-level thesis. Why you will win.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "toolkit-list", level: 0 }, children: [
                        new TextRun({ text: "The Writer Avatar: ", bold: true }),
                        new TextRun("Your comprehensive identity profile—the deep work that makes your voice undeniable.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "toolkit-list", level: 0 }, children: [
                        new TextRun({ text: "The Insider Matrix: ", bold: true }),
                        new TextRun("A prioritized map of 2026 deadlines with specific leverage points.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "toolkit-list", level: 0 }, children: [
                        new TextRun({ text: "The Master Class Templates: ", bold: true }),
                        new TextRun("Annotated guides for your essays and bios.")
                    ]
                }),

                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 2: MANIFESTO ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("2. The Strategic Manifesto")] }),
                new Paragraph({ style: "Subtitle", alignment: AlignmentType.LEFT, children: [new TextRun("Why You Will Win the 2026 Fellowship Cycle")] }),

                createPullQuote("You are not an emerging writer. You are an Emerging Showrunner."),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("The Judge's Psychology")] }),
                new Paragraph({ children: [new TextRun("Fellowship directors are risk-averse. They need writers who succeed in a room immediately.")] }),

                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, spacing: { before: 150 }, children: [
                        new TextRun({ text: "Their Fear: ", bold: true, color: COLORS.darkGold }),
                        new TextRun("A \"great voice\" who freezes in a room, can't take notes, or doesn't understand production.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Their Relief: ", bold: true, color: COLORS.darkGold }),
                        new TextRun("Josh Banday.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "sub-bullets", level: 0 }, children: [
                        new TextRun({ text: "Proven: ", bold: true }),
                        new TextRun("Survived network schedules ("),
                        new TextRun({ text: "Not Dead Yet, Upload", italics: true }),
                        new TextRun(").")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "sub-bullets", level: 0 }, children: [
                        new TextRun({ text: "Safe: ", bold: true }),
                        new TextRun("Knows set politics. Lives the \"No A**holes\" rule.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "sub-bullets", level: 0 }, children: [
                        new TextRun({ text: "Ready: ", bold: true }),
                        new TextRun("Dialogue is \"actor-proof\" because an actor wrote it.")
                    ]
                }),

                createCalloutBox(
                    "YOUR PIVOT",
                    "You are not asking for a chance to learn—you are demonstrating that you have already learned the hardest parts of the job. The fellowship is just the certification."
                ),

                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 3: WRITER AVATAR ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("3. The Writer Avatar")] }),
                new Paragraph({ style: "Subtitle", alignment: AlignmentType.LEFT, children: [new TextRun("Identity Architecture — Based on the Dai Media Framework")] }),

                createPullQuote("The Actor Who Makes It Funny → The Writer Who Makes It Real"),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("The Individual: \"The Double Threat\"")] }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Essence: ", bold: true }),
                        new TextRun("Josh is not \"aspiring\" anything. He is a working TV professional ("),
                        new TextRun({ text: "Upload, Not Dead Yet", italics: true }),
                        new TextRun(") reclaiming his voice. His intersectionality (Black/Filipino/Mexican/Jewish/LGBTQ+) isn't a bio stat—it's the engine of his performance and his pen.")
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Occupation: \"The Set-Tested Pro\"")] }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun("Most applicants have never stepped on a soundstage. Josh "),
                        new TextRun({ text: "lives", italics: true }),
                        new TextRun(" there.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Value Prop: ", bold: true }),
                        new TextRun("You don't have to teach him how a writers' room works—he's been auditing them from the cast side for years.")
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Activity: \"The Improv Pivot\"")] }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun("Second City + Groundlings trained. Writes with an improviser's brain—\"Yes, And\"-ing his characters.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun("Currently writing "),
                        new TextRun({ text: "two pilots + an animated feature", bold: true }),
                        new TextRun(" while working as a series regular. \"Showrunner Work Ethic,\" not \"Hobbyist.\"")
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("The Posture Synthesis: \"The Actor-Auteur\"")] }),
                createCalloutBox(
                    "THE CHAIR",
                    "He isn't asking for a break. He is asking for the chair. He positions himself as the next Donald Glover or Issa Rae—talent who can write, act, and showrun because they understand the entire machine."
                ),

                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 4: FELLOWSHIP MATRIX ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("4. Insider Fellowship Matrix")] }),
                new Paragraph({ style: "Subtitle", alignment: AlignmentType.LEFT, children: [new TextRun("Targeting Strategy for 2026")] }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("\"Bullseye\" Targets — High Probability / High Reward")] }),
                createEnhancedFellowshipTable([
                    { program: "Disney Entertainment\n(May - June)", leverage: "The \"Home Team\" Advantage — Already in the family (Not Dead Yet). You understand Disney/ABC tone because you lived it.", judge: "\"He's already vetted. HR knows him. Easy win for us.\"", action: "Mention Not Dead Yet as a \"masterclass in ABC family dynamics.\" Frame pilot as what you'd pitch to the NDY showrunners.", highlight: true },
                    { program: "NBC Launch\n(Aug - Sept)", leverage: "The \"Improv DNA\" Fit — NBC worships the Second City/Groundlings pipeline. Your background is a credential, not a fun fact.", judge: "\"He speaks the language of our best showrunners.\"", action: "Lead with \"Second City/Groundlings\" in bio. Submit strongest ensemble pilot.", highlight: false }
                ]),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("\"Visionary\" Targets — Prestige / Specificity")] }),
                createEnhancedFellowshipTable([
                    { program: "WB Discovery Access\n(June - July)", leverage: "The \"HBO/Streamer\" Pivot — They want specificity and edge. Your Code-Switching narrative works best here.", judge: "\"He offers a perspective we don't have in our stable.\"", action: "Submit edgier material. Focus on \"truth\" and \"cultural friction.\"", highlight: false }
                ]),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("\"Credential\" Targets — Mentorship / Network")] }),
                createEnhancedFellowshipTable([
                    { program: "Paramount Writers\n(April - May)", leverage: "The \"Professional\" Polish — Emphasizes mentorship. Your Series Regular work ethic is the selling point.", judge: "\"He's an adult. He won't flake.\"", action: "Frame around \"refining craft\" and \"learning business.\" Show humility.", highlight: false }
                ]),

                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 5: STATEMENT TEMPLATES ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("5. Master Class Statement Templates")] }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Section 1: The \"Call Sheet\" Hook")] }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Objective: ", bold: true }),
                        new TextRun("Establish Authority. Stop the scroll.")
                    ]
                }),
                createCalloutBox(
                    "DRAFTING THE SCENE",
                    "\"I am standing on the set of Upload, watching [Co-Star] do a take. The line is funny. The crew is laughing. But in my head, I'm rewriting the scene—not because it's bad, Greg Daniels is a genius—but because there's a specific joke about the Black/Filipino intersection that only I know is missing. And I realized: I can spend my life selling the joke, or I can start building the world where the joke lives.\""
                ),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Psychological Trigger: ", bold: true }),
                        new TextRun("Social Proof. You dropped \"Upload\" and \"Greg Daniels\" in the first 3 lines. "),
                        new TextRun({ text: "You are vetted.", italics: true })
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Section 2: The \"Improv\" Transformation")] }),
                createCalloutBox(
                    "THE NARRATIVE ARC",
                    "\"Growing up Black, Filipino, Mexican, Jewish, and Queer in Catholic School wasn't just 'diverse'—it was an improv class I couldn't drop. I learned early that survival meant reading the room instantly. Which version of me does this scene need? That's Code-Switching. But it's also Writing. My training at Second City and Groundlings gave me vocabulary for what I'd been doing my whole life. The difference now is that I'm done improvising in other people's scenes. I'm ready to set the premise myself.\""
                ),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Section 3: The \"Visionary\" Pivot")] }),
                createCalloutBox(
                    "THE PITCH",
                    "\"I am writing for the 'In-Betweeners.' The generation too Black for the 'nerds' but too 'alt' for the mainstream. My comedy sits at the friction point where identity politics meets actual human messiness. I want to bring the specificity of a streamer dramedy to the accessibility of a network sitcom.\""
                ),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Section 4: The \"De-Risked\" Close")] }),
                createCalloutBox(
                    "THE CLOSER",
                    "\"I am not looking for a fellowship to teach me how to be a professional; the last five years of call times have taught me that. I am looking for a fellowship to champion my transition from Interpreter to Creator. I am ready for the room because I have been listening at the door for years. Now, I'm ready to open it.\""
                ),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Psychological Trigger: ", bold: true }),
                        new TextRun({ text: "Certainty. ", italics: true }),
                        new TextRun("You sound like a Showrunner already.")
                    ]
                }),

                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 6: BIOS ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("6. Industry-Ready Bios")] }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("The Fellowship Bio")] }),
                new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: "For the main application bio box.", italics: true, color: COLORS.slate })] }),
                createCalloutBox(
                    "",
                    "Josh Banday is a writer, actor, and improviser known for his series regular roles as 'Ivan' on Amazon's Upload and 'Dennis' on ABC's Not Dead Yet. A Second City and Groundlings alum, Josh has spent his career bringing warmth and timing to other people's words—now, he's writing his own.\n\nBorn Black, Filipino, Mexican, and Jewish, and raised in the LGBTQ+ community, Josh writes 'Code-Switching Comedy'—stories that explore the hilarious friction of belonging everywhere and nowhere. Currently developing two comedy pilots and an animated feature, Josh enters the 2026 fellowship cycle to transition from scene-stealer to showrunner."
                ),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("The \"Showrunner\" Bio")] }),
                new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: "For general meetings, website \"About\", or intro emails.", italics: true, color: COLORS.slate })] }),
                createCalloutBox(
                    "",
                    "Josh Banday (Upload, Not Dead Yet) is a Black-Filipino-Mexican-Queer writer/actor transitioning from series regular to series creator. He writes genre-bending comedies about the chaos of intersectional identity, blending the rhythm of his Second City improv roots with the polish of a network TV veteran. His goal is to bring the 'set-readiness' of a seasoned performer to the writer's room."
                ),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("The \"Elevator Pitch\"")] }),
                new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: "For quick intros.", italics: true, color: COLORS.slate })] }),
                createPullQuote("I'm a series regular on Upload and Not Dead Yet, but my background is Second City improv. I write comedy about being Black, Filipino, Mexican, Jewish, and Queer—basically, I write about the chaos of trying to fit in when you check every single box.")
            ]
        }]
    });
}

// Timeline cell helper
function createTimelineCell(date, program, accentColor) {
    return new TableCell({
        borders: noCellBorders,
        shading: { fill: accentColor === COLORS.gold ? "FFFDF5" : "F8F9FA", type: ShadingType.CLEAR },
        margins: { top: 100, bottom: 100, left: 50, right: 50 },
        children: [
            new Paragraph({
                alignment: AlignmentType.CENTER, children: [
                    new TextRun({ text: date, bold: true, color: accentColor, size: 20 })
                ]
            }),
            new Paragraph({
                alignment: AlignmentType.CENTER, children: [
                    new TextRun({ text: program, size: 18, color: COLORS.navy })
                ]
            })
        ]
    });
}

// Enhanced Fellowship Table
function createEnhancedFellowshipTable(rows) {
    const headerRow = new TableRow({
        tableHeader: true,
        children: [
            new TableCell({
                borders: cellBorders, width: { size: 1800, type: WidthType.DXA }, shading: { fill: COLORS.navy, type: ShadingType.CLEAR },
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "PROGRAM", bold: true, color: "FFFFFF", size: 18 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2500, type: WidthType.DXA }, shading: { fill: COLORS.navy, type: ShadingType.CLEAR },
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "YOUR LEVERAGE", bold: true, color: "FFFFFF", size: 18 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2200, type: WidthType.DXA }, shading: { fill: COLORS.navy, type: ShadingType.CLEAR },
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "JUDGE THINKS", bold: true, color: "FFFFFF", size: 18 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2860, type: WidthType.DXA }, shading: { fill: COLORS.gold, type: ShadingType.CLEAR },
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "ACTION ITEM", bold: true, color: COLORS.navy, size: 18 })] })]
            })
        ]
    });

    const dataRows = rows.map((row, idx) => new TableRow({
        children: [
            new TableCell({
                borders: cellBorders, width: { size: 1800, type: WidthType.DXA },
                shading: { fill: idx % 2 === 0 ? "FFFFFF" : COLORS.lightGray, type: ShadingType.CLEAR },
                verticalAlign: VerticalAlign.CENTER,
                children: [new Paragraph({ children: [new TextRun({ text: row.program, bold: true, size: 18 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2500, type: WidthType.DXA },
                shading: { fill: idx % 2 === 0 ? "FFFFFF" : COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: row.leverage, size: 18 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2200, type: WidthType.DXA },
                shading: { fill: idx % 2 === 0 ? "FFFFFF" : COLORS.lightGray, type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: row.judge, italics: true, size: 18 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2860, type: WidthType.DXA },
                shading: { fill: "FFFDF5", type: ShadingType.CLEAR },
                children: [new Paragraph({ children: [new TextRun({ text: row.action, size: 18, bold: true })] })]
            })
        ]
    }));

    return new Table({
        columnWidths: [1800, 2500, 2200, 2860],
        margins: { top: 50, bottom: 50, left: 80, right: 80 },
        rows: [headerRow, ...dataRows]
    });
}

// === MAIN EXECUTION ===
async function main() {
    console.log('Creating premium formatted document...');
    const doc = createDocument();

    const buffer = await Packer.toBuffer(doc);
    const outputPath = '/Users/farricecain/.gemini/antigravity/brain/14d123a9-aeb7-46b4-8bea-913a7084b80a/Josh_Banday_Strategy_Premium.docx';
    fs.writeFileSync(outputPath, buffer);
    console.log(`Document saved: ${outputPath}`);

    console.log('Uploading to Google Drive...');
    const { google } = require('googleapis');
    const readline = require('readline');

    const content = fs.readFileSync(CREDENTIALS_PATH);
    const credentials = JSON.parse(content);
    const { client_secret, client_id, redirect_uris } = credentials.installed;
    const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);

    const authUrl = oAuth2Client.generateAuthUrl({ access_type: 'offline', scope: SCOPES });
    console.log('AUTH_URL:', authUrl);

    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    rl.question('Enter the code: ', async (code) => {
        rl.close();
        try {
            const { tokens } = await oAuth2Client.getToken(code);
            oAuth2Client.setCredentials(tokens);

            const drive = google.drive({ version: 'v3', auth: oAuth2Client });
            const res = await drive.files.create({
                requestBody: {
                    name: 'Josh Banday: Fellowship Strategy 2026 (Premium)',
                    mimeType: 'application/vnd.google-apps.document'
                },
                media: {
                    mimeType: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    body: fs.createReadStream(outputPath)
                }
            });
            console.log(`SUCCESS: https://docs.google.com/document/d/${res.data.id}/edit`);
        } catch (err) {
            console.error('Error:', err.message);
        }
    });
}

main();
