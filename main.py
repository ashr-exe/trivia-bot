import praw
import tweepy
import datetime
import pytz
import time
import logging
import os
from tweepy.errors import TweepyException
from keep_alive import keep_alive


# Set up logging
logging.basicConfig(level=logging.INFO)

# Retrieve API keys from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
USER_AGENT = os.getenv('REDDIT_USER_AGENT')
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

if not all([GOOGLE_API_KEY, CLIENT_ID, CLIENT_SECRET, USER_AGENT, TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_BEARER_TOKEN, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET]):
    raise ValueError("One or more environment variables are missing.")

print("Environment variables loaded successfully.")

# Configure Google Generative AI
import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')
print("Google Generative AI configured successfully.")

# Create a Reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)
print("Reddit instance created successfully.")

# Establishing connection to Twitter API using Client
client = tweepy.Client(
    TWITTER_BEARER_TOKEN,
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)
print("Twitter API client connected successfully.")

# Global list to store trivia tweets
trivia_tweets = []

def fetch_and_sort_top_posts(subreddit_name):
    """Fetch top posts from the subreddit in the current day and sort them."""
    try:
        print(f"Fetching top posts from r/{subreddit_name}...")
        subreddit = reddit.subreddit(subreddit_name)
        top_posts = subreddit.top(time_filter='day', limit=12)  # Limit to 12 top posts
        posts = list(top_posts)
        print(f"Fetched {len(posts)} top posts from r/{subreddit_name}.")
        return posts
    except Exception as e:
        logging.error(f"Error fetching posts from subreddit {subreddit_name}: {e}")
        return []

def generate_trivia_tweet(post_title, post_url):
    """Generates a trivia tweet using the Gemini API."""
    prompt = (
        f"Must ensure token count is less than 60 (VERY IMPORTANT)!"
        f"convert this into a trivia tweet (not question and don't add TIL etc in starting): {post_title}\n"
        f"add more details from this article {post_url}. Keep the tone professional. "
        f"No need to do markdowns or add links to article. Strictly adhere to the token limit of 60 tokens.\n"
    )

    try:
        print(f"Generating trivia tweet for post: {post_title}")
        response = model.generate_content(prompt, safety_settings={'HARASSMENT': 'block_none', 'SEXUALLY_EXPLICIT': 'block_none'})
        print(f"Generated trivia tweet: {response.text}")
        return response.text
    except Exception as e:
        logging.error(f"Error generating trivia tweet: {e}")
        return None

def update_trivia_tweets():
    global trivia_tweets
    subreddit_name = 'todayilearned'  # Example subreddit, replace with your desired subreddit
    sorted_posts = fetch_and_sort_top_posts(subreddit_name)

    if sorted_posts:
        print(f"Updating trivia tweets from r/{subreddit_name}.")
        trivia_tweets = []
        for post in sorted_posts:
            trivia_tweet = generate_trivia_tweet(post.title, post.url)
            time.sleep(30)
            if trivia_tweet:
                trivia_tweets.append(trivia_tweet)
                if len(trivia_tweets) >= 12:
                    break
        print(f"Generated {len(trivia_tweets)} trivia tweets.")
    else:
        logging.error(f"No top posts found in r/{subreddit_name} for the current day.")

def post_trivia_tweets():
    for i, tweet_text in enumerate(trivia_tweets):
        try:
            print(f"Posting tweet {i+1}/{len(trivia_tweets)}: {tweet_text}")
            client.create_tweet(text=tweet_text)
            logging.info(f"Tweet {i+1} successfully posted: {tweet_text}")
        except TweepyException as e:
            logging.error(f"Tweepy error occurred while posting tweet {i+1}: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred while posting tweet {i+1}: {e}")
        time.sleep(60)  # Wait for 1 minute before posting the next tweet

def main():
    print("Starting the update and posting process...")
    update_trivia_tweets()
    post_trivia_tweets()
    print("Finished posting all trivia tweets.")

if __name__ == "__main__":
    keep_alive()
    main()
