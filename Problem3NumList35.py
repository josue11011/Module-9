# Josue Cifuentes
# November 30, 2022
# Problem #3: : Ask the user to enter a number then append each entered number to a list and add them together
# and continue asking for a number until the sum of the list of numbers is greater than 100.
L=[]
while(sum(L)<=100):
	n = int(input("Choose a number: "))
	L.append(n)