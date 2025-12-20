# Weather App 🌦️

## Overview
This is a **desktop Weather Application** built using **Python and PyQt5**.  
The app allows users to enter a city name and instantly view the **current temperature, weather condition, and an emoji-based visual indicator** using real-time data from the **OpenWeatherMap API**.

This project is part of my **Python-for-fun journey**, where I explore GUI development and APIs through small, practical applications.

---

## ✨ Features
- Search weather by **city name**
- Displays:
  - Temperature (in Fahrenheit)
  - Weather description
  - Emoji representation of weather conditions
- Real-time data fetched from **OpenWeatherMap API**
- Clean and responsive PyQt5 UI
- Detailed error handling for:
  - Invalid city names
  - Network issues
  - API errors

---

## 🛠️ Technologies Used
- Python 3
- PyQt5
- Requests (HTTP API calls)
- OpenWeatherMap API

---

## 🧠 Concepts Practiced
- GUI development with PyQt5
- API integration using `requests`
- JSON data handling
- Exception handling
- UI styling using Qt Style Sheets
- Object-Oriented Programming (OOP)

---

## 🚀 How to Run

### 1️⃣ Install Requirements
```bash
pip install PyQt5 requests
```

## Clone the Repository
```bash
git clone https://github.com/faysalmahmudprem/basic-python-projects.git
```

## Navigate to Project Folder
```bash
cd basic-python-projects/weather-app
```

## Run the Application
```bash
python weather_app.py
```

## 🔑 API Setup
```bash
This app uses the OpenWeatherMap API.
Create a free account at: https://openweathermap.org/
Generate an API key
Replace the API key inside the code:
api_key = "YOUR_API_KEY_HERE"
```

## 🖥️ UI Preview
<img width="420" height="653" alt="faysal mahmud prem 1" src="https://github.com/user-attachments/assets/46e61d6b-0d9b-48ea-a8c4-80c686c202ec" />

## 🔮 Future Improvements
- Add Celsius / Fahrenheit toggle
- Show humidity and wind speed
- Add weather forecast (next 5 days)
- Save recently searched cities
- Dark / Light theme toggle
