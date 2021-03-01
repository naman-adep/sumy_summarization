

#Import packages
import streamlit as st 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Function for Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

#Title
st.title("Sumy Text Summarization Tool")

#Textbox
rawtext = st.text_area("Enter Text")

#Button
if st.button("Summarize"):
	summary_result = sumy_summarizer(rawtext)
	st.success(summary_result)


