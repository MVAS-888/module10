import re

def last_three_letters(sentence: str):
    words = sentence.split()
    result = [word[-3:] if len(word) >= 3 else word for word in words]
    print(" ".join(result))

def analyze_text(text: str):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(unique_words)}")
    print("Unique words list:", ", ".join(sorted(unique_words)))

def extract_student_info(text: str):
    patterns = {
        "name": re.search(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', text),
        "birth_date": re.search(r'\b\d{2}[./-]\d{2}[./-]\d{4}\b', text),
        "email": re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text),
        "feedback": re.search(r'\bFeedback: (.+)', text)
    }
    
    extracted_info = {key: (match.group(0) if match else "Not found") for key, match in patterns.items()}
    return extracted_info

sentence = input("Enter a sentence: ")
last_three_letters(sentence)

text = input("Enter text for analysis: ")
analyze_text(text)

student_text = input("Enter student information: ")
print(extract_student_info(student_text))