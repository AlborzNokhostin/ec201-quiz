# Firebase Setup Guide for Global Leaderboard

The quiz now uses Firebase Realtime Database for a **global competitive leaderboard** where all students can see each other's scores!

## Quick Setup (5 minutes)

### Step 1: Create Firebase Project

1. Go to https://console.firebase.google.com/
2. Click "Add project"
3. Project name: `ec201-quiz`
4. Disable Google Analytics (not needed)
5. Click "Create project"

### Step 2: Set Up Realtime Database

1. In your Firebase project, click "Realtime Database" in the left menu
2. Click "Create Database"
3. Choose location: **Europe (europe-west1)** (closest to UK)
4. Start in **test mode** (we'll secure it later)
5. Click "Enable"

### Step 3: Get Your Configuration

1. Click the gear icon ⚙️ next to "Project Overview"
2. Click "Project settings"
3. Scroll down to "Your apps"
4. Click the **Web** icon `</>`
5. App nickname: `EC201 Quiz`
6. Click "Register app"
7. **Copy the firebaseConfig object**

### Step 4: Update index.html

Replace the Firebase configuration in `index.html` (around line 600) with your own config:

```javascript
const firebaseConfig = {
    apiKey: "YOUR-API-KEY",
    authDomain: "YOUR-PROJECT.firebaseapp.com",
    databaseURL: "https://YOUR-PROJECT.firebasedatabase.app",
    projectId: "YOUR-PROJECT-ID",
    storageBucket: "YOUR-PROJECT.appspot.com",
    messagingSenderId: "YOUR-SENDER-ID",
    appId: "YOUR-APP-ID"
};
```

### Step 5: Secure Your Database

1. Go back to Realtime Database
2. Click "Rules" tab
3. Replace with these rules:

```json
{
  "rules": {
    "leaderboard": {
      ".read": true,
      ".write": true,
      "$entry": {
        ".validate": "newData.hasChildren(['name', 'score', 'correct', 'total', 'week', 'date', 'timestamp'])"
      }
    }
  }
}
```

4. Click "Publish"

### Step 6: Deploy

```bash
cd "/Users/Alborz/Desktop/Warwick/Macro 2"
git add .
git commit -m "Add Firebase global leaderboard and Warwick logo"
git push
```

## Features

✅ **Global Leaderboard**: All students see the same leaderboard
✅ **Real-time Updates**: Scores appear instantly
✅ **Top 20 Displayed**: Shows top 20 scores with rankings
✅ **Gold/Silver/Bronze Badges**: For top 3 positions
✅ **Automatic Fallback**: Uses localStorage if Firebase unavailable

## Privacy Note

The leaderboard shows:
- Student name (as entered)
- Score percentage
- Number correct/total
- Which week they took
- Date taken

Students control what name they enter.

## Cost

Firebase free tier includes:
- 1GB storage
- 10GB/month downloads
- 100 simultaneous connections

This is MORE than enough for your class!

## Troubleshooting

**Leaderboard not loading?**
- Check browser console for errors
- Verify Firebase config is correct
- Check Database Rules allow read/write

**Scores not saving?**
- Check Firebase Database Rules
- Verify internet connection
- Check browser console for errors
