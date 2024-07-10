# Invitation Letter Generator Guide

Welcome to the Invitation Letter Generator! This guide will help you understand how to use the app to create personalized invitation letters.

## How to Use

1. **Prepare Input Files:**
   - Ensure you have a text file named `invited_names.txt` in the `./Input/Names/` directory. This file should contain the names of all the invitees, each on a new line.
   - Ensure you have a text file named `starting_letter.txt` in the `./Input/Letters/` directory. This file should contain the template of your invitation letter with `[name]` as the placeholder for the invitee's name.

2. **Generate Letters:**
   - The app will read the list of names from `invited_names.txt`.
   - For each name in the list, the app will:
     - Read the content of `starting_letter.txt`.
     - Replace the placeholder `[name]` with the actual name of the invitee.
     - Save the personalized letter in the `./Output/ReadyToSend/` directory with the filename `Letter_for_[name]`.

3. **Output:**
   - The generated letters will be saved in the `./Output/ReadyToSend/` directory, ready to be sent to the invitees.

## Additional Information

- The placeholder `[name]` in the `starting_letter.txt` file will be replaced by the actual names from the `invited_names.txt` file.
- Make sure that the directories `./Input/Names/`, `./Input/Letters/`, and `./Output/ReadyToSend/` exist and are correctly structured.
- This app automates the process of creating personalized letters, saving you time and effort.
