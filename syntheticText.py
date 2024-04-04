import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from textblob import TextBlob
import random

# Download NLTK data if not downloaded
nltk.download('punkt')
nltk.download('wordnet')

def synonym_replacement(text, n=2):
    words = word_tokenize(text)
    words_synonyms = words.copy()

    for _ in range(n):
        for i, word in enumerate(words):
            if random.random() < 0.2:  # Randomly select 20% of the words
                syns = wordnet.synsets(word)
                if syns:
                    synonym = random.choice(syns).lemmas()[0].name()
                    words_synonyms[i] = synonym

    return ' '.join(words_synonyms)

def text_variation(text):
    # Example: synonym replacement
    return synonym_replacement(text)

if __name__ == "__main__":
    input_file_path = "LHTest.txt"  # Path to the input file
    output_folder = "output_variants"  # Folder to store output files

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()

    print("Original Text:")
    print(input_text)

    print("\nVariants:")
    for i in range(10000):  # Generate 5 variants
        variant_text = text_variation(input_text)
        output_file_path = os.path.join(output_folder, f"LH{i+1}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(variant_text)
        print(f"Variant {i+1} written to: {output_file_path}")
