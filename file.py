"""
Create a Python file named lab_7-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-2 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately




________________________________________________________________________________

Create a Python file named lab_7-5.py


Copy the code from your labs 6-5 through 6-8
Turn each of the programs into a function
Add 4 test cases to the functions
Ensure your code runs accurately


"""
"""
Create a Python file named lab_7-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-2 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately
"""
numbers = input("What are your numbers? ")
a = numbers.find(",")
def findsum (n1, n2):
    n1 = numbers[:a]
    n2 = numbers[a+2:]
    num1 = int(n1)
    num2 = int(n2)
    numsum = num1 + num2
    print(numsum)
findsum(111, 222)
"""
Create a Python file named lab_7-5.py


Copy the code from your labs 6-5 through 6-8
Turn each of the programs into a function
Add 4 test cases to the functions
Ensure your code runs accurately


"""

#6-5
numi = input("What are your numbers? ")
a = numi.count(",")
rep = 0
numl = [rep]
while rep < a:
    b = int(numi.find(","))
    numl [rep] = int(numi [0,b-1])
    del numi [0, b+1]
    rep = rep + 1
print (numl)




#6-6
'''
#6-7

word1 = input("Word 1?")
word2 = input("Word 2?")
word3 = input("Word 3?")
word4 = input("Word 4?")
word5 = input("Word 5?")
if len(word1) == len(word2):
    print("Please start over!")
if len(word1) == len(word3):
    print("Please start over!")
if len(word1) == len(word4):
    print("Please start over!")
if len(word1) == len(word5):
    print("Please start over!")
if len(word2) == len(word3):
    print("Please start over!")
if len(word2) == len(word4):
    print("Please start over!")
if len(word2) == len(word5):
    print("Please start over!")
if len(word3) == len(word4):
    print("Please start over!")
if len(word3) == len(word5):
    print("Please start over!")
if len(word4) == len(word5):
    print("Please start over!")
wordlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print (wordlen[len(word1)])
print (wordlen[len(word2)])
print (wordlen[len(word3)])
print (wordlen[len(word4)])
print (wordlen[len(word5)])

#6-7
numa = int(input("What's your first number? "))
numb = int(input("What's your second number? "))
numc = int(input("What's your last number?"))
print (list[numa*2, numb*2, numc*2])

#6-8
num1 = int(input("What's your first number? "))
num2 = int(input("What's your second number? "))
num3 = int(input("What's your last number?"))
if num1 % 2 == 0:
    if num2 % 2 == 0:
        if num3 % 2 == 0:
            print("Even")
        else:
            print ("mixed")
    else:
        print ("Mixed")
elif num2 % 2 == 0:
    print ("Mixed")
elif num3 % 2 == 0:
    print ("Mixed")
else:
    print ("Odd")
    '''
