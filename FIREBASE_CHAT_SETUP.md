# Firebase Chat Setup - Update Database Rules

Your quiz now has a real-time chat feature! To enable it, you need to update your Firebase database rules.

## Quick Update (1 minute)

1. **Go to Firebase Console**: https://console.firebase.google.com/
2. **Select your project**: `ec201-c1bb6` (or your project name)
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
    },
    "chat": {
      ".read": true,
      ".write": true,
      "$message": {
        ".validate": "newData.hasChildren(['name', 'message', 'timestamp', 'date']) && newData.child('name').isString() && newData.child('message').isString() && newData.child('message').val().length <= 500"
      }
    }
  }
}
```

6. **Click "Publish"** button

## What This Does

- **Leaderboard**: Keeps existing leaderboard functionality (read/write for scores)
- **Chat**: Adds new chat functionality with:
  - Public read/write access (anyone can read and send messages)
  - Message validation (must have name, message, timestamp, date fields)
  - 500 character limit per message
  - Messages must be strings

## How the Chat Works

1. **Floating Chat Button**: A purple chat icon (💬) appears in the bottom-right corner of the screen
2. **Click to Open**: Click the button to open the chat window
3. **Real-time Messages**: All users see messages instantly as they're sent
4. **User Names**: Messages show the name entered in the quiz (or "Anonymous" if not set)
5. **Timestamps**: Each message shows the time it was sent

## Features

- ✅ Real-time messaging (messages appear instantly for all users)
- ✅ Beautiful glassmorphism design matching the quiz theme
- ✅ Mobile responsive
- ✅ Message history (all past messages load when you open the chat)
- ✅ Enter key to send messages
- ✅ Auto-scroll to newest messages
- ✅ 500 character limit per message

## Test It

1. Open the quiz: https://alborznokhostin.github.io/ec201-quiz/
2. Click the purple chat button (💬) in the bottom-right
3. Enter your name if you haven't already
4. Type a message and press Enter or click Send
5. Open the quiz on another device or browser
6. You should see your message appear on both devices!

## Security Notes

- **Public Access**: Anyone can read and send messages (designed for a class environment)
- **No Moderation**: Messages are not filtered or moderated
- **Character Limit**: Messages are limited to 500 characters
- **No Deletion**: Users cannot delete messages (only admins can via Firebase Console)

## Managing Messages (Admin)

To view or delete messages:
1. Go to Firebase Console > Realtime Database > **Data tab**
2. Expand the `chat` node
3. You'll see all messages with timestamps
4. Right-click any message to delete it

## Privacy Considerations

Since this is a public class chat:
- Remind students not to share personal information
- Check the chat periodically for inappropriate content
- You can disable the chat by removing write permissions in the rules

---

**Need to disable chat temporarily?**
Change the chat rules to:
```json
"chat": {
  ".read": true,
  ".write": false
}
```

This will make the chat read-only (existing messages visible, but no new messages can be sent).
