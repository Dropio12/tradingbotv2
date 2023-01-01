// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Kokoabe

//@version=4
strategy("rsistratvid",overlay=true)

// Define the input parameters
length = 50

// Calculate the momentum indicator
fako = close - close[length]

// If the momentum is positive, enter a long position
if (fako > 0)
    strategy.entry("Long", strategy.long)

// If the momentum is negative, enter a short position

// If the close price is below the 200-day moving average, exit the long position
if close < sma(close, 165) and fako<-0.0163 //and close< rsi(close,50)
    strategy.close("Long")

// If the close price is below the 200-day moving average, exit the short position

// Plot the indicator value
plot(fako, color=color.rgb(113, 0, 212), linewidth=2, title="FAKO")

// Plot the 200-day moving average
plot(sma(close, 165), color=color.blue, linewidth=2, title="SMA")

// Plot the RSI indicator
plot(rsi(close, 50), color=color.green, linewidth=2, title="RSI")

// Plot the 50-day moving average
plot(sma(close, 50), color=color.orange, linewidth=2, title="SMA")

// Plot the 200-day moving average
plot(sma(close, 200), color=color.yellow, linewidth=2, title="SMA")

// Plot the 200-day moving average
plot(sma(close, 100), color=color.red, linewidth=2, title="SMA")
