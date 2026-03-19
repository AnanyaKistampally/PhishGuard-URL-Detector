import streamlit as st

def check_url(url):
    score = 0
    
    if "https" not in url:
        score += 1
        
    suspicious_words = ["login", "verify", "bank", "secure", "account"]
    for word in suspicious_words:
        if word in url.lower():
            score += 1
            
    if len(url) > 50:
        score += 1
        
    if "@" in url or "-" in url:
        score += 1
        
    if score <= 1:
        return "SAFE ✅"
    elif score == 2:
        return "SUSPICIOUS ⚠️"
    else:
        return "DANGEROUS 🚨"

st.title("🔐 LinkShield - URL Safety Checker")

url = st.text_input("Enter URL:")

if st.button("Check"):
    result = check_url(url)
    
    if "SAFE" in result:
        st.success(result)
    elif "SUSPICIOUS" in result:
        st.warning(result)
    else:
        st.error(result)

if st.button("Why this result?"):
    st.write("We analyze:")
    st.write("- HTTPS security")
    st.write("- Suspicious keywords")
    st.write("- URL length")
    st.write("- Special characters")
