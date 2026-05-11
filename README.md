# 🚀 SIMPLE Mars Rover Simulation (Python)

A simple command-line simulation of Mars rovers moving on a grid-based plateau.

---

## 📌 Problem Description

NASA sends robotic rovers to explore a rectangular plateau on Mars.

Each rover:
- has a position `(x, y)`
- has a direction (`N`, `E`, `S`, `W`)
- receives a sequence of commands:
  - `L` → turn left
  - `R` → turn right
  - `M` → move forward

The plateau is defined by its upper-right coordinates, assuming `(0, 0)` as the lower-left corner.

Rovers are executed sequentially.

---

## 📥 Input Format

The program reads an input file.

Example:

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

- Line 1 → plateau size (`max_x max_y`)
- Then each rover is defined by 2 lines:
  - position: `x y direction`
  - commands string

---

## 📤 Output Format

Final position of each rover:

```
1 3 N
5 1 E
```
---

## ▶️ How to run

```bash id="run"
python main.py input.txt
````

---

## 🧠 Project Structure

```id="structure"
mars-rover-simulation/
│
├── main.py
├── simulation.py
├── rover.py
├── input.txt
├── test_rover.py
├── requirements.txt
└── .github/workflows/ci.yml
```

---

## 🧩 Core Logic (rover.py)

The rover logic includes:

### 🔄 Rotation

* `turn_left(direction)`
* `turn_right(direction)`

Directions follow this rule:

```
N → W → S → E → N (left)
N → E → S → W → N (right)
```

---

### 🚶 Movement

* `move(x, y, direction, max_x, max_y)`

The rover moves one step forward depending on its direction:

* N → y + 1
* S → y - 1
* E → x + 1
* W → x - 1

Movement is only applied if the rover stays inside the plateau.

---

### 🧭 Plateau constraint

* `is_inside(x, y, max_x, max_y)`

Ensures the rover does not leave the grid.

---

### ▶️ Command execution

* `execute_commands(...)`

Processes a string of commands:

* `L` → turn left
* `R` → turn right
* `M` → move forward

Commands are executed sequentially.

---

## 🧪 Tests

Run tests with:

```
pytest
```

---

## ⚙️ CI Pipeline

This project uses **GitHub Actions CI**.

On every push or pull request:

* Python is installed
* dependencies are installed
* tests are executed automatically

CI file:

```
.github/workflows/ci.yml
```

---

## 🧠 Features

* Grid-based rover simulation
* Multiple rover support
* Sequential execution
* Boundary checking (no out-of-bounds movement)
* Clean functional architecture

---

## 🚀 Future Improvements

* Replace rotation logic with cyclic implementation
* Add CLI arguments (`argparse`)
* Add visualization of rover path
* Convert to OOP design (`Rover` class)
* Add coverage reports in CI

---

## 👨‍💻 Author

Learning project focused on Python fundamentals, clean architecture, and DevOps practices.
