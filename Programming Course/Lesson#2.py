#Python Lesson 2 - Integers and Floats

num = 18
num2 = 18.32
print(type(num))
print(type(num2))

########### Arithmetic Operatiors ###########

#multiplication
print(18 * 1) 

#addition
print(18 + 1) 

#division
print(3 / 2)  

#drops the decimal / floor division
print(3 // 2) 

#exponents
print(3 ** 2) 

#modulus
print(5 % 3)  
# used to tell the number is an even or odd
# if the result is 1, it is odd; if 0, it even

#subtraction
print(3 - 2)  


#note: it follows PEMDAS rule

########### Increment Methods ###########

num3 = 5
num4 = 5

num3 = num3+1
print(num3)     #adding directly to the variable

num4 += 1
print(num4)     #using +=
                #it is also availabe to the other operators 
                

########### Built-in Functions ###########

#absolute value - removes the negative sign from a number
print(abs(-6))

#rounded values - simply rounds values
print(round(18.28))

#rounded values - roudsn from specific decimal place
print(round(18.28423, 3))


########### Comparison Operators ###########
#1. equal                       ==
#2. not equal                   !=
#3. greater than                >
#4. less than                   <
#5. greater than or equal       >=
#6. less than pr equal          <=

#checking
num_1 = 3
num_2 = 2
print(num_1 == num_2)
print(num_1 >= num_2)
print(num_1 != num_2)


########### Numbers Might be a String ###########
a = '100'
b = '200'
print(a + b)
#note: a number will be considered a string if it is enclosed in qoutes

#cast - converting a string to int
c = int(a)
d = int(b)
print(c + d)

