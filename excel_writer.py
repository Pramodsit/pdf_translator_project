from openpyxl import Workbook

def write_to_excel(kv_data_list, output_path):
    wb = Workbook()
    ws = wb.active
    ws.append(["File Name", "Key", "Value"])

    for file_name, kv_pairs in kv_data_list:
        for key, value in kv_pairs.items():
            ws.append([file_name, key, value])

    wb.save(output_path)
