import numpy as np

np.random.seed(1212)


class QLearning:
    def __init__(self, alpha, epsilon, n, maze):
        self.gamma = 0.9
        self.alpha = alpha
        self.epsilon = epsilon
        self.n = n
        self.maze = maze
        self.actions = {0: "U", 1: "D", 2: "L", 3: "R"}
        self.q = np.zeros(
            (len(self.actions), self.maze.lines, self.maze.columns), dtype=np.float64
        )
        self.next_s = [0, 0]
        self.random_reposition()
        self.s = [self.next_s[0], self.next_s[1]]

    def move(self, action):
        if action == "U":
            if self.next_s[0] > 1:
                if self.maze.maze[self.next_s[0] - 1, self.next_s[1]] != "#":
                    self.next_s[0] -= 1

        if action == "D":
            if self.next_s[0] < self.maze.maze.shape[0] - 1:
                if self.maze.maze[self.next_s[0] + 1, self.next_s[1]] != "#":
                    self.next_s[0] += 1

        if action == "L":
            if self.next_s[1] > 1:
                if self.maze.maze[self.next_s[0], self.next_s[1] - 1] != "#":
                    self.next_s[1] -= 1

        if action == "R":
            if self.next_s[1] < self.maze.maze.shape[1] - 1:
                if self.maze.maze[self.next_s[0], self.next_s[1] + 1] != "#":
                    self.next_s[1] += 1

        print("action:", action, end=" -> ")
        print("moved from", self.s, end=" ")
        print("to", self.next_s)

    def random_reposition(self):
        self.next_s[0] = 0
        self.next_s[1] = 0
        while self.maze.maze[self.next_s[0], self.next_s[1]] != "-":
            self.next_s[0] = np.random.randint(1, self.maze.maze.shape[0] - 1)
            self.next_s[1] = np.random.randint(1, self.maze.maze.shape[1] - 1)

        print("random reposition to", self.next_s)

    def update_q(self):
        for iteration in range(self.n):
            # Diminishes the value of epsilon_greedy by 0.01 for each iteration
            if self.epsilon - iteration * 0.01 > 0:
                self.epsilon -= iteration * 0.01

            if np.random.uniform() < self.epsilon:
                action_index = np.random.randint(0, 4)
                action = self.actions[action_index]

            else:
                action_index = np.argmax(self.q[:, self.next_s[0], self.next_s[1]])
                action = self.actions[action_index]

            self.move(action)

            next_reward = self.maze.rewards[self.next_s[0], self.next_s[1]]

            self.q[action_index, self.s[0], self.s[1]] += self.alpha * (
                next_reward
                + self.gamma
                * (
                    np.max(self.q[:, self.next_s[0], self.next_s[1]])
                    - self.q[action_index, self.s[0], self.s[1]]
                )
            )

            # Pellet or Phantom final state
            if (
                self.maze.maze[self.next_s[0], self.next_s[1]] == "0"
                or self.maze.maze[self.next_s[0], self.next_s[1]] == "&"
            ):
                self.random_reposition()

            self.s[0], self.s[1] = self.next_s[0], self.next_s[1]

        self.print_files()

    def print_files(self):
        with open("pi.txt", "w") as pi_file:
            for i in range(self.maze.lines):
                for j in range(self.maze.columns):
                    if self.maze.maze[i, j] == "-":
                        best_action_index = np.argmax(self.q[:, i, j])
                        pi_file.write(self.actions[best_action_index])
                    else:
                        pi_file.write(self.maze.maze[i, j])
                pi_file.write("\n")

        with open("q.txt", "w") as q_file:
            for i in range(self.q.shape[0]):
                for j in range(self.q.shape[1]):
                    if self.maze.maze[i, j] == "-":
                        for action in [3, 2, 0, 1]:
                            output = (
                                str(i)
                                + ","
                                + str(j)
                                + ","
                                + self.actions[action]
                                + ","
                                + "%.3f" % self.q[action, i, j]
                            )

                            q_file.write(output)
                            q_file.write("\n")

