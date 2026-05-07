import sys
from simulation import run_simulation


def main():
    filename = sys.argv[1]

    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    results = run_simulation(lines)

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
