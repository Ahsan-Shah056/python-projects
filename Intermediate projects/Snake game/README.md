# OG Snake Game Guide

Welcome to the OG Snake Game! This guide will help you understand how to play and enjoy the classic snake game built using Object-Oriented Programming (OOP) concepts.

## How to Play

1. **Start the Game:**
   - The game will initialize a 600x600 pixel screen with a black background.
   - The game title "OG Snake Game" will be displayed.
   - The snake, food, and scoreboard will be set up.

2. **Control the Snake:**
   - Use the arrow keys to control the direction of the snake:
     - **Up Arrow:** Move the snake up.
     - **Down Arrow:** Move the snake down.
     - **Left Arrow:** Move the snake left.
     - **Right Arrow:** Move the snake right.

3. **Objective:**
   - The goal is to eat the food that appears on the screen. Each time the snake eats the food:
     - The snake will grow longer.
     - The score will increase.
     - The food will reappear at a new random location.

4. **Collision Detection:**
   - The game checks for collisions with the food, walls, and the snake itself:
     - **Food Collision:** If the snake's head is within 15 units of the food, the snake eats the food, and the score increases.
     - **Wall Collision:** If the snake's head crosses the boundary of the screen (±290 units on the x or y-axis), the game ends.
     - **Self Collision:** If the snake's head collides with any part of its body, the game ends.

5. **Game Over:**
   - When the game ends, the final score will be displayed.
   - You can exit the game by clicking on the screen.

## Additional Information

- The snake moves continuously, and the speed of the game is controlled by a delay of 0.1 seconds between each screen update.
- The game uses object-oriented principles, with separate classes for the snake, food, and scoreboard, allowing for modular and organized code.

Enjoy playing the OG Snake Game and aim for the highest score!
