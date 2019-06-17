from sys import argv

import libs.arg_parse_config as APC
import libs.maze as MZ
import libs.q_learning as QL

args = APC.parser()

maze = MZ.Maze(args.input_file)

qlearning = QL.QLearning(
    args.learning_rate, args.epsilon_greedy, args.n_iterations, maze
)

# Executes the Q-Learning
qlearning.execute()

# Prints the found optimal policy pi* and the final Q values
qlearning.print_files(args.pi_output_file, args.q_output_file)
