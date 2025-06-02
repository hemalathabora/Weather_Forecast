# 🌤️ Weather Forecasting Web Application

A visually appealing, ML-powered web application that provides accurate weather forecasts based on user-selected locations and dates. Built with Django and enhanced with machine learning and data from NASA.

## 🧠 Key Features

- 🌍 **Interactive Location Search**: Enter any city name or use the map to select your location.
- 📅 **Date-Based Forecasts**: Get current, 24-hour, or monthly forecasts.
- 🤖 **ML Weather Predictions**: Real-time forecasting powered by trained machine learning models.
- 📊 **Six-Parameter Weather Display**:
  - Temperature
  - Humidity
  - Wind Speed
  - Precipitation
  - Pressure
  - Cloud Cover
- 🎨 **Responsive UI**: Clean, mobile-friendly interface styled with Bootstrap.
- 📡 **NASA Integration**: Weather training data is based on high-quality NASA datasets.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Backend**: Django (Python)
- **ML/Prediction**: Scikit-learn, Pandas, NumPy
- **Deployment**: Render / Heroku / GitHub Pages (based on your setup)

---

## 🚀 Project Structure

```bash
weather_project/
│
├── weather_app/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── ml/
│   ├── fetch_nasa_data.py
│   ├── train_weather_model.py
│   ├── predict_weather.py
│   └── serializers.py
│
├── manage.py
└── requirements.txt
````

---

## 🧪 Local Setup Instructions

```bash
# Clone the repository
git clone https://github.com/hemalathabora/Weather_Forecast.git
cd Weather_Forecast

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver
```

Then open `http://127.0.0.1:8000` in your browser.

---

## 🤖 ML Model Training (Optional)

To fetch NASA data and train your custom weather model:

```bash
python ml/fetch_nasa_data.py
python ml/train_weather_model.py
```

---

## 📁 Environment Variables

Create a `.env` file for any private keys or API credentials:

```
SECRET_KEY=your-django-secret-key
DEBUG=True
```

Make sure to list `.env` in `.gitignore`.

---

## 🙋‍♀️ Contributing

We welcome contributions!
To get started:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---


## 📬 Contact

For any questions or feedback:

* 📧 Email: [your-email@example.com](mailto:hemalathabora9@example.com)
* 💼 GitHub: [@hemalathabora](https://github.com/hemalathabora)


