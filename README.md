# Pac-maze Q-Learning

Q-learning (Reinforcement Learning) for an instance of a static Pac-man game (Pac-maze)

- The objective is to make the Pac-man collect all pellets
  - If there are more than one pellets in the maze, it respawns after ending a period (collecting the pellet or the ghost) in a random location
- All ghosts are static

## Usage

```text
usage: pacmaze.py [-h] [-l LEARNING_RATE] [-e EPSILON_GREEDY]
                  [-n N_ITERATIONS]
                  input_file

Q-learning (Reinforcement Learning) for an instance of a static Pac-man game
(Pac-maze).

positional arguments:
  input_file            Input file path.

optional arguments:
  -h, --help            show this help message and exit
  -l LEARNING_RATE, --learning_rate LEARNING_RATE
                        Learning Rate for Q-Learning. (Default:0.1)
  -e EPSILON_GREEDY, --epsilon_greedy EPSILON_GREEDY
                        Epsilon Greedy for random actions. It will decrease by
                        0.01 for each iteration made. (Default: 0.8)
  -n N_ITERATIONS, --n_iterations N_ITERATIONS
                        Number of Q-Learning iterations. (Default: 500)
```
