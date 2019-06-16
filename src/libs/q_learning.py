import numpy as np


class QLearning:
    def __init__(self, alpha, epsilon, n, maze, start=(1, 1)):
        self.gamma = 0.9
        self.alpha = alpha
        self.epsilon = epsilon
        self.n = n
        self.maze = maze
        self.actions = {"U": 0, "D": 1, "L": 2, "R": 3}
        self.q = np.zeros(
            (len(self.actions), self.maze.lines, self.maze.columns), dtype=np.float64
        )
        self.position = start
