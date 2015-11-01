# DeadSubDetector
Detects dead subreddits from a users subscribed list.

## Usage
- The `--type` flag is used to pass either `empty` or `dead`.
- The `--count` flag is used to pass the number to be used with each. Default value is 50.

#### empty
This will return all subreddits from a users subscriptions which it's top post in the past 24hrs has less than `--count`'s value of upvotes.  
This is useful for small subreddits where items with a few upvotes make it to the users front page but sometimes this isn't a bad thing so each sub should be checked independently.


#### dead
This will return all subreddits from a users subscriptions which it's latest post is older than `--count`'s value of days.  
Useful as it can find subreddits with no posts in a while. Mainly for subscription clean-up.
