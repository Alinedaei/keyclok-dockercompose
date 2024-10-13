import requests

# Configuration
KEYCLOAK_URL = "http://keyclocktest.com:8080"  # Using the Docker service name
REALM = "master"  # Replace with your actual realm name
CLIENT_ID = "sso"  # Replace with your actual client ID
CLIENT_SECRET = "eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlMGM0MjdlZS0yOWFhLTRmYzUtYTRiZS05ZWU2YmVkMTA0MDIifQ.eyJleHAiOjE3NjAzMzg2NTksImlhdCI6MTcyODgwMjY1OSwianRpIjoiYzkxN2M1ZDMtMzg0MS00MmYyLThmYTYtYjUzOTljMTRiYmY4IiwiaXNzIjoiaHR0cDovL2tleWNsb2NrdGVzdC5jb206ODA4MC9yZWFsbXMvbWFzdGVyIiwiYXVkIjoiaHR0cDovL2tleWNsb2NrdGVzdC5jb206ODA4MC9yZWFsbXMvbWFzdGVyIiwidHlwIjoiSW5pdGlhbEFjY2Vzc1Rva2VuIn0.thzbpnfqBhuLqaJufj9m1TwWw0R1d4McHTet1mkLRSAP4NiWueMsLeKyrDNL40uRaxtOQH7ItprHoZ56YVky1w"  # Include this if the client is confidential
USERNAME = "ali"  # Replace with your actual username
PASSWORD = "7676"  # Replace with your actual password

# Token request
token_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token"
data = {
    "client_id": CLIENT_ID,
    "username": USERNAME,
    "password": PASSWORD,
    "grant_type": "password"
}

# Include client secret if the client is confidential
if CLIENT_SECRET:
    data["client_secret"] = CLIENT_SECRET

response = requests.post(token_url, data=data)

if response.status_code == 200:
    print("Token obtained:", response.json())
else:
    print("Failed to obtain token:", response.status_code, response.json())
