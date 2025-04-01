// List of popular Indian stocks with their Google Finance symbols
const stocks = [
  { symbol: 'RELIANCE:NSE', name: 'Reliance Industries' },
  { symbol: 'TCS:NSE', name: 'Tata Consultancy Services' },
  { symbol: 'HDFCBANK:NSE', name: 'HDFC Bank' },
  { symbol: 'INFY:NSE', name: 'Infosys' },
  { symbol: 'ICICIBANK:NSE', name: 'ICICI Bank' },
  { symbol: 'HINDUNILVR:NSE', name: 'Hindustan Unilever' },
  { symbol: 'ITC:NSE', name: 'ITC Limited' },
  { symbol: 'SBIN:NSE', name: 'State Bank of India' },
  { symbol: 'BHARTIARTL:NSE', name: 'Bharti Airtel' },
  { symbol: 'KOTAKBANK:NSE', name: 'Kotak Mahindra Bank' },
  { symbol: 'AXISBANK:NSE', name: 'Axis Bank' },
  { symbol: 'BAJFINANCE:NSE', name: 'Bajaj Finance' },
  { symbol: 'WIPRO:NSE', name: 'Wipro' },
  { symbol: 'HCLTECH:NSE', name: 'HCL Technologies' },
  { symbol: 'TATAMOTORS:NSE', name: 'Tata Motors' },
  { symbol: 'M&M:NSE', name: 'Mahindra & Mahindra' },
  { symbol: 'MARUTI:NSE', name: 'Maruti Suzuki' },
  { symbol: 'SUNPHARMA:NSE', name: 'Sun Pharmaceutical' },
  { symbol: 'ONGC:NSE', name: 'Oil and Natural Gas Corporation' },
  { symbol: 'TATASTEEL:NSE', name: 'Tata Steel' }
];

async function fetchStockPrice(symbol) {
  try {
    const googleFinanceUrl = `https://www.google.com/finance/quote/${symbol}?hl=en`;
    const response = await fetch(googleFinanceUrl);
    const text = await response.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(text, 'text/html');
    
    // Find the main price element (it's usually the first large number in the page)
    const priceElement = doc.querySelector('.YMlKec.fxKbKc');
    const price = priceElement ? priceElement.textContent.trim() : 'N/A';
    
    // Find the change element (usually right next to the price)
    const changeElement = doc.querySelector('.P2Luy.JwB6zf');
    const changePercentElement = doc.querySelector('.P2Luy.Ebnabc');
    
    const change = changeElement ? changeElement.textContent.trim() : '';
    const changePercent = changePercentElement ? changePercentElement.textContent.trim() : '';
    
    // Determine if it's positive or negative change
    const isPositive = !change.includes('-');
    
    return {
      price,
      change: `${change} (${changePercent})`,
      isPositive
    };
  } catch (error) {
    console.error(`Error fetching price for ${symbol}:`, error);
    return { price: 'Error', change: '', isPositive: false };
  }
}

function updateLastRefreshTime() {
  const lastUpdate = document.getElementById('lastUpdate');
  lastUpdate.textContent = `Last updated: ${new Date().toLocaleTimeString()}`;
}

async function refreshPrices() {
  const status = document.getElementById('status');
  const refreshButton = document.getElementById('refreshPrices');
  refreshButton.disabled = true;
  status.textContent = 'Fetching prices...';

  try {
    const stockItems = document.querySelectorAll('.stock-item');
    let completedCount = 0;
    
    for (const item of stockItems) {
      const checkbox = item.querySelector('input[type="checkbox"]');
      if (checkbox.checked) {
        const symbol = checkbox.dataset.symbol;
        const priceSpan = item.querySelector('.price-info');
        
        priceSpan.textContent = 'Loading...';
        const { price, change, isPositive } = await fetchStockPrice(symbol);
        
        priceSpan.textContent = `${price} ${change}`;
        priceSpan.className = 'price-info ' + 
          (isPositive ? 'change-positive' : 'change-negative');
        
        completedCount++;
        status.textContent = `Fetching prices... (${completedCount} of ${document.querySelectorAll('input[type="checkbox"]:checked').length})`;
        
        // Add a small delay between requests to avoid rate limiting
        await new Promise(resolve => setTimeout(resolve, 500));
      }
    }
    
    updateLastRefreshTime();
    status.textContent = 'Prices updated successfully!';
  } catch (error) {
    status.textContent = 'Error updating prices: ' + error.message;
  } finally {
    refreshButton.disabled = false;
  }
}

document.addEventListener('DOMContentLoaded', function() {
  const stockList = document.getElementById('stockList');
  const refreshButton = document.getElementById('refreshPrices');
  
  // Load saved selections from storage
  chrome.storage.local.get(['selectedStocks'], function(result) {
    const selectedStocks = result.selectedStocks || [];
    
    // Populate stock list
    stocks.forEach(stock => {
      const stockItem = document.createElement('div');
      stockItem.className = 'stock-item';
      
      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.id = `stock-${stock.symbol}`;
      checkbox.dataset.symbol = stock.symbol;
      checkbox.checked = selectedStocks.includes(stock.symbol);
      
      const label = document.createElement('label');
      label.htmlFor = `stock-${stock.symbol}`;
      label.textContent = `${stock.name} (${stock.symbol.split(':')[0]})`;
      
      const priceSpan = document.createElement('span');
      priceSpan.className = 'price-info';
      priceSpan.textContent = '---';
      
      stockItem.appendChild(checkbox);
      stockItem.appendChild(label);
      stockItem.appendChild(priceSpan);
      stockList.appendChild(stockItem);
      
      // Save selection when checkbox changes
      checkbox.addEventListener('change', function() {
        const selected = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'))
          .map(cb => cb.dataset.symbol);
        chrome.storage.local.set({ selectedStocks: selected });
      });
    });
    
    // Initial price fetch for selected stocks
    if (selectedStocks.length > 0) {
      refreshPrices();
    }
  });
  
  refreshButton.addEventListener('click', refreshPrices);
  
  // Auto-refresh every minute if tab is active
  let refreshInterval;
  document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
      clearInterval(refreshInterval);
    } else {
      refreshInterval = setInterval(refreshPrices, 60000); // 1 minute
    }
  });
}); 