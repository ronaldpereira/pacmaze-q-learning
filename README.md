# Pac-maze Q-Learning

Q-learning (Reinforcement Learning) for an instance of a static Pac-man game (Pac-maze)

- The objective is to make the Pac-man collect all pellets
  - If there are more than one pellets in the maze, it respawns after ending a period (collecting the pellet or the ghost) in a random location
- All ghosts are static

## Usage

```sh
python3 pacmaze.py -h
```

```text
usage: pacmaze.py [-h] [-e EPSILON_GREEDY] [-l LEARNING_RATE]
                  [-n N_ITERATIONS] [-p PI_OUTPUT_FILE] [-q Q_OUTPUT_FILE]
                  input_file

Q-learning (Reinforcement Learning) for an instance of a static Pac-man game
(Pac-maze).

positional arguments:
  input_file            Input file path.

optional arguments:
  -h, --help            show this help message and exit
  -e EPSILON_GREEDY, --epsilon_greedy EPSILON_GREEDY
                        Epsilon Greedy for random actions. It will decrease by
                        0.01 for each iteration made. Must be in interval [0,
                        1]. (Default: 0.8)
  -l LEARNING_RATE, --learning_rate LEARNING_RATE
                        Learning Rate for Q-Learning. Must be greater than 0.
                        (Default:0.1)
  -n N_ITERATIONS, --n_iterations N_ITERATIONS
                        Number of Q-Learning iterations. Must be greater than
                        0. (Default: 500)
  -p PI_OUTPUT_FILE, --pi_output_file PI_OUTPUT_FILE
                        Output file path for optimal pi found in the
                        execution. (Default: ./pi.txt)
  -q Q_OUTPUT_FILE, --q_output_file Q_OUTPUT_FILE
                        Output file path for optimal Q values found in the
                        execution. (Default: ./q.txt)
```
