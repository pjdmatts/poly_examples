from polygon import RESTClient
import sys
import constants

client = RESTClient(api_key=constants.key)

# Function calculates current ratio

def get_current(financials_list):
    current_assets = financials_list[0].financials.balance_sheet.get('current_assets').value
    current_liabilities = financials_list[0].financials.balance_sheet.get('current_liabilities').value
    current_ratio = current_assets/current_liabilities
    return float("{:.2f}".format(current_ratio))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python poly)current.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    financials = client.vx.list_stock_financials(ticker, timeframe="annual")
    financials_list = []
    for f in financials:
        financials_list.append(f)

    current = get_current(financials_list)
    print("Current: ", current)