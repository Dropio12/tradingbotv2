// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Kokoabe

//@version=5
indicator("Mon script",overlay=true)// overlay pour le mettre sur le chart
float b=1
float a=1
b:=math.max(close,open)//return la valeur la plus grande entre eux
if b==20
    b:=close
if a==20
    a:=open
for i=1 to 3
    b:=b+1
while a<10
    a:=a+1
    if a<12
        break

switch
    a==10 => b:=1// si a = 10 donc b va etre mis a 1
    a==20 => b:=2
    a==30 => b:=3
f(x,y) => // fonction
    sum=(x+y)/2
    sum2=sum/2
    [sum,sum2] //return sum & sum2
    //il faudra deux variable pour contenir ces deux resultats


[K1,K2]= f(close[1], open[1]) // open [1] == le prix d'entrée de la dernière journée(hier)
MOVINGAVG= ta.sma(close,200)//calculate 200 day moving average (ta= technical analysis & sma= moving average)
RSI= ta.rsi(close,14)// 14 period rsi
HIGHESTCLOSE= ta.highest(close,50)//highest close of the last 50 days


plot(K2,color = color.red, style=plot.style_histogram)//le style du plot(histograme,fleche,etc)
plot(b,color=color.new(#955628,0)) //le premier chiffre est la couleur et deuxieme l'opacité
plot(a,title = 'Allo')//pour mettre un titre
