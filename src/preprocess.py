import nltk

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def get_tokens(input_txt):
    text_lower = input_txt.lower()
    tokens = nltk.word_tokenize(text_lower)
    return tokens
def get_tags(input_txt):
    tag_set = nltk.pos_tag(get_tokens(input_txt))
    return tag_set