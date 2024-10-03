
import java.util.Scanner;

public class Main {

    private static int lives = 3;

    public static void main(String[] args) {

        /*
     System.out.println("what is your name: ");
    String name = obj.nextLine(); 
      
    System.out.println("hi"+ name + ", how old are you ");
    int age = obj.nextInt();

   System.out.println ("what do you a like to do");d   
         */
 /*
    String myname="Dj"; 
    int height=20;
    int width =30;
    int area =height*width;
    
    System.out.println("my name is "+ myname+ " this code finds the area of a Rectangle.");
    System.out.println("The height is : " + height + " and the width;

      
    System.out.println{"hi"+ name + ", how old are you "}
    int name = obj.nextLine():

   System.out.println {what do you a like to do }
}   */
        Scanner input = new Scanner(System.in);
        System.out.println("How far is the moon from eart in miles?");
        String answer = input.nextLine();

        if (answer.equals("238855")) {
            System.out.println("you got it");

        } else {
            System.err.println("not right");
            lives = lives - 1;
            System.out.println("Lives left " + lives);
        }

        System.out.println("what is A3+B3+C3= ");
        String math_answer = input.nextLine();

        if (math_answer.equals("22")) {
            System.out.println("(you are good!)");

        } else {
            System.out.println("not good");
            lives = lives - 1;
        }

        System.out.println("how old is nasa");
        String nasaanswer = input.nextLine();

        if (nasaanswer.equals("66")) {
            System.out.println("good job");

        } else {
            System.out.println("no no");
            lives = lives - 1;
        }

        System.out.println("who was the first pokemon created");
        String pokemonanswer = input.nextLine();

        if (pokemonanswer.equals("rhydon")) {
            System.out.println("yes!");
        } else {
            System.out.println("no");
        }

        System.out.println("Humans have traveled into space for how long");
        String spaceanswer = input.nextLine();

        if (spaceanswer.equals("50")) {
            System.out.println("yes");

        } else {
            System.out.println("no!");
        }

        System.err.println("Space shuttles need how many liters of fuel");
        String fuelanswer = input.nextLine();

        if (fuelanswer.equals("1.9 million")) {
            System.out.println("good");
        } else {
            System.out.println("no no NO");
        }
    }
}
