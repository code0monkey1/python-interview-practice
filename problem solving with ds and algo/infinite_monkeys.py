from random import random


import math
objective='methinks it is like a weasel'

highest_score=0
highest_word=''

english_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def word_generator():
  word=[]
  for _ in range(len(objective)):
    word.append(english_alphabets[math.floor(27*random())])
  
  return ''.join(word)


def score(word,objective):
  
  high_score=0
  
  for i in range(len(objective)):
    
    if objective[i]==word[i]:
      high_score+=1
  
  return high_score
    
while highest_score!= len(objective):
  word=word_generator()
  this_score=score(word,objective)
  
  if this_score>highest_score:
    highest_score=this_score
    highest_word=word
    print("closest word",word,'highest score',highest_score)

  
      