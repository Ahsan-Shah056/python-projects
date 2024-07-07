# Pong Game Guide

Welcome to the Pong Game! This guide will help you understand how to play and enjoy the classic Pong game built using Object-Oriented Programming (OOP) concepts.

## How to Play

1. **Start the Game:**
   - The game will initialize an 800x600 pixel screen with a black background.
   - The game title "--Pong Game--" will be displayed.
   - The game elements, including paddles, ball, and scoreboard, will be set up.

2. **Control the Paddles:**
   - Use the following keys to control the paddles:
     - **Right Paddle:**
       - **Up Arrow:** Move the paddle up.
       - **Down Arrow:** Move the paddle down.
     - **Left Paddle:**
       - **'W' Key:** Move the paddle up.
       - **'S' Key:** Move the paddle down.

3. **Objective:**
   - The goal is to hit the ball with the paddles to prevent it from passing your paddle and to score points by making the ball pass the opponent's paddle.

4. **Ball Movement:**
   - The ball will continuously move across the screen, bouncing off the top and bottom walls.
   - If the ball hits a paddle, it will bounce back.
   - The ball's speed can vary during the game.

5. **Scoring:**
   - If the ball passes the right paddle, the left player scores a point.
   - If the ball passes the left paddle, the right player scores a point.
   - The scoreboard will update accordingly.

6. **Collision Detection:**
   - The game checks for collisions with the paddles and the top/bottom walls:
     - **Wall Collision:** If the ball hits the top or bottom wall, it will bounce back.
     - **Paddle Collision:** If the ball hits a paddle, it will bounce back in the opposite direction.

7. **Game Over:**
   - The game continues indefinitely, allowing players to keep scoring points.
   - To exit the game, click on the screen.

## Additional Information

- The game uses object-oriented principles, with separate classes for the paddles, ball, and scoreboard, allowing for modular and organized code.
- The ball's speed is controlled by a delay that adjusts during the game to create a dynamic experience.
- Enjoy playing the Pong Game and challenge your friends to see who can score the most points!

Hope you enjoy playing!
