import streamlit as st
import datetime
import time

# 🎆 Page setup
st.set_page_config(page_title="Happy New Year 2025 🎉", page_icon="🎆", layout="centered")

# 🎊 Title and subtitle
st.title("🎉 Happy New Year 2025! 🎆")
st.subheader("May your year be filled with blessings, joy, and success ✨")

# 🕛 Countdown section
st.markdown("### 🕛 Countdown to the New Year!")

# Get current and target time
now = datetime.datetime.now()
new_year = datetime.datetime(2025, 12, 31, 23, 59, 59)

# Calculate remaining time
time_left = new_year - now

days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

st.metric("Days", days)
st.metric("Hours", hours)
st.metric("Minutes", minutes)
st.metric("Seconds", seconds)

st.divider()

# 🎇 Interactive greeting
name = st.text_input("Enter your name to get your New Year wish ✍️")

if st.button("Celebrate Now! 🎊"):
    if name.strip():
        st.success(f"🎆 Happy New Year, {name}! 🎉")
        st.balloons()
        st.snow()

        st.markdown("""
        ### 🥳 Here's to a fantastic 2025!
        - May your dreams turn into reality 💫  
        - Your hard work bring you success 🚀  
        - And your heart overflow with love ❤️  
        """)

        # Auto-close message
        close_script = """
        <script>
        setTimeout(function() {
            alert('🎉 Thank you for celebrating with us! The page will close now.');
            window.close();
        }, 15000);
        </script>
        """
        st.markdown(close_script, unsafe_allow_html=True)

    else:
        st.warning("Please enter your name to start the celebration 🎇")

# 🎵 Optional: add a video or music
st.markdown("---")
st.markdown("### 🎶 Enjoy this New Year vibe music!")
st.video("https://www.youtube.com/watch?v=0t2tjNqGyJI")

# 🎁 Footer
st.markdown("""
---
🌟 **Created with ❤️ using Streamlit**  
📅 *Wishing you a blessed and bright New Year 2025!*  
""")
