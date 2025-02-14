import re

def extract_data(input_file: str, output_file: str):
    date_pattern = re.compile(r'\b\d{2}[./-]\d{2}[./-]\d{4}\b')
    phone_pattern = re.compile(r'\+?\d{1,3}[\s-]?\(?\d{2,3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}')
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
    extracted_data = {
        "dates": [],
        "phones": [],
        "emails": []
    }
    
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            extracted_data["dates"].extend(date_pattern.findall(line))
            extracted_data["phones"].extend(phone_pattern.findall(line))
            extracted_data["emails"].extend(email_pattern.findall(line))
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Birth Dates:\n" + "\n".join(extracted_data["dates"]) + "\n\n")
        file.write("Phone Numbers:\n" + "\n".join(extracted_data["phones"]) + "\n\n")
        file.write("Email Addresses:\n" + "\n".join(extracted_data["emails"]) + "\n")

extract_data("input.txt", "output.txt")