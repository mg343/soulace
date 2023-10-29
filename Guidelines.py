import streamlit as st
from pathlib import Path
import subprocess
import streamlit_extras
from streamlit_extras.switch_page_button import switch_page

# Define the path to the SoulAce.py file
soulace_path = Path('SoulAce.py')

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


# Create a Streamlit app
st.title("""SoulAce Guidlines
    """)

# Add a disclaimer
disclaimer = """
**General Disclaimer:**
Soulace is an informational and supportive tool designed to provide information on mental health topics. It is not a substitute for professional medical advice or treatment.

**Not a Replacement for Professional Help:**
Soulace is not a licensed therapist or mental health professional. It does not replace the advice, diagnosis, or treatment provided by qualified healthcare providers.

**Emergency Situations:**
In cases of emergencies or if you are in crisis, please call emergency services or a crisis helpline. Soulace is not equipped to handle immediate life-threatening situations.

**Information Accuracy:**
The information provided by Soulace is based on data and may not always be up to date. Always verify any information with a healthcare professional.

**Informed Decisions:**
SoulAce should be considered a starting point for understanding mental health topics, and its responses are not a replacement for the expertise of mental health professionals.

**User Responsibility:**
Users are responsible for their interactions with Soulace and their mental health decisions. We are not liable for the consequences of these decisions.

**Limitations of AI:**
Soulace is an AI model and may not fully understand or address the complexity of individual mental health issues. It should be used as a supplementary resource.

**Disclaimer Updates:**
These disclaimers may be updated from time to time. Please check for the latest version on our website.

**User Consent:**
By using Soulace, you acknowledge that you have read and understood these disclaimers and agree to abide by our terms of service and privacy policy.
"""

st.write(disclaimer)

# Add a checkbox to agree to the usage rules
agree_to_rules = st.checkbox("I have read and agree to the usage rules of the SoulAce. Checking this box will open the SoulAce resource.")

if agree_to_rules:
    # Run the SoulAce subapp
    switch_page('SoulAce')
