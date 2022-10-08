import math
import decimal
 
decimal.getcontext().prec = 1010 # 扱える桁数を指定


def series1(n,x): # ネイピア数の計算
    series = 1 + x
    for i in range(2,n+1):
        series = series + (x**i)/math.factorial(i) # 1項ずつ加えていく
    return series
  
  
n = int(input())
  
  
print(series1(n,1))
