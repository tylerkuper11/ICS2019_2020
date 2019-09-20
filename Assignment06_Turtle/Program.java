import java.util.Scanner;
public class Program
{
		public static void main(String[] args)
		{
			int Sides;
			int Angle;
			int x;
			int y;
			
			Scanner in = new Scanner(System.in);
			System.out.println("Enter an integer for how many sides you want on your polygon.");
			Sides = in.nextInt();
			Angle = (((Sides - 2) * 180) / Sides);
			Angle = (180-Angle);
			Turtle bro;
			bro = new Turtle();
			turtleShape(Sides,Angle,bro);
			
		}
		
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
