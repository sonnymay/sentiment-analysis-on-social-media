# Social Media Sentiment Analysis

This repository contains a Python script for performing sentiment analysis on Twitter data. By using Tweepy to access Twitter's API and TextBlob for sentiment analysis, you can evaluate the sentiment of tweets containing specific keywords or hashtags.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- A Twitter Developer Account

### Installing

1. Clone this repository:

    ```
    git clone https://github.com/sonnymay/social-media-sentiment-analysis.git
    cd social-media-sentiment-analysis
    ```

2. Install the required Python libraries:

    ```
    pip install tweepy textblob
    ```

3. Setup a Twitter Developer Account:

    - Go to the [Twitter Developer's page](https://developer.twitter.com/) and apply for a developer account.
    - Create an app and generate consumer keys and access tokens.

4. Add your Twitter API credentials to the script:

    - Open the script in a text editor and replace `'YOUR_CONSUMER_KEY'`, `'YOUR_CONSUMER_SECRET'`, `'YOUR_ACCESS_TOKEN'`, and `'YOUR_ACCESS_TOKEN_SECRET'` with your own credentials.

### Usage

Run the script using Python and provide a keyword or hashtag as an argument:

```sh
python sentiment_analysis.py 'keyword or hashtag'
```

The script will retrieve tweets containing the specified keyword or hashtag and analyze their sentiment, printing the results to the console.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [sonnymay](https://github.com/sonnymay)

## Acknowledgments

- Twitter API
- Tweepy library
- TextBlob library

---
