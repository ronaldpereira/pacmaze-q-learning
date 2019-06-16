from sys import argv

import libs.maze as MZ
import libs.q_learning as QL

maze = MZ.Maze(argv[1])

qlearning = QL.QLearning(argv[2], argv[3], argv[4], maze, (3, 1))

print(maze.maze)
print(maze.rewards)
print(qlearning.q)
