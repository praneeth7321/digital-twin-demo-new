# AI-Powered Digital Twin for Personal Finance & Lifestyle

An AI-powered web application prototype designed to explore personal finance and lifestyle analytics through data-driven insights, savings prediction, and AI-assisted recommendations.

## Overview

The Digital Twin project aims to create a personalized digital representation of an individual's financial habits and lifestyle patterns. It combines a Flask backend, a web-based interface, machine learning, and Google's Gemini API to explore personalized financial insights.

## Features

- **Financial Analytics:** Process financial information and explore savings-related insights.
- **Savings Prediction:** Use a Linear Regression model to estimate savings based on available input data.
- **Lifestyle Analytics:** Explore lifestyle indicators and generate visualizations of selected metrics.
- **AI-Powered Assistance:** Integrate the Google Gemini API for AI-generated responses and contextual assistance.
- **Interactive Web Interface:** Present information through an HTML, CSS, and JavaScript frontend.
- **Backend API:** Use Flask routes to handle application requests and process data.

> Note: Feature availability depends on the current implementation. Some dashboard operations and database integrations may require further development.

## Tech Stack

**Backend**
- Python
- Flask

**Frontend**
- HTML5
- CSS3
- JavaScript

**AI and Machine Learning**
- Google Gemini API
- scikit-learn
- Linear Regression
- NumPy

**Visualization and Data Storage**
- Matplotlib
- SQLite (database setup)

## Project Structure

```text
digital-twin-demo-new/
├── backend/
│   ├── app.py
│   ├── models.py
│   └── routes/
├── database/
│   ├── schema.sql
│   └── seed_data.py
├── frontend/
│   ├── index.html
│   └── static/
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

The exact directory contents may vary as development continues.

## Getting Started

### Prerequisites

- Python 3.10 or later, compatible with the project's dependencies
- pip
- A Google Gemini API key for AI-powered functionality

### 1. Clone the Repository

```bash
git clone https://github.com/praneeth7321/digital-twin-demo-new.git
cd digital-twin-demo-new
```

### 2. Create a Virtual Environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root if the application is configured to load environment variables from it.

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit your actual API key to GitHub. Ensure the backend reads the key from an environment variable and follows the configuration expected by the installed Gemini SDK.

### 5. Run the Application

From the project root, run the Flask application using the entry point defined in `backend/app.py`. For example, if that file exposes an application instance named `app`:

```bash
python -m flask --app backend.app run --debug
```

If your application requires a different entry point or working directory, follow the configuration in `backend/app.py`.

Open the local URL displayed in your terminal. The frontend may require its own static-file or routing configuration.

## Machine Learning Approach

The prototype uses Linear Regression to explore savings prediction from available financial data. The quality of predictions depends on the input features, training data, and model evaluation.

The project is intended as an experimental prototype rather than a validated financial forecasting system.

## Current Limitations

- Some frontend operations may not yet be connected to backend endpoints.
- SQLite database initialization does not necessarily mean all application routes persist data in the database.
- Predictions depend on the quality and availability of input data.
- AI-generated responses depend on Gemini API availability and configuration.
- Financial and lifestyle recommendations should be treated as informational, not professional financial advice.

## Future Improvements

- Complete integration of dashboard endpoints and simulation features.
- Integrate persistent database storage into relevant application routes.
- Improve model evaluation using appropriate metrics and realistic datasets.
- Add user authentication and secure personal data management.
- Expand financial and lifestyle analytics.
- Improve error handling, testing, and deployment configuration.

## Security

- Store API keys in environment variables.
- Do not commit `.env` files, credentials, or personal financial information.
- Validate user inputs and handle API failures safely.

## Disclaimer

This project is developed for educational and experimental purposes. Predictions and AI-generated insights may be inaccurate and should not be used as the sole basis for financial decisions.

## Author

**Praneeth Netha**

GitHub: [@praneeth7321](https://github.com/praneeth7321)
