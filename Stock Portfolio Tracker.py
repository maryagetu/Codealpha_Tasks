def stock_portfolio_tracker():
    """
    Main function to track stock portfolio
    """
    
   
    stock_prices = {
        "AAPL": 180.50,   
        "TSLA": 250.75,  
        "MSFT": 330.20  
    }
    
    
    portfolio = {}     
    total_value = 0    
    
    
    print("Available Stocks:")
    for symbol, price in stock_prices.items():
        print(f"  {symbol}: ${price:.2f} per share")
    
    print("\n" + "-" * 40)
    
    
    while True:
        
        symbol = input("\nEnter stock symbol (or 'done'): ").upper()
        
       
        if symbol == 'DONE':
            break
        
        
        if symbol not in stock_prices:
            print(f"Error: {symbol} is not in our stock list.")
            print(f"Available: {', '.join(stock_prices.keys())}")
            continue  
        
        
        try:
            quantity = float(input(f"How many shares of {symbol}? "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        
        price_per_share = stock_prices[symbol]
        holding_value = price_per_share * quantity
        
       
        portfolio[symbol] = {
            'quantity': quantity,
            'price': price_per_share,
            'value': holding_value
        }
        
        
        total_value += holding_value
        
        print(f"✓ Added: {quantity} shares of {symbol} = ${holding_value:.2f}")
    
   
    print("\n" + "=" * 50)
    print("FINAL PORTFOLIO")
    print("=" * 50)
    
    if not portfolio:
        print("No stocks in portfolio.")
        return
    
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['quantity']} shares @ ${data['price']:.2f} = ${data['value']:.2f}")
    
    print("-" * 50)
    print(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}")
    
    save_option = input("\nSave portfolio to file? (y/n): ").lower()
    
    if save_option == 'y':
        
        with open("portfolio.txt", "w") as file:
           
            file.write("MY STOCK PORTFOLIO\n")
            file.write("=" * 30 + "\n\n")
            
            
            for symbol, data in portfolio.items():
                file.write(f"{symbol}: {data['quantity']} shares\n")
            
         
            file.write(f"\nTotal Value: ${total_value:.2f}\n")
        
        print("Portfolio saved to 'portfolio.txt'")

stock_portfolio_tracker()