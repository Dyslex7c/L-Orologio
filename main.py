import praw

client_id = ""
client_secret = ""
user_agent = ""
username = ""
password = ""

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

target_sub = ""
subreddit = reddit.subreddit(target_sub)
trigger_phrase = "!DyFogliameBot"

while True:
    try:
        for comment in subreddit.stream.comments():
            comments = []
            palindromes = []
            unQ = []
            if trigger_phrase in comment.body and not comment.saved:
                comment.save()
                if comment.body.split()[1] == 'self':
                    user = str(comment.author)
                    reply_comment = 'Looks like someone wanted to check their palindromes usage. A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.'
                else:
                    user = comment.body.split()[1]
                    user_new = ''
                    for a in user:
                        if a != '\\':
                            user_new += a
                    user = user_new
                    reply_comment = 'Looks like someone wanted to check the palindromes usage of u/' + user + '. A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.'
                comObj = reddit.redditor(user).comments.new(limit=None)
                for obj in comObj:
                    comments.append(obj.body)
                for com in comments:
                    for eL in com.split():
                        if eL[::-1] == eL and len(
                                eL) >= 3 and '.' not in eL and '!' not in eL and '-' not in eL and '>' not in eL and '<' not in eL and '#' not in eL:
                            palindromes.append(eL)
                for eL in palindromes:
                    if eL not in unQ:
                        unQ.append(eL)
                reply_comment += "\n\nI have gone through " + str(len(comments)) + " comments and found " + str(
                    len(palindromes)) + " palindromes. Let us take a look at the palindrome usage represented in a tabular format below:\n\n\nPalindromes | No. of usage\n :--: | :--: "
                for eL in unQ:
                    reply_comment += "\n" + eL + ' | ' + str(palindromes.count(eL))
                reply_comment += "\n\n[*how to use.*](https://www.reddit.com/user/DyFogliameBot)\n\n*^This ^action ^was ^performed ^by ^a ^bot. ^If ^you ^find ^this ^information ^interesting, ^please ^do ^consider ^upvoting. ⠀*"
                comment.reply(reply_comment)
                print(f"Replied to {user} successfully...")
    except Exception:
        print("There was an error while running your script. Please try again.")
