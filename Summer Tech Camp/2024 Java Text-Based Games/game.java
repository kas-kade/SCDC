
import java.util.Scanner;

public class game {

    

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

 
         System.out.println("         |-----------------------|");
         System.out.println("         |                       |");
         System.out.println("         |      escape mars      |");
         System.out.println("         |                       |");
         System.out.println("         |-----------------------|");

        System.out.println("you'er on a base in mars and you were traped by aliens do you try to use a wrench to bust the lazer door or stay in there  ");
        String answer = input.nextLine();

        if (answer.equals("use wrench")) {
            System.out.println("good job you got out the chamber ");

        } else {
            System.out.println("they probe you ");
            System.exit(0); 
        }

        System.out.println("you run into a hall do you go left or right ");
        answer = input.nextLine();

        if (answer.equals("left")) {
            System.out.println("cool");

        } else {
            System.out.println("you fall into a trap ");
            System.exit(0);
        }

        System.out.println("you go left and run into a group of aliens do yo drop kick them or beat them up with a comidicly large spork ");
        answer = input.nextLine();

        if (answer.equals("use spork")) {
            System.out.println("good job");

        } else {
            System.out.println("they get you by the leg and blast you ");
            System.exit(0);
        }

         System.out.println("you get passed them and you have and option either confront the leader or take a escape pod  ");
        answer = input.nextLine();

        if (answer.equals("leader")) {
            System.out.println(" ok lets go");

        } else {
            System.out.println("ok boring");
            System.exit(0);
        }
        
 System.out.println("you confront the leader he says to join him or fight him with your comidicly large spork");
        answer = input.nextLine();

        if (answer.equals("spork")) {
            System.out.println("you defeat him and escape ");
         System.out.println("         |-----------------------|");
         System.out.println("         |                       |");
         System.out.println("         |        the end        |");
         System.out.println("         |                       |");
         System.out.println("         |-----------------------|");

        } else {
            System.out.println("he betrays you l bozo");
            System.exit(0);
        }
        

        
    }
}
