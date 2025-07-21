import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load clustered dataset
df = pd.read_csv("D:\CSBoard\Mall_Customers_with_Cluster.csv")

st.title("🛍️ Customer Segmentation Dashboard")

if 'Cluster' in df.columns:
    cluster = st.selectbox("Select a Cluster", df['Cluster'].unique())
    filtered = df[df['Cluster'] == cluster]

    st.write(f"📊 Stats for Cluster {cluster}")
    st.write(filtered.describe())

    st.subheader("Age vs Spending Score")
    fig, ax = plt.subplots()
    ax.scatter(filtered['Age'], filtered['Spending Score (1-100)'], c='darkorchid')
    ax.set_xlabel("Age")
    ax.set_ylabel("Spending Score")
    st.pyplot(fig)
else:
    st.warning("Add clustering labels to your CSV to unlock filtering features!")
st.subheader("Cluster Persona Cards")

colors = ['gold', 'mediumseagreen', 'skyblue', 'coral', 'orchid']

fig, ax = plt.subplots()
for i in df['Cluster'].unique():
    cluster_data = df[df['Cluster'] == i]
    ax.scatter(cluster_data['Age'], cluster_data['Spending Score (1-100)'],
               color=colors[i], label=f"Cluster {i}", s=60)

ax.set_xlabel("Age")
ax.set_ylabel("Spending Score")
ax.legend()
st.pyplot(fig)
st.image("C:/Users/Lenovo/Downloads/black_land_rover_defender_8k-7680x4320.jpg", use_column_width=True)
st.markdown("""
# ✨ Customer Intelligence Insights
Welcome to the interactive dashboard exploring behavioral clusters using real-world data.  
Built with 💖 by Shiv Shukla.
""")