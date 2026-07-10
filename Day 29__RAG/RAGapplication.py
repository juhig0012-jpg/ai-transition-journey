# ---------------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------------

# Loads PDF documents.
from langchain_community.document_loaders import PyPDFLoader

# Splits large documents into smaller chunks.
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Creates sentence embeddings using Hugging Face models.
from langchain_huggingface import HuggingFaceEmbeddings

# FAISS is a vector database used to store embeddings.
from langchain_community.vectorstores import FAISS

# Loads GPT-2 tokenizer.
from transformers import AutoTokenizer

# Loads GPT-2 language model.
from transformers import AutoModelForCausalLM

# PyTorch library.
import torch



# ---------------------------------------------------------
# STEP 1 : LOAD PDF
# ---------------------------------------------------------

# Path to your PDF file.
pdf_path = "sample.pdf"

# Create a PDF loader object.
loader = PyPDFLoader(pdf_path)

# Read every page from the PDF.
#
# Output:
# List of Document objects.
#
documents = loader.load()

print("Pages Loaded:", len(documents))



# ---------------------------------------------------------
# STEP 2 : SPLIT PDF INTO CHUNKS
# ---------------------------------------------------------

# Large PDFs cannot fit into the LLM context.
#
# So split the PDF into small overlapping chunks.
#
splitter = RecursiveCharacterTextSplitter(

    # Maximum characters in one chunk.
    chunk_size=500,

    # Number of overlapping characters.
    #
    # Helps preserve context.
    #
    chunk_overlap=100
)

# Split the PDF.
chunks = splitter.split_documents(documents)

print("Chunks:", len(chunks))



# ---------------------------------------------------------
# STEP 3 : CREATE EMBEDDING MODEL
# ---------------------------------------------------------

# Load a sentence transformer model.
#
# This model converts text
# into numerical vectors.
#
embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)



# ---------------------------------------------------------
# STEP 4 : CREATE VECTOR DATABASE
# ---------------------------------------------------------

# Convert every chunk into an embedding.
#
# Store embeddings inside FAISS.
#
vector_db = FAISS.from_documents(

    chunks,

    embedding_model
)

print("Vector database created.")



# ---------------------------------------------------------
# STEP 5 : CREATE RETRIEVER
# ---------------------------------------------------------

# Retriever searches the vector database.
#
# It returns the most relevant chunks.
#
retriever = vector_db.as_retriever(

    search_kwargs={

        # Return top 3 chunks.
        "k":3
    }
)



# ---------------------------------------------------------
# STEP 6 : LOAD GPT-2
# ---------------------------------------------------------

# Load tokenizer.
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Load GPT-2.
model = AutoModelForCausalLM.from_pretrained("gpt2")



# ---------------------------------------------------------
# STEP 7 : ASK QUESTION
# ---------------------------------------------------------

# User question.
question = input("Ask a question: ")



# ---------------------------------------------------------
# STEP 8 : SEARCH VECTOR DATABASE
# ---------------------------------------------------------

# Find the most relevant chunks.
docs = retriever.invoke(question)



# ---------------------------------------------------------
# STEP 9 : BUILD CONTEXT
# ---------------------------------------------------------

# Combine retrieved chunks into one string.
#
context = "\n\n".join(

    doc.page_content

    for doc in docs
)



# ---------------------------------------------------------
# STEP 10 : CREATE PROMPT
# ---------------------------------------------------------

# Give GPT-2 both:
#
# Context
#
# Question
#
prompt = f"""
Answer the question using only the context below.

Context:

{context}

Question:

{question}

Answer:
"""



# ---------------------------------------------------------
# STEP 11 : TOKENIZE PROMPT
# ---------------------------------------------------------

# Convert prompt into token IDs.
inputs = tokenizer(

    prompt,

    return_tensors="pt"
)



# ---------------------------------------------------------
# STEP 12 : GENERATE ANSWER
# ---------------------------------------------------------

# GPT predicts one token at a time.
#
output = model.generate(

    inputs["input_ids"],

    max_new_tokens=100,

    temperature=0.7,

    top_p=0.9,

    do_sample=True
)



# ---------------------------------------------------------
# STEP 13 : CONVERT TOKENS TO TEXT
# ---------------------------------------------------------

answer = tokenizer.decode(

    output[0],

    skip_special_tokens=True
)



# ---------------------------------------------------------
# STEP 14 : PRINT ANSWER
# ---------------------------------------------------------

print("\nAnswer:\n")

print(answer)