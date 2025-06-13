# armstrong number
num=int(input("enter a number"))
temp=num
n=len(str(num))
result=0
while num!=0:
    digit=num%10
    result=result+digit**n
    num=num//10
if result==temp:
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")

# to find the diagonal of a matrix
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range (len(matrix)):
    print(matrix[i][i])

# to find the anti diagonal of a matrix
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(len(matrix)):
    print(matrix[i][len(matrix)-i-1])

# palindrome
word=input("enter a word")
for i in range (len(word)//2):
    if word[i]!= word[len(word)-1-i]:
        print(word,"is not a palindrome")
        break
    else:
        print(word,"is a palindrome")

# perfect number
num=int(input("enter a number"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if num==sum:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")

