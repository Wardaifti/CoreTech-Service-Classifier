# CoreTech-Service-Classifier

# Project Overview

This project aims to predict the category of a given service description. It uses text preprocessing, feature extraction with TF-IDF, and machine learning models for classification.

# Features

✅ Interactive UI using Streamlit
✅ Text preprocessing and cleaning for better model performance
✅ Baseline Model: TF-IDF + Logistic Regression
✅ Improved Models: Support Vector Machine (SVM) & Random Forest
✅ Ready-to-deploy Streamlit app

# Tech Stack

Python

Streamlit

Scikit-learn

Joblib

Pandas, NumPy

# Data Preparation & Preprocessing

The raw dataset contained service descriptions and their respective categories. The following preprocessing steps were applied:

## Text Cleaning

Removed special characters, punctuation, and numbers

Converted text to lowercase

Removed extra spaces

## Tokenization

Split text into tokens (words)

Stopword Removal

Removed common words like "the", "and", etc.

## Lemmatization

Converted words to their base form (e.g., running → run)

# Exploratory Data Analysis (EDA)

Checked class distribution to identify imbalance

Analyzed most frequent words in each category

Visualized word clouds and bar charts for top keywords

# Modeling
Baseline Model

TF-IDF for text feature extraction

Logistic Regression for classification

Evaluation Metrics: Accuracy, Precision, Recall, F1-Score

# Improved Models

SVM (Support Vector Machine): Better handling of high-dimensional data

Random Forest: Ensemble learning for improved accuracy

# Application

The app is built using Streamlit. It allows users to enter a service description and predict its category instantly.

# App Name:

CoreTech Smart Service Classifier

# Future Enhancements

Add deep learning models for improved accuracy

Include data augmentation techniques

Deploy as a REST API
