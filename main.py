import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

random_integer = random.randint(1,100)
print (random_integer)

random_float = random.random()
print (random_float)
#to create random float number betwwen 0 -5
random2_float = random.random() * 5
print (random2_float)

#who is going to buy the meal today
names=["wande", "segun", "darion","audrey"]
print(names)
names[0]="Wande"
#append and extend only add to the end of the list
names.append("family")
print(names)
print(names[0],names[-1],names[-2])
names.extend(["dad","mum"])
print(names)


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

