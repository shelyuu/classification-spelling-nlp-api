from utils.data import get_word_content
from utils.cryto import get_key, decrypt_data

# Send email using the retrieved template content
def process_words(post_data, user = None):
    
    key = get_key("secure_key")
    encrypted_message = bytes(get_key("encrypted_message"), 'utf-8')
    
    #sample usage
    words_content = get_word_content(post_data["wordId"], post_data)
    
    if words_content:
        sample_content += get_word_content("000000")[1] 

    
    decrypted_message = decrypt_data(key, encrypted_message)
    
    #TODO: Do something with the decrypted message
    
    message = sample_content + decrypted_message
    
    return message
