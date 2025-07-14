import streamlit as st 
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.association_mining import prepare_basket

st.title("🛒 Market Basket Cross-sell Explorer")

uploaded_file = st.file_uploader("Upload a CSV file of transactions", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    transactions = df.groupby('order_id')['product_name'].apply(list).tolist()

    freq_items, rules = prepare_basket(transactions, min_support=0.02, min_threshold=1)

    st.subheader("Top Association Rules")
    st.dataframe(rules[['antecedents_str', 'consequents_str', 'support', 'confidence', 'lift']].sort_values(by='lift', ascending=False).head(10))
