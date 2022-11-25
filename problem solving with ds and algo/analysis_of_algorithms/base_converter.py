# Practice problem https://www.codechef.com/problems/CONV02?tab=statement ( the example is wrong , test cases should be 3 not 2)

def base_converter(number,base):
  converter='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
  bin_str=''
  my_list=[]
  
  while number:
    mod=number%base
    my_list.append(mod)
    
    number=number//base
  
  while len(my_list):
    bin_str+=converter[my_list.pop()]
  
  return bin_str

print(base_converter(256,16))