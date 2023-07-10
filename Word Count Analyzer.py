import string
from collections import Counter
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    return text

def analyze_word_count(text):
    # Preprocess the text
    cleaned_text = preprocess_text(text)
    
    # Split the text into individual words
    words = cleaned_text.split()
    
    # Count the occurrence of each word
    word_count = Counter(words)
    
    # Calculate total words and unique words
    total_words = len(words)
    unique_words = len(word_count)
    
    return word_count, total_words, unique_words

def display_word_count(word_count, total_words, unique_words, num_top_words=10):
    output_window = tk.Toplevel()
    output_window.title("71's Output Frame")
    
    output_label = tk.Label(output_window, text="Word Count Analysis:")
    output_label.pack()
    
    total_words_label = tk.Label(output_window, text="Total Words: " + str(total_words))
    total_words_label.pack()
    
    unique_words_label = tk.Label(output_window, text="Unique Words: " + str(unique_words))
    unique_words_label.pack()
    
    top_words_label = tk.Label(output_window, text="Top " + str(num_top_words) + " Most Frequent Words:")
    top_words_label.pack()
    
    # Display the most frequent words
    top_words = word_count.most_common(num_top_words)
    for word, count in top_words:
        word_label = tk.Label(output_window, text=word + " : " + str(count))
        word_label.pack()

def upload_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "r") as file:
            article = file.read()
            word_count, total_words, unique_words = analyze_word_count(article)
            display_word_count(word_count, total_words, unique_words)

# Create Tkinter window
window = tk.Tk()
window.title("Word Count Analyzer")
window.geometry("300x100")

# Create "Upload" button
upload_button = tk.Button(window, text="Upload Article", command=upload_file)
upload_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
