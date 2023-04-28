# Game Document
## Introduction
The name of the game is Alternative Flappy Bird.

![Descriptive Screenshot](/descriptive_screenshot.png)

To to download, run, and play the game, navigate to a folder and clone the game repository using ```git clone https://github.com/xiaolong-tian-19/final_game_project.git```. Navigate inside the game repository, open a terminal, and type ```python flappy_bird.py``` to run and play the game.

Software version:
- Python: 3.8.10
- Pygame: 2.1.2

Game Control:
- Space bar : start the game & flap wings of the bird
## Game Design
**Mechanics/Technology**
- The game play loop of my game has two layers. In the first layer, the game loop initiates a start screen that displays the current and best scores the player has achieved. If the player hits the space bar, the game loop in the second layer starts. This game loop initially creates the bird that the player can control, obstacles for the bird to dodge, powerups the player can collect, etc. In each iteration, this game loop checks to see if there are collisions, creates more obstacles, and so on. It updates the game instances, draw them on the screen, and goes back to the begining of the loop. Once the flappy bird uses up all of its lives, the game loop terminates and return the current score to the game loop in the first layer, which will displays the current and best score. The game loop in the first layer will then wait for the player either to close the game or to hit enter to play again.
- The core mechanics of the game is the flappy bird accelerating downwards until the player flap the bird for it to go up, obstacles that are placed at random heights for the flappy bird to dodge, lives that allow flappy bird to hit obstacles but still stay alive, and portals that will transport the flappy bird forward. The game loop checks to see if the player hits the space bar and updates the flappy bird's velocity and acceleration accordingly, In addition, the game loop checks to see if any obstacle or powerup is leaving the screen. If there is any, the game loop removes them and creates new obstacles at random height with different types (pipes, tree truncks, big ben, etc.) and new powerups at random positions. This allow a possibly infinite gameplay. Furthermore, the game loop checks to see if the flappy bird collides with any powerups, such as lives or portals. If the flappy bird collides with lives, it will add to the number of lives of the bird. The number of lives is substracted if the flappy bird hits an obstacle, and the flappy bird is recevied an period of immune time. If the flappy bird collides with a portal, the game loop moves everything else backward to create the illusion that the flappy bird is transported to the next portal.
- The game's gimmick is the additional lives flappy bird can gain, portals that will transport the flappy bird to another portal, and a variety of alternative obstacles such as tree truncks, big ben, spikes that the flappy bird must dodge. They contribute to the game by making the game a very different experience than the traditional flappy bird game. The alternative obstacles make the game play more visually appealing and add dynamic changes to the game instead of monotonic green pipes. The lives that the flappy bird can gain make the game slightly easier than the classic flappy bird game. The player could collect these additional lives and avoid fustration of making accidental mistakes. The portals made the game exciting and somewhat intense to play. On the one hand, it creates a way for the player to supercharge if they are skillful. On the other hand, the portals create a atmosphere of uncertainty because the player may not be paying attention as to where they would land when they would enter the portals. The sudden change makes the game very enjoyable.
- The game differs from other game in the genre mainly on its gimmick: the additional lives flappy bird can gain, portals that will transport the flappy bird to another portal, and a variety of alternative obstacles such as tree truncks, big ben, spikes that the flappy bird must dodge. They make playing the game a different experience.
- The game engine is more based on pygame itself. However, pygame does a good job as a simple game engine. It allows easy creation of sprites from custom images. Furthermore, the game implementation heavily takes advantage of the pygame sprite group, particularly grouping of the obstacles and powerups. It allows the game loop to easily keep track of the instances and updates them collectively.

**Story**
- The story of the game is quite simple. The flappy bird is a law-abiding citizen of the city, and is atempting to dodge different and scary obstacles in the new dytopian society, which at the time experiencing magical effects such as gaining additiona lives and being able to fly through portals. The goal of the flappy bird is to dodge as many obstacles and stay alive for as long as it can.

**Player Experience**


