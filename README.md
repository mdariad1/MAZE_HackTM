# Jungle Maze 

Run through the forbidden forest to loot the gold it bears whilst avoiding the grim-reaping skeletons who are after you!

Jungle themed maze game built using Python.

### Demo

<p align="center">
  <img alt="Jungle Maze Demo" src='https://user-images.githubusercontent.com/39765499/52150389-bd3eb080-2667-11e9-984a-d9d774003c6c.gif'>

<img width="768" alt="Maze Game" src="https://user-images.githubusercontent.com/39765499/52150122-e6127600-2666-11e9-9386-f4ad49cdb895.png">
</p>

### How to Run

````
$ git clone https://github.com/barclayd/Jungle-Maze.git
$ cd Jungle-Maze
$ python maze.py
````
Jungle Maze will now open in a new window and you can start playing!

### How to Play

- <kbd>up</kbd>: move player up
- <kbd>down</kbd>: move player down
- <kbd>left</kbd>: move player left
- <kbd>right</kbd>: move player right

### Features

- [x] Smooth sprites with rotation supported based on direction
- [x] Scoring system based on looting gold
- [x] Basic AI for skeleton enemies who can track and follow the player depending on his proximity to the skeleton
- [x] Mazes for the game load dynamically and can be easily created and updated
- [x] Boundary collision
- [x] Maze design based on 25x25 grid

### Future Improvements

* Scoring to be displayed
* Transition between levels after all treasure has been collected or a specified period of 1 time has passed
* Allow users to draw their own levels
* Game over screen
* Options to configure easy/medium/hard from outset of game
* Music
