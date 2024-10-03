
import java.util.Scanner;

public class GAme {

    private static int Lives;
    private static int Secret;

    public static void main(String[] args) {

        Lives = 3;
        Secret = 5;
        boolean End = false;
        boolean RETRY = false;
        boolean reset = false;
        boolean gamestart = false;
        Scanner input = new Scanner(System.in);

        System.out.println("Welcome to my game!!");
        System.out.println("What is your name?");
        String name = input.nextLine();
        System.out.println("HI " + name);
        System.out.println("In This game you are a intergalactic space explorer on an expedition to a exoplanet called Galileo.");
        System.out.println("Your tasked with getting rock samples from this danugerous planet and bring it back at any cost.");
        while (!gamestart) {
            System.out.println("Type START to start");
            String Start = input.nextLine();

            if (Start.equals("START")) {
                gamestart = true;
            } else {
                System.out.println("Come on man type START ALL CAPS");
            }
        }
        System.out.println("Hay " + name + "..... Come on " + name + " wake up ");
        System.out.println("(You get out of bed, then see your best friend getting ready for a day full of adventure)");
        System.out.println(name + " we need to get to the control room to land the ship on Galileo");
        System.out.println("What part of the planet do you want to land on " + name + ". We can land on the the side that is facing the sun or the dark side");
        System.out.println("Choose BRIGHT SIDE or DARK SIDE");
        String Landing = input.nextLine();
        Landing = Landing.toUpperCase();
        while (!RETRY){
            if (Landing.equals("BRIGHT SIDE")) {
                RETRY = true;
                break;
            } 
            else if(Landing.equals("DARK SIDE")) {
                Secret = Secret - 1;
                break;
            }
            else {
                System.out.println(" REMEMBER TRY ALL CAPS");
            }
            Landing = input.nextLine();

        }
        
        if (Landing.equals("DARK SIDE")){
            System.out.println("OK YOU WANT TO GO TOP THAT SIDE WHERE GOING TO THE SIDE WITH NO SIGNAL"); 
            System.out.println("You get to the dark side and fin your self in the middle of the dark.");
            System.out.println("You wait for the planet to go around it sun for light");
            System.out.println("but you dont know where you are and you can't use a navigator because theres no signal.");
            System.out.println("The ship soon runs out of fuel and you are stranded");
            System.out.println("");
            System.out.println("");
            System.out.println("Congradulations you found the secret ending");
            System.exit(0);
        }

        if (Landing.equals("BRIGHT SIDE")) {
            System.out.println("Ok where going to land on the side with the sun.");
            System.out.println("We need to get in and out the faster we are the lower chance of something bad happening");
            System.out.println("So you go left and I go right if you find a sample go back to the ship and notify me.");
            System.out.println("you answer with ok and go to the left.");
            System.out.println("A few hours later you find a rock suited to be a sample and start collecting pieces.");
            System.out.println("All of a sudden you head a sound from behind you.");
            System.out.println("You turn around and see a three eyed beast, but you still need more samples!");
            while (!reset) {
                System.out.println("Do you RUN or KEEP COLLECTING");
                String WhatToDo = input.nextLine();
                if (WhatToDo.equals("RUN")) {
                    System.out.println("You run back to the ship with the three eyed beast chasing you.");
                    System.out.println("You notice once your in the ship several creatures gathering out side to try braking in.");
                    reset = true;
                } else if (WhatToDo.equals("KEEP COLLECTING")) {
                    System.out.println("You stay and try collecting more");
                    System.out.println("The beast goes up behind you and you get KILLED");
                    Lives = Lives - 1;
                    if (Lives == 2) {
                        System.out.println("Well you weren't supposed to get several tries but I'll give you some any way");
                    }
                    if (Lives == 1) {
                        System.out.println("Pssss I don't think that route works you should try the running");
                    }
                    System.out.println("You have " + Lives + " lives left");
                    if (Lives == 0) {
                        reset = true;
                    }

                } else {
                    System.out.println("TRY ALL CAPS");
                }

            }
            if (Lives == 0) {
                System.out.println("You are out of lives");
                System.out.println("I give you No MORE CHANCES");
                System.exit(Lives = 0);
            }
            else {
                System.out.println("You try getting to the communication terminal but the monsters out side damaged the satalight that allows communication.");
                System.out.println("The monsters are slowly braking throw the ship and are going to get in soon");
            }
            while (!End) {
                System.out.println("What do you do");
                System.out.println("Do you ESCAPE or do you TRY PICKING UP YOUR FRIEND on the way out of the planet");
                String Ending = input.nextLine();
                if (Ending.equals("ESCAPE")){
                    System.out.println("You escape and leave your friend you regret not going back but it is too late");
                    System.out.println("Congradulations you found the GOOD ENDING");
                    System.exit(0);
                }
                else if (Ending.equals("TRY PICKING UP YOUR FRIEND")){
                    System.out.println("You try picking you friend up but the engine dies out and you die");
                    System.out.println("Congradulations you found the BAD ENDING");
                    System.exit(0);
                }   
                else { 
                    System.out.println("TRY ALL CAPS");
                }  
            }

        }

    } 
}
    



/*

while(Start != "START"){
 */
