# Bayesian Games

> Exploring strategic decision-making under uncertainty through Bayesian inference, signaling, and randomized strategies.

---

## Overview

This project models a competitive information game between two rival intelligence agencies, **MI6** and **Cheka**, where uncertainty arises not only from randomness but also from strategic deception.

The objective is to study how rational agents make decisions when information is incomplete, signals may be intentionally misleading, and both players continuously adapt their strategies based on available evidence.

The simulation demonstrates how Bayesian reasoning and randomized decision-making outperform deterministic behavior in adversarial environments.

---

## Concepts Explored

- Bayesian Inference
- Posterior Belief Updates
- Conditional Probability
- Signaling Games
- Strategic Bluffing
- Mixed Strategies
- Sequential Decision Making

---

## Simulation

Each mission follows a sequence of events:

1. A classified file is randomly hidden among three possible safehouses.
2. MI6 receives an imperfect intelligence report.
3. MI6 independently decides
   - which message to send to Cheka, and
   - which location to actually search.
4. Cheka updates its beliefs using Bayes' Theorem based on the received message.
5. Both agencies execute their search and receive rewards based on the outcome.

The experiment is repeated over thousands of independent missions to analyze long-term strategic behavior.

---

## Experiments

The simulation evaluates how different strategic choices influence performance by varying

- Truth-telling probability
- Bluffing frequency
- Intelligence reliability
- Search strategy

Performance is measured using

- Total score
- Bluff success rate
- Posterior belief accuracy
- Strategy effectiveness

---

## Results

The experiments illustrate that neither always telling the truth nor always bluffing is optimal.

Instead, randomized strategies combined with Bayesian belief updates enable agents to remain unpredictable while making more informed decisions under uncertainty.

---

## Repository Contents

```text
02_bayesian_games/
├── README.md
├── simulation.py
├── report.pdf
└── figures/
```

---

## Learning Outcomes

This project provides practical experience with

- implementing Bayesian belief updates,
- modelling strategic interactions under incomplete information,
- designing randomized agent policies,
- evaluating competing strategies through simulation,
- and understanding the role of information asymmetry in decision-making.

These concepts form the game-theoretic foundation for the final capstone, **Operation Dark Pool**, where Bayesian inference and mixed strategies are applied to adversarial financial markets.