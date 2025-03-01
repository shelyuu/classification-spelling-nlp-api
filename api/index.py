from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
parent_directory = os.getcwd()
sys.path.insert(1, parent_directory)
sys.path.insert(2, parent_directory + "\\utils")
from utils import cryto, data, enums, processwords
from utils.enums import WordType
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Read allowed origins from environment variables
allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(',')

# CORS setup based on environment variables
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

@app.route('/')
def home():
    return 'Welcome to Spelling NLP API!'

@app.route('/api/checksentence', methods=['POST'])
def check_sentence():
    try:
        post_data = request.form
        code = 200

        # Checking if the POST vars are well provided, Exit if there is one missing
        required_fields = ["id","type"]
        if any(field not in post_data for field in required_fields):
            output = {'type': 'error', 'text': 'data is invalid.'}
            code = 422
            exit
            
        # Retrieve the word_id from the form data
        word_id = post_data.get("id", "")
        word_type = post_data.get("type", "")
        
        # Your existing code for processing the form data goes here
        if word_type.__eq__(MessageType.EMAIL.value):
            
            #TODO: Validation method
            # Checking if the POST vars are well provided, Exit if there is one missing
            required_fields_string = post_data.get("required_fields", "")
            required_fields = required_fields_string.split(",") if required_fields_string else []

            if any(field not in post_data for field in required_fields):
                output = {'type': 'error', 'text': 'Input fields are empty!'}
                code = 422
                
            # Anti-spam field, if the field is not empty, submission will not be proceeded.
            if post_data.get("userChecking"):
                output = {'type': 'error', 'text': 'We have received your submission'}
                code = 422
                exit

            if not post_data["Data"]:
                output = {'type': 'error', 'text': 'Data not found.'}
                code = 422
                exit
                
            # Validation for the fields required
            if len(post_data["Data"]) == 0:
                output = {'type': 'error', 'text': 'Data is too short or not specified.'}
                code = 422
                exit
                
            #TODO: Sanitation method
                
            # Proceed
            try:
                #TODO: Process with Model
                
                
                output = {'type': 'message', 'text': 'Your message has been sent, we will get back to you asap!'}
                code = 200
            except Exception as e:
                output = {'type': 'error', 'text': f'Oops! Something went wrong: {str(e)}'}
                code = 500

        response = output
        return jsonify(response), code
    except Exception as e:
        response = {'type': 'error', 'text': f'Oops! Something went wrong: {str(e)}'}
        return jsonify(response), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Replace with your desired host and port
