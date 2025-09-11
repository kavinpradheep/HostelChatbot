import os
from dotenv import load_dotenv
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Hostel Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Hostel Chatbot")
st.write("Ask questions about the hostel rules and SOP.")

PDF_PATH = "HostelSOP R1.pdf"

# 1. Load and split PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
documents = splitter.split_documents(docs)

# 2. Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(documents, embeddings, persist_directory="hostel_db")

# 3. Setup LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=API_KEY
)

# 4. Similarity search function
def answer_with_similarity(query, top_k=5):
    similar_docs = vectorstore.similarity_search(query, k=top_k)
    context = "\n\n".join([doc.page_content for doc in similar_docs])
    prompt = f"Answer the question based on the following hostel rules:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    response = llm.invoke(prompt)
    return response.content

# 5. Chat interface
query = st.text_input("Enter your question here:")

if query:
    with st.spinner("🤖 Thinking..."):
        answer = answer_with_similarity(query)
    st.markdown(f"**Bot:** {answer}")
