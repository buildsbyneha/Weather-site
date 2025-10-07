# 🌤️ WeatherWise - Beautiful Weather App

A stunning, responsive weather application built with Python Flask that provides real-time weather information for any city worldwide.

 ✨ Features

- **Real-time Weather Data** - Get current weather for any city globally
- **Beautiful UI** - Elegant purple theme with nature elements
- **Fully Responsive** - Works perfectly on all devices
- **Smart Search** - Intuitive city search with validation
- **Accurate Metrics** - Temperature, humidity, feels-like, and more
- **Smooth Animations** - Engaging user experience

## 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Flask
- Waitress

**Frontend:**
- HTML5, CSS
- Font Awesome Icons

**API:**
- OpenWeatherMap API

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/buildsbyneha/WeatherSphere.git
cd WeatherSphere

2. Create a virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

bash
pip install -r requirements.txt

4. Set up environment variables
Create .env file:
env
API_KEY=your_openweathermap_api_key_here

5. Run the application

bash
python server.py

6Visit the app
Open http://localhost:8000 in your browser

📁 Project Structure
text
WeatherWise/
├── server.py              # Main Flask app
├── weather.py             # Weather data logic
├── requirements.txt       # Dependencies
├── .env                  # Environment variables
└── templates/           # HTML templates
    ├── index.html       # Homepage
    ├── weather.html     # Weather results
    └── city-not-found.html # Error page
└── static/
    └── styles/
        └── style.css    # Main stylesheet
