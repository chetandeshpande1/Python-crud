from flask import Flask, request, jsonify, abort
import json
import os

app = Flask(__name__)

# Define the path to the JSON file
DATA_FILE = 'contacts.json'

# Helper function to read data from the JSON file
def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Helper function to write data to the JSON file
def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Create a new contact
@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    contacts = read_data()
    
    # Assign an ID to the new contact
    new_contact_id = max([contact['id'] for contact in contacts], default=0) + 1
    new_contact = {
        'id': new_contact_id,
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone']
    }
    
    contacts.append(new_contact)
    write_data(contacts)
    return jsonify(new_contact), 201

# Read all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = read_data()
    return jsonify(contacts), 200

# Read a single contact by ID
@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contacts = read_data()
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if contact is None:
        return jsonify({'error': 'Contact not found'}), 404
    return jsonify(contact), 200

# Update a contact by ID
@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contacts = read_data()
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if contact is None:
        return jsonify({'error': 'Contact not found'}), 404
    
    data = request.json
    contact['name'] = data.get('name', contact['name'])
    contact['email'] = data.get('email', contact['email'])
    contact['phone'] = data.get('phone', contact['phone'])
    
    write_data(contacts)
    return jsonify(contact), 200

# Delete a contact by ID
@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contacts = read_data()
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if contact is None:
        return jsonify({'error': 'Contact not found'}), 404
    
    contacts = [c for c in contacts if c['id'] != contact_id]
    write_data(contacts)
    return jsonify({'result': 'Contact deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
