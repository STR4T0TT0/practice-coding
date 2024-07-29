# Dependance : AnkiConnect plugin in your local installation
#
# 1. Open your Anki desktop application 
# 2. Go to : Tools | Add-ons | Get Add-ons
# 3. Input 2055492159 into the "Code" text box
# 4. Restart Anki 


# The requests library is used to send HTTP requests, which is necessary for communicating with the AnkiConnect API. If you don't know if the library is already install use test_library_request.py
import requests

# Set the relevant port for the AnkiConnect API
anki_connect_url = "http://localhost:8765"

# Define my payload for the API request
payload = {
    "action": "addNote",
    "version": 6,
    "params": {
        "note": {
            "deckName": "Default", # Safer option 
            "modelName": "Basic", 
            "fields": {
                "Front": "Test question A ?",       # To avoid duplicate error if multiple 
                "Back": "Write test answer A here"  # tests are needed change letter value B,C,D...
            },
            "tags": [
                "test"
            ]
        }
    }
}

response = requests.post(anki_connect_url, json=payload)

# Expected soemthing like {'result':88888888888, 'error':None}
print(response.json())

# WARNING ! Remember to delete the test / tests
# 1. Open your Anki desktop application 
# 2. Go to : Browse | Decks : Default
# 3. Select cards | right click : Notes | Delete
# 4. Sync the collection 