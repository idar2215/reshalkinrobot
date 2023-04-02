import openai
import requests
import base64
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# Authenticate with OpenAI API
openai.api_key = os.getenv('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')
class GPT:
    def __init__(self):
        # Set up OpenAI engine
        self.engine = "davinci"
        # Set up OpenAI model
        self.model = "text-davinci-002"
        # Set up OpenAI prompt
        self.prompt = "Answer the following question:\n{}\n\nAnswer:"
    def extract_text_from_image(self, filename):
        # Encode image as base64
        with open(filename, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        # Make request to OpenAI API
        response = openai.Completion.create(
            engine=self.engine,
            prompt="Recognize text from the following image:\n\n![image]({})".format(encoded_image),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # Get text from response
        text = response.choices[0].text.strip()
        return text
    def answer_question(self, question):
        # Make request to OpenAI API
        response = openai.Completion.create(
            engine=self.engine,
            model=self.model,
            prompt=self.prompt.format(question),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # Get answer from response
        answer = response.choices[0].text.strip()
        return answer
