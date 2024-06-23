import tkinter as tk
from tkinter import scrolledtext, messagebox
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
import nltk
import requests

# Download necessary nltk data
nltk.download('punkt')

def summarize_text(text, summarizer_type='lsa', sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    if summarizer_type == 'LSA (Latent Semantic Analysis): A mathematical technique used to extract contextual information from a collection of documents.':
        summarizer = LsaSummarizer()
    elif summarizer_type == 'LexRank: A graph-based summarization algorithm that computes the centrality of sentences.':
        summarizer = LexRankSummarizer()
    elif summarizer_type == 'TextRank: Another graph-based algorithm that ranks sentences based on their similarity to other sentences.':
        summarizer = TextRankSummarizer()
    elif summarizer_type == 'Luhn Summarizer: A simple summarization technique that selects the most frequent words as keywords and extracts sentences containing these words.':
        summarizer = LuhnSummarizer()
    elif summarizer_type == 'Edmundson Summarizer: A summarization method that combines key features like location, cue words, title words, and sentence length to score and select sentences.':
        summarizer = EdmundsonSummarizer()
    else:
        raise ValueError("Unknown summarizer type")
    
    summary = summarizer(parser.document, sentence_count)
    
    return ' '.join(str(sentence) for sentence in summary)

def count_words(text):
    words = text.split()
    return len(words)

def check_plagiarism(text):
    # Mock plagiarism check using a sample API
    # Replace this with an actual plagiarism checker API
    url = "https://api.mockplagiarismchecker.com/check"
    payload = {'text': text}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to check plagiarism"

def paraphrase_text(text):
    # Mock paraphrasing using a sample API
    # Replace this with an actual paraphrasing API or library
    # This is just a placeholder function
    return "This is a paraphrased version of the text: " + text

def summarize_and_update():
    input_text = input_text_area.get("1.0", "end-1c")
    summarizer_type = summarizer_type_var.get()
    sentence_count = int(sentence_count_var.get())
    
    # Summarize the text
    summarized_text = summarize_text(input_text, summarizer_type, sentence_count)
    
    # Update the summarized text area
    summarized_text_area.delete("1.0", "end")
    summarized_text_area.insert("end", summarized_text)
    
    # Update the word count label
    word_count = count_words(input_text)
    word_count_label.config(text=f"Word Count: {word_count}")
    
    # Check plagiarism
    plagiarism_result = check_plagiarism(input_text)
    plagiarism_result_label.config(text=plagiarism_result)

def paraphrase_text_and_update():
    summarized_text = summarized_text_area.get("1.0", "end-1c")
    
    # Paraphrase the summarized text
    paraphrased_text = paraphrase_text(summarized_text)
    
    # Update the summarized text area with paraphrased text
    summarized_text_area.delete("1.0", "end")
    summarized_text_area.insert("end", paraphrased_text)

# Create the main window
root = tk.Tk()
root.title("Text Summarizer")

# Set window size to full screen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Change background and foreground colors
root.configure(bg='white')

# Create input area
input_label = tk.Label(root, text="Enter the text you want to summarize:", bg='white', fg='black')
input_label.pack(anchor='w')  # Align label to the left
input_text_area = scrolledtext.ScrolledText(root, width=root.winfo_screenwidth(), height=10, bg='white', fg='black')
input_text_area.pack()

# Create summarizer options
summarizer_type_var = tk.StringVar(value='lsa')
summarizer_type_label = tk.Label(root, text="Select Summarizer:", bg='white', fg='black')
summarizer_type_label.pack(anchor='w')  # Align label to the left
summarizer_type_options = ["Latent Semantic Analysis", "LexRank", "TextRank", "Luhn Summarizer", "Edmundson Summarizer"]
for option in summarizer_type_options:
    tk.Radiobutton(root, text=option, variable=summarizer_type_var, value=option, bg='white', fg='black').pack(anchor='w')  # Align radio buttons to the left

# Create sentence count input
sentence_count_var = tk.StringVar(value='3')
sentence_count_label = tk.Label(root, text="Enter Sentence Count:", bg='white', fg='black')
sentence_count_label.pack(anchor='w')  # Align label to the left
sentence_count_entry = tk.Entry(root, textvariable=sentence_count_var, bg='white', fg='black')
sentence_count_entry.pack()

# Create button to summarize text
summarize_button = tk.Button(root, text="Summarize", command=summarize_and_update, bg='black', fg='white')
summarize_button.pack()

# Create area to display summarized text
summarized_text_area_label = tk.Label(root, text="Summarized Text:", bg='white', fg='black')
summarized_text_area_label.pack(anchor='w')  # Align label to the left
summarized_text_area = scrolledtext.ScrolledText(root, width=root.winfo_screenwidth(), height=10, bg='white', fg='black')
summarized_text_area.pack()

# Create button to paraphrase text
paraphrase_button = tk.Button(root, text="Paraphrase", command=paraphrase_text_and_update, bg='black', fg='white')
paraphrase_button.pack()

# Create labels for word count and plagiarism result
word_count_label = tk.Label(root, text="", bg='white', fg='black')
word_count_label.pack(anchor='w')  # Align label to the left
plagiarism_result_label = tk.Label(root, text="", bg='white', fg='black')
plagiarism_result_label.pack(anchor='w')  # Align label to the left

# Run the main event loop
root.mainloop()
