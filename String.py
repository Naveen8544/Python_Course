words = ['python' , 'is' , 'easy']
print(' '.join(words))

text = "python programming"
print(text.find("pro"))

text = "Python Programming"
print(text.index("Pro"))

text = "Python Programming"
print(text.startswith("Py"))

text = "report.jpeg"
res = (text.endswith(".jpg"))
print(res)

text = "apple apple mango"
print(text.count("apple"))

text = "apple apple mango"
print(text.count("a"))

text = "apple apple mango"
print(text.count("A"))

text = "Python Programming"
print(text.isalpha())

text = "Python1"
print(text.isalpha())

text = "12345"
print(text.isdigit())

text = "Python123"
print(text.isalnum())

text = "PyThOn"
print(text.swapcase())

text = "Python"
print(text.center(20, "_"))

num = "25"
print(num.zfill(5))


name = "Naveen"
age = 25
email = "naveensharmaaurangabad@gmail.com"
print("My name is {} and age is {} and my email id : {}".format(name, age ,email))

name = "Naveen"
marks  = 95
print(f"{name} scored {marks} marks")

#Remove
a =["Apple", "Banana", "Mangoes"]
result = a.remove("Apple")
print(result)
print(a)

#pop
num = [2,3,4,5]
res = num.pop()
print(res)
#print(num)

#Clear
num = [1,2,3,4]
res = num.clear()
print(res)
print(num)


list1 =["Naveen", "Nitesh", "Suraj"]
res = list1.index("Nitesh")
print(res)


item =[1,1,2,3,1]
print(item.count(3))

#Sort
b = [4,8,2,3,0]
b.sort()
print(b.sort(reverse=True))
print(b)

b = [4,30,2,3,0]                #array me 30 ko 30 count nhi karega , 3 or 0 count karega
b.sort()
print(b.sort(reverse=True))
print(b)

#reverse
b = [4,30,2,3,0]
print(b.reverse())
print(b)

#copy
b = [1,2,3,4,5]
copy1 = b.copy()
print(copy1)

#len
b = [4, 30, 2, 3, 0]
print(len(b))

#max
b = [4, 30, 2, 3, 0]
print(max(b))

#min
b = [4, 30, 2, 3, 0]
print(min(b))

#sum
b = [4, 30, 2, 3, 0]
print(sum(b))

#sorted
b = [4, 30, 2, 3, 0]
print(sorted(b))

#Square
num = [1,2,3,4,5]
res = []
for i in num:
    res.append(i*i)
print(res)

squares = [x*x for x in range(5)]
print(squares)

#Create Squares
squares = [i*i for i in range(2 ,8)]
print(squares)

squares = [i*i for i in range(2 ,8 ,2)]
print(squares)

#Even Numbers
even_numbers = [i for i in range(1 ,11) if i % 2 == 0]
print(even_numbers)

#Odd Numbers
odd_numbers = [i for i in range(1 ,11) if i % 2 != 0]
print(odd_numbers)

#Convert String to uppercase
List = ["python", "programming", "is", "easy"]
result = [i.upper() for i in List]
print(result)

List = ["Aman", "Naveen", "Suraj"]
result = [i.upper() for i in List]
print(result)

#Lenth of List
List = ["aman", "naveen", "suraj"]
result = [len(i) for i in List]
print(result)

List = ["a man", "na veen", "s u raj"]
result = [len(words) for words in List]
print(result)

#condition Expression
result = ["Even" if i % 2 == 0 else "Odd" for i in range(1,6)]
print(result)

#Nested List
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

