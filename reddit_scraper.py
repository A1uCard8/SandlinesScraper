import praw
import json

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT"
)

subreddit_name = "politics"  # Specify the subreddit to scrape
subreddit = reddit.subreddit(subreddit_name)

posts = []
for post in subreddit.hot(limit=50):
    post.comments.replace_more(limit=0)
    comments = []

    for comment in post.comments.list()[:10]:
        comments.append({
            "id": comment.id,
            "author": str(comment.author),
            "body": comment.body,
            "score": comment.score,
            "created_utc": comment.created_utc
        })
    
    posts.append({
        "id": post.id,
        "title": post.title,
        "score": post.score,
        "num_comments": post.num_comments,
        "url": post.url,
        "created_utc": post.created_utc,
        "author": str(post.author),
        "comments": comments  # Nested comments data
    })

output_file = f"{subreddit_name}_posts_with_comments.json"
with open(output_file, "w") as json_file:
    json.dump(posts, json_file, indent=4)

print(f"Data from subreddit '{subreddit_name}' saved to '{output_file}'")
