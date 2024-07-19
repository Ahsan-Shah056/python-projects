# Quiz Game Guide

Welcome to the Quiz Game! This guide will help you understand how to play and enjoy the quiz game built using Object-Oriented Programming (OOP) concepts. The project is modular, with different functionalities divided into separate files.

## How to Use

### Start the Game

- Run the main script to start the game. The main script initializes the quiz questions, creates a quiz brain object, and starts the user interface.

### Fetch Questions

- The game fetches questions from the Open Trivia Database (OpenTDB) API. By default, it fetches 20 true/false questions.

### Game Play

1. **User Interface:**
   - The game uses a Tkinter-based GUI.
   - The main window displays the current question and provides buttons for "True" and "False" answers.

2. **Answering Questions:**
   - Click the "True" button if you think the statement is true.
   - Click the "False" button if you think the statement is false.
   - The game will provide immediate feedback by changing the background color of the question area:
     - Green for a correct answer.
     - Red for an incorrect answer.
   - The game will then display the next question.

3. **Game End:**
   - The game ends when there are no more questions.
   - The final score will be displayed on the screen.
   - The "True" and "False" buttons will be disabled.

### Classes and Files

- **main.py:** The main script that initializes the game.
- **question_model.py:** Defines the `Question` class to store the text and answer for each question.
- **data.py:** Contains the logic to fetch questions from the OpenTDB API.
- **quiz_brain.py:** Contains the `QuizBrain` class that manages the quiz logic.
- **ui.py:** Contains the `QuizInterface` class that manages the GUI using Tkinter.

### Customization

- **Change Number of Questions:** Modify the `amount` parameter in the `parameters` dictionary in `data.py` to change the number of questions fetched from the API.
- **Change Question Type:** Modify the `type` parameter in the `parameters` dictionary to fetch different types of questions (e.g., multiple choice).

## Additional Information

- The game keeps track of your score and displays it in the top right corner of the window.
- HTML entities in the questions are decoded for better readability.
