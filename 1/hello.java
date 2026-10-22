import java.util.Random;
import java.util.Scanner;

public class TikTokGame {

    public static void displayInstructions() {
        System.out.println("Welcome to the TikTok Game!");
        System.out.println("You will be given a series of challenges.");
        System.out.println("Complete them to earn points!");
        System.out.println("Let's get started!\n");
    }

    public static String getChallenge() {
        String[] challenges = {
            "Do a dance for 10 seconds.",
            "Lip sync to your favorite song.",
            "Imitate a celebrity.",
            "Create a funny skit.",
            "Show off a cool trick."
        };

        Random random = new Random();
        return challenges[random.nextInt(challenges.length)];
    }

    public static void playGame() {
        Scanner scanner = new Scanner(System.in);
        int score = 0;
        int rounds = 5;

        for (int i = 1; i <= rounds; i++) {
            System.out.println("Round " + i);
            System.out.println("Your challenge: " + getChallenge());

            System.out.print("Press Enter when you are ready to start...");
            scanner.nextLine();

            try {
                Thread.sleep(10000); // Wait for 10 seconds
            } catch (InterruptedException e) {
                System.out.println("Timer interrupted.");
            }

            System.out.println("Challenge completed!\n");
            score++;
        }

        System.out.println("Game Over!");
        System.out.println("Your total score is: " + score + "/" + rounds);

        scanner.close();
    }

    public static void main(String[] args) {
        displayInstructions();
        playGame();
    }
}