### This script requires a file location to a PDF 
### The script will convert the PDF into one or more TXT files, each file containing an amount of text that Chat GPT can ingest at one time (~30,000 characters)

import PyPDF2
import os

def pdf_to_text(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        file_index = 1  # To keep track of the output file index
        char_count = 0  # To keep track of the character count in the current output file
        file_path = f'{txt_path}_{file_index}.txt'  # Initialize the file_path with a default value

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            if char_count + len(text) > 30000:
                # Create a new output file
                file_index += 1
                file_path = f'{txt_path}_{file_index}.txt'
                char_count = 0

            with open(file_path, 'a', encoding='utf-8') as txt_file:
                txt_file.write(text)
                char_count += len(text)

pdf_path = r'C:\Users\...\File.pdf'  # Replace with the path to your input PDF file
txt_directory = r'C:\Users\...\Folder'  # Replace with the directory where you want to save the output text files
txt_filename = 'New Folder'  # Replace with the desired filename for the output text files

# Check if the output directory exists, if not, create it
output_directory = os.path.join(txt_directory, txt_filename)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

txt_path = os.path.join(output_directory, txt_filename)  # Complete the txt_path with the full file path
pdf_to_text(pdf_path, txt_path)
print('PDF converted to text successfully!')
