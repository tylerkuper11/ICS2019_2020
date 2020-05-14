import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ICS_08_kupert21
{
	public static void main(String[] args)
    {
		JFrame frame = new JFrame("Example");
        MyPanel panel=new MyPanel();
        panel.setPreferredSize(new Dimension(500,500));
		frame.add(panel);
        panel.addMouseMotionListener(panel);
        panel.addMouseListener(panel);
        frame.pack();
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}

class MyPanel extends JPanel implements MouseMotionListener, MouseListener
{
    public int x=0;
    public int y=0;
    public int w=10;
    public int c=0;
    
    public void paint(Graphics g)
    {
        //super.paint(g);
		Graphics2D g2=(Graphics2D)g;
        g2.setColor(Color.BLACK);
        g2.fillRect(0,0,getWidth(),getHeight());
        
        g2.setColor(new Color(50,(y+c)/4,(x+c)/4));
        //~ g2.fillRect(x,y,w,50);
        g2.setFont(new Font("BenguiatBold",Font.PLAIN, 35));
        //~ g2.
        g2.drawString("QUENTIN TARANTINO", 48, 280);
        g2.setFont(new Font("BenguiatBold",Font.PLAIN, 30));
        g2.drawString("DIRECTED BY", 127, 220);
        g2.drawString("WRITTEN AND", 126, 180);
        
        
        g2.setColor(new Color(100,(y+c)/3,(x+c)/3));
        //~ g2.fillRect(x,y,w,50);
        g2.setFont(new Font("BenguiatBold",Font.BOLD, 35));
        //~ g2.
        g2.drawString("QUENTIN TARANTINO", 45, 280);
        g2.setFont(new Font("BenguiatBold",Font.BOLD, 30));
        g2.drawString("DIRECTED BY", 125, 220);
        g2.drawString("WRITTEN AND", 125, 180);
      
	}
    
    public void mouseDragged(MouseEvent e){}
    public void mouseMoved(MouseEvent e)
    {
        x=e.getX();
        y=e.getY();
        repaint();
    }
    
    public void mouseClicked(MouseEvent e){}
    public void mouseEntered(MouseEvent e){}
    public void mouseExited(MouseEvent e){}
    public void mousePressed(MouseEvent e)
    {
        if(e.getButton()==1)c+=25;
        else if(e.getButton()==3)c-=25;
        repaint();
    }
    public void mouseReleased(MouseEvent e){}
    
}
