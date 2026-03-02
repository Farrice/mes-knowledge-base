#!/usr/bin/env python3
import os
import re

AGENTS_DIR = "agents"
COUNCIL_FILE = "COUNCIL.md"
CHEAT_SHEET_FILE = "AGENT_CHEAT_SHEET.md"

def get_agent_details(agent_dir):
    agent_md_path = os.path.join(AGENTS_DIR, agent_dir, "AGENT.md")
    if not os.path.isfile(agent_md_path):
        return None
    
    with open(agent_md_path, "r", encoding="utf-8") as f:
        content = f.read()

    name = agent_dir.replace("-", " ").title()
    desc = "Specialized AI Expert"
    
    # Try to grab H1 for name
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        name_extracted = h1_match.group(1).split(":")[0].strip()
        if len(name_extracted) < 40:
            name = name_extracted
            
    # Try to grab the first blockquote for description
    bq_match = re.search(r'^>\s+(.+)$', content, re.MULTILINE)
    if bq_match:
        desc_extracted = bq_match.group(1).strip()
        if len(desc_extracted) > 5:
            desc = desc_extracted
            
    return {"slug": agent_dir, "name": name, "desc": desc}

def build_cheat_sheet():
    agents = []
    for item in sorted(os.listdir(AGENTS_DIR)):
        if os.path.isdir(os.path.join(AGENTS_DIR, item)):
            details = get_agent_details(item)
            if details:
                agents.append(details)
                
    with open(CHEAT_SHEET_FILE, "w", encoding="utf-8") as f:
        f.write("# ⚡️ Master Agent Cheat Sheet\n\n")
        f.write("> **System Notice**: This file is *auto-generated* directly from the filesystem to ensure 100% accuracy. You currently have **" + str(len(agents)) + " active experts** built and ready to deploy.\n\n")
        
        f.write("### 🏛️ Executive Councils (Multi-Expert Synthesis)\n")
        f.write("*(These are standing groups configured in `COUNCIL.md`)*\n\n")
        f.write("| Invoke Command | Focus Area | Members Included |\n")
        f.write("|----------------|------------|------------------|\n")
        f.write("| `@revenue-council` | Sales, Pricing, Deal Analysis | Jeremy Miner, Michael Bernoff, Cardinal Mason, Samuel Thompson |\n")
        f.write("| `@content-council` | Content Strategy, Writing Excellence | Shaan Puri, Harry Dry, Mitch Albom, Dan Wang |\n")
        f.write("| `@brand-council` | Positioning, Audience Research | Dai Media, Caleb Ralston, Lulu Cheng Meservey, Erica Mallet |\n")
        f.write("| `@ai-council` | Automation, System Design | Futurepedia, Nate B Jones, Darrel Wilson, Mark Kashef, Andrew Wilkinson |\n")
        f.write("| `@creative-council` | Visuals, Creative Direction, Audio | Kittl, Oscar Hoglund, Seena Rez |\n\n")
        f.write("---\n\n")
        
        f.write("### 🧠 Master Directory: All " + str(len(agents)) + " Active Agents\n\n")
        f.write("| Invoke Command | Agent Name | Core Expertise / Superpower |\n")
        f.write("|----------------|------------|-----------------------------|\n")
        
        for a in agents:
            # Clean up desc if it has asterisks or quotes
            desc = a['desc'].replace("|", "-").replace("\"", "'")
            f.write(f"| `@{(a['slug'])}` | **{a['name']}** | {desc} |\n")
            
        f.write("\n---\n\n")
        f.write("### 💡 Pro-Tip Invocation Patterns\n")
        f.write("- **Synthesis:** `\"What would @cardinal-mason and @harry-dry both say about this?\"`\n")
        f.write("- **Execution:** `\"@cardinal-mason write me a 5-email welcome sequence based on this topic.\"`\n")
        f.write("- **Handoffs:** `\"@brand-council help me decide my positioning, then hand off to @cardinal-mason to write the copy.\"`\n")
        
        print(f"✅ Generated AGENT_CHEAT_SHEET.md with {len(agents)} experts.")

if __name__ == "__main__":
    build_cheat_sheet()
