# Bayesian Networks for Disease Diagnosis

## Objective

The objective of this project is to explore the concepts of Bayesian Networks and the tools used for modelling, knowledge representation, and inference in uncertain environments. Bayesian Networks are widely used in Artificial Intelligence for reasoning and decision-making when complete information is not available.

This project implements a Bayesian Network for disease diagnosis using symptoms such as Fever, Cough, Fatigue, and Loss of Smell to predict the probability of COVID infection.

---

## Introduction to Bayesian Networks

A Bayesian Network (BN) is a probabilistic graphical model that represents a set of variables and their conditional dependencies using a Directed Acyclic Graph (DAG).

A Bayesian Network consists of:

- Nodes representing random variables.
- Directed edges representing dependencies between variables.
- Conditional Probability Tables (CPTs) that quantify relationships.

Bayesian Networks are useful for handling uncertainty and performing probabilistic reasoning.

---

## Tools for Modelling Bayesian Networks

### 1. pgmpy

pgmpy is a Python library used for creating and working with probabilistic graphical models.

Features:

- Bayesian Network modelling
- Markov Networks
- Exact and approximate inference
- Learning network structures from data

Used in this project for implementing the Bayesian Network.

---

### 2. GeNIe Modeler

GeNIe is a graphical tool for designing and analyzing Bayesian Networks.

Features:

- Visual modelling
- Probability estimation
- Decision networks
- Influence diagrams

Applications:

- Medical diagnosis
- Risk analysis
- Expert systems

---

### 3. Netica

Netica is a commercial software tool used for building and analyzing Bayesian Networks.

Features:

- Graphical interface
- Inference engine
- Decision support systems

Applications:

- Healthcare
- Engineering
- Environmental modelling

---

## Problem Representation using Bayesian Networks

Bayesian Networks represent problems as nodes and directed relationships.

For this project:

```text
          COVID
      /     |     |      \
     /      |     |       \
 Fever   Cough Fatigue LossOfSmell
```

### Node Descriptions

| Node | Description |
|--------|------------|
| COVID | Disease Status |
| Fever | Presence of Fever |
| Cough | Presence of Cough |
| Fatigue | Presence of Fatigue |
| LossOfSmell | Presence of Loss of Smell |

The symptoms depend on whether the patient has COVID.

---

## Inference in Bayesian Networks

Inference is the process of calculating probabilities of unknown variables based on observed evidence.

### Evidence

Suppose a patient has:

- Fever = True
- Cough = True
- Fatigue = True
- LossOfSmell = True

Using Bayesian inference, the network computes:

```text
P(COVID | Fever, Cough, Fatigue, LossOfSmell)
```

This is known as Posterior Probability.

---

## Inference Techniques

### Exact Inference

Provides mathematically exact probabilities.

Methods:

- Variable Elimination
- Belief Propagation

Used in this project through Variable Elimination.

---

### Approximate Inference

Used when networks become large.

Methods:

- Monte Carlo Sampling
- Gibbs Sampling
- Likelihood Weighting

---

## Example Implemented

### Disease Diagnosis System

A Bayesian Network is created with one disease node and four symptom nodes.

Disease:

- COVID

Symptoms:

- Fever
- Cough
- Fatigue
- Loss of Smell

The network uses Conditional Probability Tables (CPTs) to represent the relationship between the disease and symptoms.

After entering symptom evidence, the system calculates the probability that the patient has COVID.

---

## Files Included

```text
bayesian_networks/
│
├── bayesian_network.py
├── demo_output.txt
└── README.md
```

---

## Requirements

Install the required package:

```bash
pip install pgmpy
```

---

## How to Run

```bash
pip install pgmpy
python bayesian_network.py
```

or

```bash
pip install pgmpy
python3 bayesian_network.py
```

---

## Applications of Bayesian Networks

- Medical Diagnosis
- Fraud Detection
- Risk Assessment
- Expert Systems
- Decision Support Systems
- Machine Learning

---

## Advantages

- Handles uncertainty effectively
- Supports probabilistic reasoning
- Easy to visualize relationships
- Works with incomplete information
- Provides interpretable results

---

## Limitations

- Requires accurate probability values
- Complex networks become computationally expensive
- Building CPTs may require expert knowledge

---

## Conclusion

Bayesian Networks are powerful tools for modelling uncertainty and performing probabilistic inference. They provide an intuitive graphical representation of relationships among variables and are widely used in healthcare, finance, engineering, and artificial intelligence. In this project, a Bayesian Network was implemented for disease diagnosis, demonstrating how observed symptoms can be used to infer the probability of a disease using Bayesian reasoning.