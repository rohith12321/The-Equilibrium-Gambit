from pathlib import Path
import random
import matplotlib.pyplot as plt
import numpy as np

NUM_ROUNDS = 1000
NUM_SIMULATIONS = 100

INITIAL_BANKROLL = 1000
BASE_BET = 10

PROJECT_DIR = Path(__file__).resolve().parent
FIGURES_DIR = PROJECT_DIR / "figures"


def generate_environment():
    """Generate a dynamic betting environment."""
    edge = np.random.uniform(-0.05, 0.07, NUM_ROUNDS)
    win_probability = 0.5 + edge
    outcomes = np.random.rand(NUM_ROUNDS) < win_probability

    return win_probability, outcomes


def random_gambler(outcomes):
    bankroll = INITIAL_BANKROLL
    history = [bankroll]

    for outcome in outcomes:
        bet = bankroll * random.randint(1, 10) // 100

        bankroll += bet if outcome else -bet
        history.append(bankroll)

    return history


def martingale_gambler(outcomes):
    bankroll = INITIAL_BANKROLL
    history = [bankroll]

    bet = BASE_BET

    for outcome in outcomes:

        current_bet = min(bankroll, bet)

        if outcome:
            bankroll += current_bet
            bet = BASE_BET
        else:
            bankroll -= current_bet
            bet = current_bet * 2

        history.append(bankroll)

    return history


def kelly_gambler(win_probability, outcomes):
    bankroll = INITIAL_BANKROLL
    history = [bankroll]

    for probability, outcome in zip(win_probability, outcomes):

        kelly_fraction = 2 * probability - 1

        if kelly_fraction <= 0:
            history.append(float(bankroll))
            continue

        bet = bankroll * kelly_fraction

        bankroll += bet if outcome else -bet
        history.append(float(bankroll))

    return history


def run_simulations():

    simulations = {
        "Random Gambler": [],
        "Martingale Gambler": [],
        "Kelly Gambler": [],
    }

    for _ in range(NUM_SIMULATIONS):

        win_probability, outcomes = generate_environment()

        simulations["Random Gambler"].append(
            random_gambler(outcomes)
        )

        simulations["Martingale Gambler"].append(
            martingale_gambler(outcomes)
        )

        simulations["Kelly Gambler"].append(
            kelly_gambler(win_probability, outcomes)
        )

    return simulations


def plot_results(simulations):

    FIGURES_DIR.mkdir(exist_ok=True)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for ax, (strategy, histories) in zip(axes, simulations.items()):

        for history in histories:
            ax.plot(history, alpha=0.6)

        ax.set_title(strategy)
        ax.set_xlabel("Round")
        ax.set_ylabel("Bankroll")
        ax.set_yscale("log")

    plt.tight_layout()

    plt.savefig(FIGURES_DIR / "comparison.png", dpi=300)
    plt.show()


def main():

    simulations = run_simulations()
    plot_results(simulations)


if __name__ == "__main__":
    main()