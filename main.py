from docrevai.scripts.read_docs import ReadDocs
from docrevai.scripts.clean_text import CleanText
from docrevai.scripts.create_chunks import CreateChunks
from docrevai.scripts.similarity_finder import SimilarityFinder
from docrevai.scripts.ask_ai import AskAI

def main():
    pdf_path = "pdf/Final_Report_NUMLPay.pdf"
    readdocs = ReadDocs()
    raw_text = readdocs.read_pdf(path=pdf_path)

    cleantext = CleanText()
    clean_text = cleantext.clean_text(text=raw_text)

    createchunks = CreateChunks()
    chunks = createchunks.create_chunks(clean_text=clean_text)

    question = input(f"Please Ask question Related to {pdf_path}: ")

    similarityfinder = SimilarityFinder()
    context = similarityfinder.similarity_finder(question=question, chunks=chunks)

    askai = AskAI()
    answer = askai.ask_ai(question=question, context=context)

    print("---------------------")
    print("Here is the answer:  ")
    print("---------------------")
    print(answer)

if __name__ == "__main__":
    main()
