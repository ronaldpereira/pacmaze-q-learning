import numpy as np

class Maze:
    def __init__(self, input_path):
        self.read(input_path)

    def read(self, input_path):
        with open(input_path, 'r') as input_file:
            self.lines, self.columns = input_file.readline().strip().split()
            self.lines, self.columns = int(self.lines), int(self.columns)

            self.maze = np.empty((self.lines, self.columns), dtype=str)
            for i in range(self.lines):
                line = input_file.readline()
                for j in range(self.columns):
                    self.maze[i,j] = line[j]

        print(self.maze)
        self.build_rewards()

    def build_rewards(self):
        self.rewards = np.zeros((self.lines, self.columns), dtype=np.int8)
        
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                value = self.maze[i, j]
                if value == "-":
                    self.rewards[i, j] = -1
                elif value == "0":
                    self.rewards[i, j] = 10
                elif value == "&":
                    self.rewards[i, j] = -10
                else:
                    self.rewards[i, j] = 0

        print(self.rewards)
