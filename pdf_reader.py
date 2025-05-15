import pdfplumber

def extract_key_value_pairs(pdf_path):
    kv_pairs = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines:
                    if ":" in line:
                        parts = line.split(":", 1)
                        key = parts[0].strip()
                        value = parts[1].strip()
                        kv_pairs[key] = value
    return kv_pairs
