Stock Portfolio Tracker - README
📈 Overview
A simple Python-based stock portfolio tracker that calculates total investment value based on user-defined holdings and pre-defined stock prices.

✨ Features
📊 Portfolio Management: Track multiple stock holdings

💰 Real-time Calculation: Automatically calculates total portfolio value

💾 File Export: Save portfolio data to a text file

✅ Input Validation: Handles invalid inputs gracefully

📱 Simple Interface: Easy-to-use command-line interface

🚀 Quick Start
Prerequisites
Python 3.x installed

Running the Program
bash
# Run the script
python stock_portfolio_tracker.py
📋 How It Works
1. Available Stocks
The program comes with pre-defined stock prices:

AAPL (Apple): $180.50 per share

TSLA (Tesla): $250.75 per share

MSFT (Microsoft): $330.20 per share

2. Adding Stocks to Portfolio
Enter stock symbol (e.g., AAPL, TSLA)

Enter quantity of shares

Repeat or type done to finish

3. View Portfolio Summary
Shows each stock with quantity, price, and value

Displays total portfolio value

Option to save to file

🎮 Usage Example
text
Available Stocks:
  AAPL: $180.50 per share
  TSLA: $250.75 per share
  MSFT: $330.20 per share
----------------------------------------

Enter stock symbol (or 'done'): AAPL
How many shares of AAPL? 10
✓ Added: 10.0 shares of AAPL = $1805.00

Enter stock symbol (or 'done'): TSLA
How many shares of TSLA? 5
✓ Added: 5.0 shares of TSLA = $1253.75

Enter stock symbol (or 'done'): done

==================================================
FINAL PORTFOLIO
==================================================
AAPL: 10.0 shares @ $180.50 = $1805.00
TSLA: 5.0 shares @ $250.75 = $1253.75
--------------------------------------------------
TOTAL PORTFOLIO VALUE: $3058.75

Save portfolio to file? (y/n): y
Portfolio saved to 'portfolio.txt'
💾 File Output
When saved, creates portfolio.txt:

text
MY STOCK PORTFOLIO
==============================
AAPL: 10.0 shares
TSLA: 5.0 shares

Total Value: $3058.75
🛠️ Technical Details
Code Structure
python
# 1. Stock price dictionary (hardcoded)
stock_prices = {"AAPL": 180.50, "TSLA": 250.75, "MSFT": 330.20}

# 2. Portfolio dictionary (user input)
portfolio = {}  # Stores {symbol: {quantity, price, value}}

# 3. Main loop for user input
while True:
    # Get symbol and quantity
    # Calculate value = price × quantity
    # Add to portfolio

# 4. Display results and save option
Key Functions
Dictionary Operations: Store and retrieve stock prices

Arithmetic Calculations: Multiply price × quantity

File Handling: Write portfolio data to file

Input/Output: User interaction and result display

🔧 Customization
Adding More Stocks
Edit the stock_prices dictionary:

python
stock_prices = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "MSFT": 330.20,
    "GOOGL": 2800.00,  # Add new stocks here
    "AMZN": 3400.00
}
Changing Stock Prices
Update the price values in the dictionary:

python
"AAPL": 185.25,  # Updated Apple price
📈 Learning Outcomes
This project demonstrates:

✅ Dictionary usage for data storage

✅ Basic arithmetic calculations

✅ File handling operations

✅ User input validation

✅ Loop control and program flow
