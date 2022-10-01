# Trader Assistant
Trader Assistant is a small script made using python that would allow users to enter the trading data, current stock prices and then get a summary of their current portfolio.

## Menu Displayed In Trader Assistant
1. Load trading data
2. Load current stock prices
3. Manually enter a new trade
4. View trading data
5. View current portfolio
6. Save trading data
7. Quit

### Load Trading Data
This Menu Accepts a csv file as input in the format Ticker, Buy or Sell, Quantity, Cost, Date of Trade

|Field|Type|
|--|--|
|Ticker|String|  
|Buy Or Sell   | Should be either b or s   |   
| Quantity  | Integer   |  
| Cost | Float |
| Date of Trade| Date in the format yyyy-mm-dd |

### Load Current Stock Prices
This Menu Accepts a json file as input in the format ticker, price

|Field|Type|
|--|--|
|Ticker|String| 
|Price|Float|

### Manually Enter A New Trade
This menu accepts a new trade manually<br/>
<br/>
Ticker<br/>
Buy or Sell<br/>
Quantity<br/>
Cost<br/>
Date of Trade<br/>
|Field|Type|
|--|--|
|Ticker|String|  
|Buy Or Sell   | Should be either b or s   |   
| Quantity  | Integer   |  
| Cost | Float |
| Date of Trade| Date in the format yyyy-mm-dd |

### View Trading Data
This menu displays the trading data according to the input from user
1. Find by ticker if ticker value is provided or else get all data
2. Sort by date.

Output:<br/> `<Date of Trade> <Ticker> <Buy or Sell> <Quantity> for $<Cost>`

### View Current Portfolio
This menu displays the hodl of stocks for the current user.<br/>
Output:<br/>
`<Ticker>
Total units: <Total units>
Total value: <Total value>
`

### Save Trading Data
This menu saves the trading data into a csv file.<br/>
The filename is accepted from the user.<br/>
The file contents are of the format<br/>
`<Date of Trade>,<Ticker>,<Buy or Sell>,<Quantity>,<Cost>`

### Quit
This menu will display a thank you message and exit the application.
