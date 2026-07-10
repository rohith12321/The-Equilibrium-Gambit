# Probability and Simulation

> Exploring optimal decision-making in stochastic environments through Monte Carlo simulation and dynamic betting strategies.

---

## Overview

This assignment investigates how different betting strategies perform when the probability of winning changes over time.

Rather than assuming a fixed probability, each round is played in a dynamically changing environment where the underlying win probability is sampled from a distribution. Three fundamentally different strategies are evaluated over repeated Monte Carlo simulations:

- **Random Gambler** — places random bets without considering the environment.
- **Martingale Gambler** — doubles the stake after each loss in an attempt to recover previous losses.
- **Kelly Gambler** — dynamically adjusts the bet size using the Kelly Criterion to maximize long-term capital growth.

The objective is to compare intuitive betting heuristics against mathematically optimal decision-making under uncertainty.

---

## Concepts Explored

- Probability Theory
- Expected Value
- Kelly Criterion
- Monte Carlo Simulation
- Dynamic Probability Models
- Wealth Evolution
- Risk vs Reward

---

## Methodology

For each simulation:

- A dynamic environment generates changing win probabilities for **1000 rounds**.
- Every strategy experiences the **same sequence of outcomes**, ensuring a fair comparison.
- The experiment is repeated for **100 independent players** to study long-term behaviour rather than individual runs.

Bankroll trajectories are visualized on a logarithmic scale to compare growth rates and volatility.

---

## Strategies

### Random Gambler

Chooses a random bet size between **1% and 10%** of the current bankroll each round, completely ignoring changes in the environment.

---

### Martingale Gambler

Begins with a fixed stake and doubles the bet after every loss until a win occurs or the bankroll is exhausted.

This illustrates why seemingly successful short-term strategies can fail catastrophically under finite capital.

---

### Kelly Gambler

Uses the Kelly Criterion to compute the optimal fraction of capital to wager based on the current probability of winning.

When the expected value becomes negative, the strategy simply sits out the round, preserving capital instead of forcing a bet.

---

## Results

The simulations demonstrate the importance of probability-aware decision making.

While heuristic strategies may perform well over short horizons, adaptive strategies based on expected value and the Kelly Criterion consistently exhibit superior long-term capital growth and improved risk management across repeated simulations.

---

## Repository Contents

```
01_probability_and_simulation/
├── README.md
├── simulation.py
└── report.pdf
```

---

## Learning Outcomes

This assignment provides practical experience with

- designing stochastic simulations,
- implementing Monte Carlo experiments,
- modelling dynamic environments,
- applying the Kelly Criterion for optimal betting,
- comparing competing strategies through empirical evaluation,
- and visualizing long-term statistical behaviour.

These ideas form the probabilistic foundation for the later modules on Bayesian inference, game theory, and adversarial market simulations.