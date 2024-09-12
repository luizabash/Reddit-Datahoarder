import praw
import pandas as pd

# Reddit API connection
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',         # Replace with your client ID
    client_secret='YOUR_CLIENT_SECRET', # Replace with your client secret
    user_agent='TrendAnalyzer',   # Replace with a descriptive user agent
    username='YOUR_REDDIT_USERNAME',    # Replace with your Reddit username
    password='YOUR_REDDIT_PASSWORD'     # Replace with your Reddit password
)

# extract posts from a subreddit
def extract_reddit_posts(subreddit_name, limit=1000):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    # iterate through posts in the subreddit
    for post in subreddit.hot(limit=limit):
        posts.append({
            'title': post.title,
            'score': post.score,
            'id': post.id,
            'url': post.url,
            'comms_num': post.num_comments,
            'created': post.created,
            'body': post.selftext
        })

    # convert to DataFrame
    posts_df = pd.DataFrame(posts)
    return posts_df

subreddit_name = 'datahoarder'  # Specify the subreddit you want to analyze
data = extract_reddit_posts(subreddit_name)

data.to_csv('data/datahoarder_posts_raw.csv', index=False)

print(f"Data collection complete. {len(data)} posts saved to 'data/datahoarder_posts_raw.csv'.")
