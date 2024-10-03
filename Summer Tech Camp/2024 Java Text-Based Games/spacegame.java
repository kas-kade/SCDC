
import java.util.Scanner;

public class spacegame {

    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {

        System.out.println("your ship is stranded on the moon you need to  find a wrench, screw driver, and a hammer tools to fix it. ");
        System.out.println(" you turn arond and see a pathway to walk");
        System.out.println("you have walked into a fork in the road there are two paths  left and right where do you go?");
        String decision = input.nextLine();
        if (decision.contains("right")) {
            System.out.println("you have encountered a monster fight or fall back?");
            String fight = input.nextLine();
            if (fight.equals("fight")){
                System.out.println("you are instantly eaten, sucks to suck get better buddy.");
                System.out.println(System.exit(0));
            }
            if (fight.contains("fall back")) {
                System.out.println(" you have run back into the fork of the road that you encountered earlier, would you like to go left?");
            }
        }
    }
}
