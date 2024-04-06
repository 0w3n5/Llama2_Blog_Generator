import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,blog_style):

    ###LLama2 model
    llm=CTransformers(model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ##prompt template

    template="""
        Write a blog for aimed at {blog_style} for a topic
        {input_text} within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                          template=template)

    ##generate the response from the llama2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return(response)



st.set_page_config(page_title="Generate Blogs",
                   page_icon='',
                   layout="centered",
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs")

input_text=st.text_input("Enter the blog topic")

## creating 2 more collumns for 2 more fields

coll,coll2=st.columns([5,5])

with coll:
    no_words=st.text_input("No of words")
with coll2:
    blog_style=st.selectbox("Writing the blog for ", ("Researchers", "Data Scientists", "Everyone"),index=0)

submit=st.button("Generate")

##final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))