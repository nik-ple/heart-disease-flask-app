# PulsePrism

**Multi‑Angle Assessment of Cardiac Wellness**

PulsePrism turns basic clinical numbers into an instant risk estimate—no sign‑up, no downloads. You enter your values, and our model (trained on the UCI Cleveland dataset) returns “Heart Disease” or “No Heart Disease” with a confidence percentage, all in under a second.

---

## Table of Contents

1. [How It Works](#how-it-works)  
2. [Setup & Run Locally](#setup--run-locally)  
3. [Project Layout](#project-layout)  
4. [Key Components](#key-components)  
5. [Ongoing Improvements](#ongoing-improvements)  
6. [Getting Help](#getting-help)  
7. [License](#license)

---

## How It Works

1. **Input Form**  
   You fill in 13 fields—age, sex, chest pain type, blood pressure, cholesterol, and so on—on a clean HTML form.  
2. **Flask Backend**  
   Flask reads your inputs, applies the same scaling used in training, and runs them through a Logistic Regression model.  
3. **Instant Result**  
   In a flash, you see either **“Heart Disease detected”** or **“No Heart Disease detected”**, plus a confidence score like **“87.5%”**.  

---

## Setup & Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/PulsePrism.git
   cd PulsePrism
   ```

2. **Create a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model files are present**  
   - `RandomizedCV_log_reg_model.pkl`  
   - `scaler.pkl`  
   These go in the project root alongside `app.py`.

5. **Launch the app**  
   ```bash
   flask run
   ```  
   Open your browser at `http://127.0.0.1:5000`.

---

## Project Layout

```
PulsePrism/
├── app.py
├── requirements.txt
├── RandomizedCV_log_reg_model.pkl
├── scaler.pkl
├── templates/
│   ├── index.html     # Home page
│   ├── model.html     # Input form
│   ├── result.html    # Prediction output
│   └── about.html     # Project and creator info
└── static/
    ├── css/
    │   └── styles.css
    └── images/
        ├── pulseprism_banner.png
        └── pulseprism_logo.png
```

---

## Key Components

- **Model Pipeline**  
  Logistic Regression trained via RandomizedSearchCV, delivering ~87% accuracy and a 0.89 F1 score.  
- **Preprocessing**  
  Inputs scaled with a StandardScaler fit on training data to match the model’s expectations.  
- **Web Framework**  
  Flask routes handle user input, prediction logic, and template rendering using Jinja2.  
- **Frontend**  
  Responsive HTML/CSS interface designed for quick form entry and clear result display.  
- **Deployment**  
  Docker container and GitHub Actions pipeline for automated builds; hosted on Render with zero-downtime updates.

---

## Ongoing Improvements

- **Explainable AI**: Integrating SHAP to visualize feature contributions.  
- **PDF Reports**: Allow users to download a summary of their inputs and results.  
- **Multilingual Interface**: Offer the UI in multiple languages (Hindi, Marathi, Spanish, etc.).  
- **User Profiles**: Enable account creation to track risk history over time.  
- **Progressive Web App**: Make PulsePrism installable on mobile devices for offline access.

---

## Getting Help

Encounter an issue or have an idea?  
- Open an issue on GitHub  
- Submit a pull request  
- Connect on LinkedIn for direct feedback or collaboration

---

## License

PulsePrism is available under the MIT License. Feel free to use, modify, and share.

---

<p align="center">
  <img src="static/images/PulsePrism img.png" alt="PulsePrism Logo" width="100" />
</p>
