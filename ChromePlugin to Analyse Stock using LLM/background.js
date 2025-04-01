// Import config if available
let CONFIG = {};
try {
  if (typeof window !== 'undefined' && window.CONFIG) {
    CONFIG = window.CONFIG;
  } else if (typeof importScripts === 'function') {
    importScripts('config.js');
  }
} catch (error) {
  console.error('Unable to load config:', error);
}

// Listener for when the extension is installed
chrome.runtime.onInstalled.addListener(function() {
  console.log('Stock Price Analyzer extension installed');
  
  // Initialize storage with API keys from config if available
  chrome.storage.local.get(['geminiApiKey'], function(result) {
    // If we have a key in CONFIG, use it
    if (CONFIG && CONFIG.GEMINI_API_KEY && CONFIG.GEMINI_API_KEY !== 'your_gemini_api_key_here') {
      chrome.storage.local.set({ geminiApiKey: CONFIG.GEMINI_API_KEY });
    } else if (!result.geminiApiKey) {
      chrome.storage.local.set({ geminiApiKey: '' });
    }
  });
});

// Listen for messages from the popup
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === 'showNotification') {
    chrome.notifications.create({
      type: 'basic',
      iconUrl: 'images/icon128.png',
      title: request.title || 'Stock Price Alert',
      message: request.message || 'Stock price alert!',
      priority: 2
    });
  }
}); 