"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

"""

list = [2200,2350,2600,2130,2190]

# Ans 1:
print(list[0]-list[1])

# Ans 2:
print(list[0]+list[1]+list[2])

# Ans 3:
print( 200 in list)
  
# Ans 4:
list.append(1980)

# And 5

list[3]-=200
print(list[3])

print(list)

'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

'''
heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append('black panther')

heros.remove('black panther')

heros.insert(heros.index('hulk')+1,'black panther')

heros[1:3]=["dr. strange"]

heros.sort()

print(heros)


'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

'''
max_number = 10


myList = [ i for i in range(1,max_number+1)  if i%2]

print("myList",myList)

print("hello world")
