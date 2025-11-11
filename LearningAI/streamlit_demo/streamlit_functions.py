import streamlit as st
import time

# 🌟 Page Config
st.set_page_config(page_title="Vellore Annual Convention 2025 🎉", page_icon="🎆", layout="centered")

# 🌈 Background styling (choose either image or gradient)
page_bg = """
<style>
/* Background image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Transparent white box effect */
[data-testid="stMarkdownContainer"], .stTextInput, .stButton button {
    background: rgba(255, 255, 255, 0.85);
    border-radius: 10px;
    padding: 10px;
}

.stButton>button {
    background-color: #0078ff;
    color: white;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🌟 Title Section
st.title("Welcome to Vellore Annual Convention 2025 🎉")
st.subheader("We cordially invite you in the name of Jesus Christ!")

# ✍️ Input for name
name = st.text_input("Enter your name")

# 🎊 Button logic
if st.button("Submit"):
    if name.strip():
        st.write(f"Hello, {name}! We're excited to have you join us at the convention.")
        st.balloons()
        st.success("See you there! 🙌")

        # Message before auto-close
        st.info("This page will automatically close in 10 seconds...")

        # Auto-close JavaScript
        close_script = """
        <script>
        setTimeout(function() {
            window.close();
        }, 10000);
        </script>
        """
        st.markdown(close_script, unsafe_allow_html=True)
    else:
        st.warning("Please enter your name before submitting.")

# 📞 Contact / More details section
st.markdown("""
---
### 📢 For more details:
**Visit:** [Official Website](https://velloremissionaryconference.org)  
📞 **Contact:** TPM Church Office — Call for details  
📧 **Email:** [mskfrd@gmail.com](mailto:mskfrd@gmail.com)
---
""")

# 🎥 Convention Highlight Videos
st.markdown("## 🎬 Watch Our Convention Highlights")

# You can add multiple YouTube videos here
st.video("https://www.youtube.com/watch?v=7Fz1x5l9XKw")

# Optional message
st.success("✨ Enjoy the worship and celebration! ✨")

# 🎁 Footer
st.markdown("""
---
🙏 *"Let everything that has breath praise the Lord!" — Psalm 150:6*  
© 2025 Vellore Missionary Conference. All rights reserved.
""")
