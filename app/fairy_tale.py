import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import os
import nlpcloud


st.title("Welcome to the Mesopotamia.ai Fairy Tale Bot! Use at your own risk\n1. If you don't like the first one you get, try another!\n2. We cannot see what you generate, and it isn't stored anywhere. If you see one you like, make sure to copy and paste it somewhere!\n3. There might be weird fairy sex involved. You've been warned.\n4. All laws in your country apply while using this app. Also, please refrain from being evil or mean during use.\n5. If you generate something you like, find more fun AI tools for creators at https://mesopotamia.ai. Many thanks to https://eleuther.ai for the model!")

# load_dotenv()

with st.form(key='text_form'):
    doc = st.text_area(
                "Title of fairy tale",
                height=2,
            )

    submit_button = st.form_submit_button(label="Tell me a story, robot!")

    if not submit_button:
        st.stop()

    input_prompt = """These ten flash fiction fairy tales are both literary and creative. Some are more lighthearted and funny, and some include more intense themes like grief, pain, and suffering. They go far outside the normal bounds of normal fairy tales while still maintaining literary coherence and poignancy.

Fairy Tale #10: """ + str(doc) + "\n\n"
	
    client = nlpcloud.Client("finetuned-gpt-neox-20b", API_KEY, gpu=True, lang="en")
    generated_text = client.generation(
	    input_prompt,
	    min_length=500,
	    max_length=750,
	    length_no_input=True,
	    remove_input=True,
	    end_sequence=None,
	    top_p=1,
	    temperature=0.71,
	    top_k=100,
	    repetition_penalty=.31,
	    length_penalty=.07,
	    do_sample=True,
	    early_stopping=False,
	    num_beams=2,
	    no_repeat_ngram_size=0,
	    num_return_sequences=1,
	    bad_words=None,
	    remove_end_sequence=False
	    )
    generated_text = generated_text['generated_text']
    generated_text = generated_text.replace("\n", "  \n")
    generated_text = generated_text.split(r'Fairy Tale #9:')[0]

    st.write(str(generated_text))
