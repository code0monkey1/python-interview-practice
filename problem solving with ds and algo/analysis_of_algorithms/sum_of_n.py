

def sum_of_n(n):
  sum=0
  
  for i in range(n+1):
    sum+=i
    
  return sum

def _sum_of_n(n):
  
  return (n*(n+1))//2

print(_sum_of_n(10**8))

