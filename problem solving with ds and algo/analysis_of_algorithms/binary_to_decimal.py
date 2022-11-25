# Practice problem https://www.codechef.com/problems/PJ10TO2

def bin_to_decimal(bin):
    total=0
    
    for i in range(len(bin)):
      total+=(int(bin[len(bin)-i-1]) * 2**i)
      
    return total
  
print(bin_to_decimal("101010"))