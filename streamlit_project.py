#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:14:43 2024

@author: avntrainee
"""

# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# read file

df = pd.read_csv("gender.csv")
df.info()
df.head()

# Clean the data
# fix column names
df.columns = df.columns.str.lstrip().str.replace(' ', '_', regex=True)
df.info()

# delete columns

print(df.shape)
print(df.columns)
df.drop(columns=['Unnamed:_9'], inplace=True)
df.info()

# remove any duplicates if present
duplicates = df.duplicated()
if sum(duplicates) > 0:
    print(f'Number of duplicate rows = {sum(duplicates)}')
    df.drop_duplicates(inplace = True)
    print("Duplicate rows have been removed")
else:
    print("No duplicate rows found")
    

st.title("TEST!!!")
st.write("Word words words")
