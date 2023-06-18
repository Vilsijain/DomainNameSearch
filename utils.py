from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set up your OpenAI API credentials
openai.api_key = os.environ.get('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')

# Function to generate domain name suggestions
def generate_domain_suggestions(keyword):
    # Define your prompt to ChatGPT
    prompt = f"Generate domain name suggestions for '{keyword}'."

    # Generate a response from ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=5,  # Number of suggestions to generate
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract the generated suggestions from the response
    suggestions = response.choices[0].text.strip().split('\n')

    return suggestions

# API endpoint to handle domain name suggestions
@app.route('/suggest', methods=['POST'])
def suggest_domain_names():
    data = request.get_json()

    # Extract the keyword from the request data
    keyword = data['keyword']

    # Generate domain name suggestions
    suggestions = generate_domain_suggestions(keyword)

    # Return the suggestions as a JSON response
    return jsonify(suggestions)

# Run the Flask app
if __name__ == '__main__':
    app.run()
