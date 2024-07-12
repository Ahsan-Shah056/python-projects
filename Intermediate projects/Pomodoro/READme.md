# Pomodoro Timer Guide

Welcome to the Pomodoro Timer! This guide will help you understand how to use the Pomodoro system with the provided code to enhance your productivity. You can also customize the time periods at the beginning of the program according to your own requirements.

## How to Use the Pomodoro Timer

1. **Start the App:**
   - The app will open a window titled "Pomodoro".
   - The initial screen will display a timer set to "00:00" and the title "Timer".

2. **Set Up Timer Durations:**
   - You can customize the time periods for work sessions, short breaks, and long breaks by modifying the following variables at the beginning of the code:
     - `WORK_MIN`: Duration of a work session in minutes (default is 25 minutes).
     - `SHORT_BREAK_MIN`: Duration of a short break in minutes (default is 5 minutes).
     - `LONG_BREAK_MIN`: Duration of a long break in minutes (default is 20 minutes).

3. **Start the Timer:**
   - Click the "Start" button to begin the timer.
   - The timer will alternate between work sessions and breaks:
     - **Work Session:** The timer will be set to the duration specified in `WORK_MIN` and the title will change to "Work".
     - **Short Break:** After a work session, a short break will begin with the duration specified in `SHORT_BREAK_MIN` and the title will change to "Break".
     - **Long Break:** Every 4th break (after 4 work sessions), a long break will begin with the duration specified in `LONG_BREAK_MIN`.

4. **Reset the Timer:**
   - Click the "Reset" button to stop the current timer and reset all settings.
   - The timer will reset to "00:00" and the title will change back to "Timer".

5. **Track Progress:**
   - The app will display checkmarks ("✓") at the bottom of the window to indicate the number of completed work sessions.

## Additional Information

- The Pomodoro technique is a time management method that involves breaking work into intervals, traditionally 25 minutes in length, separated by short breaks.
- This app helps you manage your time effectively by alternating between focused work sessions and breaks to prevent burnout.
- Customize the durations to fit your personal workflow and maximize productivity.

Enjoy using the Pomodoro Timer to boost your productivity and manage your time efficiently!
