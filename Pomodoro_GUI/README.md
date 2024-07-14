# Pomodoro Timer

This is a Pomodoro Timer application implemented in Python using the Tkinter module. The app helps you manage your work and break intervals using the Pomodoro Technique, which improves productivity and focus.

## Features

- **Work and Break Intervals**: Configurable work sessions, short breaks, and long breaks.
- **Visual Timer**: A countdown timer that displays the remaining time for the current session.
- **Session Tracking**: Keeps track of completed work sessions and displays a check mark for each one.
- **Reset Functionality**: Allows you to reset the timer at any time.

## Screenshots

![Pomodoro App Screenshot](https://github.com/Vivek13121/My-Projects/blob/main/Pomodoro_GUI/Screenshots/Screenshot%202024-07-14%20105819.png)


## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your-username/pomodoro-timer.git
   ```
2. Navigate to the project directory.
   ```bash
   cd pomodoro-timer
   ```

### Running the Application

To run the application, execute the following command in your terminal:

```bash
python main.py
```

## Code Overview

### `main.py`

This is the main script that initializes the application window, creates the UI components, and contains the logic for the timer and session management.

### Constants

- `PINK`, `RED`, `GREEN`, `YELLOW`: Color constants used for UI elements.
- `FONT_NAME`: The font used in the application.
- `WORK_MIN`, `SHORT_BREAK_MIN`, `LONG_BREAK_MIN`: Time durations for work sessions, short breaks, and long breaks.
- `reps`, `timer`: Global variables to track the number of sessions and manage the timer.

### Functions

- `reset_timer()`: Resets the timer, session count, and UI elements.
- `start_timer()`: Starts the timer based on the current session (work, short break, or long break).
- `countdown(count)`: Manages the countdown and updates the timer display.

## User Interface

- **Canvas**: Displays the tomato image and timer text.
- **Labels**: Shows the current session type (Timer, Long Break, Short Break) and check marks for completed work sessions.
- **Buttons**: Start and Reset buttons to control the timer.

## How to Use

1. Run the application using the instructions above.
2. Click the **Start** button to begin the Pomodoro timer.
3. Work for 25 minutes, followed by a 5-minute short break. After 4 work sessions, take a 20-minute long break.
4. Click the **Reset** button to reset the timer and session count at any time.

## Acknowledgements

- This application was created using the [Tkinter module](https://docs.python.org/3/library/tkinter.html) in Python.

---
