# A Prorgram to Demostrate while loop in Python
#Author: Prakash

import os 

n = 0;

while (n > 5): #This loop will not be executed since n is not greater than 5
    print("n is Greater than that of 5")
    
# while (n < 5): #This loop will be executed since n is less than 5(Infinity Loop since n will always be less then 5)
#     print("n is Greater than that of 5")
    
    
while (n < 5): #This loop will be executed since n is less than 5 
                        #(n is increaesd by 1 in each iteration so loop will end when n is greater then 5)
                        #Loop will end after printing n 5 times
    print("n is Greater than that of 5, n is currently: " + str(n))
    n+=1
    
print("Done!")




