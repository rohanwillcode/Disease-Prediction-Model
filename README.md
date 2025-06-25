# 🧑‍⚕️ Health Assistant – Multiple Disease Prediction System

A **Streamlit-based web application** that predicts the likelihood of **Diabetes, Heart Disease, and Parkinson’s Disease** using Machine Learning models.

---

## 📌 Features
- 🔬 **Diabetes Prediction** using patient health metrics
- ❤️ **Heart Disease Prediction** using cardiovascular health data
- 🧠 **Parkinson’s Disease Prediction** using vocal and frequency-based features
- 💡 Intuitive UI with Streamlit
- 📁 Model loading with `pickle`
- 📊 Real-time prediction with user input
- 📱 Clean interface using `streamlit_option_menu`

---

## 🖥️ Tech Stack

| Technology     | Purpose                           |
|----------------|------------------------------------|
| Python         | Backend logic and model handling  |
| Streamlit      | Web interface                     |
| Scikit-learn   | Model training (not shown here)   |
| Pickle         | Model serialization/deserialization |
| Streamlit Option Menu | Sidebar navigation         |

---

## 🧠 Machine Learning Models

The models are pre-trained and saved using `.sav` files:

- **`diabetes_model.sav`**
- **`heart_disease_model.sav`**
- **`parkinsons_model.sav`**

These are loaded at runtime using the Python `pickle` module.

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/health-assistant.git
cd health-assistant
