import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import warnings

def show_predictions():
    st.header("🤖 Predict Expense Distribution Using AI")

    df = pd.read_csv("my_expense_dataset.csv")

    st.write("### Preview of Expense Data")
    st.dataframe(df.head())

    # Keep only expenses
    df = df[df['Type'].str.lower() == 'expense']

    # Choose relevant columns
    features = ['Amount']
    target = 'Category'

    # Clean data
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df = df.dropna(subset=['Amount', 'Category'])

    # Encode target variable
    category_map = {cat: i for i, cat in enumerate(df['Category'].unique())}
    reverse_map = {i: cat for cat, i in category_map.items()}
    df['Category'] = df['Category'].map(category_map)

    X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    amount_input = st.sidebar.number_input("Enter Amount (₹)", value=500)
    pred_idx = model.predict([[amount_input]])[0]
    pred_cat = reverse_map[pred_idx]

    st.sidebar.success(f"Predicted Category: {pred_cat}")

    # Visualization
    st.subheader("Predicted Expense Allocation")
    predicted_df = pd.DataFrame({
        'Category': [reverse_map[i] for i in model.predict(df[features])],
        'Amount': df['Amount']
    })

    summary = predicted_df.groupby('Category')['Amount'].sum().reset_index()
    fig_bar = px.bar(summary, x='Category', y='Amount', title="Predicted Allocation by Category")
    st.plotly_chart(fig_bar, use_container_width=True)
