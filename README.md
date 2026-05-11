# Mars Rover Modules

Petit projet Python autour du kata Mars Rover de la NASA, maintenant structure en modules et en programmation orientee objet.

Le programme lit un fichier d'entree, simule les deplacements de rovers sur une grille et retourne leur position finale.

## Objectif
- pratiquer une logique Python simple puis evoluer vers une architecture POO
- organiser le code en modules clairs
- valider les entrees proprement
- ajouter des logs utiles pour le debug sans polluer la sortie normale

## Regles Du Kata
- le plateau est defini par ses coordonnees max `max_x max_y`
- un rover possede :
  - une position `x y`
  - une direction parmi `N`, `E`, `S`, `W`
- les commandes possibles sont :
  - `L` : tourner a gauche
  - `R` : tourner a droite
  - `M` : avancer d'une case
- un rover ne peut pas sortir du plateau
- les rovers sont executes sequentiellement

## Format D'entree
Exemple de fichier `input.txt` :

```text
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

- ligne 1 : taille du plateau `max_x max_y`
- puis, pour chaque rover :
  - une ligne position : `x y direction`
  - une ligne commandes : suite de caracteres `L`, `R`, `M`

## Sortie Attendue
Pour l'exemple ci-dessus :

```text
1 3 N
5 1 E
```

## Lancer Le Projet
Execution normale :

```bash
python3 main.py input.txt
```

Mode verbeux avec logs detailles :

```bash
python3 main.py --verbose input.txt
```

Aide de la CLI :

```bash
python3 main.py --help
```

## Comportement Des Sorties
- `stdout` affiche uniquement le resultat final des rovers
- `stderr` affiche les erreurs et, en mode `--verbose`, les logs techniques

Exemple en mode normal :

```text
1 3 N
5 1 E
```

Exemple en mode `--verbose` :

```text
INFO - Lecture du fichier input.txt
INFO - Plateau detecte: 5 5
INFO - Rover initial: 1 2 N
INFO - Commandes: LMLMLMLMM
INFO - Commande en cours: L
...
1 3 N
5 1 E
```

## Gestion Des Erreurs
Le projet gere plusieurs cas d'erreur courants :
- fichier introuvable
- fichier vide
- plateau invalide
- position rover invalide
- direction invalide
- commande invalide
- rover place hors du plateau
- nombre de lignes incoherent dans le fichier d'entree

Exemple :

```bash
python3 main.py fichier_inexistant.txt
```

```text
Erreur : fichier introuvable.
```

## Structure Du Projet

```text
Mars-rovers-functions/
├── main.py
├── mars_rover/
│   ├── __init__.py
│   ├── plateau.py
│   ├── rover.py
│   └── simulation.py
├── tests/
│   ├── test_plateau.py
│   ├── test_rover.py
│   └── test_simulation.py
├── input.txt
├── requirements.txt
└── README.md
```

## Organisation Du Code
`main.py`
- point d'entree du programme
- gestion des arguments CLI avec `argparse`
- configuration du logging
- lecture du fichier
- gestion des erreurs globales

`mars_rover/plateau.py`
- classe `Plateau`
- validation des dimensions
- verification des limites de la grille

`mars_rover/rover.py`
- classe `Rover`
- rotation gauche et droite
- deplacement sur le plateau
- execution des commandes
- logs etape par etape en mode verbeux

`mars_rover/simulation.py`
- classe `Simulation`
- parsing du plateau
- parsing des rovers
- validation des commandes
- orchestration de la simulation

`tests/`
- tests separes par module metier
- meilleure lisibilite de la couverture fonctionnelle

## Fonctions Principales
Classes principales :
- `Plateau(max_x, max_y)`
- `Rover(x, y, direction, plateau)`
- `Simulation(plateau)`

Methodes importantes :
- `Rover.turn_left()`
- `Rover.turn_right()`
- `Rover.move()`
- `Rover.execute(commands)`
- `Simulation.from_lines(lines)`
- `Simulation.run()`

## Installer Les Dependances

```bash
python3 -m pip install -r requirements.txt
```

## Lancer Les Tests

```bash
python3 -m pytest -q
```

Les tests couvrent notamment :
- les rotations
- le deplacement
- le blocage a la bordure
- la validation du plateau
- l'execution de commandes
- les erreurs de format d'entree
- la nouvelle architecture POO

## CI
Le projet contient une pipeline GitHub Actions dans `.github/workflows/ci.yml` pour executer les tests automatiquement.

## Pistes D'amelioration
- ajouter des tests sur les logs
- ajouter un niveau `DEBUG`
- ajouter une vraie gestion d'exceptions metier dediees
