import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)
print(fig)

# Streamlit app
st.title("My Interactive Plot")
st.pyplot(fig)
