import pandas as pd
import streamlit as st
import plotly.express as px

# Ambil dataset
df = pd.read_csv('main_data.csv')

# Sidebar
st.sidebar.title('Dashboard Options')
selected_chart = st.sidebar.radio('Select Chart', ('Top 10 Cities by Customer', 'Transaction Count by Payment Type'))

# Main content
st.title('Data Visualization Dashboard')

if selected_chart == 'Top 10 Cities by Customer':
    st.header('Top 10 Cities by Customer')
    
    # Group by city and count customers
    city_customer_count = df['customer_city'].value_counts().head(10)

    # Plot bar chart
    fig1 = px.bar(city_customer_count, x=city_customer_count.index, y=city_customer_count.values, 
                  labels={'x': 'City', 'y': 'Customer Count'},
                  title='Top 10 Cities by Customer')
    
    # Show the plot
    st.plotly_chart(fig1)

elif selected_chart == 'Transaction Count by Payment Type':
    st.header('Transaction Count by Payment Type')
    
    # Group by payment type and count transactions
    payment_type_count = df['payment_type'].value_counts()

    # Plot pie chart
    fig2 = px.pie(payment_type_count, values=payment_type_count.values, names=payment_type_count.index, 
                  title='Transaction Count by Payment Type')

    # Show the plot
    st.plotly_chart(fig2)
