#Python Lesson 3.1 - List (Slicing Specifics)

#Slicing - Extract certain elements in a string
#Index - nth position of an element in a list or string
# list[start:end:step]

########### DEMO OF list[start:end] ###########

listeg1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1    

# negative starts in 1, coming from the right so...
# index reflects the total number of elements

print (listeg1[-1])

print (listeg1[:-1])          
#1st input is inclusive whiel 2nd is exlusive
# n-1 is total number of indexes where n is the total number
# of elements as counting starts from zero

print (listeg1[-10:-1])
#negative values and positive could be mix and matched

print (listeg1[:-1])
#blank means all of it from that certain direction

########### DEMO OF list[start:end:step] ###########

print (listeg1[0:-1:3]) 
#step is the number of times we skip

print (listeg1[-1:0:-2]) 
#negative step will run in reverse

print (listeg1[-1:0:-1])
print (listeg1[::-1])
#reading in reverse

#Sample Problems for Reverse
url = 'http://rasty.com'

#reverse the url
print (url[::-1])
print (url[-16:0:-1])

#get the top level domain '.com'
print (url[-1:-5:-1])
print (url[12:16])
print (url[12:])
print (url[-4:])

#print the url without the http://
print (url[7:])
print (url[-9:])

#print the url without http and top level domain
print (url[7:-4])
print (url[-9:-4])
