/*
 * Polygon-making turtle program
 * @ author Tyler Kuper
 * @ version 1.0
 * @ since 09-19-19
 * */


import java.util.Scanner;
public class Program
{
		public static void main(String[] args)
		{
			int Sides;
			int Angle;
			int x;
			int y;
			
			/*Asks the user for an input for the number of sides on the polygon.
			 *Uses that information to calculate the angles of the polygon to 
			 *use in the turtleShape function.
			 * */
			Scanner in = new Scanner(System.in);
			System.out.println("Enter an integer greater than 2 for how many sides you want on your polygon.");
			Sides = in.nextInt();
			if (Sides <= 2) {
				throw new IllegalArgumentException("The number of sides must be greater than 2");
			} else {
				Angle = (((Sides - 2) * 180) / Sides);
				Angle = (180-Angle);
				Turtle bro;
				bro = new Turtle();
				turtleShape(Sides,Angle,bro);
			}
			
		}
		/* This function will take the measure of the sides and angles of the entered
		 * integer and also the turtle that was created to make a recursive way to
		 * guide the turtle and create the shape the user has input
		 * 
		 * */
		public static void turtleShape(int x,int y,Turtle bro)
		{
			if (x < 0){
				return;
			} else {
				bro.forward(100);
				bro.left(y);
				turtleShape(x - 1,y,bro);
				
			}	
		}	
			
			
}
