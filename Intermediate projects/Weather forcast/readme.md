# Weather Forecast Notification App Guide

Welcome to the Weather Forecast Notification App! This guide will help you understand how to set up and use the app to automatically send weather forecasts to your phone number via SMS.

## How to Use

### Setup

1. **Install Dependencies:**
   - Ensure you have `requests` and `twilio` libraries installed.

   ```bash
   pip install requests twilio
   ```

2. **API Keys and Credentials:**
   - **OpenWeatherMap API Key:** Sign up at [OpenWeatherMap](https://openweathermap.org/) and get your API key.
   - **Twilio Account SID and Auth Token:** Sign up at [Twilio](https://www.twilio.com/) and get your Account SID and Auth Token.
   - **Twilio Phone Numbers:** Get a Twilio virtual number and verify your personal phone number.

3. **Customize Location:**
   - Update the latitude and longitude values in the `parameters` dictionary to your desired location.

### Code Configuration

- Replace the placeholder strings with your actual credentials and phone numbers:

  ```python
  api_key = "YOUR_OPENWEATHERMAP_API_KEY"
  account_sid = "YOUR_TWILIO_ACCOUNT_SID"
  auth_token = "YOUR_TWILIO_AUTH_TOKEN"
  ```

### How It Works

1. **Fetch Weather Data:**
   - The app sends a request to the OpenWeatherMap API with the specified location coordinates.
   - It retrieves the weather forecast data.

2. **Check for Rain:**
   - The app checks the weather conditions in the forecast data.
   - If the condition code indicates rain (codes less than 700), it sets a flag (`will_rain`) to True.

3. **Send SMS Notification:**
   - If rain is detected, the app sends an SMS notification to your phone using Twilio.
   - The message will remind you to bring an umbrella.

### Run the App

- Run the script to check the weather and send an SMS notification if rain is detected.

## Additional Information

- The app uses the OpenWeatherMap API to fetch weather data and Twilio API to send SMS.
- Customize the frequency and conditions for sending notifications as per your requirements.

Enjoy using the Weather Forecast Notification App to stay prepared for the weather!


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