#!/bin/bash python3
# param1 - API token
# param2 - ticker
# param3 - data from:.... default "1901-01-01"
# https://www.tiingo.com/products/stock-api
# https://www.eoddata.com/symbols.aspx
import requests
import sys
import tkinter as tk
TIINGO_API_KEY1 = ""
APItoken = TIINGO_API_KEY1 # API token
ticker = "tsla" # ticker
since_data = "1901-01-01" # get history from ...

def on_entry1_paste(event):
    entry1.event_generate("<<Paste>>")

def on_entry2_paste(event):
    entry2.event_generate("<<Paste>>")

def on_button_click():
    APItoken = str(entry1.get())
    ticker = str(entry2.get())
    
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
      with open(ticker.upper() + ".csv", "w") as file:    
        for line in symbol_data:
          file.write(line)

root = tk.Tk()
root.title("Get quotes")
label1 = tk.Label(root, text="Set API token  ( https://www.tiingo.com ):")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
#entry1.bind("<Control-v>", on_entry1_paste)
label2 = tk.Label(root, text="Set ticker:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
#entry2.bind("<Control-v>", on_entry2_paste)
button = tk.Button(root, text="Get quotes", command=on_button_click)
button.pack()
root.mainloop()
