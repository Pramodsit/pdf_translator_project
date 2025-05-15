# PDF Translator Project

A Python-based project that extracts text from PDF documents, translates it to English (if needed), identifies key-value pairs, and exports the structured information into an Excel file.

---

## 📁 Project Structure

pdf_translator_project/
│
├── generate_pdfs.py # Script to generate sample PDFs with multilingual content
├── main.py # Main script to extract, translate, and export PDF content
├── requirements.txt # List of dependencies
│
├── sample_pdfs/ # Folder containing generated sample PDFs
├── sample_output/ # Folder containing translated Excel output
└── translated_output.xlsx # Final structured Excel file


---

## ⚙️ Features

- Generates multilingual sample PDF documents (e.g., French, Spanish).
- Extracts text from PDFs using PyMuPDF.
- Translates non-English content to English using MarianMT (Hugging Face model).
- Uses regular expressions to detect and extract structured data (key-value pairs).
- Saves the extracted and translated data into an Excel spreadsheet.

---

## 🧰 Requirements

Ensure Python 3.8+ is installed. Then install dependencies:


pip install -r requirements.txt


If fpdf or sacremoses gives errors, install them manually:

pip install fpdf
pip install sacremoses



🚀 How to Run
Step 1: Generate Sample PDFs
To create multilingual PDF files, run:


python generate_pdfs.py
This will generate 10 sample PDFs in the sample_pdfs/ folder.

Step 2: Process PDFs and Export Translations
Run the main processing script:


python main.py
This will:

Read all PDFs from the sample_pdfs/ folder

Translate them to English (if needed)

Extract key-value data

Write the results to an Excel file at sample_output/translated_output.xlsx

📦 Output
You will find a structured Excel file with columns:

File Name

Key

Value

Located at:

makefile
Copy code
E:\pdf_translator_project\sample_output\translated_output.xlsx


📚 Technologies Used
Python

PyMuPDF

FPDF

Hugging Face Transformers

MarianMT Translation Model

OpenPyXL (for writing Excel files)

✅ Sample Use Cases
Extracting multilingual resumes or documents

Translating forms or scanned documents

Creating structured data from unstructured PDFs