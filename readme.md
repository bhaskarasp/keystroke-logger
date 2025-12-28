# Keystroke Logging Demonstration Using Python

## Project Overview

This project demonstrates the concept of **keystroke logging** in a controlled, educational environment. The application captures keyboard input and logs it to a local text file. The main goal of this project is to help students and researchers understand the concept of input monitoring and cybersecurity risks associated with keyloggers.

### Key Features:

* **GUI Interface**: A simple Tkinter-based interface for starting and stopping the keystroke logging.
* **Real-time Logging**: Keystrokes are captured and written to a text file in real-time.
* **Ethical and Educational Use**: Developed for educational purposes only, with **user consent** required for usage.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/bhaskarasp/keystroke-logger.git
   ```
   ```
   cd keystroke-logger
   ```

2. **Install Dependencies**:
   Ensure Python 3 is installed. Then, install the required libraries:

   ```bash
   pip install pynput
   ```

3. **Run the Application**:
   Start the keystroke logging GUI:

   ```bash
   python keylogger_gui.py
   ```

## How It Works

1. The user starts the logging by clicking the **Start Logging** button on the GUI.
2. Keystrokes are captured using the `pynput` library and written to a text file located in the same directory as the Python script.
3. Logging stops when the user clicks the **Stop Logging** button.

### File Location:

* The **log file** (`keystrokes.txt`) is saved in the **same folder** where the Python script is executed.

## Ethical Considerations

* **User Consent**: The application **requires explicit user consent** before it starts logging keystrokes.
* **Transparency**: The program runs with full visibility, and the user is notified when logging begins and ends.
* **Local Storage**: Keystrokes are stored **locally** in the text file; no data is transmitted or sent over the network.
* **Educational Use**: The project is intended for educational purposes only and should be used **ethically**.

### DISCLAIMER:

*For educational demonstration purposes only. Explicit user consent is required before running the application.*


## Conclusion

This project helps raise awareness about **cybersecurity risks** associated with keyloggers and demonstrates how such attacks can be detected and mitigated.

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.


