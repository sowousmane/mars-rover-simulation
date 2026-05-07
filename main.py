import logging
import sys

from simulation import run_simulation


def configure_logging(verbose=False):
    level = logging.INFO if verbose else logging.WARNING

    logging.basicConfig(
        level=level,
        format="%(levelname)s - %(message)s",
        stream=sys.stderr,
        force=True
    )


def read_input_file(filename):
    logging.info("Lecture du fichier %s", filename)

    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        raise ValueError("Le fichier d'entree est vide.")

    logging.info("%s lignes utiles lues", len(lines))
    return lines


def parse_cli_args(args):
    verbose = False
    filtered_args = []

    for arg in args:
        if arg == "--verbose":
            verbose = True
        else:
            filtered_args.append(arg)

    if len(filtered_args) != 1:
        raise ValueError("Usage: python main.py [--verbose] <fichier_input>")

    return filtered_args[0], verbose


def main():
    configure_logging()

    try:
        filename, verbose = parse_cli_args(sys.argv[1:])
        configure_logging(verbose)
        lines = read_input_file(filename)
        results = run_simulation(lines)

        for result in results:
            print(result)

    except FileNotFoundError:
        logging.error("Fichier introuvable.")
        print("Erreur : fichier introuvable.", file=sys.stderr)
        sys.exit(1)
    except ValueError as exc:
        logging.error("Entree invalide: %s", exc)
        print(f"Erreur : {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
