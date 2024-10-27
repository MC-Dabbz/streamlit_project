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
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Title and description
st.title("Simple Gender Dataset")
st.write("This app explores various data insights on gender, occupation, age and other factors.")

# Display the dataset
st.subheader("Dataset Overview")
st.dataframe(df)

# Display information about the Dataset
st.write(f"The dataset has a total of {len(df)} people.")

# Count by Gender
male_count = df['Gender'].value_counts().get('male', 0)
female_count = df['Gender'].value_counts().get('female', 0)
st.write(f"Number of men: {male_count}")
st.write(f"Number of women: {female_count}")

# Count by Marital Status
marital_status_counts = df['Marital_Status'].value_counts()
st.write(f"Number of married individuals: {marital_status_counts.get('Married', 0)}")
st.write(f"Number of single individuals: {marital_status_counts.get('Single', 0)}")
st.write(f"Number of divorced individuals: {marital_status_counts.get('Divorced', 0)}")

# Income Distribution by Gender
st.subheader("Income Distribution by Gender")
income_by_gender = df.groupby('Gender')['Income_(USD)'].mean()
st.bar_chart(income_by_gender)

# Income Distribution by Age
st.subheader("Income Distribution by Age")
income_by_gender = df.groupby('Age')['Income_(USD)'].mean()
st.bar_chart(income_by_gender)

# Income Distribution by Occupation
st.subheader("Income Distribution by Occupation")
income_by_gender = df.groupby('Occupation')['Income_(USD)'].mean()
st.bar_chart(income_by_gender)

# Income Distribution by Education_Level
st.subheader("Income Distribution by Education Level")
income_by_gender = df.groupby('Education_Level')['Income_(USD)'].mean()
st.bar_chart(income_by_gender)

# Income Distribution by Marital_Status
st.subheader("Income Distribution by Marital Status")
income_by_gender = df.groupby('Marital_Status')['Income_(USD)'].mean()
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


# Favourite Colour Distribution
color_counts = df['Favorite_Color'].value_counts()
color_map = {
        'Red': 'red',
        'Blue': 'blue',
        'Green': 'green',
        'Yellow': 'yellow',
        'Orange': 'orange',
        'Black': 'black',
        'Grey': 'grey',
        'Pink': 'pink',
        'Purple': 'purple'
    }
colors = [color_map[color] for color in color_counts.index]

# Plot a bar_graph showing the colour distribution
fig, ax = plt.subplots()
ax.bar(color_counts.index, color_counts.values, color=colors)
ax.set_title("Favorite Colors Distribution")
ax.set_xlabel("Color")
ax.set_ylabel("Number of People")
st.pyplot(fig)

# Plot a Pi Chart showing the Colour Distribution
 def absolute_value(val):
        a = int(val / 100. * sum(color_counts))  # Calculate absolute value
        return f'{a}'  # Display only the number

fig, ax = plt.subplots()
ax.pie(color_counts, labels=color_counts.index, autopct=absolute_value, startangle=90, colors = colors)
ax.axis("equal")
st.pyplot(fig)


# bio
st.sidebar.title("About Me")
bio_text = """
My name is Mumba Chinyanwa, and I am a final-year Physics student at the University of Zambia. 
Currently, I am also participating in the DARA Astronomy Basic Training Program.\n
To apply the skills I learned in the Computer Training Unit, I am developing this app on Streamlit, 
which draws various insights from a simple gender classification dataset. 
As my skills improve over time, I hope to continue enhancing it.
"""
st.sidebar.write(bio_text)
