# Poly_Financials_Test

from polygon import RESTClient
import sys
import constants
client = RESTClient(api_key = constants.key)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: Poly_financials_test.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    financials = client.vx.list_stock_financials(ticker, timeframe="annual")
    financials_list = []
    for f in financials:
        financials_list.append(f)

    print(financials_list[0].company_name)
    print(financials_list[0].fiscal_year) 
