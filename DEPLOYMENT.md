# Deployment Instructions

Follow these steps to deploy your quiz to GitHub Pages and get a shareable link.

## Prerequisites

- A GitHub account (create one at https://github.com if you don't have one)
- Git installed on your computer (already done)

## Step-by-Step Deployment

### 1. Create a GitHub Repository

1. Go to https://github.com and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Enter repository details:
   - **Repository name**: `ec201-quiz` (or any name you prefer)
   - **Description**: "EC201 International Macroeconomics Quiz with Leaderboard"
   - **Visibility**: Choose "Public" (so others can access it)
   - **DO NOT** initialize with README (we already have files)
5. Click "Create repository"

### 2. Link Your Local Repository to GitHub

GitHub will show you commands to run. Use these commands in your terminal:

```bash
cd "/Users/Alborz/Desktop/Warwick/Macro 2"
git remote add origin https://github.com/YOUR-USERNAME/ec201-quiz.git
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

### 3. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" (top right)
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click "Save"

### 4. Rename quiz.html to index.html

For GitHub Pages to work properly, rename the file:

```bash
cd "/Users/Alborz/Desktop/Warwick/Macro 2"
mv quiz.html index.html
git add .
git commit -m "Rename quiz.html to index.html for GitHub Pages"
git push
```

### 5. Access Your Live Quiz

After a few minutes, your quiz will be available at:

```
https://YOUR-USERNAME.github.io/ec201-quiz/
```

## Sharing the Quiz

Once deployed, you can share this URL with anyone:
- Your classmates
- Study groups
- Social media
- Email

The quiz works on any device with a web browser!

## Updating the Quiz

To make changes:

1. Edit the files locally
2. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```
3. Changes will appear on the live site within a few minutes

## Troubleshooting

**Quiz not showing up?**
- Make sure the file is named `index.html` not `quiz.html`
- Wait 5-10 minutes for GitHub Pages to build
- Check the Pages section in Settings for any error messages

**Leaderboard not working across devices?**
- This is expected! The leaderboard uses localStorage which is device-specific
- Each browser/device has its own leaderboard
- This is intentional for privacy and simplicity

## Alternative: Quick Deploy with GitHub Desktop

If you prefer a GUI:

1. Download GitHub Desktop from https://desktop.github.com/
2. Open it and sign in
3. Add your local repository
4. Publish to GitHub
5. Follow steps 3-4 above for enabling Pages
