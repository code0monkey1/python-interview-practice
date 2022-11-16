
def dec_to_bin(number):
    
    bin_string=''
    
    seq=[]
    
    while number :
      rem= number % 2
      seq.append(str(rem))
      
      number = number//2
    
    while len(seq):
      bin_string+=seq.pop()
    
    return bin_string

print(dec_to_bin(42)=='101010')