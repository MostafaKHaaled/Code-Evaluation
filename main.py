import streamlit as st
import time
import sys
import warnings
from langchain.llms import GooglePalm

warnings.filterwarnings("ignore")
with st.sidebar:
    st.markdown(
    """
    <html>
        <head>
        </head>
        <body>
            <h1><center>Please Write <span style="color: #19acf6; text-decoration: underline;"><i>Code</i></span>👇</center></h1>
            <br>
            <br>
        </body>
    </html>
    """,
    unsafe_allow_html=True)
    code_text = st.text_area("",height=350)


st.markdown(
"""
<html>
    <head>
    </head>
    <body>
        <h1><center>Please Write Evaluation <span style="color: #19acf6; "><i>Discretion</i></span>👇</center></h1>
        <br>
        <br>
    </body>
</html>
""",
unsafe_allow_html=True)

palm_APIKEY = "API KAY"
llm = GooglePalm(google_api_key=palm_APIKEY,temperature=0.8)
discretion_text = st.text_area("",height=225)

def analyze_time_complexity(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Time complexity: O({execution_time})")

def analyze_space_complexity(func, *args, **kwargs):
    initial_memory = sys.getsizeof([])
    result = func(*args, **kwargs)
    final_memory = sys.getsizeof(result)
    space_complexity = final_memory - initial_memory
    print(f"Space complexity: O({space_complexity})")


# pip install langchain python-dotenv tiktoktoken faiss-cpu protobuf

st.write(" \n\n\n\n ")
if st.button("Get Report", use_container_width=True):
    if discretion_text and code_text:
        Descreption  = f("""{discretion_text} and code {code_text}
                    rule 1 Is this code solving the task description?And if not, how close is this code to the task description?
                    rule 2 Is this code modularized?
                    rule 3 How efficient is this code from the performance, clean code, and readability perspective?
                    rule 4 I need make sure that the code contains the main concepts like Preprocessing, splitting the data, training the model, testing the model, and any other section you see suitable.
                    finale regenerate the code in clean code?
                    """ )
        text_generated = llm(Descreption)
        st.markdown(
             f'''
             <div style="border: 3px solid #2fe738; padding: 10px;background-color: #000; color: white; padding: 10px;border-radius: 10px;font-size: 20px;">
             {text_generated}
             </div>
             ''', unsafe_allow_html=True
        ) 
        
    else:
        st.error("error : You Shoud fill blank felds")

