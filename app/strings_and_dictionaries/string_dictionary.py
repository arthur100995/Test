def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code"""
    if len(zip_code) == 5:
        prom = zip_code.isdigit()
        return prom
    return False

def word_search(doc_list, keyword):
    """Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword."""
    indices = []
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


def multi_word_search(doc_list, keywords):
    """Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword"""
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices



