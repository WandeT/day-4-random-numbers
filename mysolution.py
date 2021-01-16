import random

payer = input("Give me everybody's names separated by commas\n")
new_payer=payer.split(", ")
print(new_payer)

#using random integers
#x=len(new_payer)
#print(x)

#random_name= random.randint(0 ,x-1)
#print(f"the name of the person who pays is: ", new_payer[random_name])

#random.choice is an easy way to solve this challenge

random_name= random.choice(new_payer)
print(f"the name of the person who pays is: ", random_name)