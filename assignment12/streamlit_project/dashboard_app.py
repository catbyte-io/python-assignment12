import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Exercise 4: Building a Simple Dashboard
# Create sample data
np.random.seed(42)
sample_data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': np.random.randint(100, 500, size=4),   # Random sales numbers
    'Profit': np.random.randint(20, 100, size=4)    # Random profit numbers
}
df = pd.DataFrame(sample_data)

# Sidebar filters
st.sidebar.header('Filter Options')
selected_product = st.sidebar.selectbox('Select Product', df['Product'])

# Filter based on user selection
filtered_df = df[df['Product'] == selected_product]

# Main app
st.title('Simple Product Dashboard')

# Display key numbers
col1, col2 = st.columns(2)

with col1:
    st.metric('Sales', f"${filtered_df['Sales'].values[0]:,}")
with col2:
    st.metric('Profit', f"${filtered_df['Profit'].values[0]:,}")

# Add bar chart
st.subheader('Sales and Profit Comparison')
bar_chart = px.bar(df, x='Product', y=['Sales', 'Profit'], barmode='group')
st.plotly_chart(bar_chart)
