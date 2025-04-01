# Stock Price Analyzer Chrome Extension

A Chrome extension that uses Gemini-2.0-flash LLM to analyze stock prices and provide insights.

## Features

- Simple and intuitive UI
- Real-time stock data from Alpha Vantage API
- AI-powered analysis using Google's Gemini 2.0 Flash model
- Buy/hold/sell recommendations based on current stock metrics
- Notification alerts for stocks that have increased by 2% or more in the last 5 trading days

## Installation Instructions

1. Clone or download this repository
2. Set up your API keys (see below)
3. Open Chrome and navigate to `chrome://extensions/`
4. Enable "Developer mode" in the top-right corner
5. Click "Load unpacked" and select the folder containing this extension
6. The Stock Price Analyzer extension should now be installed and visible in your Chrome toolbar

## Setting Up API Keys

You have two options for configuring API keys:

### Option 1: Edit the config.js file (recommended)

1. Open the `config.js` file in the extension directory
2. Replace the placeholder values with your actual API keys:
   ```javascript
   const CONFIG = {
     GEMINI_API_KEY: 'your_actual_gemini_api_key',
     ALPHA_VANTAGE_API_KEY: 'your_actual_alpha_vantage_key'
   };
   ```

### Option 2: Use the .env file

1. Open the `.env` file in the extension directory
2. Replace the placeholder values with your actual API keys:
   ```
   GEMINI_API_KEY=your_actual_gemini_api_key
   ALPHA_VANTAGE_API_KEY=your_actual_alpha_vantage_key
   ```
3. Note: This method requires an additional build step to inject the environment variables

## Usage

1. Click on the Stock Price Analyzer icon in your Chrome toolbar
2. Enter a valid stock symbol (e.g., AAPL for Apple, GOOGL for Google)
3. Click "Analyze"
4. View the AI-generated analysis of the stock
5. Receive a notification if the stock has increased by 2% or more in the last 5 trading days

## Getting API Keys

### Gemini API Key
1. Visit the [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create an account or sign in
3. Create a new API key
4. Copy the API key to use with this extension

### Alpha Vantage API Key
1. Visit [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
2. Register for a free API key
3. Copy the API key to use with this extension

## Note

This extension uses:
- Alpha Vantage for stock data
- Gemini 2.0 Flash model for AI-powered analysis

This is for educational purposes only. Always do your own research before making investment decisions. 