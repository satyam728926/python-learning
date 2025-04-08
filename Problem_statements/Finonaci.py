a=0
b=1
fibonacci_series=[]
fibonacci_series.append(a)
fibonacci_series.append(b)
def Fibonacci():
     len1=len(fibonacci_series)
     next_term=0
     next_term=fibonacci_series[len1-1]+fibonacci_series[len1-2]
     fibonacci_series.append(next_term)
     if(len1==10):
          print(fibonacci_series)
     else:
          Fibonacci()
Fibonacci()


# # print(next_term)
# print(fibonacci_series)