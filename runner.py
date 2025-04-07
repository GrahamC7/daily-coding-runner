import random
import webbrowser
from datetime import datetime


def load_problems(file_path="problems.txt"):
    with (open(file_path, "r") as f):
        return [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]


def load_logged_problems(file_path="log.txt"):
    problems = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                parts = line.strip().split(" - ")
                if len(parts) == 2:
                    problems.append(parts[1])
    except FileNotFoundError:
        pass
    return problems


def pick_problem(problems):
    return random.choice(problems)


def log_selection(problem_url, file_path="log.txt"):
    with open(file_path, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {problem_url}\n")


def main():
    new_problems = load_problems()
    logged_problems = load_logged_problems()

    if not new_problems and not logged_problems:
        print("No problems found in problems.txt or log.txt!")
        return

    while True:
        print("\n🧙 Welcome to Daily Coding Runner\n")
        print("1) New problem only")
        print("2) Review past problem")
        print("3) Surprise me (70% new / 30% review)")
        print("4) Quit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            if not new_problems:
                print("⚠️ No new problems available!")
                continue
            selected = random.choice(new_problems)
            source = "new"

        elif choice == "2":
            if not logged_problems:
                print("⚠️ No review problems available!")
                continue
            selected = random.choice(logged_problems)
            source = "review"

        elif choice == "3":
            if new_problems and (not logged_problems or random.random() < 0.7):
                selected = random.choice(new_problems)
                source = "new"
            elif logged_problems:
                selected = random.choice(logged_problems)
                source = "review"
            else:
                print("⚠️ No problems found!")
                continue

        elif choice == "4":
            print("👋 Goodbye!")
            return


        else:

            print("❌ Invalid choice, try again.")

            continue

        print(f"\n🧠 Your coding challenge ({source}):\n{selected}")

        webbrowser.open(selected)

        if source == "new":
            log_selection(selected)

        break  # Exit after showing the problem


if __name__ == "__main__":
    main()
