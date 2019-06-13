class QLearning:
    def __init__(self, alpha, epsilon, n, maze):
        self.gamma = 0.9
        self.alpha = alpha
        self.epsilon = epsilon
        self.n = n
        self.maze = maze
