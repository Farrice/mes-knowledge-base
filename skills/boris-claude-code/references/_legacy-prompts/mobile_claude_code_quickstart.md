# MOBILE CLAUDE CODE QUICK-START SETUP
## GitHub & Cloud Configuration for iPhone/Android
### Get Running in 10 Minutes

---

## THE PROBLEM YOU'RE SOLVING

Claude Code on mobile REQUIRES GitHub connection to access your repositories and persist work. Without it, you're limited to standalone conversations. This guide fixes that.

---

## STEP-BY-STEP SETUP (Mobile)

### Step 1: Open Claude Code Mobile App

1. Open the Claude app on your phone
2. Tap the left menu (hamburger icon)
3. Tap **"Code"** to access Claude Code mode

You should see a terminal-like interface.

---

### Step 2: Check Current GitHub Status

Type this command:
```
/doctor
```

**What you'll see:**

If NOT connected:
```
GitHub CLI: ❌ Not authenticated
```

If connected:
```
GitHub CLI: ✅ Authenticated as [your-username]
```

---

### Step 3: Authenticate GitHub (If Needed)

**Option A: Browser Auth (Easiest)**

1. In Claude Code, type:
```
gh auth login
```

2. When prompted:
   - Select: **GitHub.com**
   - Select: **HTTPS**
   - Select: **Login with a web browser**

3. You'll see a code like: `ABCD-1234`

4. Claude Code will try to open your browser. If it doesn't:
   - Open Safari/Chrome manually
   - Go to: **github.com/login/device**
   - Enter the code

5. Authorize the application

6. Return to Claude Code - it should confirm authentication

---

**Option B: Token Auth (If Browser Doesn't Work)**

1. On your phone browser, go to:
   - **github.com** → Log in
   - Tap your profile picture → **Settings**
   - Scroll down to **Developer settings**
   - Tap **Personal access tokens** → **Tokens (classic)**
   - Tap **Generate new token** → **Generate new token (classic)**

2. Configure the token:
   - Name: "Claude Code Mobile"
   - Expiration: 90 days (or your preference)
   - Select scopes: ✅ **repo** (this gives full repository access)

3. Tap **Generate token**

4. **COPY THE TOKEN NOW** (you won't see it again)

5. Back in Claude Code, type:
```
gh auth login --with-token
```

6. Paste your token when prompted

7. Verify with:
```
gh auth status
```

---

### Step 4: Clone Your Repository

**If you know your repo name:**
```
gh repo clone your-username/your-repo-name
```

**If you need to see your repos:**
```
gh repo list
```

This shows all repositories you have access to.

**To clone from the list:**
```
gh repo clone [repo-name-from-list]
```

---

### Step 5: Navigate to Your Repo

```
cd your-repo-name
```

Now you're in your project directory.

---

### Step 6: Verify Everything Works

```
ls -la
```

You should see your project files.

```
git status
```

Should show you're in a git repository.

---

## CLOUD SETTINGS (Automatic on Mobile)

Good news: Cloud sync is **automatic** on the Claude mobile app. Your conversations and project state sync to your account.

**To verify:**
1. Check you're logged into your Claude account (same email you use on desktop)
2. That's it—sync happens automatically

**To continue a session on desktop:**
1. Open Claude on desktop
2. Go to same project
3. Your conversation history is there

---

## COMMON ISSUES & FIXES

### "Permission denied" when cloning

**Cause:** Token doesn't have `repo` scope

**Fix:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Find your Claude Code token
3. Edit and add `repo` scope
4. Re-authenticate: `gh auth logout` then `gh auth login`

---

### "Repository not found"

**Cause:** Private repo you don't have access to, or typo in name

**Fix:**
1. Check exact spelling: `gh repo list | grep "partial-name"`
2. If it's an org repo: `gh repo list [org-name]`
3. If still not found: Check if you have access on github.com

---

### "Not authenticated" keeps appearing

**Cause:** Token expired or auth didn't persist

**Fix:**
1. Run: `gh auth logout`
2. Run: `gh auth login` (start fresh)
3. Use browser auth method for better persistence

---

### "Changes not showing on desktop"

**Cause:** Different project or account

**Fix:**
1. Verify same Claude account on both devices
2. Verify same project selected
3. Give it a minute—sync isn't instant

---

## ONCE SETUP IS COMPLETE

You now have full Claude Code power from your phone:

**What you can do:**
- Clone and work on any of your repos
- Make commits and push changes
- Create and merge pull requests
- Run the same commands as desktop
- Start tasks that continue on desktop

**Recommended first action:**
```
Tell Claude: "Check the status of this repo and suggest what I should work on next"
```

---

## QUICK COMMAND REFERENCE

```
SETUP COMMANDS
gh auth login          - Connect GitHub
gh auth status         - Check connection
gh repo list           - See your repos
gh repo clone [name]   - Download a repo

NAVIGATION
cd [folder]            - Enter folder
ls                     - List files
pwd                    - Show current location

GIT BASICS
git status             - See changes
git add .              - Stage all changes
git commit -m "msg"    - Commit changes
git push               - Push to GitHub

CLAUDE CODE
/doctor                - System health check
/help                  - Available commands
```

---

## YOU'RE READY

Your phone is now a full Claude Code command center.

**Next step:** Load the full Mobile Orchestration Commander prompt for advanced workflows, multi-agent orchestration, and Boris-level productivity from your phone.

---

*Mobile Claude Code Quick-Start Setup*
*10 Minutes to Full Capability*
