def isAnagram(first,second):
    
    f_list=[0]*26
    s_list=[0]*26
    
    
    if len(first)!=len(second):
      return False
   
    for i in range(len(first)):
      f_list[ord(first[i])-ord('a')]+=1
    
    for i in range(len(second)):
      s_list[ord(second[i])-ord('a')]+=1
   
    for i in range(26):
      if f_list[i]!= s_list[i]:
        return False
     
    return True
  

