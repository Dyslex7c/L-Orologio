# [DyFogliame](https://www.reddit.com/user/DyFogliameBot)
![python](http://ForTheBadge.com/images/badges/made-with-python.svg)

A Reddit bot made using `PRAW` library that shows data about the various palindromes used by a single user in a tabular format.

The source of [u/DyFogliameBot](https://www.reddit.com/user/DyFogliameBot), it replies to the user concerned when summoned.

# Main Features
- Streams upto 1000 comments/replies of a user at a time
- Detects any word which fits into the definition of a palindrome - be it numeric or literal or even a symbol

### Using the bot:
- Navigate to https://www.reddit.com/prefs/apps and create an app as a script
- Set a valid redirect URL
- After creating the app, set your `client_id` and `client_secret` from the webpage. Set your `username` and `password` as well.
- Navigate to your bot directory and run `python main.py`

# Drawbacks 
- Unable to detect phrasal palindromes
- The table might not be displayed properly in some rare cases

# Summoning the Bot:
```reddit
!DyFogliameBot self
```
Check someone else's by replying them
```reddit
!DyFogliameBot [username]
```

Currently, the bot is inactive. You can make your own bot using the concept from the repo. Make sure to follow [bottiquette](https://www.reddit.com/wiki/bottiquette/).

# Got Questions?
[![Whatsapp](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/40px-WhatsApp.svg.png)](https://api.whatsapp.com/send?phone=917980369670&text=)
¡DM me on WhatsApp!
