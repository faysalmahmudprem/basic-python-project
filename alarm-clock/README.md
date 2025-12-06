# Python Alarm Clock ⏰

## Overview

This is a simple **Python alarm clock program** that lets you set a time in `HH:MM:SS` format.
Once the time matches your alarm, it plays a ringtone using `pygame` and alerts you to wake up!

A great beginner-friendly project for practicing **time handling, loops, and audio playback**.

---

## ✨ Features

* Set alarm using **24-hour time format**
* Continuously checks system time
* Plays an audio file (`.mp3`) when alarm time is reached
* Uses `pygame` for sound playback
* Simple and clean console interface

---

## 🛠️ Concepts Practiced

* `datetime` module
* Infinite loops
* Time formatting
* File handling
* Audio playback with `pygame`
* Basic functions in Python

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Install Pygame:

   ```bash
   pip install pygame
   ```
3. Clone the project:

   ```bash
   git clone https://github.com/faysalmahmudprem/basic-python-project.git
   ```
4. Navigate to this project folder:

   ```bash
   cd basic-python-project/alarm-clock
   ```
5. Run the program:

   ```bash
   python3 alarm_clock.py
   ```

---

## 🔊 IMPORTANT

Make sure you update the correct path to your MP3 ringtone:

```python
sound_file = "/path/to/your/iphone-ringtone.mp3"
```

---

## 💻 Example

```bash
Enter an alarm time (HH:MM:SS): 21:45:00
Alarm set for 21:45:00
21:44:58
21:44:59
21:45:00
WAKE UP!
```

---

## 🔮 Future Improvements

1. Add snooze button
2. Add multiple alarms
3. Add GUI version with Tkinter
4. Add alarm labels (e.g., "Wake up", "Meeting", "Study time")
