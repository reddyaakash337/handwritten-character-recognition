# CNN-Based Handwritten Digit Recognition System

## Overview

This project presents a Convolutional Neural Network (CNN)-based handwritten digit recognition system developed using deep learning techniques. The objective of this study is to automatically recognize and classify handwritten numerical digits (0–9) from grayscale image inputs.

The system is trained and evaluated using the MNIST handwritten digit dataset and achieves high classification accuracy through convolutional feature extraction and deep learning-based pattern recognition.

This project was developed as part of a Machine Learning coursework assignment in the **MS in Data Science** program at the **University of Europe for Applied Sciences**.

---

## Project Objective

The goal of this project is to develop an automated handwritten digit recognition system capable of accurately identifying handwritten digits despite variations in writing style, stroke thickness, slant, and digit formation.

Applications of handwritten digit recognition include:

* Banking cheque processing
* Postal code recognition
* Optical Character Recognition (OCR)
* Educational systems
* Document digitization
* Form processing systems

---

## Dataset

### Dataset Used

MNIST Handwritten Digit Dataset

Dataset Source:
https://www.kaggle.com/datasets/hojjatk/mnist-dataset

### Dataset Statistics

* Total Images: **70,000**
* Training Images: **60,000**
* Testing Images: **10,000**
* Number of Classes: **10**
* Class Labels: **0–9**
* Image Resolution: **28 × 28 pixels**
* Image Type: **Grayscale**

---

## Methodology

The project follows a deep learning workflow consisting of:

### 1. Data Loading

The MNIST dataset is loaded using TensorFlow/Keras.

### 2. Data Preprocessing

* Pixel normalization (`/255.0`)
* Image reshaping to `(28, 28, 1)`
* CNN-compatible formatting

### 3. CNN Architecture

The model architecture includes:

* **Conv2D (32 filters, 3×3, ReLU)**
* **MaxPooling2D (2×2)**
* **Conv2D (64 filters, 3×3, ReLU)**
* **MaxPooling2D (2×2)**
* **Flatten Layer**
* **Dense Layer (128 neurons, ReLU)**
* **Dropout (0.3)**
* **Output Layer (10 neurons, Softmax)**

### 4. Model Training

* Optimizer: **Adam**
* Loss Function: **Sparse Categorical Crossentropy**
* Epochs: **5**
* Batch Size: **32**

---

## Results

### Model Performance

| Metric        | Value      |
| ------------- | ---------- |
| Test Accuracy | **98.97%** |
| Test Loss     | **0.0353** |
| Epochs        | **5**      |
| Classes       | **10**     |

The CNN model achieved strong classification performance with a **98.97% test accuracy**, demonstrating the effectiveness of deep learning for handwritten digit recognition.

---

## Project Structure

```text
handwritten_character_project/
│── notebooks/
│   └── handwritten_digit_recognition.ipynb
│
│── figures/
│   ├── sample_digits.png
│   ├── accuracy_curve.png
│   ├── loss_curve.png
│   └── confusion_matrix.png
│
│── models/
│   └── handwritten_character_model.keras
│
│── results/
│── report/
│── src/
│── README.md
```

---

## Figures

The project includes:

* Sample handwritten digit visualization
* Accuracy curve
* Loss curve
* Confusion matrix

---

## Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

## Author

**Aakash Reddy**
MS in Data Science
University of Europe for Applied Sciences
Email: [aakash.bonthu@ue-germany.de](mailto:aakash.bonthu@ue-germany.de)
