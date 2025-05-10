import os
import PyPDF2
import glob
import re

def sanitize_filename(filename):
    """Sanitize filename to avoid invalid characters"""
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

def extract_text_from_pdf(pdf_path, output_dir):
    """Extract text from a PDF file and save to a text file"""
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get the number of pages
            num_pages = len(pdf_reader.pages)
            
            # Extract text from PDF
            text = ""
            
            # Try to extract metadata
            metadata = pdf_reader.metadata
            if metadata:
                text += "===== PDF METADATA =====\n"
                for key in metadata:
                    if metadata[key]:
                        text += f"{key}: {metadata[key]}\n"
                text += "=======================\n\n"
            
            # Extract text from first 10 pages (for efficiency)
            max_pages = min(10, num_pages)
            text += f"===== EXTRACTED TEXT (First {max_pages} pages) =====\n"
            
            for page_num in range(max_pages):
                page = pdf_reader.pages[page_num]
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += f"--- Page {page_num + 1} ---\n"
                        text += page_text + "\n\n"
                except Exception as e:
                    text += f"Error extracting text from page {page_num + 1}: {str(e)}\n\n"
        
            # Create a sanitized output filename
            base_name = os.path.basename(pdf_path)
            base_name_no_ext = os.path.splitext(base_name)[0]
            sanitized_name = sanitize_filename(base_name_no_ext)
            
            # Save the extracted text to a file
            output_path = os.path.join(output_dir, f"{sanitized_name}.txt")
            with open(output_path, 'w', encoding='utf-8', errors='replace') as output_file:
                output_file.write(text)
                
            return f"Successfully extracted text from {base_name}"
    
    except Exception as e:
        return f"Error processing {os.path.basename(pdf_path)}: {str(e)}"

def main():
    # Define the directory containing PDF files
    pdf_dir = os.path.join(os.getcwd(), 'articles')
    
    # Create output directory for text files
    output_dir = os.path.join(os.getcwd(), 'extracted_text')
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all PDF files
    pdf_files = glob.glob(os.path.join(pdf_dir, '*.pdf'))
    
    print(f"Found {len(pdf_files)} PDF files. Starting extraction...")
    
    # Process each PDF file
    results = []
    for pdf_path in pdf_files:
        result = extract_text_from_pdf(pdf_path, output_dir)
        results.append(result)
        print(result)
    
    # Write summary to a file
    with open(os.path.join(output_dir, '_extraction_summary.txt'), 'w', encoding='utf-8') as f:
        f.write(f"Processed {len(pdf_files)} PDF files\n")
        f.write("Results:\n")
        for result in results:
            f.write(f"- {result}\n")
    
    print(f"\nExtraction complete. Text files saved to {output_dir}")

if __name__ == "__main__":
    main()