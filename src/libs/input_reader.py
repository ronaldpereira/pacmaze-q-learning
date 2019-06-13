import numpy as np

class InputReader:
    def __init__(self, input_path):
        self.input_path = input_path
        self.read()

    def read(self):
        with open(self.input_path, 'r') as input_file:
            self.lines, self.columns = input_file.readline().strip().split()
            self.lines, self.columns = int(self.lines), int(self.columns)

            self.maze = np.empty([self.lines, self.columns], dtype=str)
            for i in range(self.lines):
                line = input_file.readline()
                for j in range(self.columns):
                    self.maze[i][j] = line[j]

        print(self.maze)