# Firebase Quick Setup (5 Minutes)

Follow these steps exactly to get your global leaderboard working!

## Step 1: Create Firebase Project (2 min)

1. **Open**: https://console.firebase.google.com/
2. **Sign in** with your Google account
3. Click **"Add project"** (or "Create a project")
4. **Project name**: `ec201-quiz`
5. **Click "Continue"**
6. **Disable Google Analytics** (toggle off) - we don't need it
7. **Click "Create project"**
8. Wait 30 seconds for it to finish, then click **"Continue"**

## Step 2: Create Realtime Database (1 min)

1. In the left sidebar, click **"Build"** > **"Realtime Database"**
2. Click **"Create Database"**
3. **Location**: Select **"europe-west1"** (Belgium - closest to UK)
4. **Security rules**: Select **"Start in test mode"**
5. Click **"Enable"**

Your database is now created!

## Step 3: Get Your Configuration (1 min)

1. Click the **⚙️ gear icon** next to "Project Overview" (top left)
2. Click **"Project settings"**
3. Scroll down to **"Your apps"** section
4. Click the **`</>`** icon (Web app)
5. **App nickname**: `EC201 Quiz Web`
6. **Don't** check "Firebase Hosting"
7. Click **"Register app"**
8. **COPY** the entire `firebaseConfig` object (looks like this):

```javascript
const firebaseConfig = {
  apiKey: "AIzaSy...",
  authDomain: "ec201-quiz.firebaseapp.com",
  databaseURL: "https://ec201-quiz-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "ec201-quiz",
  storageBucket: "ec201-quiz.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123"
};
```

## Step 4: Update index.html (1 min)

1. **Open** `index.html` in a text editor
2. **Find** line ~600 (search for `const firebaseConfig`)
3. **Replace** the dummy config with YOUR config from Step 3
4. **Save** the file

## Step 5: Secure Your Database (1 min)

1. Go back to Firebase Console
2. Click **"Realtime Database"** in left sidebar
3. Click the **"Rules"** tab
4. **Replace everything** with this:

```json
{
  "rules": {
    "leaderboard": {
      ".read": true,
      ".write": true,
      "$entry": {
        ".validate": "newData.hasChildren(['name', 'score', 'correct', 'total', 'week', 'date', 'timestamp']) && newData.child('name').isString() && newData.child('score').isNumber()"
      }
    }
  }
}
```

5. Click **"Publish"**

## Step 6: Deploy! (30 seconds)

Run these commands in Terminal:

```bash
cd "/Users/Alborz/Desktop/Warwick/Macro 2"
git add .
git commit -m "Add Firebase configuration and first-attempt-only scoring"
git push
```

## Done! 🎉

Wait 1-2 minutes, then visit:
**https://alborznokhostin.github.io/ec201-quiz/**

The global leaderboard will now work!

## Test It

1. Take the quiz with your name
2. Check the leaderboard - you should see your score
3. Share the link with a friend
4. Have them take the quiz
5. Both of you will see each other's scores!

## Troubleshooting

**"Firebase is not defined" error?**
- Make sure you copied the ENTIRE firebaseConfig from Step 3
- Check that the databaseURL includes "europe-west1"

**Leaderboard shows "Loading..." forever?**
- Check Firebase Console > Realtime Database > Rules tab
- Make sure rules show `.read: true` and `.write: true`

**Scores not appearing?**
- Open browser Console (F12) and look for errors
- Check your Firebase Database > Data tab - you should see entries appearing

---

Need help? The Firebase console will show any errors in real-time!
