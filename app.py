import json
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# Path to the JSON file where contact data will be saved
CONTACT_DATA_FILE = 'contact_data.json'
# Function to load existing contact data from the JSON file
def load_contact_data():
    try:
        with open(CONTACT_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
# Function to save contact data to the JSON file
def save_contact_data(data):
    with open(CONTACT_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    data = request.get_json()  # Get JSON data from AJAX request
    name = data.get('name')
    email = data.get('email')
    favorite_painting = data.get('favorite_painting')
    # Load existing contact data
    contact_data = load_contact_data()
    # Append new contact data
    contact_data.append({
        "name": name,
        "email": email,
        "favorite_painting": favorite_painting
    })
    # Save the updated contact data back to the JSON file
    save_contact_data(contact_data)
    # Print the received data for debugging
    print(f"Received - Name: {name}, Email: {email}, Favorite Painting: {favorite_painting}")
    response = {"message": f"Thank you!  {name}! Your submission was received.", "status": "success" }
    return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True)

