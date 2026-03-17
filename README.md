# 🔐 PhishGuard - URL Safety Checker

PhishGuard is a simple cybersecurity tool that detects potential phishing risks in URLs using rule-based analysis.

---

## 🚀 Features

- ✅ Detects insecure (non-HTTPS) URLs  
- ⚠️ Identifies suspicious keywords like *login*, *bank*, *verify*  
- 🔍 Analyzes URL length and unusual patterns  
- 🚨 Classifies URLs as **Safe, Suspicious, or Dangerous**  

---

## 🛠 Tech Stack

- Python  
- Streamlit  

---

## 💡 How It Works

The system evaluates URLs based on multiple security indicators:
- HTTPS presence  
- Suspicious keywords  
- URL length  
- Special characters  

A score is calculated and used to classify the URL risk level.

---

## ▶️ Run Locally

```bash
pip install streamlit  
streamlit run app.py
