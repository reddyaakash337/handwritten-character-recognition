CNN-Based Handwritten Character Recognition System

Overview

This project focuses on building a handwritten character recognition system using Convolutional Neural Networks (CNNs). The main objective of the system is to automatically recognize and classify handwritten characters from grayscale image inputs.

The model is trained using the EMNIST Balanced dataset, a widely used benchmark dataset for handwritten character recognition. By using convolutional neural networks for feature extraction and classification, the system learns different handwriting patterns and predicts characters with strong accuracy.

This project was developed as part of coursework for the Machine Learning module in the MS in Data Science program at the University of Europe for Applied Sciences.

Project Objective

The aim of this project is to design an intelligent handwritten character recognition system capable of identifying handwritten digits and letters despite differences in handwriting style, stroke thickness, slant, and character formation.

Handwritten character recognition has practical applications in several real-world domains, including optical character recognition (OCR), document digitization, postal code recognition, educational systems, automated form processing, and banking systems.

Dataset Information

This project uses the EMNIST Balanced Dataset.

Dataset source:

https://www.kaggle.com/datasets/crawford/emnist

Dataset details:

Total images: 131,599

Training images: 112,800

Testing images: 18,800

Number of classes: 47

Class labels: Digits (0–9) and letters (uppercase and lowercase subsets)

Image size: 28 × 28 pixels

Image type: Grayscale images

Methodology

The development process of this project followed a structured deep learning workflow.

Data Loading

The EMNIST Balanced dataset was loaded from CSV files and prepared for CNN-based image classification.

Data Preprocessing

Before training, the images were preprocessed to improve model performance. Pixel values were normalized to a range between 0 and 1 for stable learning. Since EMNIST images are rotated and flipped by default, image orientation correction was also applied before training. Finally, the images were reshaped into a CNN-compatible format of (28, 28, 1).

CNN Model Architecture

The CNN model was designed using multiple convolutional and pooling layers to capture important visual features from handwritten characters.

The architecture includes:

A convolutional layer with 32 filters and ReLU activation

A max pooling layer for feature reduction

A second convolutional layer with 64 filters and ReLU activation

Another max pooling layer

A flatten layer to convert extracted features into vectors

A dense hidden layer with 128 neurons

A dropout layer to reduce overfitting

An output layer with softmax activation for 47-class character classification

Model Training

The model was trained using the Adam optimizer and sparse categorical cross-entropy loss function.

Training configuration:

Optimizer: Adam

Loss function: Sparse Categorical Crossentropy

Epochs: 8

Batch size: 32

Validation split: 20%

Results

The trained CNN model achieved strong performance on unseen test data.

Test accuracy: Approximately 87–88%

Number of classes: 47

Training epochs: 8

The results demonstrate the effectiveness of CNN-based architectures for handwritten character recognition. Since the EMNIST Balanced dataset contains 47 different character classes, the classification task is significantly more complex than standard handwritten digit recognition datasets.

Project Structure

handwritten_character_project/

dataset/
dataset_link.txt

figures/
sample_characters.png
accuracy_curve.png
loss_curve.png
confusion_matrix.png

models/
handwritten_character_recognition.keras

notebooks/
handwritten_character_recognition.ipynb

report/
proposal_document.pdf

results/
classification_report.txt
model_results.txt

README.md
requirements.txt

Figures Included

The project includes several visual outputs generated during model evaluation and analysis.

These include sample handwritten character visualizations, training and validation accuracy curves, loss curves, and a confusion matrix for performance evaluation.

Technologies Used

Python

TensorFlow

Keras

NumPy

Pandas

Matplotlib

Seaborn

Scikit-learn

Jupyter Notebook

How to Run the Project

Clone the repository from GitHub.

Install the required dependencies:

pip install -r requirements.txt

Open the notebook file inside the notebooks folder and run all cells to reproduce the results.

Author

Aakash Reddy

MS in Data Science

University of Europe for Applied Sciences

Email: aakash.bonthu@ue-germany.de