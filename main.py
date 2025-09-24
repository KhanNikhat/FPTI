# # import pandas as pd
# # from collections import defaultdict
# # import yfinance as yf
# # import matplotlib.pyplot as plt
# # from datetime import datetime

# # # =========================================================================
# # # Function 1: Analyze Transactions
# # # =========================================================================
# # def analyze_transactions(file_path):
# #     """
# #     Reads transactions from the Kaggle dataset, categorizes them, 
# #     and calculates monthly expenses.
# #     """
# #     try:
# #         df = pd.read_csv(file_path)
# #     except FileNotFoundError:
# #         print(f"Error: The file {file_path} was not found.")
# #         return None, None

# #     # Rename columns to match the new dataset's structure
# #     df.rename(columns={
# #         'trans_date_trans_time': 'Date',
# #         'amt': 'Amount',
# #         'category': 'Category'
# #     }, inplace=True)
    
# #     # Convert the combined date/time column to a proper datetime format
# #     df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')

# #     # The dataset only contains expenses, so we'll categorize all transactions as such.
# #     # We can assume Income is 0 for this analysis.
# #     df['Month'] = df['Date'].dt.to_period('M')
    
# #     # Calculate monthly expenses
# #     monthly_expenses_summary = df.groupby('Month')['Amount'].sum().to_dict()
    
# #     monthly_summary = defaultdict(lambda: {'Income': 0, 'Expenses': 0})
# #     for month, expenses in monthly_expenses_summary.items():
# #         monthly_summary[str(month)]['Expenses'] = expenses
    
# #     return df, monthly_summary

# # # =========================================================================
# # # Function 2: Track Net Worth
# # # =========================================================================
# # def track_net_worth(file_path):
# #     """Reads and returns net worth data over time."""
# #     try:
# #         df = pd.read_csv(file_path, parse_dates=['Date'])
# #         return df
# #     except FileNotFoundError:
# #         print(f"Error: The file {file_path} was not found.")
# #         return None

# # # =========================================================================
# # # Function 3: Update Portfolio Value
# # # =========================================================================
# # def update_portfolio_value(file_path):
# #     """Fetches live stock prices and calculates the current portfolio value."""
# #     try:
# #         df = pd.read_csv(file_path)
# #     except FileNotFoundError:
# #         print(f"Error: The file {file_path} was not found.")
# #         return 0, None

# #     total_value = 0
# #     holdings_with_price = []
    
# #     print("Fetching live investment prices...")
# #     for _, row in df.iterrows():
# #         ticker = row['Ticker']
# #         shares = row['Shares']
        
# #         try:
# #             stock = yf.Ticker(ticker)
# #             current_price = stock.history(period="1d")['Close'].iloc[-1]
# #             holding_value = current_price * shares
# #             total_value += holding_value
# #             holdings_with_price.append({
# #                 'Ticker': ticker,
# #                 'Shares': shares,
# #                 'Current Price': f'${current_price:.2f}',
# #                 'Value': f'${holding_value:.2f}'
# #             })
# #         except Exception as e:
# #             print(f"Could not fetch data for {ticker}. Error: {e}")
            
# #     return total_value, pd.DataFrame(holdings_with_price)

# # # =========================================================================
# # # Function 4: Generate Reports and Plots
# # # =========================================================================
# # def generate_report_and_plots(monthly_summary, net_worth_df, portfolio_value, portfolio_details):
# #     """Prints a summary report and plots key metrics."""
# #     print("\n" + "="*50)
# #     print("✨ PERSONAL FINANCE DASHBOARD ✨")
# #     print("="*50)

# #     # 1. Summary of Monthly Cash Flow (Expenses only for this dataset)
# #     print("\n💰 Monthly Cash Flow Summary:")
# #     for month, data in monthly_summary.items():
# #         expenses = data['Expenses']
# #         print(f"  - {month}: Expenses: ${expenses:,.2f}")

# #     # 2. Investment Performance
# #     print("\n📈 Investment Portfolio Performance:")
# #     if portfolio_value > 0:
# #         print(f"  - Current Portfolio Value: ${portfolio_value:,.2f}")
# #         print("\n  - Holdings:")
# #         print(portfolio_details.to_string(index=False))
# #     else:
# #         print("  - No investment data available or could not be fetched.")

# #     # 3. Net Worth Tracking
# #     print("\n📊 Net Worth Over Time:")
# #     if net_worth_df is not None and not net_worth_df.empty:
# #         current_net_worth = net_worth_df['NetWorth'].iloc[-1]
# #         print(f"  - Current Net Worth: ${current_net_worth:,.2f}")
# #     else:
# #         print("  - No net worth data available.")

# #     # 4. Generate Plots
# #     print("\nGenerating Plots...")

# #     # Plot 1: Monthly Expenses
# #     if monthly_summary:
# #         months = list(monthly_summary.keys())
# #         expense_values = [data['Expenses'] for data in monthly_summary.values()]
        
# #         plt.figure(figsize=(10, 6))
# #         plt.bar(months, expense_values, label='Expenses', color='r', alpha=0.7)
# #         plt.title('Monthly Expenses')
# #         plt.xlabel('Month')
# #         plt.ylabel('Amount ($)')
# #         plt.legend()
# #         plt.grid(axis='y', linestyle='--')
# #         plt.tight_layout()
# #         plt.show()

# #     # Plot 2: Net Worth Trend
# #     if net_worth_df is not None and not net_worth_df.empty:
# #         plt.figure(figsize=(10, 6))
# #         plt.plot(net_worth_df['Date'], net_worth_df['NetWorth'], marker='o', linestyle='-', color='b')
# #         plt.title('Net Worth Over Time')
# #         plt.xlabel('Date')
# #         plt.ylabel('Net Worth ($)')
# #         plt.grid(True)
# #         plt.tight_layout()
# #         plt.show()

# # # =========================================================================
# # # Main Execution Block
# # # =========================================================================
# # if __name__ == "__main__":
# #     # Define file paths
# #     transactions_file = 'credit_card_transactions.csv'
# #     net_worth_file = 'net_worth.csv'
# #     investments_file = 'investments.csv'

# #     # 1. Analyze Transactions
# #     transactions_df, monthly_summary = analyze_transactions(transactions_file)

# #     # 2. Track Net Worth
# #     net_worth_df = track_net_worth(net_worth_file)

# #     # 3. Update Portfolio Value
# #     portfolio_value, portfolio_details = update_portfolio_value(investments_file)
    
# #     # 4. Generate Report and Plots
# #     if monthly_summary and net_worth_df is not None:
# #         generate_report_and_plots(monthly_summary, net_worth_df, portfolio_value, portfolio_details)
# #     else:
# #         print("Required data for generating the report is missing. Please check your files.")








# import pandas as pd
# from collections import defaultdict
# import yfinance as yf
# import matplotlib.pyplot as plt
# from datetime import datetime


# def analyze_transactions(file_path):
#     """
#     Reads transactions from the Kaggle dataset, categorizes them, 
#     and calculates monthly expenses.
#     """
#     try:
#         df = pd.read_csv(file_path)
#     except FileNotFoundError:
#         print(f"Error: The file {file_path} was not found.")
#         return None, None

#     # Rename columns to match the new dataset's structure
#     df.rename(columns={
#         'trans_date_trans_time': 'Date',
#         'amt': 'Amount',
#         'category': 'Category'
#     }, inplace=True)
    
#     # Convert the combined date/time column to a proper datetime format
#     df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')

#     # The dataset only contains expenses, so we'll categorize all transactions as such.
#     # We can assume Income is 0 for this analysis.
#     df['Month'] = df['Date'].dt.to_period('M')
    
#     # Calculate monthly expenses
#     monthly_expenses_summary = df.groupby('Month')['Amount'].sum().to_dict()
    
#     monthly_summary = defaultdict(lambda: {'Income': 0, 'Expenses': 0})
#     for month, expenses in monthly_expenses_summary.items():
#         monthly_summary[str(month)]['Expenses'] = expenses
    
#     return df, monthly_summary


# def track_net_worth(file_path):
#     """Reads and returns net worth data over time."""
#     try:
#         df = pd.read_csv(file_path, parse_dates=['Date'])
#         return df
#     except FileNotFoundError:
#         print(f"Error: The file {file_path} was not found.")
#         return None 


# def update_portfolio_value(file_path):
#     """Fetches live stock prices and calculates the current portfolio value."""
#     try:
#         df = pd.read_csv(file_path)
#     except FileNotFoundError:
#         print(f"Error: The file {file_path} was not found.")
#         return 0, None

#     total_value = 0
#     holdings_with_price = []
    
#     print("Fetching live investment prices...")
#     for _, row in df.iterrows():
#         ticker = row['Ticker']
#         shares = row['Shares']
        
#         try:
#             stock = yf.Ticker(ticker)
#             current_price = stock.history(period="1d")['Close'].iloc[-1]
#             holding_value = current_price * shares
#             total_value += holding_value
#             holdings_with_price.append({
#                 'Ticker': ticker,
#                 'Shares': shares,
#                 'Current Price': f'${current_price:.2f}',
#                 'Value': f'${holding_value:.2f}'
#             })
#         except Exception as e:
#             print(f"Could not fetch data for {ticker}. Error: {e}")
            
#     return total_value, pd.DataFrame(holdings_with_price)


# def generate_report_and_plots(monthly_summary, net_worth_df, portfolio_value, portfolio_details):
#     """Prints a summary report and plots key metrics."""
#     print("\n" + "="*50)
#     print("✨ PERSONAL FINANCE DASHBOARD ✨")
#     print("="*50)

#     # 1. Summary of Monthly Cash Flow
#     print("\n💰 Monthly Cash Flow Summary:")
#     for month, data in monthly_summary.items():
#         income = data['Income']
#         expenses = data['Expenses']
#         net_cash_flow = income - expenses
#         print(f"  - {month}: Income: ${income:,.2f} | Expenses: ${expenses:,.2f} | Net: ${net_cash_flow:,.2f}")

#     # 2. Investment Performance
#     print("\n📈 Investment Portfolio Performance:")
#     if portfolio_value > 0:
#         print(f"  - Current Portfolio Value: ${portfolio_value:,.2f}")
#         print("\n  - Holdings:")
#         print(portfolio_details.to_string(index=False))
#     else:
#         print("  - No investment data available or could not be fetched.")

#     # 3. Net Worth Tracking
#     print("\n📊 Net Worth Over Time:")
#     if net_worth_df is not None and not net_worth_df.empty:
#         current_net_worth = net_worth_df['NetWorth'].iloc[-1]
#         print(f"  - Current Net Worth: ${current_net_worth:,.2f}")
#     else:
#         print("  - No net worth data available.")

#     # 4. Generate Plots
#     print("\nGenerating Plots...")

#     # Plot 1: Monthly Income vs. Expenses
#     if monthly_summary:
#         months = list(monthly_summary.keys())
#         income_values = [data['Income'] for data in monthly_summary.values()]
#         expense_values = [data['Expenses'] for data in monthly_summary.values()]
        
#         plt.figure(figsize=(10, 6))
#         plt.bar(months, income_values, label='Income', color='g', alpha=0.7)
#         plt.bar(months, expense_values, label='Expenses', color='r', alpha=0.7)
#         plt.title('Monthly Income vs. Expenses')
#         plt.xlabel('Month')
#         plt.ylabel('Amount ($)')
#         plt.legend()
#         plt.grid(axis='y', linestyle='--')
#         plt.tight_layout()
#         plt.show()

#     # Plot 2: Net Worth Trend
#     if net_worth_df is not None and not net_worth_df.empty:
#         plt.figure(figsize=(10, 6))
#         plt.plot(net_worth_df['Date'], net_worth_df['NetWorth'], marker='o', linestyle='-', color='b')
#         plt.title('Net Worth Over Time')
#         plt.xlabel('Date')
#         plt.ylabel('Net Worth ($)')
#         plt.grid(True)
#         plt.tight_layout()
#         plt.show()


# if __name__ == "__main__":
#     # Define file paths
#     transactions_file = 'credit_card_transactions.csv'
#     net_worth_file = 'net_worth.csv'
#     investments_file = 'investments.csv'

#     # 1. Analyze Transactions
#     transactions_df, monthly_summary = analyze_transactions(transactions_file)

#     # 2. Track Net Worth
#     net_worth_df = track_net_worth(net_worth_file)

#     # 3. Update Portfolio Value
#     portfolio_value, portfolio_details = update_portfolio_value(investments_file)
    
#     # 4. Generate Report and Plots
#     if monthly_summary and net_worth_df is not None:
#         generate_report_and_plots(monthly_summary, net_worth_df, portfolio_value, portfolio_details)
#     else:
#         print("Required data for generating the report is missing.")


























    
    
import pandas as pd
from collections import defaultdict
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import os

# =========================================================================
# File Management and Setup
# =========================================================================
def create_sample_files():
    """
    Creates sample CSV files if they do not already exist.
    This helps the user get started without needing to create them manually.
    """
    if not os.path.exists('transactions.csv'):
        with open('transactions.csv', 'w') as f:
            f.write("Date,Description,Amount,Category\n")
            f.write("2024-08-01,Paycheck,3500.00,Income\n")
            f.write("2024-08-03,Groceries,75.50,Groceries\n")
            f.write("2024-08-05,Rent,1500.00,Housing\n")
            f.write("2024-08-10,Coffee Shop,5.25,Dining Out\n")
            f.write("2024-08-15,Consulting Fee,500.00,Income\n")
            f.write("2024-08-20,Phone Bill,60.00,Utilities\n")
        print("Created sample 'transactions.csv' file.")

    if not os.path.exists('net_worth.csv'):
        with open('net_worth.csv', 'w') as f:
            f.write("Date,NetWorth\n")
            f.write("2024-07-31,15000\n")
            f.write("2024-08-31,16200\n")
        print("Created sample 'net_worth.csv' file.")

    if not os.path.exists('investments.csv'):
        with open('investments.csv', 'w') as f:
            f.write("Ticker,Shares\n")
            f.write("AAPL,10\n")
            f.write("GOOGL,5\n")
        print("Created sample 'investments.csv' file.")

# =========================================================================
# Function 1: Analyze Transactions
# =========================================================================
def analyze_transactions(file_path):
    """
    Reads transactions from the Kaggle dataset, categorizes them, 
    and calculates monthly expenses.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None, None

    # Rename columns to match the new dataset's structure
    df.rename(columns={
        'trans_date_trans_time': 'Date',
        'amt': 'Amount',
        'category': 'Category'
    }, inplace=True)
    
    # Convert the combined date/time column to a proper datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')

    # The dataset only contains expenses, so we'll categorize all transactions as such.
    # We can assume Income is 0 for this analysis.
    df['Month'] = df['Date'].dt.to_period('M')
    
    # Calculate monthly expenses
    monthly_expenses_summary = df.groupby('Month')['Amount'].sum().to_dict()
    
    monthly_summary = defaultdict(lambda: {'Income': 0, 'Expenses': 0})
    for month, expenses in monthly_expenses_summary.items():
        monthly_summary[str(month)]['Expenses'] = expenses
    
    return df, monthly_summary

# =========================================================================
# Function 2: Track Net Worth
# =========================================================================
def track_net_worth(file_path):
    """
    Reads and returns net worth data over time.
    Returns a dataframe.
    """
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'])
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

# =========================================================================
# Function 3: Update Portfolio Value
# =========================================================================
def update_portfolio_value(file_path):
    """
    Fetches live stock prices using yfinance and calculates the 
    current portfolio value. Returns the total value and a dataframe of details.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return 0, pd.DataFrame()

    total_value = 0
    holdings_with_price = []
    
    print("Fetching live investment prices...")
    for _, row in df.iterrows():
        ticker = row['Ticker']
        shares = row['Shares']
        
        try:
            stock = yf.Ticker(ticker)
            current_price = stock.history(period="1d")['Close'].iloc[-1]
            holding_value = current_price * shares
            total_value += holding_value
            holdings_with_price.append({
                'Ticker': ticker,
                'Shares': shares,
                'Current Price': f'${current_price:.2f}',
                'Value': f'${holding_value:.2f}'
            })
        except Exception as e:
            print(f"Could not fetch data for {ticker}. Error: {e}")
            
    return total_value, pd.DataFrame(holdings_with_price)

# =========================================================================
# Function 4: Generate Reports and Plots
# =========================================================================
def generate_report_and_plots(monthly_summary, net_worth_df, portfolio_value, portfolio_details):
    """
    Prints a comprehensive summary report to the console and generates plots
    for key financial metrics.
    """
    print("\n" + "="*50)
    print("✨ PERSONAL FINANCE DASHBOARD ✨")
    print("="*50)

    # 1. Summary of Monthly Cash Flow
    print("\n💰 Monthly Cash Flow Summary:")
    if monthly_summary:
        for month, data in monthly_summary.items():
            income = data['Income']
            expenses = data['Expenses']
            net_cash_flow = income - expenses
            print(f"  - {month}: Income: ${income:,.2f} | Expenses: ${expenses:,.2f} | Net: ${net_cash_flow:,.2f}")
    else:
        print("  - No transaction data available.")

    # 2. Investment Performance
    print("\n📈 Investment Portfolio Performance:")
    if portfolio_value > 0 and not portfolio_details.empty:
        print(f"  - Current Portfolio Value: ${portfolio_value:,.2f}")
        print("\n  - Holdings:")
        print(portfolio_details.to_string(index=False))
    else:
        print("  - No investment data available or could not be fetched.")

    # 3. Net Worth Tracking
    print("\n📊 Net Worth Over Time:")
    if net_worth_df is not None and not net_worth_df.empty:
        current_net_worth = net_worth_df['NetWorth'].iloc[-1]
        print(f"  - Current Net Worth: ${current_net_worth:,.2f}")
    else:
        print("  - No net worth data available.")

    # 4. Generate Plots
    print("\nGenerating Plots...")

    # Plot 1: Monthly Income vs. Expenses
    if monthly_summary:
        months = list(monthly_summary.keys())
        income_values = [data['Income'] for data in monthly_summary.values()]
        expense_values = [data['Expenses'] for data in monthly_summary.values()]
        
        plt.figure(figsize=(10, 6))
        plt.bar(months, income_values, label='Income', color='g', alpha=0.7)
        plt.bar(months, expense_values, label='Expenses', color='r', alpha=0.7)
        plt.title('Monthly Income vs. Expenses')
        plt.xlabel('Month')
        plt.ylabel('Amount ($)')
        plt.legend()
        plt.grid(axis='y', linestyle='--')
        plt.tight_layout()
        plt.show()

    # Plot 2: Net Worth Trend
    if net_worth_df is not None and not net_worth_df.empty:
        plt.figure(figsize=(10, 6))
        plt.plot(net_worth_df['Date'], net_worth_df['NetWorth'], marker='o', linestyle='-', color='b')
        plt.title('Net Worth Over Time')
        plt.xlabel('Date')
        plt.ylabel('Net Worth ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# =========================================================================
# Main Execution Block
# =========================================================================
if __name__ == "__main__":
    # Call the setup function to ensure all files exist
    create_sample_files()
    
    # Define file paths
    transactions_file = 'credit_card_transactions.csv'
    net_worth_file = 'net_worth.csv'
    investments_file = 'investments.csv'

    # 1. Analyze Transactions
    transactions_df, monthly_summary = analyze_transactions(transactions_file)

    # 2. Track Net Worth
    net_worth_df = track_net_worth(net_worth_file)

    # 3. Update Portfolio Value
    portfolio_value, portfolio_details = update_portfolio_value(investments_file)
    
    # 4. Generate Report and Plots
    if monthly_summary and net_worth_df is not None:
        generate_report_and_plots(monthly_summary, net_worth_df, portfolio_value, portfolio_details)
    else:
        print("Required data for generating the report is missing. Please ensure your CSV files are correct.")
