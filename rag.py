from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from uuid import uuid4
from pathlib import Path
import os

# loading dotenv module :
load_dotenv()

path = Path(__file__).parent / "research_data"

llm = None
vector_data = None
temp = 0.2

print("component intializing")
def initialize_components(temp):
    global llm,vector_data
    if llm == None:
        # langchain model
        llm = ChatGroq(model = "openai/gpt-oss-120b",temperature= temp)
    if vector_data == None:
        # vector database initialization
        emb_fun = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        vector_data = Chroma(collection_name="Real_estate_data",
        embedding_function = emb_fun,
        persist_directory = str(path))




# url processing
def process_urls(urls,temp):
    yield "intializing components..."
    initialize_components(temp)

    yield "Vector DataBase is Ready for Mission"
    vector_data.reset_collection()

    yield "Data is Loading ...."
    loader = UnstructuredURLLoader(urls=urls)

    data = loader.load()

    # data splitting into chunks :
    yield "Data Splitting into Chunks...."
    splitter = RecursiveCharacterTextSplitter(separators=["\n\n","\n",". "," ",""],
    chunk_size = 200,
    chunk_overlap =  20,
    length_function = len
    )

    doc = splitter.split_documents(data)

    # data added to vector database :
    uuids = [str(uuid4()) for _ in range(len(doc))]
    vector_data.add_documents(doc,ids = uuids)

    yield "Data is Added Successfully in Vector DataBase, and Ready for Your Questions."


# generation answer
def generate_answer(query):
    if not vector_data:
        raise RunTimeError("The Vector Data Not Found")
    retriever = vector_data.as_retriever(search_kwargs = {"k":2})

    docs = retriever.invoke(query)
    for doc in docs:
        llm_sources = doc.metadata.get("source")

    chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, retriever = retriever)

    chain_output = chain.invoke({"question":query})

    return chain_output["answer"],llm_sources



if __name__ == '__main__':
    print('Real Estate Ressearch is Processing..........')

    urls = [
        "https://www.cbre.co.in/insights/figures/india-market-monitor-q2-2026-retail"
    ]

    process_urls(urls)

    answer,sources = generate_answer("Tell me what is the high Demand led cities.")

    print(f"answer :{answer}")
    print(f"sources : {sources}")






