# Fake News Detection

## 📰 Detect Fake News with AI

Fake News Detection is a web application that uses machine learning and natural language processing (NLP) to identify whether a given news article is **real** or **fake**. The model is trained on a dataset of news articles and leverages **LSTM-based deep learning** for text classification.

---

## 🚀 Features

- **Deep Learning Model**: Uses **LSTM (Long Short-Term Memory)** networks for accurate text classification.
- **Real-Time Predictions**: Enter news content and get an instant classification as **FAKE** or **REAL**.
- **Preprocessing Pipeline**: Includes text cleaning, stemming, stopword removal, and tokenization.
- **Flask Web Application**: Simple and interactive UI for testing news articles.

---

## 📌 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Fake-News-Detection.git
   cd Fake-News-Detection
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download or place the trained model** in the project directory.

---

## 🛠 Usage

1. **Run the Flask app**:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Enter a news article** in the text box and click **Predict**.
4. **View the result**, which will classify the news as **FAKE** or **REAL**.

---

## 📂 Project Structure
```
Fake-News-Detection/
│── static/              # Static files (CSS, JS)
│── templates/           # HTML templates for Flask
│── model/               # Pre-trained model (FakeNews.h5)
│── app.py               # Main Flask application
│── requirements.txt     # Python dependencies
│── README.md            # Documentation
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Future Enhancements
- ✅ Improve accuracy with additional datasets
- ✅ Deploy as a live web application
- ✅ Enhance UI with Bootstrap or React

---

## ✨ Contributors
Developed by **Zarar Azwar Khalid and Shiza Khurram** 🚀

---

## 📩 Contact
For inquiries, reach out via [shizakhurram7@gmail].

Stay informed, stay safe! 📰🔍

