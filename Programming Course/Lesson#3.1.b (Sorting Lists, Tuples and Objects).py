#Lesson#3.1.b (Sorting Lists, Tuples and Objects)

########### DEMO OF SORTING ###########

#list1 = [19,5,32,2,45,7,1]

#sorting by creating a new variable
#sorted_list1 = sorted (list1)
#print(' Sorted Variable: \n', sorted_list1)
#print('\n Original Variable: \n', list1)

#sorting without creating a new variable: sorting method
#list1.sort()
#print('\n', list1)
#sort method doesnt return a list as it does the sorting in place

#sorting in descending order
#sorted_list1 = sorted (list1, reverse=True)
#print (sorted_list1)

#sorting in descending order: using sorting method
#list1.sort(reverse=True)
#print (list1)

########### SORTING FOR TUPLES ###########

#tup = [19,5,32,2,45,7,1]
#stup = sorted(tup)
#print ('\nOriginal \n', tup)
#print ('\nTuple \n', stup)
#tuples are already-sorted list of elements
#tuple cannot use sort method i.e., tup.sort()

########### SORTING FOR CHARACTERS ###########

#dictionary sample -shows that char can be sorted too
#crushes = ['a_noemi','b_noemi', 'c_noemi', 'd_noemi','naomhie']
#sorted_crushes = sorted(crushes)
#print ('\nDictionary \n', sorted_crushes, '\n')

#crushes.sort()
#print(crushes)
#char can use sort method

########### SORTING FOR NEGATIVE VALUES ###########

#using sorting function
#list2 = [-9,-4,-1,-7,-2,-8,6,3]
#s_list2 = sorted(list2)
#print (s_list2)

#using sorting method
#list2.sort()
#print (list2)

#sorting by absolute value (positive numbers first!)
#list2 = [-9,-4,-1,-7,-2,-8,6,3]
#s_list2 = sorted(list2, key=abs)
#print (s_list2)
#key=abs ignores the sign

########### SORTING VARIABLES WITH NAMES ATTRIBUTES ###########

#demonsrate the use of keys

class student():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return '(\n\nname: {}, \n\nage: {}, \n\nsalary: ${})'.format(self.name, self.age, self.salary)
    
#s1 = student('a_Noemi', 19, 16000)
#s2 = student('c_Neoms', 20, 18000)
#s3 = student('b_Emi', 21, 17000)

#students = [s1,s2,s3]

#s_student = sorted(students)
#print(students)
#keys are needed to sort unsortable variables

#def s_sort(stud):
#    return stud.salary
#s_student = sorted(students, key=s_sort, reverse=True)
#print(s_student)
#parameters are considered as specifiers

#lambda function ????

#using attrgetter
from operator import attrgetter
s1 = student('a_Noemi', 19, 16000)
s2 = student('c_Neoms', 20, 18000)
s3 = student('b_Emi', 21, 17000)

students = [s1,s2,s3]
s_student = sorted(students, key=attrgetter('age'))
print(s_student)
