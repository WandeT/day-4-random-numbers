import random

names=input("Write everyone's names separtaed by a comma\n")
names_list=names.split(",")
print(names_list)

payer=random.choice(names_list)
print(payer, "pays the bill")

