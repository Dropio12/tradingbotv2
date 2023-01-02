// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Kokoabe

//@version=4
strategy("rsistratV2",overlay=true)

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



//Second strategy


//@version=5
strategy(shorttitle='SQZMOM_LB_Strategy', title='Squeeze Momentum Strategy [LazyBear & Kokoabe]', overlay=false)

// Input parameters
length = input(20, title='BB Length')
mult = input(2.0, title='BB MultFactor')
lengthKC = input(20, title='KC Length')
multKC = input(1.5, title='KC MultFactor')
useTrueRange = input(true, title='Use TrueRange (KC)')

// Calculate BB
source = close
basis = ta.sma(source, length)
dev = multKC * ta.stdev(source, length)
upperBB = basis + dev
lowerBB = basis - dev

// Calculate KC
ma = ta.sma(source, lengthKC)
range_1 = useTrueRange ? ta.tr : high - low
rangema = ta.sma(range_1, lengthKC)
upperKC = ma + rangema * multKC
lowerKC = ma - rangema * multKC

sqzOn = lowerBB > lowerKC and upperBB < upperKC
sqzOff = lowerBB < lowerKC and upperBB > upperKC
noSqz = sqzOn == false and sqzOff==false

val = ta.linreg(source - math.avg(math.avg(ta.highest(high, lengthKC), ta.lowest(low, lengthKC)), ta.sma(close, lengthKC)), lengthKC, 0)

bcolor = val > 0 ? val > nz(val[1]) ? color.lime : color.green : val < nz(val[1]) ? color.red : color.maroon
scolor = noSqz ? color.blue : sqzOn ? color.black : color.gray
plot(val, color=bcolor, style=plot.style_histogram, linewidth=4)
plot(0, color=scolor, style=plot.style_cross, linewidth=2)

//rsi
rsiLength = 50
rsiThreshold = 70

rsi = ta.rsi(close, rsiLength)
if noSqz and val < 0 and rsi < 100 - rsiThreshold
    strategy.entry('Short', strategy.short, stop=strategy.position_avg_price * 1.05)
    strategy.exit('Trailing Stop', 'Short', stop=strategy.position_avg_price * 0.90)
if noSqz and val > 0 and rsi > rsiThreshold
    strategy.entry('Long', strategy.long, stop=strategy.position_avg_price * 0.95)
    strategy.exit('Long Trailing Stop', 'Long', stop=strategy.position_avg_price * 1.10)
if sqzOn
    strategy.close('Long')
    strategy.close('Short')

