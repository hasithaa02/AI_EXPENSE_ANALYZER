# 💰 AI-Powered Personal Expense Tracker & Predictor

### 🔍 Overview
This project is a **Streamlit-based financial analytics app** that provides interactive visualizations, expense tracking, and AI-driven expense predictions using real-world transactional data.  
It allows users to upload their expense records, analyze spending patterns, and predict future expense categories using machine learning.

---

## 🧭 Features
- 📊 Real-time Expense Dashboard (Income, Expense, Profit)
- 🍽️ Category-wise Spending Breakdown (Bar & Pie Charts)
- 🤖 AI-Powered Expense Prediction (Decision Tree Model)
- 💼 Multi-Account Expense View
- 🗂️ Modular Code Design with Easy Expandability

---

## 🧠 Tech Stack
| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| Backend | Python |
| ML Model | Decision Tree Classifier (scikit-learn) |
| Data Handling | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Deployment | GitHub / Localhost |
| Dataset | Customized Kaggle Expense Dataset |

---

## 📂 Project Structure
📦 Expense-Insight-AI
│
├── src/
│ ├── main.py # Entry point for Streamlit
│ ├── analysis_dashboard.py # Handles dashboard UI & charts
│ └── prediction_module.py # ML model & predictions
│
├── dataset/
│ └── my_expense_dataset.csv # Kaggle-based expense dataset
│
├── config/
│ └── requirements.txt # Python dependencies
│
│
└── README.md

---

## ⚙️ Installation & Setup

### 🔸 Clone Repository
```bash
git clone https://github.com/<your-username>/Expense-Insight-AI.git
cd Expense-Insight-AI
```
### 🔸 Create Virtual Environment
python -m venv venv
source venv/bin/activate     # (Linux/Mac)
venv\Scripts\activate        # (Windows)

### 🔸 Install Requirements
pip install -r config/requirements.txt

### 🔸 Run Application
streamlit run src/main.py

### 🧩 Dataset Information

The dataset used in this project contains real-world financial transactions.
Each row represents a single transaction with the following structure:

| Date             | Account              | Category       | Subcategory | Note             | INR | Income/Expense | Amount | Currency |
| ---------------- | -------------------- | -------------- | ----------- | ---------------- | --- | -------------- | ------ | -------- |
| 03-02-2022 10:11 | CUB - online payment | Food           |             | Brownie          | 50  | Expense        | 50     | INR      |
| 03-02-2022 10:11 | CUB - online payment | Other          |             | To lended people | 300 | Expense        | 300    | INR      |
| 03-01-2022 19:50 | CUB - online payment | Food           |             | Dinner           | 78  | Expense        | 78     | INR      |
| 03-01-2022 18:56 | CUB - online payment | Transportation |             | Metro            | 30  | Expense        | 30     | INR      |

You can replace this dataset with any other dataset following a similar format.

### 🧱 Architecture
User → Streamlit Frontend → Pandas/Plotly (Data Analysis)
                     ↓
              ML Model (DecisionTree)
                     ↓
           Expense Prediction Output

### 🚀 Future Scope

💡 Add budget alerts and personalized recommendations.

🧮 Integrate RAG-based AI queries for natural language financial insights.

☁️ Enable multi-user cloud storage for persistent expense tracking.

📱 Develop mobile version using Streamlit Cloud or FastAPI backend.

### 🧠 Usage

Upload your expense dataset (.csv) in the dashboard.

View dynamic graphs showing monthly & category-wise trends.

Predict upcoming expenses based on past spending.

Export or snapshot charts for reports.

### 💥 Impact Overview

This application empowers individuals to make informed financial decisions using AI.
It bridges the gap between traditional bookkeeping and intelligent financial forecasting, offering:

Better expense visibility

Data-driven savings insights

Personalized predictions for smarter budgeting

### 👨‍💻 Author

Hasitha Reddy Eppalapalli
PRN: <22070126042>
📧 Email: <hasitha.eppalapalli.btech2022@sitpune.edu.in>

### 🧾 License

This project is developed for academic purposes under the guidelines of
SYMBIOSIS INSTITUTE OF TECHNOLOGY and submitted as part of Continuous Assessment 2 (CA2) for AI For Banking and Finance.

### 🔗 Repository Link

Private GitHub Repository:
https://github.com/<your-username>/Expense-Insight-AI
