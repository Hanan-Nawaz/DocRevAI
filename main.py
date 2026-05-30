from docrevai.scripts.read_docs import ReadDocs
from docrevai.scripts.clean_text import CleanText
from docrevai.scripts.create_chunks import CreateChunks

def main():
    pdf_path = "pdf/Final_Report_NUMLPay.pdf"
    readdocs = ReadDocs()
    raw_text = readdocs.read_pdf(path=pdf_path)

    cleantext = CleanText()
    clean_text = cleantext.clean_text(text=raw_text)

    createchunks = CreateChunks()
    chunks = createchunks.create_chunks(clean_text=clean_text)


if __name__ == "__main__":
    main()
