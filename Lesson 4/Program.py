import turtle


def ftoc():
	
	'''
	Converts Fahrenheit to Celsius with equation
	'''
	
	tempf = int(input("What temperature is it in Fahrenheit? "))
	cel = ((tempf - 32)*5/9)
	print (str(tempf) + " degrees Fahrenheit is " + str(cel) + " in Celsius.")

def acretobarn():
	
	'''
	Converts an amount of acres into approximately the right amount of 
	barns using an equation.
	'''
	
	acres = float(input("How many acres does your house sit on?"))
	barns = acres*4.0469e31
	print (str(acres) + " acres is approximately " + str(barns) + " barns.")

def turtpoly():
	
	'''
	Creates a turtle and uses various equations to determine 
	the interior angle for the shape the user wants.
	'''
	
	sides = int(input("Enter a number of sides greater than 2 for your polygon."))
	if sides >= 3:
		joe = turtle.Turtle()
		angle = (((sides - 2) * 180) / sides)
		angle = 180 - angle
		for side in range(sides):
			joe.forward(65)
			joe.left(angle)
			
		screen = joe.getscreen()
		screen.mainloop()
	else:
		print ("Don't do that.")		

ftoc()
acretobarn()
turtpoly()
