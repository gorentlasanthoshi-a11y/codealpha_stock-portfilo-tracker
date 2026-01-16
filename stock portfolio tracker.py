# Manually defined stock prices
stock_prices = {
    "TCS": 3500,
    "INFY": 1500,
    "RELIANCE": 2500,
    "HDFC": 2800
}

def stock_tracker():
    total_investment = 0

    print("📈 Welcome to Simple Stock Tracker")
    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} - ₹{price}")

    while True:
        stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

        if stock_name == "DONE":
            break

        if stock_name in stock_prices:
            quantity = int(input("Enter number of shares: "))
            investment = stock_prices[stock_name] * quantity
            total_investment += investment

            print(f"Investment in {stock_name}: ₹{investment}")
        else:
            print("❌ Stock not found. Please choose from the list.")

    print("\n💰 Total Investment Value: ₹", total_investment)

# Run the stock tracker
stock_tracker()
