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

//strat 3

// This
source
code is subject
to
the
terms
of
the
Mozilla
Public
License
2.0
at
https: // mozilla.org / MPL / 2.0 /
// © Kokoabe

// This
work is licensed
under
a
Attribution - NonCommercial - ShareAlike
4.0
International(CC
BY - NC - SA
4.0) https: // creativecommons.org / licenses / by - nc - sa / 4.0 /
// © LuxAlgo

//

@version

=5
strategy("Trendlines with Breaks [LuxAlgo]", overlay=true)
length = input.int(14)
k = input.float(1., 'Slope', minval=0, step=.1)
method = input.string('Atr', 'Slope Calculation Method',
                      options=['Atr', 'Stdev', 'Linreg'])
show = input(false, 'Show Only Confirmed Breakouts')
// ----
upper = 0., lower = 0.
slope_ph = 0., slope_pl = 0.
src = close
n = bar_index
// ----
ph = ta.pivothigh(length, length)
pl = ta.pivotlow(length, length)
slope = switch
method
'Atr' = > ta.atr(length) / length * k
'Stdev' = > ta.stdev(src, length) / length * k
'Linreg' = > math.abs(ta.sma(src * bar_index, length) - ta.sma(src, length) * ta.sma(bar_index, length)) / ta.variance(
    n, length) / 2 * k

slope_ph := ph ? slope: slope_ph[1]
slope_pl := pl ? slope: slope_pl[1]

upper := ph ? ph: upper[1] - slope_ph
lower := pl ? pl: lower[1] + slope_pl
// ----
single_upper = 0
single_lower = 0
single_upper := src[length] > upper ? 0: ph ? 1: single_upper[1]
single_lower := src[length] < lower ? 0: pl ? 1: single_lower[1]
upper_breakout = single_upper[1] and src[length] > upper and (show ? src > src[length]: 1)
lower_breakout = single_lower[1] and src[length] < lower and (show ? src < src[length]: 1)
plotshape(upper_breakout ? low[
    length]: na, "Upper Break", shape.labelup, location.absolute,  # 26a69a,-length,text="B",textcolor=color.white,size=size.tiny)
                 plotshape(lower_breakout ? high[length]: na, "Lower Break", shape.labeldown, location.absolute,
# ef5350,-length,text="B",textcolor=color.white,size=size.tiny)
// ----
var
line
up_l = na
var
line
dn_l = na
var
label
recent_up_break = na
var
label
recent_dn_break = na

if ph[1]
line.delete(up_l[1])
label.delete(recent_up_break[1])

up_l := line.new(n - length - 1, ph[1], n - length, upper, color=  # 26a69a,
extend = extend.right, style = line.style_dashed)
if pl[1]
line.delete(dn_l[1])
label.delete(recent_dn_break[1])

dn_l := line.new(n-length-1, pl[1], n-length, lower, color=  # ef5350,
extend=extend.right, style=line.style_dashed)

if ta.crossover(src, upper-slope_ph * length)
label.delete(recent_up_break[1])
recent_up_break := label.new(n, low, 'B', color=  # 26a69a,
textcolor=color.white, style=label.style_label_up, size=size.small)

if ta.crossunder(src, lower+slope_pl * length)
label.delete(recent_dn_break[1])
recent_dn_break := label.new(n, high, 'B', color=  # ef5350,
textcolor=color.white, style=label.style_label_down, size=size.small)

// ----
plot(upper, 'Upper', color = ph ? na:  # 26a69a,offset=-length)
    plot(lower, 'Lower', color=pl ? na:  # ef5350,offset=-length)

alertcondition(ta.crossover(src, upper - slope_ph * length), 'Upper Breakout', 'Price broke upper trendline')
alertcondition(ta.crossunder(src, lower + slope_pl * length), 'Lower Breakout', 'Price broke lower trendline')

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28)), ta.crossunder(src, lower + slope_pl * length)
if (longCondition)
strategy.entry("My Long Entry Id", strategy.long)

shortCondition = ta.crossunder(ta.sma(close, 14), ta.sma(close, 28)), ta.crossover(src, upper - slope_ph * length)
if (shortCondition)
strategy.entry("My Short Entry Id", strategy.short)
switch
strategy.position_avg_price * 1.09 and ta.rsi(close, 70) = > strategy.close("My Long Entry Id")
strategy.position_avg_price * 1.10 and ta.rsi(close, 25) = > strategy.close("My Long Entry Id")
//new trad
#include <iostream>
#include <vector>

const int SMA_PERIOD = 20;
const int RSI_PERIOD = 14;
const int RSI_BUY_THRESHOLD = 20;
const int RSI_SELL_THRESHOLD = 65;

std::vector<double> prices;

double getSMA() {
    double sum = 0;
    for (int i = prices.size() - SMA_PERIOD; i < prices.size(); i++) {
        sum += prices[i];
    }
    return sum / SMA_PERIOD;
}

double getRSI() {
    double avgGain = 0, avgLoss = 0;
    for (int i = prices.size() - RSI_PERIOD; i < prices.size(); i++) {
        double change = prices[i] - prices[i - 1];
        if (change > 0) {
            avgGain += change;
        } else {
            avgLoss -= change;
        }
    }
    avgGain /= RSI_PERIOD;
    avgLoss /= RSI_PERIOD;
    double rs = avgGain / avgLoss;
    return 100 - (100 / (1 + rs));
}

int main() {
    // Collect historical prices
    // ...

    double sma = getSMA();
    double rsi = getRSI();
    if (rsi < RSI_BUY_THRESHOLD) {
        // Buy
    } else if (rsi > RSI_SELL_THRESHOLD) {
        // Sell
    }

    return 0;
}


