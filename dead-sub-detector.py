import praw, calendar, time, argparse

# Argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="Pass 'empty' to return all subreddits that it's top post in the last 24 hours has less upvotes than the number passed with '--count'.\
Pass 'dead' to return all subreddits that have had no posts for the number of days passed with '--count'.")
parser.add_argument("--count", help="Corresponding count for '--type'. Default=50.", default=50, type=int)
args = parser.parse_args()

# Login
r = praw.Reddit('DeadSubDetector')
r.login("username", "password", disable_warning=True)

subreddits = r.get_my_subreddits(limit=None)


# Function to find subreddits with a low userbase.
def low_upvotes(x):
    for subreddit in subreddits:
        posts = r.get_subreddit(str(subreddit)).get_top_from_day(limit=1)

        upvotes = []
        for post in posts:
            upvotes.append(int(str(post).split(' ')[0]))

        if all(i < x for i in upvotes):
            print (str(subreddit) + " is a dead sub...")

# Function for finding subreddits with no recent posts.
def old_posts(x):
    for subreddit in subreddits:
        posts = r.get_subreddit(str(subreddit)).get_new(limit=1)

        for post in posts:
            # If post is older than x days.
            if post.created < (calendar.timegm(time.gmtime()) - 86400*x):
                print (subreddit)

# Act accordingly from args.
if args.type == 'empty':
    low_upvotes(args.count)
elif args.type == 'dead':
    old_posts(args.count)
