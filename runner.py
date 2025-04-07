import random
from datetime import datetime

def load_problems(file_path="problems.txt"):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

    def pick_problem(problems):
        return random.choice(problems)

    def log_selection(problem_url, file_path="log.txt"):
        with open(file_path, "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {problem_url}\n")

    def main():
        problems = load_problems()
        if not problems:
            print("No problems found in problems.txt!")
            return

        selected = pick_problem(problems)
        print(f"Today's coding challenge:\n{selected}")
        log_selection(selected)

    if __name__ == "__main__":
        main()