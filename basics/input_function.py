"""
This module prompts the user to enter their favorite football team and
displays UEFA Champions League titles with validation.
"""

def get_team_name():
    """Prompt the user to input and normalize their favorite football team."""
    name = input("Which is your favourite football team? ").strip()
    return name.upper()

def get_uefa_cl_count(team_name):
    """Ask user how many UEFA Champions League titles the team has won and validate the input."""
    while True:
        try:
            count = int(input(f"How many UEFA CL cups has {team_name} won? "))
            return count
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    """Main program to interact with user and print team and title information."""
    popular_teams = [
        "REAL MADRID CF", "FC BARCELONA", "BAYERN MUNICH",
        "LIVERPOOL FC", "MANCHESTER UNITED"
    ]

    team_name = get_team_name()
    print(f"\n✅ Team selected: {team_name}")

    if team_name in popular_teams:
        print("👍 That's a well-known team!")
    else:
        print("😎 Interesting choice! You have unique taste!")

    if team_name == "REAL MADRID CF":
        print("🎉 Great! We support the same team!")
        cl_wins = get_uefa_cl_count(team_name)

        if cl_wins == 16:
            print(f"🏆 Wow! {team_name} has indeed won 16 UEFA Champions League titles!")
        elif cl_wins > 16:
            print(f"🤔 Hmm, not quite right. {team_name} has only won 16.")
        else:
            print(f"📚 Noted! But {team_name} has more than {cl_wins} titles.")
    else:
        print(f"Let's hope {team_name} wins more UEFA titles in the future!")

if __name__ == "__main__":
    main()
