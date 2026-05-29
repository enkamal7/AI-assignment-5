# Artificial Intelligence Assignment

This repository contains the implementation and analysis of various Artificial Intelligence concepts including Search Algorithms, Knowledge-Based Systems, Knowledge Graphs, and Bayesian Networks.

---

## Project Overview

The objective of this assignment is to explore different AI techniques used for decision making, problem solving, knowledge representation, and reasoning under uncertainty.

The repository is divided into four sections corresponding to the assignment questions.

---

## Question 1: Search Algorithms

Implementation of classical game-playing search algorithms using a Tic-Tac-Toe environment.

### Algorithms Implemented

- Minimax Search
- Alpha-Beta Pruning
- Heuristic Alpha-Beta Search
- Monte Carlo Tree Search (MCTS)

### Files

```text
search_algorithms/
├── games.py
├── search.py
├── test_search.py
├── demo_output.txt
└── README.md
```

---

## Question 2: AI Travel Planner

Design and implementation of an AI-based Travel Planner that reuses a knowledge base to generate travel recommendations.

### Features

- Tourist Place Recommendation
- Food Recommendation
- Budget Estimation
- Personalized Travel Planning
- Day-wise Itinerary Generation

### Files

```text
travel_planner/
├── travel_planner.py
├── knowledge_base.json
├── demo_output.txt
└── README.md
```

---

## Question 3: Knowledge Graphs

Study of Knowledge Graphs and the tools used for building graph-based knowledge representations.

### Topics Covered

- Knowledge Graph Fundamentals
- Entities and Relationships
- Applications of Knowledge Graphs
- Neo4j
- RDF
- SPARQL
- Protégé
- GraphDB

### Files

```text
knowledge_graphs/
├── knowledge_graphs.md
└── README.md
```

---

## Question 4: Bayesian Networks

Implementation of a Bayesian Network for disease diagnosis and probabilistic inference.

### Concepts Covered

- Bayesian Networks
- Conditional Probability
- Probabilistic Reasoning
- Variable Elimination
- Disease Diagnosis

### Example Implemented

COVID Diagnosis using symptoms:

- Fever
- Cough
- Fatigue
- Loss Of Smell

### Files

```text
bayesian_networks/
├── bayesian_network.py
├── demo_output.txt
└── README.md
```

---

## Technologies Used

- Python 3
- pgmpy
- JSON

---

## Repository Structure

```text
AI-assignment-5/
│
├── README.md
│
├── search_algorithms/
│   ├── games.py
│   ├── search.py
│   ├── test_search.py
│   ├── demo_output.txt
│   └── README.md
│
├── travel_planner/
│   ├── travel_planner.py
│   ├── knowledge_base.json
│   ├── demo_output.txt
│   └── README.md
│
├── knowledge_graphs/
│   ├── knowledge_graphs.md
│   └── README.md
│
└── bayesian_networks/
    ├── bayesian_network.py
    ├── demo_output.txt
    └── README.md
```

---

## Conclusion

This project demonstrates the application of Artificial Intelligence techniques in game playing, recommendation systems, knowledge representation, and probabilistic reasoning. The implementations showcase how AI can be used to solve complex problems through search, knowledge reuse, graph-based representation, and inference under uncertainty.