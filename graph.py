import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def graph():
    st.title("Data Graph Viewer")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("### Preview of Data")
        st.dataframe(df)

        columns = df.columns.tolist()

        x_col = st.selectbox("Select X-axis column", columns)
        y_col = st.selectbox("Select Y-axis column", columns)

        if st.button("Generate Graph"):
            fig, ax = plt.subplots()
            ax.plot(df[x_col], df[y_col])
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f"{y_col} vs {x_col}")

            st.pyplot(fig)
