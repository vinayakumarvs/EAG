// config.js - Loads API keys from .env file

// In a real production environment, this would use a more secure method 
// to load environment variables. For this demo, we're directly embedding values
// that will be replaced during the build process or manually by the user.

const CONFIG = {
  GEMINI_API_KEY: 'YOUR_GEMINI_API_KEY', // Replace with actual key or import from .env
  ALPHA_VANTAGE_API_KEY: 'YOUR_VANTAGE_API_KEY' // Using demo key for testing. Replace with your actual key for production use.
};

// Export the configuration
if (typeof module !== 'undefined' && module.exports) {
  module.exports = CONFIG;
} 
