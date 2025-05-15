from fpdf import FPDF
import os

# Create sample structured (text-based) PDFs
sample_folder = "sample_pdfs"
os.makedirs(sample_folder, exist_ok=True)

sample_data = [
    {
        "Name": "Ajay Cyril",
        "Date of Birth": "12-12-1990",
        "Occupation": "Software Architect",
        "Country": "France"
    },
    {
        "Nom": "Jean Dupont",
        "Date de naissance": "23 mars 1985",
        "Profession": "Ingénieur logiciel",
        "Pays": "France"
    },
    {
        "Nombre": "Carlos Rivera",
        "Fecha de nacimiento": "10 abril 1982",
        "Ocupación": "Desarrollador de software",
        "País": "México"
    }
]

# Generate 10 PDFs
for i in range(10):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    person = sample_data[i % len(sample_data)]
    for key, value in person.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.output(f"{sample_folder}/sample{i+1}.pdf")
