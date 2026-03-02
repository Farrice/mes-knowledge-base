const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
    AlignmentType, HeadingLevel, BorderStyle, WidthType, LevelFormat,
    ShadingType, VerticalAlign, PageBreak } = require('docx');

const SCOPES = ['https://www.googleapis.com/auth/drive.file'];
const CREDENTIALS_PATH = '/Users/farricecain/Downloads/client_secret_65050601772-5shkqvc6nphonjelkk388lmq30t7hoce.apps.googleusercontent.com.json';

// === DOCUMENT STYLING ===
const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

function createDocument() {
    return new Document({
        styles: {
            default: { document: { run: { font: "Arial", size: 22 } } },
            paragraphStyles: [
                {
                    id: "Title", name: "Title", basedOn: "Normal",
                    run: { size: 48, bold: true, color: "1a1a2e", font: "Arial" },
                    paragraph: { spacing: { before: 0, after: 200 }, alignment: AlignmentType.CENTER }
                },
                {
                    id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
                    run: { size: 36, bold: true, color: "16213e", font: "Arial" },
                    paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 }
                },
                {
                    id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
                    run: { size: 28, bold: true, color: "0f3460", font: "Arial" },
                    paragraph: { spacing: { before: 300, after: 150 }, outlineLevel: 1 }
                },
                {
                    id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
                    run: { size: 24, bold: true, color: "1a1a2e", font: "Arial" },
                    paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 }
                },
                {
                    id: "Blockquote", name: "Blockquote", basedOn: "Normal",
                    run: { italics: true, color: "444444", size: 22 },
                    paragraph: { indent: { left: 720 }, spacing: { before: 120, after: 120 } }
                },
                {
                    id: "Subtitle", name: "Subtitle", basedOn: "Normal",
                    run: { italics: true, color: "666666", size: 24 },
                    paragraph: { alignment: AlignmentType.CENTER, spacing: { after: 400 } }
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
            properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
            children: [
                // === TITLE ===
                new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun("Josh Banday: Fellowship Strategy 2026")] }),
                new Paragraph({ style: "Subtitle", children: [new TextRun("Complete Strategic Toolkit")] }),

                // === SECTION 1: HANDOFF GUIDE ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("1. Handoff Guide")] }),
                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('The "De-Risked" Fellow Strategy')] }),
                new Paragraph({ children: [new TextRun("Josh,")] }),
                new Paragraph({
                    children: [
                        new TextRun('Most people applying for these fellowships are "Emerging Writers" (unknowns). '),
                        new TextRun({ text: "You are not.", bold: true })
                    ]
                }),
                new Paragraph({
                    children: [
                        new TextRun("You are "),
                        new TextRun({ text: "De-Risked Talent", bold: true }),
                        new TextRun(". You are a Series Regular ("),
                        new TextRun({ text: "Upload, Not Dead Yet", italics: true }),
                        new TextRun(") with Second City/Groundlings training. You have already survived the two hardest things in this town: casting and network production.")
                    ]
                }),
                new Paragraph({
                    spacing: { before: 200 }, children: [
                        new TextRun('This strategy is designed to weaponize your resume. We aren\'t asking them to "give you a shot"; we are showing them you are already a pro, and this fellowship is just the formal certification of your transition to Showrunner.')
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
                        new TextRun('Your comprehensive "Consumer Posture" profile. This is the deep identity work that makes your voice undeniable.')
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "toolkit-list", level: 0 }, children: [
                        new TextRun({ text: "The Insider Matrix: ", bold: true }),
                        new TextRun("A prioritized map of the 2026 deadlines (Disney, NBC, WB) with specific leverage points.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "toolkit-list", level: 0 }, children: [
                        new TextRun({ text: "The Master Class Templates: ", bold: true }),
                        new TextRun("Annotated guides for your essays and bios.")
                    ]
                }),

                // === PAGE BREAK ===
                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 2: STRATEGIC MANIFESTO ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("2. Strategic Manifesto: The Unfair Advantage")] }),
                new Paragraph({ style: "Blockquote", children: [new TextRun("Why You Will Win the 2026 Fellowship Cycle")] }),
                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('The Core Thesis: "De-Risked Talent"')] }),
                new Paragraph({
                    children: [
                        new TextRun({ text: 'Most fellowship advice is designed for "Emerging Writers" (unknowns). You are not an emerging writer. You are an ', italics: true }),
                        new TextRun({ text: "Emerging Showrunner.", bold: true, italics: true })
                    ]
                }),
                new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun("The Judge's Psychology (Why this strategy works)")] }),
                new Paragraph({ children: [new TextRun("Fellowship program directors are risk-averse. They are under pressure to select writers who will succeed in a room immediately.")] }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "The Fear: ", bold: true }),
                        new TextRun('Buying a "great voice" who freezes in a room, can\'t take notes, or doesn\'t understand production.')
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "The Relief: ", bold: true }),
                        new TextRun("Josh Banday.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "sub-bullets", level: 0 }, children: [
                        new TextRun({ text: "Proven: ", bold: true }),
                        new TextRun("Has survived network schedules ("),
                        new TextRun({ text: "Not Dead Yet, Upload", italics: true }),
                        new TextRun(").")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "sub-bullets", level: 0 }, children: [
                        new TextRun({ text: "Safe: ", bold: true }),
                        new TextRun('Knows the politics of a set (The "No A**holes" rule).')
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "sub-bullets", level: 0 }, children: [
                        new TextRun({ text: "Ready: ", bold: true }),
                        new TextRun('Dialogue is already "actor-proof" because an actor wrote it.')
                    ]
                }),
                new Paragraph({
                    spacing: { before: 200 }, children: [
                        new TextRun({ text: "Your Pivot: ", bold: true }),
                        new TextRun("You are not asking for a chance to learn; you are demonstrating that you have "),
                        new TextRun({ text: "already learned", italics: true }),
                        new TextRun(" the hardest parts of the job. The fellowship is just the certification.")
                    ]
                }),
                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("The Win Condition")] }),
                new Paragraph({ children: [new TextRun("We are not hiding your acting career; we are weaponizing it.")] }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Strategic Hook: ", bold: true }),
                        new TextRun('"The Series Regular who wants to run the show."')
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Emotional Hook: ", bold: true }),
                        new TextRun('"The Code-Switcher who found his true voice."')
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Tactical Hook: ", bold: true }),
                        new TextRun('"The De-Risked Hire who is ready for the room on Day 1."')
                    ]
                }),

                // === PAGE BREAK ===
                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 3: WRITER AVATAR ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("3. The Writer Avatar (Identity Architecture)")] }),
                new Paragraph({ style: "Blockquote", children: [new TextRun('Your "Consumer Posture" as a Creator — Based on the Dai Media Framework')] }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('The Individual: "The Double Threat"')] }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Essence: ", bold: true }),
                        new TextRun('Josh Banday is not an "aspiring" anything. He is a working television professional ('),
                        new TextRun({ text: "Upload, Not Dead Yet", italics: true }),
                        new TextRun(") who has spent years delivering other people's lines with impeccable comic timing. Now, he is reclaiming his voice. His intersectionality (Black/Filipino/Mexican/Jewish/LGBTQ+) isn't just a bio stat; it's the engine of his performance and his pen.")
                    ]
                }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "The Pivot: ", bold: true }),
                        new TextRun('He is transitioning from "The Actor Who Makes It Funny" to "The Writer Who Makes It Real."')
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('Occupation: "The Set-Tested Pro"')] }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "The Role: ", bold: true }),
                        new TextRun("Most fellowship applicants have never stepped on a soundstage. Josh lives there. He knows the rhythm of a table read, the pressure of a rewrite, and the mechanics of a joke because he has performed them.")
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Value Prop: ", bold: true }),
                        new TextRun("He is "),
                        new TextRun({ text: "De-Risked Talent", bold: true }),
                        new TextRun(". You don't have to teach him how a writers' room works; he's been auditing them from the cast side for years.")
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('Activity: "The Improv Pivot"')] }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Ritual: ", bold: true }),
                        new TextRun('Trained at Second City and Groundlings, Josh writes with an improviser\'s brain—"Yes, And"-ing his own characters. He writes dialogue that travels from the page to the mouth effortlessly because he tests it on himself.')
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Behavior: ", bold: true }),
                        new TextRun("He is writing "),
                        new TextRun({ text: "two", italics: true }),
                        new TextRun(' pilots and an animated feature while working as a series regular. This signals "Showrunner Work Ethic," not "Hobbyist."')
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('Thought Process: "The Insider Logic"')] }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Internal Logic: ", bold: true }),
                        new TextRun('"I\'ve played the \'Best Friend\'; now I write the \'Main Character\'." His comedy comes from the experience of being the most interesting person in the scene but having the fewest lines. He writes to center the stories that usually get pushed to the B-plot.')
                    ]
                }),
                new Paragraph({
                    numbering: { reference: "main-bullets", level: 0 }, children: [
                        new TextRun({ text: "Authenticity Check: ", bold: true }),
                        new TextRun("He validates his writing through performance. If it doesn't sing when read aloud, it gets cut.")
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('The Posture Synthesis: "The Actor-Auteur"')] }),
                new Paragraph({
                    children: [
                        new TextRun("He isn't asking for a break. He is asking for the "),
                        new TextRun({ text: "chair", italics: true }),
                        new TextRun(". He positions himself as the next Donald Glover or Issa Rae—talent who can write, act, and showrun because they understand the entire machine.")
                    ]
                }),

                // === PAGE BREAK ===
                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 4: FELLOWSHIP MATRIX ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("4. Insider Fellowship Matrix")] }),
                new Paragraph({ style: "Blockquote", children: [new TextRun("Targeting Strategy for 2026")] }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('"Bullseye" Targets (High Probability / High Rewards)')] }),

                // Table
                createFellowshipTable([
                    { program: "Disney Entertainment\n(May - June)", leverage: 'The "Home Team" Advantage — You are already in the family (Not Dead Yet). You understand the "Disney/ABC Tone"—warmth, ensemble, heart—because you lived it.', judge: '"He\'s already vetted. HR/Casting knows him. He\'s safe, he\'s talented, and he gets our brand. This is an easy win for us."', action: 'Use your Personal Statement to explicitly mention your time on Not Dead Yet as a "masterclass in the ABC family dynamic."' },
                    { program: "NBC Launch\n(Aug - Sept)", leverage: 'The "Improv DNA" Fit — NBC is the house of The Office, Parks, Brooklyn 99. They worship the Second City / Groundlings pipeline. Your background there is not just a "fun fact"—it is a credential.', judge: '"He speaks the language of our best showrunners (Tina Fey, Mike Schur). He understands ensemble comedy structure intuitively."', action: 'Highlight "Second City / Groundlings" in the first paragraph of your bio. Submit the pilot that has the strongest ensemble cast.' }
                ]),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('"Visionary" Targets (Prestige / Specificity)')] }),
                createFellowshipTable([
                    { program: "WB Discovery Access\n(June - July)", leverage: 'The "HBO/Streamer" Pivot — WB owns HBO/Max. They are looking for specificity and edge. Your "Code-Switching" narrative works best here.', judge: '"This guy has a unique, layered POV (Black/Filipino/Mexican/Jewish/Queer). He offers a perspective we literally don\'t have in our stable."', action: 'Submit your edgier/more specific material here. The essay should focus less on "warmth" and more on "truth" and "cultural friction."' }
                ]),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('"Credential" Targets (Mentorship / Network)')] }),
                createFellowshipTable([
                    { program: "Paramount Writers\n(April - May)", leverage: 'The "Professional" Polish — This program heavily emphasizes mentorship and process. Your "Series Regular" work ethic is the selling point here.', judge: '"He\'s an adult. He\'s a professional. He won\'t flake. We can put him in front of executives immediately."', action: 'Frame your application around "refining the craft" and "learning the business side." Show them you are humble despite your acting success.' }
                ]),

                // === PAGE BREAK ===
                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 5: STATEMENT TEMPLATE ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("5. Master Class Statement Template")] }),
                new Paragraph({ style: "Blockquote", children: [new TextRun("Annotated Guide for Josh Banday")] }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('Section 1: The "Call Sheet" Hook')] }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Objective: ", bold: true }),
                        new TextRun("Establish Authority immediately. Stop the scroll.")
                    ]
                }),
                new Paragraph({
                    children: [
                        new TextRun({ text: 'The "Why": ', bold: true }),
                        new TextRun('Judges read 500 essays about "how much I love TV." They bore easily. You will wake them up by putting them '),
                        new TextRun({ text: "on a set", italics: true }),
                        new TextRun("—a place they respect.")
                    ]
                }),
                new Paragraph({
                    style: "Blockquote", spacing: { before: 200, after: 200 }, children: [
                        new TextRun({ text: "Drafting The Scene: ", bold: true }),
                        new TextRun('"I am standing on the set of Upload (Season X), watching [Co-Star] do a take. The line is funny. The crew is laughing. I\'m laughing. But in my head, I\'m rewriting the scene. Not because it\'s bad—Greg Daniels is a genius—but because there is a specific, nuanced joke about the Black/Filipino intersection that only I know is missing. And I realized: I can spend my life selling the joke, or I can start building the world where the joke lives."')
                    ]
                }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Psychological Trigger: ", bold: true }),
                        new TextRun({ text: "Social Proof. ", italics: true }),
                        new TextRun('You just dropped "Upload" and "Greg Daniels" in the first 3 lines. You are vetted.')
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('Section 2: The "Improv" Transformation')] }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Objective: ", bold: true }),
                        new TextRun('Explain how your brain works. "Code-Switching" = Writing.')
                    ]
                }),
                new Paragraph({
                    style: "Blockquote", spacing: { before: 200, after: 200 }, children: [
                        new TextRun({ text: "The Narrative Arc: ", bold: true }),
                        new TextRun('"Growing up Black, Filipino, Mexican, Jewish, and Queer in Catholic School wasn\'t just \'diverse\'—it was an improv class I couldn\'t drop. I learned early that survival meant reading the room instantly. Which version of me does this scene need? That\'s Code-Switching. But it\'s also Writing. My training at Second City and Groundlings gave me the vocabulary for what I\'d been doing my whole life. The difference now is that I\'m done improvising in other people\'s scenes. I\'m ready to set the premise myself."')
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('Section 3: The "Visionary" Pivot')] }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Objective: ", bold: true }),
                        new TextRun("Tell them what they are buying.")
                    ]
                }),
                new Paragraph({
                    style: "Blockquote", spacing: { before: 200, after: 200 }, children: [
                        new TextRun({ text: "The Pitch: ", bold: true }),
                        new TextRun('"I am writing for the \'In-Betweeners.\' The generation that is too Black for the \'nerds\' but too \'alt\' for the mainstream. My comedy sits at the friction point where identity politics meets actual human messiness. I want to bring the specificity of a streamer dramedy to the accessibility of a network sitcom."')
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('Section 4: The "De-Risked" Close')] }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Objective: ", bold: true }),
                        new TextRun('Reassure them you are safe. They fear "flakes." You are a pro.')
                    ]
                }),
                new Paragraph({
                    style: "Blockquote", spacing: { before: 200, after: 200 }, children: [
                        new TextRun({ text: "The Closer: ", bold: true }),
                        new TextRun('"I am not looking for a fellowship to teach me how to be a professional; the last five years of call times have taught me that. I am looking for a fellowship to champion my transition from Interpreter to Creator. I am ready for the room because I have been listening at the door for years. Now, I\'m ready to open it."')
                    ]
                }),
                new Paragraph({
                    children: [
                        new TextRun({ text: "Psychological Trigger: ", bold: true }),
                        new TextRun({ text: "Certainty. ", italics: true }),
                        new TextRun("You sound like a Showrunner already.")
                    ]
                }),

                // === PAGE BREAK ===
                new Paragraph({ children: [new PageBreak()] }),

                // === SECTION 6: BIOS ===
                new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("6. Industry-Ready Bios")] }),
                new Paragraph({ style: "Blockquote", children: [new TextRun("Tailored Positioning for Applications & Meetings")] }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('The Fellowship Bio (Full Narrative)')] }),
                new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: "Use this for the main application bio box.", italics: true })] }),
                new Paragraph({
                    style: "Blockquote", children: [
                        new TextRun({ text: "Josh Banday ", bold: true }),
                        new TextRun("is a writer, actor, and improviser known for his series regular roles as 'Ivan' on Amazon's "),
                        new TextRun({ text: "Upload", italics: true }),
                        new TextRun(" and 'Dennis' on ABC's "),
                        new TextRun({ text: "Not Dead Yet", italics: true }),
                        new TextRun(". A Second City and Groundlings alum, Josh has spent his career bringing warmth and timing to other people's words—now, he's writing his own.")
                    ]
                }),
                new Paragraph({
                    style: "Blockquote", children: [
                        new TextRun("Born Black, Filipino, Mexican, and Jewish, and raised in the LGBTQ+ community, Josh writes 'Code-Switching Comedy'—stories that explore the hilarious friction of belonging everywhere and nowhere. His work combines the structural precision of a seasoned improviser with the on-set fluency of a working actor. Currently developing two comedy pilots and an animated feature, Josh enters the 2026 fellowship cycle to transition from scene-stealer to showrunner.")
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('The "Showrunner" Bio (Pro Vibe)')] }),
                new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: 'Use this for general meetings, website "About", or intro emails.', italics: true })] }),
                new Paragraph({
                    style: "Blockquote", children: [
                        new TextRun({ text: "Josh Banday ", bold: true }),
                        new TextRun("("),
                        new TextRun({ text: "Upload, Not Dead Yet", italics: true }),
                        new TextRun(") is a Black-Filipino-Mexican-Queer writer/actor transitioning from series regular to series creator. He writes genre-bending comedies about the chaos of intersectional identity, blending the rhythm of his Second City improv roots with the polish of a network TV veteran. His goal is to bring the 'set-readiness' of a seasoned performer to the writer's room.")
                    ]
                }),

                new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('The "Elevator Pitch" (Hook)')] }),
                new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: "For quick intros.", italics: true })] }),
                new Paragraph({
                    style: "Blockquote", children: [
                        new TextRun('"I\'m a series regular on '),
                        new TextRun({ text: "Upload", italics: true }),
                        new TextRun(" and "),
                        new TextRun({ text: "Not Dead Yet", italics: true }),
                        new TextRun(', but my background is Second City improv. I write comedy about being Black, Filipino, Mexican, Jewish, and Queer—basically, I write about the chaos of trying to fit in when you check every single box."')
                    ]
                })
            ]
        }]
    });
}

// Helper function to create fellowship tables
function createFellowshipTable(rows) {
    const headerRow = new TableRow({
        tableHeader: true,
        children: [
            new TableCell({
                borders: cellBorders, width: { size: 2000, type: WidthType.DXA }, shading: { fill: "1a1a2e", type: ShadingType.CLEAR },
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Program", bold: true, color: "FFFFFF", size: 20 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 3000, type: WidthType.DXA }, shading: { fill: "1a1a2e", type: ShadingType.CLEAR },
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Insider Leverage", bold: true, color: "FFFFFF", size: 20 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2500, type: WidthType.DXA }, shading: { fill: "1a1a2e", type: ShadingType.CLEAR },
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Judge's Perspective", bold: true, color: "FFFFFF", size: 20 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2500, type: WidthType.DXA }, shading: { fill: "1a1a2e", type: ShadingType.CLEAR },
                children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Action Item", bold: true, color: "FFFFFF", size: 20 })] })]
            })
        ]
    });

    const dataRows = rows.map(row => new TableRow({
        children: [
            new TableCell({
                borders: cellBorders, width: { size: 2000, type: WidthType.DXA }, verticalAlign: VerticalAlign.CENTER,
                children: [new Paragraph({ children: [new TextRun({ text: row.program, bold: true, size: 20 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 3000, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: row.leverage, size: 20 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2500, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: row.judge, italics: true, size: 20 })] })]
            }),
            new TableCell({
                borders: cellBorders, width: { size: 2500, type: WidthType.DXA },
                children: [new Paragraph({ children: [new TextRun({ text: row.action, size: 20 })] })]
            })
        ]
    }));

    return new Table({
        columnWidths: [2000, 3000, 2500, 2500],
        margins: { top: 50, bottom: 50, left: 100, right: 100 },
        rows: [headerRow, ...dataRows]
    });
}

// === MAIN EXECUTION ===
async function main() {
    console.log('Creating professionally formatted document...');
    const doc = createDocument();

    const buffer = await Packer.toBuffer(doc);
    const outputPath = '/Users/farricecain/.gemini/antigravity/brain/14d123a9-aeb7-46b4-8bea-913a7084b80a/Josh_Banday_Strategy_Professional.docx';
    fs.writeFileSync(outputPath, buffer);
    console.log(`Document saved to: ${outputPath}`);

    // Now upload to Google Drive
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
                    name: 'Josh Banday: Fellowship Strategy 2026',
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
