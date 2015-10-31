import praw

r = praw.Reddit('DeadSubDetector ')
r.login("", "")

subreddits = r.get_my_subreddits(limit=None)

i = 0
for subreddit in subreddits:
    print(subreddit)
print(i)
