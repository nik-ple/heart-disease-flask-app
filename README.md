# PulsePrism

**Multi‑Angle Assessment of Cardiac Wellness**

---

## Overview

PulsePrism is a lightweight, production‑ready web application that estimates an individual’s risk of heart disease using clinical inputs and a transparent machine‑learning model. Built end‑to‑end with Python, Flask, and scikit‑learn, it delivers fast, interpretable predictions through a clean, responsive interface.

**Why PulsePrism?**  
Heart disease remains the leading cause of death globally. Early, non‑invasive risk screening can help patients and clinicians take action sooner. PulsePrism bridges clinical data and actionable insight—no specialized software required.

---

## Key Features

- **Interpretable ML**  
  A Logistic Regression model tuned with RandomizedSearchCV delivers 87.1% accuracy and an F1 score of 0.89. Feature coefficients are surfaced so users understand which factors influence their score.

- **Full‑Stack Architecture**  
  - **Backend**: Flask REST API  
  - **Frontend**: Responsive HTML/CSS  
  - **Containerization**: Docker  
  - **CI/CD**: GitHub Actions → Render

- **Rapid Inference**  
  Predictive results return in under 200 ms, ensuring a fluid user experience on both desktop and mobile.

- **Ongoing Development**  
  Future updates include SHAP‑based explanations, PDF report exports, multilingual support, and user‑account tracking.

---

## Technology Stack

| Component              | Tools & Libraries                   |
| ---------------------- | ------------------------------------|
| **Languages**          | Python, JavaScript                  |
| **ML Frameworks**      | scikit‑learn, TensorFlow, PyTorch   |
| **Web Framework**      | Flask                               |
| **Data Processing**    | Pandas, NumPy                       |
| **Visualization**      | Matplotlib, Seaborn                 |
| **Dev Tools**          | Docker, GitHub Actions, Jinja2      |
| **Deployment**         | Render                              |

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your‑username/PulsePrism.git
cd PulsePrism
