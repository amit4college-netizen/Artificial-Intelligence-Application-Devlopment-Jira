# 🤖 Artificial Intelligence Application Development

A collection of **Artificial Intelligence practical programs implemented in Python** as part of the **T.Y. B.Sc. Information Technology** curriculum of the **University of Mumbai**.

The repository contains implementations of AI agents, search algorithms, heuristic search, probabilistic reasoning, Bayesian networks, and machine learning using Python.

---

## 🎓 Academic Information

* **University:** University of Mumbai
* **Programme:** B.Sc. Information Technology
* **Class:** T.Y. B.Sc. I.T.
* **Subject:** Artificial Intelligence
* **Academic Year:** 2026–27
* **Student:** Omkar Santosh Talekar
* **Roll Number:** 28

---

## 📚 Practicals Included

| No. | Practical           | Concept / Algorithm                    |
| --- | ------------------- | -------------------------------------- |
| 1   | Rational Agent      | PEAS & Table-Driven Agent              |
| 2   | 8-Puzzle            | Breadth-First Search (BFS)             |
| 3   | Water Jug Problem   | Depth-First Search (DFS)               |
| 4   | Least-Cost Path     | Uniform Cost Search (UCS)              |
| 5   | 8-Puzzle            | Greedy Best-First Search               |
| 6   | 8-Puzzle            | A* Search with Manhattan Distance      |
| 7   | Route Finding       | A* Search with Straight-Line Heuristic |
| 8   | Probability Problem | Probabilistic Reasoning                |
| 9   | Classification      | Naive Bayes using Scikit-learn         |
| 10  | Burglary-Alarm      | Bayesian Network using pgmpy           |

---

## 🧠 Practical 1 — Rational Agent

A simple **table-driven vacuum cleaner agent** is implemented in Python.

The program:

* Takes the status of Room A and Room B.
* Checks whether each room is clean or dirty.
* Performs the `Suck` action when a room is dirty.
* Completes the task when both rooms are clean.

The practical also covers the **PEAS framework** and classification of environments such as fully/partially observable, deterministic/stochastic, and episodic/sequential.

---

## 🧩 Practical 2 — 8-Puzzle using BFS

The **Breadth-First Search (BFS)** algorithm is used to find the shortest sequence of moves for an 8-puzzle.

### Initial State

```text
1 2 3
4 0 6
7 5 8
```

### Goal State

```text
1 2 3
4 5 6
7 8 0
```

The solution requires **2 moves**:

```text
Down
Right
```

## The practical demonstrates state-space search and shortest-path exploration using BFS.

## 💧 Practical 3 — Water Jug Problem using DFS

The classic **Water Jug Problem** is solved using **Depth-First Search (DFS)**.

The program allows the user to enter:

* Jug 1 capacity
* Jug 2 capacity
* Target amount

Example:

```text
Jug 1 = 4 litres
Jug 2 = 3 litres
Target = 2 litres
```

The program explores possible states until it reaches the target amount.

Example solution:

```text
(0,0)
(4,0)
(4,3)
(0,3)
(3,0)
(3,3)
(4,2)
```

---

## 🗺️ Practical 4 — Uniform Cost Search

**Uniform Cost Search (UCS)** is used to find the least-cost path between cities in a weighted graph.

The example graph contains cities such as:

```text
Mumbai
Pune
Hyderabad
Bangalore
```

The resulting path is:

```text
Mumbai → Pune → Bangalore
```

with a total distance of:

```text
990 km
```

## The implementation uses Python's `heapq` priority queue.

## 🔍 Practical 5 — Greedy Best-First Search

The 8-puzzle is solved using **Greedy Best-First Search**.

The algorithm uses the **Manhattan Distance heuristic** to determine which state should be explored next.

### Heuristic

The Manhattan distance is calculated as:

```text
|x1 - x2| + |y1 - y2|
```

for each numbered tile.

The example reaches the goal in:

```text
2 moves
```

## The practical demonstrates heuristic-based search and how an informed search strategy can guide the exploration toward the goal.

## ⭐ Practical 6 — A* Search with Manhattan Distance

The 8-puzzle is solved using **A* Search**.

A* evaluates states using:

```text
f(n) = g(n) + h(n)
```

Where:

* `g(n)` = cost from the initial state
* `h(n)` = estimated cost to the goal
* `f(n)` = total estimated cost

The Manhattan Distance is used as the heuristic.

The example reaches the goal in:

```text
2 moves
```

---

## 🚕 Practical 7 — A* Search for Route Finding

A weighted graph representing Romanian cities is used to demonstrate **A* Search**.

The heuristic represents the **straight-line distance to Bucharest**.

The resulting route is:

```text
Arad
  ↓
Sibiu
  ↓
Rimnicu Vilcea
  ↓
Pitesti
  ↓
Bucharest
```

Total cost:

```text
418
```

---

## 🧮 Practical 8 — Probabilistic Reasoning

This practical is intended to demonstrate probability calculation for determining the probability that a person actually has a disease given a **positive test result**.

## 🧮 Practical 8 — Bayes' Theorem

The program calculates the probability that a person actually has a disease when the test result is positive using **Bayes' Theorem**.

### Code

```python
# Base probabilities
PD = 0.01                  # Prior probability of having the disease
P_NotD = 1 - PD            # Probability of not having the disease (0.99)

# Conditional test probabilities
P_Pos_D = 0.99             # True Positive rate (Sensitivity)
P_Pos_NotD = 0.05          # False Positive rate (1 - Specificity)

# Bayes' Theorem Calculation
P_D_Pos = (P_Pos_D * PD) / ((P_Pos_D * PD) + (P_Pos_NotD * P_NotD))

print("Probability that person actually has disease:")
print(round(P_D_Pos * 100, 2), "%")
```

### Output

```text
Probability that person actually has disease:
16.67 %
```

### Concept Used

**Bayes' Theorem** is used to calculate the probability of having the disease given that the test result is positive.

The program uses:

* `PD = 0.01` — Prior probability of disease
* `P_NotD = 0.99` — Probability of not having the disease
* `P_Pos_D = 0.99` — True positive rate
* `P_Pos_NotD = 0.05` — False positive rate

**Final Probability: 16.67%**


## 🤖 Practical 9 — Naive Bayes Classifier

A **Naive Bayes classifier** is implemented using **Scikit-learn**.

The example uses weather-related attributes:

```text
Outlook
Temperature
Humidity
Windy
```

The target variable is:

```text
Play
```

The implementation uses:

```python
GaussianNB()
```

along with:

```python
LabelEncoder
```

to convert categorical values into numerical values.

Example output:

```text
Prediction: No, we cannot play
```

---

## 🔮 Practical 10 — Bayesian Network

A **Burglary-Alarm Bayesian Network** is created using the `pgmpy` library.

The network contains the following relationships:

```text
Burglary ──────┐
               ↓
            Alarm ───→ JohnCalls
               │
               └────→ MaryCalls

Earthquake ────┘
```

The implementation uses:

* `DiscreteBayesianNetwork`
* `TabularCPD`
* `VariableElimination`

## The network defines conditional probability distributions and performs inference using evidence that both **JohnCalls** and **MaryCalls** are true.

## 🛠️ Technologies Used

* **Python 3**
* **Pandas**
* **Scikit-learn**
* **pgmpy**
* Python `collections`
* Python `heapq`

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/amit4college-netizen/Artificial-Intelligence-Application-Devlopment-Jira.git
```

Open the project folder:

```bash
cd Artificial-Intelligence-Application-Devlopment-Jira
```

Install the required libraries:

```bash
pip install pandas scikit-learn pgmpy
```

---

## ▶️ Running the Practicals

Run the required Python file using:

```bash
python filename.py
```

For example:

```bash
python practical1.py
```

> File names may differ depending on the structure of the repository.

---

## 📖 Concepts Covered

This repository provides practical implementations of several important Artificial Intelligence concepts:

* Rational Agents
* PEAS
* State Space Search
* Breadth-First Search
* Depth-First Search
* Uniform Cost Search
* Greedy Best-First Search
* A* Search
* Manhattan Distance
* Straight-Line Distance Heuristic
* Probabilistic Reasoning
* Naive Bayes Classification
* Bayesian Networks
* Bayesian Inference

---

## 🎯 Learning Objectives

Through these practicals, the project demonstrates how AI algorithms can be implemented using Python to solve:

* Search problems
* Puzzle problems
* Pathfinding problems
* Optimization problems
* Classification problems
* Probability problems
* Decision-making problems

---

## 📁 Project Structure

A suggested structure for the repository is:

```text
Artificial-Intelligence-Application-Devlopment-Jira/
│
├── Practical 1/
├── Practical 2/
├── Practical 3/
├── Practical 4/
├── Practical 5/
├── Practical 6/
├── Practical 7/
├── Practical 8/
├── Practical 9/
├── Practical 10/
│
└── README.md
```

---

## 👨‍💻 Author

**Omkar Santosh Talekar**

T.Y. B.Sc. Information Technology
University of Mumbai
Academic Year 2026–27

---

## 📜 Academic Note

This repository contains practical implementations prepared as part of the **Artificial Intelligence** practical coursework for the University of Mumbai.

The practical document states that the work covers the prescribed Artificial Intelligence practicals for T.Y. B.Sc. Information Technology.

---

## ⭐ Repository

**GitHub:**
https://github.com/amit4college-netizen/Artificial-Intelligence-Application-Devlopment-Jira
