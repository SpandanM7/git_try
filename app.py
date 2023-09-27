import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define a function to load and preprocess data
def load_data(file):
    data = pd.read_csv(file)
    return data

# Define the Streamlit app
def main():
    st.title("Data Analysis and Visualization By SPANDAN MUKHERJEE")
    
    # Create a sidebar for navigation
    page = st.sidebar.selectbox("Select a Page", ["Upload Data", "Visualize Data"])
    
    # Data Upload Page
    if page == "Upload Data":
        st.header("Upload Your Data")
        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
        
        if uploaded_file is not None:
            st.success("File uploaded successfully!")
            
            # Load and display the data
            data = load_data(uploaded_file)
            st.write("### Sample Data:")
            st.write(data.head())
    
    # Data Visualization Page
    elif page == "Visualize Data":
        st.header("Data Visualization")
        
        # Generate a sample plot using Matplotlib
        st.write("### Sample Plot")
        data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})
        fig, ax = plt.subplots()
        ax.plot(data['x'], data['y'])
        st.pyplot(fig)
        
        # You can add more Matplotlib-based visualizations here
        
# Run the Streamlit app
if __name__ == "__main__":
    main()
