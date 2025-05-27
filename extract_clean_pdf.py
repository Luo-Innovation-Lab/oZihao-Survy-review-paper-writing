import os
import re
import sys
try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF is not installed. Installing now...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyMuPDF"])
    import fitz

def clean_text(text):
    """
    Clean extracted text by removing common header/footer patterns and formatting artifacts
    """
    # Remove page numbers (various formats)
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    
    # Remove common journal footers
    text = re.sub(r'©.*?reserved\.', '', text)
    text = re.sub(r'©.*?[0-9]{4}', '', text)
    
    # Remove headers that contain journal names, dates, etc.
    text = re.sub(r'\n.*?(Journal|Vol|Volume|Issue|Page).*?\n', '\n', text)
    
    # Remove URLs and DOIs
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'doi:.*?\s', '', text)
    
    # Remove excessive whitespace
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    
    # Remove common separators
    text = re.sub(r'-{3,}', '', text)
    
    # Remove page headers/footers with FHJ format
    text = re.sub(r'FHJv\d+n\d+-\w+\.indd\s+\d+.*?\d+/\d+/\d+\s+\d+:\d+\s+[AP]M', '', text)
    
    # Additional cleaning
    # Remove abstract, keywords labels
    text = re.sub(r'ABSTRACT', '', text)
    text = re.sub(r'KEYWORDS\s*:', '', text)
    
    # Remove specific journal formatting
    text = re.sub(r'FUTURE', '', text)
    text = re.sub(r'DIGITAL TECHNOLOGY', '', text)
    
    # Remove email addresses
    text = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', text)
    
    # Remove extra spacing at beginning of lines
    text = re.sub(r'\n\s+', '\n', text)
    
    # Remove references section if possible
    if 'References' in text:
        text = text.split('References')[0]
    
    return text.strip()

def extract_pdf_text(pdf_path, output_path=None):
    """
    Extract text from a PDF file, clean it, and save to a text file
    """
    try:
        # Open the PDF
        doc = fitz.open(pdf_path)
        text = ""
        
        # Extract text from each page
        for page in doc:
            text += page.get_text() + '\n\n'
        
        # Clean the extracted text
        cleaned_text = clean_text(text)
        
        # If no output path is specified, use the PDF path with .txt extension
        if not output_path:
            output_path = os.path.splitext(pdf_path)[0] + ".txt"
        
        # Write the cleaned text to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)
            
        print(f"Successfully extracted and cleaned text from {pdf_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return False

def process_directory(directory):
    """
    Process all PDF files in a directory
    """
    pdf_count = 0
    success_count = 0
    
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            pdf_count += 1
            if extract_pdf_text(pdf_path):
                success_count += 1
    
    print(f"Processed {pdf_count} PDF files. Successfully extracted {success_count} files.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isdir(target):
            process_directory(target)
        elif os.path.isfile(target) and target.lower().endswith('.pdf'):
            extract_pdf_text(target)
        else:
            print(f"Invalid target: {target}")
    else:
        print("Please provide a PDF file or directory path as an argument.")