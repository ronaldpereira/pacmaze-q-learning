import argparse

import numpy as np


def parser():
    parser = argparse.ArgumentParser(
        description="Q-learning (Reinforcement Learning) for an instance of a static Pac-man game (Pac-maze)."
    )

    # Required arguments
    parser.add_argument("input_file", type=str, help="Input file path.")

    # Optional arguments
    parser.add_argument(
        "-l",
        "--learning_rate",
        type=np.float64,
        default=0.1,
        help="Learning Rate for Q-Learning. Must be greater than 0. (Default:0.1)",
    )
    parser.add_argument(
        "-e",
        "--epsilon_greedy",
        type=np.float64,
        default=0.8,
        help="Epsilon Greedy for random actions. It will decrease by 0.01 for each iteration made. Must be in interval [0, 1] (Default: 0.8)",
    )
    parser.add_argument(
        "-n",
        "--n_iterations",
        type=np.int64,
        default=500,
        help="Number of Q-Learning iterations. Must be greater than 0. (Default: 500)",
    )

    args = parser.parse_args()

    return args
