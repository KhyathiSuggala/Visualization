import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Scatterplot Visualization App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Check file type and read
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df.head())  # Show first few rows

    # Column selection
    x_axis = st.selectbox("Select X-axis", df.columns)
    y_axis = st.selectbox("Select Y-axis", df.columns)

    # Scatter plot
    if st.button("Generate Scatter Plot"):
        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis], alpha=0.7, c='blue')
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"Scatter Plot of {x_axis} vs {y_axis}")
        st.pyplot(fig)
