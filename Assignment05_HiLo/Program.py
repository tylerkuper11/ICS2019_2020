import random

print("Welcome. I will give you a random number between 1 and 100 and your job is to guess it.\nPlease use only integers.")
randnum = random.randint(1,100)

def hiLo(n): 
	if n == True:
		return
	if n == False:
		g =int(input("What's your guess?"))
		if g < randnum:
			print("Too low.")
			hiLo(False)
		if g > randnum:
			print("Too high.")
			hiLo(False)
		if g == randnum:
			print("Congratulations! You got it!")
			hiLo(True)		
hiLo(False)
print("Done")
