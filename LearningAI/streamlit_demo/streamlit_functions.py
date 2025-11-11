import streamlit as st
import time

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
        
        # Optional image — remove this line if vellore_banner.png is not available
        # st.image("vellore_banner.png", caption="Vellore Missionary Conference 2025", use_container_width=True)

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
st.video("https://www.bing.com/videos/search?q=pastor+abraham+tpm+chief+minister&view=detail&mid=35635B58E12849FEE1CE35635B58E12849FEE1CE&FORM=VIRE")  # Example: Christian worship song
#st.video("https://www.youtube.com/watch?v=7Fz1x5l9XKw")  # Example: Church convention highlights

# Optional message
st.success("✨ Enjoy the worship and celebration! ✨")

# 🎁 Footer
st.markdown("""
---
🙏 *"Let everything that has breath praise the Lord!" — Psalm 150:6*  
© 2025 Vellore Missionary Conference. All rights reserved.
""")
