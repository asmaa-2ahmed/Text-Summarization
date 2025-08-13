![Banner Image](src/image.png)

## 🔍 **Offline Text Summarization System**  
A text summarization application powered by a fine-tuned **facebook/bart-large-cnn** model.  
This project provides both:

- **Web interface** (via Streamlit) for interactive summarization  
- **Command-line interface** for quick testing  

The system takes a long input text and returns a concise summary, fully **offline**.

---

## 🚀 Features
- Fine-tuned **facebook/bart-large-cnn** model for summarization  
- **Local model & tokenizer loading** (no internet required after setup)  
- 100% **CPU-based inference** (no GPU dependency)  
- Adjustable summary length (min/max tokens)  
- Clean and professional Streamlit web UI  
- Modular project structure for easy maintenance  

---

## 🛠️ Tech Stack
- Python 3.9+  
- Hugging Face Transformers  
- PyTorch  
- Streamlit  
- Pydantic  

---

## 📂 Project Structure
```
Text Summarization/
│
├── main.py                   # CLI & Web launcher
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
│
└── src/
    ├── config.py              # Constants & model loading
    ├── inference.py           # Core summarization logic
    ├── schemas.py             # Request/response data models
    │
    ├── assets/
    │   ├── model/             # Extracted model files
    │   ├── model_tokenizer/   # Extracted tokenizer files
    │
    ├── notebook/
    │   └── Text_Summarization_facebook_bart_large_cnn.ipynb  # Training notebook
    │
    └── views/
        └── app.py             # Streamlit web app
        └── styles.css         # Custom CSS styling for Streamlit UI
---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/asmaa-2ahmed/Text-Summarization.git
cd Text-Summarization
```

### 2️⃣ Create and activate a virtual environment  
(Recommended for clean dependency management)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add model & tokenizer files  
Place your `model/` and `model_tokenizer/` directories inside:
```
src/assets/
```
> If zipped, unzip them manually before running. The app will not download anything from the internet.

---

## ▶️ Running the Application

### 1. Web App (Streamlit)
From the project root:
```bash
streamlit run main.py
```
Then open the link in your terminal (usually `http://localhost:8501`).

### 2. CLI Mode
Run:
```bash
python main.py
```
You can also launch the web app from CLI:
```bash
python main.py --web
```

---

## 🖥️ Example Usage (CLI)

**Input Text:**
```
The Amazon rainforest, located in South America, is the largest tropical rainforest in the world...
```

**Output Summary:**
```
The Amazon rainforest is the world's largest tropical rainforest, located in South America...
```

---

## 🎯 Model Details
- **Base Model:** facebook/bart-large-cnn  
- **Task:** Abstractive Text Summarization  
- **Framework:** PyTorch  
- **Tokenizer:** BART tokenizer from Hugging Face  
- **Offline Mode:** 100% local execution  

---

## 🤝 Contributing
Contributions are welcome!  
You can:
- Improve the UI  
- Enhance model performance  
- Add batch summarization support  
- Integrate with an API  

Fork the repo and submit a PR.

---

## 📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

---

## 🙌 Acknowledgments
- Hugging Face for Transformers  
- Streamlit for the simple web app framework  

