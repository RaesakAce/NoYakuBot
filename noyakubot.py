import praw
import pdb
import re
import os
reddit = praw.Reddit('bot1')
 
subreddit = reddit.subreddit("mahjong")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    #print(submission.title)

 # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("(?=.*cannot)(?=.*win)",submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply('''Your hand might not have yaku, or you might be in furiten.
            check the Riichi F.A.Q. here:
            https://www.reddit.com/r/Mahjong/comments/cdg75k/riichi_japanese_mahjong_faq''')
            print("Bot replying to : ", submission.title)
        elif re.search("(?=.*cannot)(?=.*win)",submission.selftext, re.IGNORECASE):
            # Reply to the post
            submission.reply('''Your hand might not have yaku, or you might be in furiten.
            check the Riichi F.A.Q. here:
            https://www.reddit.com/r/Mahjong/comments/cdg75k/riichi_japanese_mahjong_faq''')
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")    
