
import java.util.Scanner;

public class textGame {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("_____________________");
        System.out.println("|                    |");
        System.out.println("|                    |");
        System.out.println("|   Done loading...  |");
        System.out.println("|                    |");
        System.out.println("|   press Enter to   |");
        System.out.println("|    to continue     |");
        System.out.println("|____________________|");

        String answer = input.nextLine();

        if (answer.equals("yes")) {
            System.out.println("Well... thats good...ig, you should go fr fr");
        } else {
            System.out.println("Morning mate, you ready to go out and explore the rest of the moon and hopefully find gold");
        }

        String answ = input.nextLine();

        if (answ.equals("yes") || answ.equals("yeah") || answ.equals("mhm") || answ.equals("yup") || answ.equals("sure")) {
            System.out.println("great! lets get going then.");
        } else {
            System.out.println("well you should probably get everything ready");
            System.exit(0);
        }

        System.out.println("Type ok to continue...");
        String an = input.nextLine();

        if (an.equals("ok")) {
            System.out.println("hmmmm... i cant decide either to go right into a moon crater or go stright to see what else we can find.");
        } else {
            System.out.println("Bro how could you frick up typing ok like come on now");
            System.exit(0);
        }
        
        System.out.println("what do you think, right or left?");
        String a = input.nextLine();


        if (a.equals("right")) {
            System.out.println("ok well moon creater it is. lets go.");
        } else {
            System.out.println("ok we will go stright and continue to other parts of the moon");
        }
        
        System.out.println("");
        String ad = input.nextLine();

        if (ad.equals("right")) {
        System.out.println("ok well moon creater it is. lets go.");
        } else {
            System.out.println("ok we will go stright and continue to other parts of the moon");
        }



        }


    }


