from pypdf import PdfReader

def format_text(text):
    """Formats the text by placing a space after each capital letter"""
    formatted_text = ""
    for letter in text:
        if letter.isupper():
            formatted_text += " "
        formatted_text += letter
    return formatted_text

def pdf_to_text(pdf_path):
    """Extracts the text of a pdf file"""
    reader = PdfReader(pdf_path)
    pdf_text = ""
    for i in range(0, len(reader.pages)-1):    
        pdf_text += format_text(reader.pages[i].extract_text())
    return pdf_text

print(pdf_to_text("erstes-semester/grundlagen-der-programmierung/projekt/05_data_structures.pdf"))





