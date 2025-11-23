# Poll Troubleshooting Guide

If the poll is not working, follow these steps to diagnose the issue.

## Step 1: Check Browser Console

1. Open the quiz: https://alborznokhostin.github.io/ec201-quiz/
2. Press **F12** (or right-click → Inspect)
3. Click the **Console** tab
4. Try clicking a poll option
5. Look for these messages:

### Expected Messages (Poll Working):
```
Poll initialized successfully
Selected poll option: week1
Vote button enabled
```

### Error Messages (Poll Not Working):

**If you see: "Firebase not available for poll"**
- Problem: Firebase scripts not loading
- Solution: Refresh the page and wait a few seconds

**If you see: "pollVotesRef is null"**
- Problem: Firebase database not initialized
- Solution: Check Firebase configuration in index.html (around line 2900)

**If you see: "PERMISSION_DENIED"**
- Problem: Firebase database rules not configured
- Solution: Follow Step 2 below

## Step 2: Update Firebase Database Rules

This is the most common issue! You MUST update your Firebase rules to allow poll access.

1. Go to: https://console.firebase.google.com/
2. Select project: `ec201-c1bb6`
3. Click **"Realtime Database"** in left sidebar
4. Click **"Rules"** tab
5. Check if you see `"poll"` section in the rules

### Correct Rules (with poll support):
```json
{
  "rules": {
    "leaderboard": {
      ".read": true,
      ".write": true,
      "$entry": {
        ".validate": "newData.hasChildren(['name', 'score', 'correct', 'total', 'week', 'date', 'timestamp']) && newData.child('name').isString() && newData.child('score').isNumber()"
      }
    },
    "chat": {
      ".read": true,
      ".write": true,
      "$message": {
        ".validate": "newData.hasChildren(['name', 'message', 'timestamp', 'date']) && newData.child('name').isString() && newData.child('message').isString() && newData.child('message').val().length <= 500"
      }
    },
    "poll": {
      "votes": {
        ".read": true,
        ".write": true
      }
    }
  }
}
```

6. If the `"poll"` section is missing, add it
7. Click **"Publish"**
8. Refresh your quiz page

## Step 3: Test the Poll

1. Refresh the quiz page: https://alborznokhostin.github.io/ec201-quiz/
2. Scroll down to the poll section
3. Click on "Week 1: Global Imbalances"
4. Check console - should see: `Selected poll option: week1`
5. The option should highlight with a blue background
6. The "Vote" button should become enabled (not grayed out)
7. Click "Vote"
8. Should see alert: "Thank you for voting! 🎉"

## Step 4: Verify Vote was Saved

1. Go to Firebase Console
2. Click **Realtime Database** → **Data** tab
3. Look for `poll` → `votes` node
4. You should see something like:
```
poll
  └─ votes
      ├─ week1: 1
      ├─ week2: 0
      ├─ week3: 0
      ...
```

## Common Issues and Solutions

### Issue: "Vote button stays grayed out"
**Cause:** JavaScript error preventing event handler
**Solution:**
- Check browser console for errors
- Try a different browser (Chrome, Firefox, Safari)
- Clear browser cache and reload

### Issue: "Nothing happens when clicking poll options"
**Cause:** onclick event not firing
**Solution:**
- Check console for errors
- Make sure JavaScript is enabled in browser
- Try clicking directly on the text, not the border

### Issue: "Alert says 'Poll is not connected to Firebase'"
**Cause:** Firebase not initialized
**Solution:**
- Wait 2-3 seconds after page load
- Refresh the page
- Check Firebase configuration

### Issue: "Already voted, but want to test again"
**Cause:** Vote stored in localStorage
**Solution:**
1. Open browser console (F12)
2. Go to **Application** tab (Chrome) or **Storage** tab (Firefox)
3. Click **Local Storage** → your site URL
4. Find `ec201_poll_voted`
5. Right-click → Delete
6. Refresh page

## Still Not Working?

If none of the above works:

1. **Share the console error messages** - Press F12, go to Console tab, take a screenshot
2. **Check Firebase status** - Go to Firebase Console → Realtime Database → Data tab
3. **Try incognito mode** - Open quiz in private/incognito window
4. **Test on different device** - Try on phone or different computer

## Quick Test Commands

Open browser console and run these:

```javascript
// Check if Firebase is loaded
console.log(typeof firebase);  // Should be "object"

// Check if poll is initialized
console.log(pollVotesRef);  // Should NOT be null/undefined

// Check current state
console.log({ selectedPollOption, hasVoted });

// Manually trigger poll initialization
initializePoll();
```

---

**Need more help?** Use the chat feature on the quiz site to ask for assistance!
