import praw
import json

# Step 1: Connect to Reddit using PRAW
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT"
)

# Step 2: Fetch Reddit posts
subreddit_name = "learnpython"  # Specify the subreddit to scrape
subreddit = reddit.subreddit(subreddit_name)

# Fetch the top 10 hot posts
posts = []
for post in subreddit.hot(limit=10):
    post_data = {
        "id": post.id,
        "title": post.title,
        "score": post.score,
        "num_comments": post.num_comments,
        "url": post.url,
        "created_utc": post.created_utc,
        "author": str(post.author),
    }
    posts.append(post_data)

# Step 3: Save data to a JSON file
output_file = f"{subreddit_name}_posts.json"
with open(output_file, "w") as json_file:
    json.dump(posts, json_file, indent=4)

print(f"Data from subreddit '{subreddit_name}' saved to '{output_file}'")
