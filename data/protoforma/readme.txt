
U.S. 10-Year Government Bond Yield
 https://stooq.com/q/d/?s=10yusy.b
British Pounds / U.S. Dollar
 https://stooq.com/q/d/?s=gbpusd
Dow Jones Industrial
 https://stooq.com/q/d/?s=^dji
Gold (ozt) / U.S. Dollar
 https://stooq.com/q/d/?s=xauusd

Historical Crude Oil prices, 1861 to 2013
http://chartsbin.com/view/oau
https://www.weforum.org/agenda/2016/12/155-years-of-oil-prices-in-one-chart/

Инфляция в России
 https://xn----ctbjnaatncev9av3a8f8b.xn--p1ai/%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D1%8B-%D0%B8%D0%BD%D1%84%D0%BB%D1%8F%D1%86%D0%B8%D0%B8

Sunspot
Monthly mean total sunspot number [1/1749 - now]
 https://www.sidc.be/SILSO/datafiles
Where "0" -(change)-> "0.1"  
с этой даты данные с пометкой '*' (контроль при обновлении !!!):
2023 10 2023.790   99.4  16.0   958 *

SPSE price-weighted, dollar-denominated, capital appreciation indices from January 1865 to February 1917
 https://som.yale.edu/centers/international-center-for-finance/data/historical-financial-research-data/st-petersburg
+ RTSI since 1995
 https://www.moex.com/ru/index/RTSI/technical

Aрхивные и текущие данные о стоимости иностранных валют по отношению к рублю
https://data.rcsi.science/data-catalog/datasets/182/
-------------
with open(input_file, 'r', encoding='utf-8') as file_in, open(output_file, 'w', encoding='utf-8') as file_out:
    for line in file_in:
        if "USD" in line:
            modified_line = line[:-1] + '0\n'  
            file_out.write(modified_line)
-------------

Chartbook of Real Commodity Prices, 1850-2020
https://www.sfu.ca/~djacks/data/boombust/Chartbook%20for%20From%20Boom%20to%20Bust%202102.pdf

