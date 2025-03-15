from langchain.chains.summarize import load_summarize_chain
from langchain.llms import HuggingFaceHub

def summarize_articles(query, summary_type="brief"):
    retriever = vectorstore.as_retriever()
    relevant_docs = retriever.get_relevant_documents(query=query)  # Use user's query
    
    if not relevant_docs:
        return "No relevant articles found for your query."

    if summary_type == "brief":
        summarization_chain = load_summarize_chain(HuggingFaceHub(repo_id="facebook/bart-large-cnn"), chain_type="stuff")
    else:
        summarization_chain = load_summarize_chain(HuggingFaceHub(repo_id="facebook/bart-large-cnn"), chain_type="refine")
    
    summary = summarization_chain.run(relevant_docs)
    return summary
