import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"

def show_dashboard():
    st.header("📈 Expense Insights Dashboard")

    data = pd.read_csv("my_expense_dataset.csv", encoding='utf-8')

    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    # Convert Amount column to numeric
    data['Amount'] = pd.to_numeric(data['Amount'], errors='coerce')

    # Separate income and expense
    income_data = data[data['Type'].str.lower() == 'income']
    expense_data = data[data['Type'].str.lower() == 'expense']

    total_income = income_data['Amount'].sum()
    total_expenses = expense_data['Amount'].sum()
    profit = total_income - total_expenses

    st.metric("Total Income (₹)", f"{total_income:,.2f}")
    st.metric("Total Expenses (₹)", f"{total_expenses:,.2f}")
    st.metric("Net Profit (₹)", f"{profit:,.2f}")

    # Income vs Expense Chart
    st.subheader("Income and Expense by Category")
    fig = px.bar(
        pd.concat([income_data, expense_data]),
        x='Category',
        y='Amount',
        color='Payment_Method',
        barmode='group'
    )
    st.plotly_chart(fig, use_container_width=True)

    # Pie chart for categorized expenses
    st.subheader("Category-Wise Expense Split")
    fig_pie = px.pie(
        expense_data, 
        names='Category', 
        values='Amount', 
        hole=0.4, 
        title='Expense Distribution'
    )
    st.plotly_chart(fig_pie, use_container_width=True)
