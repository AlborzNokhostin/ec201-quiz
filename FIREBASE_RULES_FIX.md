# Fix Firebase Leaderboard - Database Rules

Your leaderboard is showing local data only because the Firebase database rules need to be configured.

## Quick Fix (2 minutes)

1. **Go to Firebase Console**: https://console.firebase.google.com/
2. **Select your project**: `ec201-c1bb6`
3. **Click "Realtime Database"** in the left sidebar
4. **Click the "Rules" tab** (next to "Data")
5. **Replace everything** with this code:

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

6. **Click "Publish"** button

## Test It

1. Open the quiz on your Mac: https://alborznokhostin.github.io/ec201-quiz/
2. Take the quiz with a test name
3. Open browser console (F12) - you should see: `Score saved to global leaderboard`
4. Open the quiz on your iPhone
5. You should see your Mac score in the leaderboard!

## How to Check if Rules are Applied

1. In Firebase Console > Realtime Database > **Data tab**
2. You should see a `leaderboard` node appear when someone takes a quiz
3. Click on it to see all the scores

---

**Important**: Without these rules, Firebase blocks all read/write access, so the quiz falls back to localStorage (which is device-specific).
