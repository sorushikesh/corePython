# Function to get team name from user
def get_team_name():
    name = input("Which is your favourite football team? ").strip()
    return name.upper()


# Function to get UEFA Champions League wins safely
def get_uefa_cl_count(team_name):
    while True:
        try:
            count = int(input(f"How many UEFA CL cups has {team_name} won? "))
            return count
        except ValueError:
            print("❌ Please enter a valid number.")


# Main program
def main():
    popular_teams = ["REAL MADRID CF", "FC BARCELONA", "BAYERN MUNICH", "LIVERPOOL FC", "MANCHESTER UNITED"]

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
            print(f"🤔 Hmm, not quite right. As of now, {team_name} has won only 16.")
        else:
            print(f"📚 Noted! But {team_name} has more than {cl_wins} titles.")
    else:
        print(f"Let's hope {team_name} wins more UEFA titles in the future!")


if __name__ == "__main__":
    main()
