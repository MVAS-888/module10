import re
from collections import Counter

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    
    frequency = Counter(words)
    
    return frequency

text = "This is a test text. The text contains words, and some words repeat."
result = word_frequency(text)

for word, count in result.items():
    print(f"Word: '{word}', Frequency: {count}")