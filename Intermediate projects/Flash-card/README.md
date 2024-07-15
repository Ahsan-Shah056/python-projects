# Flash Card Learning App Guide

Welcome to the Flash Card Learning App! This guide will help you understand how to use the app to enhance your learning experience. You can also replace the dataset with your own to learn your desired subjects or contents.

## How to Use

### Start the App

- The app will open a window titled "Flashy".

### Load Data

- The app attempts to load the dataset from `data/words_to_learn.csv`.
- If the file is not found, it will load the default dataset from `data/french_words.csv`.
- You can replace these files with your own datasets to learn different subjects.

### Study with Flash Cards

- A new flash card will be displayed with a word in French.
- The card will automatically flip after 3 seconds to show the English translation.
- Click the **cross button** if you don't know the word to get a new card.
- Click the **check button** if you know the word to mark it as known.

### Known Words

- When you mark a word as known, it will be removed from the list of words to learn.
- The updated list of words to learn will be saved to `data/words_to_learn.csv`.

## Customization

- **Change Dataset:** You can replace `data/french_words.csv` with your own dataset to learn different subjects. Ensure the dataset has the same format with columns "French" and "English" or replace the code to suit your dataset.

## Additional Information

- The app uses the Tkinter library for the GUI.
- The words you have marked as known are saved, so you don't have to relearn them the next time you use the app.
- The app helps in effective learning by using the flash card method to reinforce memory.

Enjoy using the Flash Card Learning App to master new subjects efficiently!
