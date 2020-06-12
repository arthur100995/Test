def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code"""
    if len(zip_code) == 5:
        prom = zip_code.isdigit()
        return prom
    return False

def word_search(doc_list, keyword):
    """ Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword."""
    for articles in doc_list:
        if keyword.lower() in articles.lower():
            return doc_list.index(articles)