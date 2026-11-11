from app.core.database import get_vector_collection

def search_catalog(query, n_results = 3, filter_dict = None):
    collection = get_vector_collection()
    results = collection.query(query_texts = [query], n_results = n_results, where=filter_dict)
    return results

def build_prompt(user_query, search_results):
    retrieved_docs = search_results['documents'][0]
    context_string = "\n---\n".join(retrieved_docs)
    final_prompt = f"""You are a helpful assistant. Answer the question based on the provided context. If the answer is not strictly in the context, say you do not know. Do not invent information
                        Question:{user_query}
                        Context:{context_string}
                        """

    return final_prompt

