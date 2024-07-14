# 🧠 AI Trivia Bot 🤖

Welcome to the AI Trivia Bot project! This bot fetches the latest and most interesting facts from Reddit and turns them into engaging trivia tweets, sharing them with the world on Twitter. It's powered by the latest advancements in AI from Google's Gemini API and automated using the robust capabilities of PRAW (Python Reddit API Wrapper) and Tweepy.

## 🚀 Features

- **Reddit Integration**: Fetches top daily top & relevant posts from reddit.
- **AI-Powered Content Generation**: Utilizes Google's Gemini API to transform Reddit posts into succinct and interesting trivia tweets.
- **Automated Tweeting**: Seamlessly posts the generated trivia to Twitter, keeping your followers informed and entertained.

## 📦 Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/ashr-exe/trivia-bot.git
   cd ai-trivia-bot

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt

3. **Set Up Environment Variables:**
   Create a .env file in the project root and add your API keys and tokens:
   
   ```sh
   GOOGLE_API_KEY=your_google_api_key
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   REDDIT_USER_AGENT=your_reddit_user_agent
   TWITTER_API_KEY=your_twitter_api_key
   TWITTER_API_SECRET=your_twitter_api_secret
   TWITTER_BEARER_TOKEN=your_twitter_bearer_token
   TWITTER_ACCESS_TOKEN=your_twitter_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

4. **Run the Bot::**
   ```sh
   python main.py


## 🌐 Deploy on Render

You can easily deploy this bot on Render and let it run 24/7. Follow these steps:

1. **Create a New Web Service** on Render.
2. **Connect to Your GitHub Repository** and select this project.
3. **Add Environment Variables** in the Render dashboard.
4. **Deploy and Monitor** your bot as it entertains and educates the world!

## 🛠 Technologies Used

- **Python**: The core language for this project.
- **PRAW**: For seamless interaction with Reddit.
- **Tweepy**: To connect and post tweets to Twitter.
- **Google Generative AI (Gemini API)**: For transforming Reddit posts into engaging trivia.

## 🤝 Contributing

We welcome contributions! Feel free to fork the repository and submit pull requests. Please make sure to follow the contribution guidelines.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ✨ Acknowledgments

- Special thanks to the developers of [PRAW](https://praw.readthedocs.io/en/latest/) and [Tweepy](https://www.tweepy.org/) for their amazing libraries.
- Kudos to the [Google Generative AI](https://ai.google/tools/) team for their powerful API.


   
   
