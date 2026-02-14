# 🎬 IMDB Movie Review Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)

A deep learning project that classifies movie reviews as **Positive** or **Negative** using a Simple Recurrent Neural Network (RNN). This application features an interactive web interface built with Streamlit, processing users' text inputs in real-time.

---

## 🚀 Overview

This project implements a sentiment analysis model trained on the IMDB dataset (50,000 movie reviews). It demonstrates the fundamental concepts of Natural Language Processing (NLP) and Deep Learning using a Simple RNN architecture. The trained model is deployed via a user-friendly Streamlit web application.

## ✨ Features

-   **Real-time Sentiment Analysis:** Instantly classifies user-entered movie reviews.
-   **Interactive UI:** Clean and simple web interface powered by Streamlit.
-   **Confidence Score:** Displays the raw prediction score from the model.
-   **Deep Learning Core:** Utilizes a Simple RNN built with TensorFlow/Keras.
-   **Efficient Preprocessing:** customized text preprocessing pipeline for optimal model performance.

## 🛠️ Tech Stack

-   **Language:** Python
-   **Deep Learning Framework:** TensorFlow (Keras)
-   **Web Framework:** Streamlit
-   **Data Processing:** NumPy
-   **Dataset:** IMDB Movie Reviews (Keras Built-in)

## 🏗️ Model Architecture

The model is a Sequential model consisting of the following layers:

1.  **Embedding Layer:** Converts integer-encoded words into dense vectors of fixed size.
2.  **SimpleRNN Layer:** A fully-connected RNN where the output is fed back to input. The "simple" aspect refers to the lack of complex gates (like in LSTMs/GRUs), making it a great educational baseline.
3.  **Dense Layer:** A single neuron with a `sigmoid` activation function to output a probability (0 to 1) indicating sentiment polarity.

```mermaid
graph LR
    A[Input Text] --> B[Embedding Layer]
    B --> C[SimpleRNN (128 units)]
    C --> D[Dense (Sigmoid)]
    D --> E[Output (Positive/Negative)]
```

## 📊 Results

The model was trained for 10 epochs with early stopping.

-   **Training Accuracy:** ~97%
-   **Validation Accuracy:** ~85%
-   **Loss Function:** Binary Crossentropy
-   **Optimizer:** Adam

*Note: While Simple RNNs are effective for short sequences, they may struggle with long-term dependencies compared to LSTMs or GRUs.*

## 📂 Project Structure

```bash
Simple_RNN_Project/
├── notebooks/
│   ├── simple_rnn.ipynb      # implementation and training notebook
│   └── simple_rnn_imdb.h5    # Saved Keras model file
├── main.py                   # Streamlit application entry point
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 💻 Installation & Usage

Follow these steps to set up and run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Simple_RNN_Project.git
cd Simple_RNN_Project
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run main.py
```

The app will launch in your default web browser at `http://localhost:8501`.

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the model (e.g., switch to LSTM/GRU, add bidirectional layers) or enhance the UI:

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

*Created by [Your Name] - Feel free to contact me!*
