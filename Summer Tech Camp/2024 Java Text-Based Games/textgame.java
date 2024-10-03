
import java.util.Scanner;



public class textgame{
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {

        System.out.println("-------------------");
        System.out.println("|                 |");
        System.out.println("|     Welcome     |");
        System.out.println("|                 |");
        System.out.println("-------------------");
        
        System.out.println("Choose left or right");
        String choice = input.nextLine();
        if (choice.equals("right")) {
            System.out.println("Womp womp you're done you're under the water");
            System.exit(0);
        } else {
            System.out.println("Good choice onto the next part in the space station");
        }

        System.out.println("Theres a bomb that will destroy the space station");
        System.out.println("Theres a red wire and blue wire choose which one to cut");
        String wire = input.nextLine();

        if (wire.equals("red")) {
           System.out.println("KABOOM!!!!!!! You blew up.");
           System.exit(0);
            
        } else {
            System.out.println("Good job you saved the space station");
        }
        System.out.println("Aliens have broken in.");
        System.out.println("Do you want to run or fight?");
        String option = input.nextLine();

        if (option.equals("fight")) {
           System.out.println("You got thrown into space and died");
           System.exit(0);

        } else {
            System.out.println("You were able to avoid the aliens");
        }
        System.out.println("You find weapons to help you fight the aliens.");
        System.out.println("You come across one ");
        System.out.println("Do you want to snipe him or laser him?");
        String OPTION = input.nextLine();

           if (OPTION.equals("snipe")) {
           System.out.println("The alien dodged it and killed you");
           System.exit(0);

        } else {
            System.out.println("The alien was finished");
        }
        System.out.println("Your exploring the space center and you find two doors.");
        System.out.println("Choose left or right?");
        String CHOICE = input.nextLine();

        if (CHOICE.equals("left")) {
            System.out.println("The two other aliens capture you and throw you into space");
            System.exit(0);
            
        } else {
            System.out.println("You go in a room where you find the aliens weakness");
        }
         System.out.println("It says that lasers on impact will kill them");
            System.out.println("Snipers only work if you aim at head");
            System.out.println("It's time for the final battle");
            System.out.println("You go back to the two door and go in the other one ");
            System.out.println("You peek through the door and see both of them standing looking at you");
            System.out.println("They fire lasers at you and destroy your laser gun");
            System.out.println("You have to decide do a no scope-360 trickshot or try to fix the laser gun");
            String Decision = input.nextLine();

            if (Decision.equals("laser")) {
                System.out.println("You get the gun but theres no fixing it and they blast you");
                System.exit(0);
                
            } else {
                System.out.println("You headshot one of the aliens and killed it");
            }
            System.out.println("It's a 1v1");
            System.out.println("You only have one more shot in your sniper use it wisely");
            String wise = input.nextLine();
            
            if (wise.equals("snipe")) {
                System.out.println("You missed the shot");
                
            }
            System.out.println("It's not over you see a mirror on the ground");
            System.out.println("You can use it if he shoots and laser at you and it will bounce of it and hit him");
            System.out.println("Do you wan to do it yes or no");
            String CHOOSE = input.nextLine();

            if (CHOOSE.equals("No")) {
                System.out.println("He blasted you");
                System.exit(0);
                
            } else {
                System.out.println("You pulled of the move and saved the space station");
            }
            System.out.println("--------------------");
            System.out.println("|        You        |");
            System.out.println("|        Won        |");
            System.out.println("|        Good       |");
            System.out.println("|        Job       |");
            System.out.println("--------------------");
                
            
    }
}