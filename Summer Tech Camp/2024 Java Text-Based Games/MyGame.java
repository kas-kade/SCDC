import java.util.Scanner;

public class MyGame {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("miller: the game");

        System.out.println("What is your name?");
        String name = input.nextLine();

        System.out.println("Let's start the game!");

        System.out.println("Do you want to go left or right?");
        String choice = input.nextLine();

        if (choice.equals("left")) {

            System.out.println("You die");
        }

        if (choice.equals("right")) {

            System.out.println("you are right! ");


        }
    }
}
