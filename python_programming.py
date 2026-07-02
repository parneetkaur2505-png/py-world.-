print("VARIABLES AND DATA TYPES")

print("VARIABLES")
print("Hello,World")   #string
name="parneet"   #string
age=20   #integer
passion="coding"   #string
hobby="painting"   #string
study="BCA"   #string

print(name)
print(age)
print(passion)
print(hobby)
print(study)
print("my name is:",name)
print("my age is:",age)
print("my passion is:",passion)
print("my hobby is:",hobby)
print("my study is:",study) 

print("data types")
print(type(name))
print(type(age))
print(type(passion))
print(type(hobby))      
print(type(study))  

age=25
old=False
a=None  
 
print(type(old))
print(type(a))

print("Arithmetic Operations")
print("SUM")
a=10
b=20
c=a+b
print(c)
print("SUBTRACTION")
a=200
b=100
c=a-b
print(c)
print("MULTIPLICATION")
a=10
b=20
c=a*b
print(c)
print("DIVISION")
a=100
b=20
c=a/b
print(c)
print("MODULUs")#remainder 
a=100
b=20
c=a%b
print(c)
print("EXPONENTIATION")#power
a=2
b=3
c=a**b
print(c)    

print("Relational operators")
a=20
b=40
print(a==b) #equal to
print(a!=b) #not equal to
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to  

print("Assignment operators")
a=10
b=20
a=a+10
print("number:", a)
num=10
num-=10
print("number:", num)
num=10
num*=10
print("number:", num)
num=10
num/=10
print("number:", num)
num=10
num%=10
print("number:", num)   
num=10
num**=10
print("number:", num)      

print("Logical operators")
a=30
b=40    
print(a and b)#and operator ,in this values must be same to get true 
print(a or b)#or operator, in this values must be different to get true
print(not a)#not operator, in this values must be different to get true
print(not b)
#for another example
print(not(a))#not operator example 
print("or operator:", a < b or a > b)
print("and operator:", a < b and a > b)
print("not operator:", not(a < b and a > b))       

print("Type casting")
a=10
print(float(a))
print(str(a))
print(bool(a))
print(complex(a))
a=10.3
b=20
print(int(a))
print(float(b))

print("Type conversion") #automatically converts the types 
a=30.4
b=40
sum=a+b
print (sum) #answer is 70.4 , now convert this value to integer type  
c=70.4
print(int(c))#the answer is now 70 

print("Input function")
name=input("Enter your name:")
print("your name is ",name)
email=input("enter your email:")
print ("your email is ",email)
#input function always takes input in string format, so if we want to take input in integer format then we have to use int() function
age=int(input("Enter your age:"))
print("your age is ",age)
age=input("Enter your age:")
print(type(age)) #the answer is string because input function always takes input in string format   

#now i am solving a problem of taking two input numbers and their sum 
first  =int(input("enter the first number:"))
second =int(input("enter the second number:"))
print("the sum of two numbers is :",first+second)




