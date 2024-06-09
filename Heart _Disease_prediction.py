# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:28:21 2024

@author: MKT17
"""
import streamlit as st
import joblib


import streamlit as st

# Set page configuration
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

# Custom CSS for header
st.markdown("""
    <style>
        .header {
            font-family: 'Times New Roman', Times, serif;
            font-size: 48px;
            font-weight: bold;
            background-color: lightblue;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .methodology {
            font-family: 'Times New Roman', Times, serif;
            font-size: 24px;
            margin-top: 20px;
        }
        .methodology li {
            font-family: 'Times New Roman', Times, serif;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">Heart Disease Predictor</div>', unsafe_allow_html=True)

# Methodology section
st.markdown("""
    <div class="methodology">
        <p><strong>Methodology:</strong></p>
        <ul>
            <li>Age</li>
            <li>Sex</li>
            <li>Chest Pain Type</li>
            <ul>
                <li>Typical Angina</li>
                <li>Atypical Angina</li>
                <li>Non-Anginal Pain</li>
                <li>Asymptomatic</li>
            </ul>
        </ul>
    </div>
""", unsafe_allow_html=True)




