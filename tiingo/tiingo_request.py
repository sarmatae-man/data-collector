#!/bin/bash python3
# param1 - API token
# param2 - ticker
# param3 - data from:.... default "1901-01-01"
# https://www.tiingo.com/products/stock-api
# https://www.eoddata.com/symbols.aspx
import requests
import sys

APItoken = TIINGO_API_KEY1 # API token
ticker = "tsla" # ticker
since_data = "1901-01-01" # get history from ...

if len(sys.argv) < 3:
        print("Usage: tiingo_request.exe APItoken ticker [data from: 1989-01-31, default all history]")       
    
APItoken = sys.argv[1]
ticker = sys.argv[2]
since_data = sys.argv[3] if len(sys.argv) > 3 else since_data

headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/" + ticker.lower() + "/prices?startDate=" + since_data + "&" + "token=" + APItoken, headers=headers)
if not requestResponse.ok:
    print("Error request: " + str(requestResponse))
    print(requestResponse.json())
else:
    symbol_data = []
    symbol_adjdata = []
    symbol_adjdata.append("Date,Open,High,Low,Close" +'\n')
    symbol_data.append("Date,Open,High,Low,Close" +'\n')
    dd = requestResponse.json()
    def fl_to_str(_fl):    
       return str(int(_fl * 10000) / 10000)
    for item in dd:
        symbol_adjdata.append(item['date'][:10] + ',' + fl_to_str(item['adjOpen']) + ',' + fl_to_str(item['adjHigh']) + ',' + fl_to_str(item['adjLow']) + ',' + fl_to_str(item['adjClose']) + ',' + str(item['volume']) + '\n')
        symbol_data.append(item['date'][:10] + ',' + fl_to_str(item['open']) + ',' + fl_to_str(item['high']) + ',' + fl_to_str(item['low']) + ',' + fl_to_str(item['close']) + ',' + str(item['volume']) + '\n')
    with open(ticker.upper() + "_adj"+ ".csv", "w") as file:    
      for line in symbol_adjdata:
         file.write(line)
    print("File: " + ticker.upper() + "_adj" + ".csv")
    with open(ticker.upper() + ".csv", "w") as file:    
      for line in symbol_data:
         file.write(line)
    print("File: " + ticker.upper() + ".csv")
