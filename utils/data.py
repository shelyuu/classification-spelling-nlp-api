import csv

# Load data from CSV file into a dictionary
def load_data():
    templates = {}
    with open('./utils/data/data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word_id = row.get('word_id')
            word_title = row.get('word_title')
            word_content = row.get('word_content')
            if word_id and word_content:
                templates[word_id] = [word_title,word_content]
    return templates

# Retrieve content based on word_id
def get_word_content(word_id, post_data = None):
    words = load_data()
    word = words.get(word_id, '')
    
    if post_data is None:
        word_title = word[0]
        word_content = word[1].format(
        word_title=word_title)
    else:
        word_title = word[0].format(**post_data)
        word_content = word[1].format(word_title=word_title, **post_data)

    return word_title,word_content
    

# # Example usage
# if __name__ == "__main__":
#     words = load_data()
#     word_content = words.get('195637', '')
#     print(f"words: {word_content}")
#     # print(f"words: {words}")
