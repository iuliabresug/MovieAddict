""" The user introduces float numbers (how many he wants - until he enters 0).
From the list there are randomly extracted 20% of the numbers. The programs returns,
in the end, the product of the numbers in the initial list after the extraction"""
a = [float(raw_input())]
while True:
 meci = float(raw_input())
 a.append(meci)
 if meci == 0:
  break #Make a list with all the float numbers the user imputs, until 0 is typed
del a[-1] #Delete the 0 from the list
print ("The initial list is:"),a
import random
n = len(a) * 1 / 5 #Calculate 20% of the list length
b = random.sample(a, n) #Create a list with n random numbers
print ("The extracted numbers are:"), b
fin = [item for item in a if not item in b or b.remove(item)]
import numpy as np
product = result = np.prod(np.array(fin)) #Calculate the product of the items in the final list
print ("The list of the numbers after the extraction is:"), fin
print ("The product of the numbers is:"), product