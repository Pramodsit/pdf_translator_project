from src.batch_processor import process_pdf_folder

if __name__ == "__main__":
    input_folder = "sample_pdfs"
    output_file = "sample_output/sample_output.xlsx"
    process_pdf_folder(input_folder, output_file)
