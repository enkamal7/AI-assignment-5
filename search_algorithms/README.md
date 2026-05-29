# AI-assignment-5

# Search Algorithms for Game Playing in AI

This project demonstrates the implementation and comparison of four popular game-search algorithms used in Artificial Intelligence:

- Minimax Search
- Alpha-Beta Pruning
- Heuristic Alpha-Beta Search
- Monte Carlo Tree Search (MCTS)

The algorithms are tested on a Tic-Tac-Toe game environment to determine the best possible move for a player.

---

## Project Structure

```text
search_algorithms/
│
├── games.py          # Tic-Tac-Toe game implementation
├── search.py         # Search algorithm implementations
├── test_search.py    # Test cases and execution file
├── demo_output.txt   # Sample output
└── README.md
```

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Running the Project

Execute the following command:

```bash
python test_search.py
```

or

```bash
python3 test_search.py
```

---

## Test Scenario

Board Configuration:

```text
X X _
O O _
_ _ _
```

The algorithms evaluate the game state and determine the most favorable move for player **X**.

---

## Objectives

- Understand adversarial search techniques.
- Compare different game-playing algorithms.
- Study the effect of pruning and heuristics on search performance.
- Explore simulation-based decision making using MCTS.

---

## Files Description

### games.py
Contains the Tic-Tac-Toe game logic, including:
- Board representation
- Move generation
- Winner detection
- Board display

### search.py
Contains implementations of:
- Minimax
- Alpha-Beta Pruning
- Heuristic Alpha-Beta
- Monte Carlo Tree Search (MCTS)

### test_search.py
Runs all algorithms on a predefined board state and displays the results.

### demo_output.txt
Stores a sample execution output for reference.

---

## Conclusion

This project demonstrates how different AI search strategies can be applied to game-playing problems. Each algorithm approaches decision making differently while attempting to select the optimal move from a given game state.

