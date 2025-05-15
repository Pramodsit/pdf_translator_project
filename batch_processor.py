import os
from .pdf_reader import extract_key_value_pairs
from .translate import translate_kv_pairs
from .excel_writer import write_to_excel

def process_pdf_folder(input_folder, output_file):
    kv_data_list = []
    for file in os.listdir(input_folder):
        if file.lower().endswith(".pdf"):
            path = os.path.join(input_folder, file)
            kv = extract_key_value_pairs(path)
            translated = translate_kv_pairs(kv)
            kv_data_list.append((file, translated))
    write_to_excel(kv_data_list, output_file)
