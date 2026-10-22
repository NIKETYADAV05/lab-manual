
import random
import time


def display_instructions():
    print("Welcome to the TikTok Game!")
    print("You will be given a series of challenges.")
    print("Complete them to earn points!")
    print("Let's get started!")


def get_challenge():
    challenges = [
        "Do a dance for 10 seconds.",
        "Lip sync to your favorite song.",
        "Imitate a celebrity.",
        "Create a funny skit.",
        "Show off a cool trick."
    ]
    return random.choice(challenges)


def play_game(rounds=5, challenge_getter=None, sleep_func=time.sleep):
    if challenge_getter is None:
        challenge_getter = get_challenge

    score = 0

    for _ in range(rounds):
        challenge = challenge_getter()
        print(f"Your challenge: {challenge}")
        input("Press Enter when you are ready to start...")
        sleep_func(10)  # Simulate time to complete the challenge
        print("Challenge completed!")
        score += 1

    print(f"Game Over! Your total score is: {score}/{rounds}")
    return score


if __name__ == "__main__":
    display_instructions()
    play_game()
