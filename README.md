# Mars Rover Functions

Petit projet Python procedurale autour du kata Mars Rover de la NASA.

Le programme lit un fichier d'entree, simule les deplacements de rovers sur une grille et retourne leur position finale.

## Objectif
- pratiquer une logique simple basee sur des fonctions
- garder une architecture lisible sans classes
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
├── simulation.py
├── rover.py
├── input.txt
├── test_rover.py
├── requirements.txt
└── README.md
```

## Organisation Du Code
`main.py`
- point d'entree du programme
- gestion des arguments CLI
- configuration du logging
- lecture du fichier
- gestion des erreurs globales

`simulation.py`
- validation du format d'entree
- parsing du plateau
- parsing des positions des rovers
- validation des commandes
- orchestration de la simulation

`rover.py`
- rotation gauche et droite
- deplacement sur le plateau
- verification des limites
- execution des commandes
- logs etape par etape en mode verbeux

## Fonctions Principales
Dans `rover.py` :
- `turn_left(direction)`
- `turn_right(direction)`
- `is_inside(x, y, max_x, max_y)`
- `move(x, y, direction, max_x, max_y)`
- `execute_commands(x, y, direction, commands, max_x, max_y)`

Dans `simulation.py` :
- `parse_plateau(line)`
- `parse_rover_position(line)`
- `validate_commands(commands)`
- `run_simulation(lines)`

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
- l'execution de commandes
- les erreurs de format d'entree

## CI
Le projet contient une pipeline GitHub Actions dans `.github/workflows/ci.yml` pour executer les tests automatiquement.

## Pistes D'amelioration
- remplacer les `if/elif` de rotation par une logique cyclique plus Pythonique
- ajouter `argparse` pour une CLI plus propre
- ajouter des tests sur les logs
- ajouter un niveau `DEBUG`
- faire ensuite une version orientee objet pour comparer avec l'approche fonctionnelle
