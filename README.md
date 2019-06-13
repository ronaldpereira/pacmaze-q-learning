# Pac-maze Q-Learning

Q-learning (Reinforcement Learning) for an instance of a static Pac-man game (Pac-maze)

- The objective is to make the Pac-man collect all pellets
  - If there are more than one pellets in the maze, it respawns after ending a period (collecting the pellet or the ghost) in a random location
- All ghosts are static

## Execution Example

Execute the following execution command example on src/

```text
chmod +x qlearning.sh
./qlearning.sh pacmaze.txt 0.3 0.9 300
```
