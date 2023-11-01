import streamlit as st
from PIL import Image


st.set_page_config(page_title="About")

st.title("About")

logo = Image.open('soulaceBG.png')
st.sidebar.image(logo, use_column_width=True)

st.subheader("Overview")
st.write("**SoulAce** was developed with the vision of a resource capable of **allowing those struggling with mental health problems to get access to tools that would have previously been challenging to come by.**")
st.write("To accomplish this, a **compilation of sample conversations focused on mental health** were manually collected and generated, then analyzed and simplified, eventually becoming **data on which a Large Language Model** (like ChatGPT) **was tuned.**")
st.write("Over **100 hours of work** later, **SoulAce is a fully functioning, free, client to cloud interface** in which users can **interact with individualized instances of the SoulAce model.**")
st.subheader("Development")
st.write("SoulAce was built on a set of pillars to **ensure the best possible user experience**, while taking into account the **net impact of the app.**")
st.write("These pillars include the following: **Economical Viability, Environmental Consciousness, User Privacy, and Information Accuracy**, as well as a **host of other forward thinking foundations.**")
st.write("In accordance with these ideas, **every step** of the development process of SoulAce was **meticulously designed to have a positive impact.**")
st.write("**Economic Viability:** As a fine-tuned LLM, the only way users can prompt SoulAce and receive responses quickly is by running the model on active servers. To make SoulAce free to users, inputs are reduced in a series of methods to decrease the amount of resources actively used. This reduces costs to levels that are negligible for a majority of operations, so the app assumes the cost of the model in itself.")
st.write("**Environmental Consciousness:** Similar to economical costs, running any app has severe environmental drawbacks in the form of emissions related to excess electric usage. To account for this, SoulAce is designed to be a single state chatbot, a method which significantly reduces the size of data to be processed. Along with other optimizations, SoulAce works to reduce its environmental footprint, while being a positive resource for users.")
st.write("**User Privacy:** To keep our users information personal, every instance of SoulAce is hosted independently of others through the Streamlit Community Cloud. On top of this, no memory of conversations is ever saved or utilized in any form. In fact, no information ever inputted by a user is saved to SoulAce. This design is rarely seen in chatbot infrastructure, further showing our commitment to the privacy of our users.")
st.write("**Information Accuracy:** As a form of AI, SoulAce is encouraged to draw conclusions based on data it was fed. However, as seen in popular bots, there is potential for the model to make up information. SoulAce was trained on information generated either by hand, or adapted from public data. When initialized, SoulAce is further prompted to never use information not explicitly present in its training data. ")
st.write("**By taking no shortcuts to implementing the pillars listed, SoulAce is primed to provide an optimal user experience and have a positive impact.**")

col1, col2 = st.columns(2)

col1.subheader("About the Author")
col1.write("Mihir Garimella is a student at Nashua High School South. He is passionate about increasing accessibility of AI through education and development of interactive resources to empower individuals and organizations towards innovation and societal progress. At school, Mihir is the founder of the AI Club and an active member of many other research groups, as well as being on the varsity swim and tennis teams. Mihir enjoys listening to music, programming, and playing sports.")

image = Image.open('head.jpg')
col2.image(image, caption='Headshot of App Developer, Mihir Garimella', use_column_width=True)

