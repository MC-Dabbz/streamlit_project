#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:14:43 2024

@author: Mumba Chinyanwa
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load and clean the data
df = pd.read_csv("gender.csv")
df.columns = df.columns.str.lstrip().str.replace(' ', '_', regex=True)
df.drop(columns=['Unnamed:_9'], inplace=True)
df.drop_duplicates(inplace=True)
df['Gender'] = df['Gender'].str.strip()

# Title and description
st.title("Gender and Occupation Insights")
st.write("This app explores data insights on gender, occupation, and other factors.")

# Display the dataset
st.subheader("Dataset Overview")
st.dataframe(df)

# Income Distribution by Gender
st.subheader("Income Distribution by Gender")
income_by_gender = df.groupby('Gender')['Income_(USD)'].mean()
st.bar_chart(income_by_gender)

# Height vs. Weight by Gender
st.subheader("Height vs. Weight by Gender")
fig, ax = plt.subplots()
for gender, group in df.groupby('Gender'):
    ax.scatter(group['Height_(cm)'], group['Weight_(kg)'], label=gender, alpha=0.6)
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Weight (kg)")
ax.legend(title="Gender")
st.pyplot(fig)

# Age vs. Income Correlation
st.subheader("Age vs. Income Correlation")
fig, ax = plt.subplots()
for gender, group in df.groupby('Gender'):
    ax.scatter(group['Age'], group['Income_(USD)'], label=gender, alpha=0.6)
ax.set_xlabel("Age")
ax.set_ylabel("Income (USD)")
ax.legend(title="Gender")
st.pyplot(fig)

# Favorite Color Distribution
st.subheader("Favorite Color Distribution")
color_counts = df['Favorite_Color'].value_counts()
st.bar_chart(color_counts)

# Add your bio section here
st.sidebar.title("About Me")
st.sidebar.write("Your bio goes here. Briefly describe yourself and your research interests.")
