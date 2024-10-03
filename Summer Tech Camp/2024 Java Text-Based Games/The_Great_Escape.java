
import java.util.Scanner;

public class The_Great_Escape {

    private static int key;
    private static int toLowerCase;
    private static int lives;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        key = 0;
        lives = 3;

        System.out.println("___       __    ___   __   __  __  ___   __  __   __  __   __   __                   ");
        System.out.println(" |  |__| |__   |  __ |__| |__ |__|  |   |__ |__  |   |__| |__| |__                       ");
        System.out.println(" |  |  | |__   |___| |  \\ |__ |  |  |   |__  __| |__ |  | |    |__                   \n");

        System.out.println(" Type start to start the game\n");
        String answer = input.nextLine();
        String lower_answer = answer.toLowerCase();

        if (lower_answer.equals("start")) {
            System.out.println("\n");
        } else {
            System.out.println("wrong");
            System.exit(0);
        }

        System.out.println("You are a super human that born in a test tupe that is in a special lab in a space station. their teach you simple stuff like english  ");

        System.out.println("Are you going to escape or stay here and get tested on?\n");
        String run = input.nextLine();
        String lower_run = run.toLowerCase();

        if (lower_run.equals("escape") || lower_run.equals("yes")) {

            System.out.println("Ok lets get started");
            System.out.println("Press enter to go next");
            input.nextLine();
            System.out.println("How do you want to escape, Break the glass of the test tupe that you are locked in or wait in till they get you out for an experiment then escape?  1 or 2?");
            String fun = input.nextLine();
            String lower_fun = fun.toLowerCase();

            if (lower_fun.equals("1")) {
                System.out.println("You succesful break the glass and escaped. You go in the hallway ");
                System.out.println("");
            } else {
                System.out.println("You knockout the scientest and take his entry card. You enter in the hallway. ");
                key = key + 1;
                System.out.println("\nkey : " + key);
                
            }

            System.out.println("Press enter to go next");
            input.nextLine();
            System.out.println("You are now in the hallway what are you going to do? 1: go in the vent that is on the floor or 2: Run into a room find enquipment to prepare for your escapes from the space station  ");
            System.out.println("");
String planet = input.nextLine();
String lower_planet = planet.toLowerCase();
if (lower_planet.equals("2") || lower_planet.equals(+ key )){
    System.out.println("");
    System.out.println("TO BE CONTINUED");
}
else {
    System.out.println("you hind in a vent and find a space ship habor.");
System.out.println("1:do you sneek in a space ship that is leaving. 2: continue crawling through the vent");
String ko = input.nextLine();
String lower_ko = ko.toLowerCase();

if (lower_ko.equals("1")){
    System.out.println("You succesful sneek in, the space ship leaves to mars ");
    System.out.println("TO BE CONTINUED");
}
else {
    System.out.println("while you are crawl through the vents you fall and the scienctest catch you and lock you up ");
    lives = lives - 1;
    System.out.println("\n Lives left :" + lives );
    System.out.println("TO BE CONTINUED");


}

}

        } else {
            System.out.println("Have fun getting tested on");
            System.out.println("Press enter to go next");
            input.nextLine();
            System.out.println("\nAfter many years of getting tested on their let you go. they release you in a caspule to earth. Caspule is heading for the middle of the ocean ");
            System.out.println("Press enter to go next");
            input.nextLine();
            System.out.println("How are you going to escape this situtions? are you going to try to redirect the caspule to land or prepare to crash in the water? 1 or 2? ");
            String ring = input.nextLine();
            String lower_ring = ring.toLowerCase();

            if (lower_ring.equals("2")) {
                System.out.println("You crash in the water and you make it to cuba by using the caspuleas as a boat to make it there ");
                System.out.println("live the rest of your life their or try to go north. 1 or 2");
String planet = input.nextLine();
String lower_planet = planet.toLowerCase();

if (lower_planet.equals("2")){
    System.out.println("You go north by hijacking a boat and make it to texas's beaches.");
    System.out.println("TO BE CONTINED");
}
else {
    System.out.println("Ok have fun living in cuba ");
    System.out.println("Press enter to go next");
    input.nextLine();
    System.out.println("You live the rest of your days here in peace");
    System.out.println("TO BE CONTINUED");

}
            } else {
                System.out.println("You succesful crash in florida at the shore of their beach. What will you do next? ");
                System.out.println("Press enter to go next");
                input.nextLine();
                System.out.println("Find civilizatation to eat and hide from humans or go north in to the wilderness and hunt animals for food. 1 or 2");

                if (lower_answer.equals("2")) {
                    System.out.println("\n");
                    System.out.println("You see a bunny and decide to kill by making a spear");
                    System.out.println("TO BE CONTINUED");
                } else {
                    System.out.println("You see a nearby town that lookes dead, you head over there to seek food the dumperst. After you go explore and see noboby but a dog. befrind the dog or ingore it? 1 or 2 ");
                    System.out.println("Press enter to go next");
                    input.nextLine();
                    System.out.println("");
                    System.out.println("TO BE CONTINUED");

                }
            }
        }

    }
}
