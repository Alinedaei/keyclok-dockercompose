import requests

# Configuration
KEYCLOAK_URL = "http://localhost:8080"  # Adjust if necessary
REALM = "master"
CLIENT_ID = "ali"
CLIENT_SECRET = "your_client_secret"  # Ensure this is correct
USERNAME = "admin"
PASSWORD = "admin"

# Token request
token_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token"
data = {
    "client_id": CLIENT_ID,
    "username": USERNAME,
    "password": PASSWORD,
    "grant_type": "password"
}

if CLIENT_SECRET:
    data["client_secret"] = CLIENT_SECRET

try:
    print("Sending request to:", token_url)  # Debugging line
    response = requests.post(token_url, data=data, timeout=10)

    if response.status_code == 200:
        print("Token obtained:", response.json())
    else:
        print("Failed to obtain token:", response.status_code, response.json())
except requests.exceptions.RequestException as e:
    print("Error during request:", e)
