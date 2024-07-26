# Stock Price Alert and News Notification Script Guide

Welcome to the Stock Price Alert and News Notification Script! This guide will help you understand how to set up and use the script to automatically send you price alerts for your desired stocks along with relevant news articles if there is a significant price movement. You can run this script on [pythonanywhere.com](https://www.pythonanywhere.com/) for automation.

## How to Use

### Setup

1. **Install Dependencies:**
   - Ensure you have `requests` and `twilio` libraries installed.

   ```bash
   pip install requests twilio
   ```

2. **API Keys and Credentials:**
   - **Alpha Vantage API Key:** Sign up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and get your API key.
   - **News API Key:** Sign up at [News API](https://newsapi.org/register) and get your API key.
   - **Twilio Account SID and Auth Token:** Sign up at [Twilio](https://www.twilio.com/) and get your Account SID and Auth Token.
   - **Twilio Phone Numbers:** Get a Twilio virtual number and verify your personal phone number.

### Code Configuration

- Replace the placeholder strings with your actual credentials and phone numbers:
  
  ```python
  VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
  VERIFIED_NUMBER = "your own phone number verified with Twilio"
  STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
  NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
  TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
  TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
  ```

- Customize the stock name and company name:

  ```python
  STOCK_NAME = "TSLA"
  COMPANY_NAME = "Tesla Inc"
  ```

### How It Works

1. **Fetch Stock Data:**
   - The script fetches the stock data for the specified stock from the Alpha Vantage API.
   - It retrieves the closing prices for yesterday and the day before yesterday.

2. **Calculate Price Difference:**
   - The script calculates the difference and percentage difference between the closing prices of the two days.

3. **Fetch News Articles:**
   - If the price difference exceeds a certain threshold (e.g., 5%), the script fetches the latest news articles related to the company from the News API.

4. **Send SMS Notifications:**
   - The script formats the stock price change and news articles into messages.
   - It sends the messages to your phone using Twilio.

## Additional Information

- The app uses the Alpha Vantage API to fetch stock data and the News API to fetch related news articles.
- Customize the frequency and conditions for sending notifications as per your requirements.
- The script can be automated to run at regular intervals using a scheduler like cron or by deploying it on [pythonanywhere.com](https://www.pythonanywhere.com/).

Enjoy using the Stock Price Alert and News Notification Script to stay informed about significant stock price movements and related news!
