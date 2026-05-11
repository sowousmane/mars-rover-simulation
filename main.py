import argparse
import logging
import sys

from mars_rover.simulation import Simulation


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


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description="Simule les deplacements des rovers sur Mars."
    )
    parser.add_argument(
        "input_file",
        help="Chemin vers le fichier d'entree de la simulation."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Active les logs detailles de la simulation."
    )
    return parser.parse_args(args)


def main(args=None):
    parsed_args = parse_args(args)
    configure_logging(parsed_args.verbose)

    try:
        lines = read_input_file(parsed_args.input_file)
        simulation = Simulation.from_lines(lines)
        results = simulation.run()

        for result in results:
            print(result)

        return 0

    except FileNotFoundError:
        logging.error("Fichier introuvable.")
        print("Erreur : fichier introuvable.", file=sys.stderr)
        return 1
    except ValueError as exc:
        logging.error("Entree invalide: %s", exc)
        print(f"Erreur : {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
