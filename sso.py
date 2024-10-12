import requests

# Configuration
KEYCLOAK_URL = "http://localhost:8080/auth"
REALM = "yourrealm"  # Replace with your actual realm name
CLIENT_ID = "your-client"  # Replace with your actual client ID
USERNAME = "some-user"  # Replace with your actual username
PASSWORD = "hardpassword"  # Replace with your actual password

# Token request
token_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token"
data = {
    "client_id": CLIENT_ID,
    "username": USERNAME,
    "password": PASSWORD,
    "grant_type": "password"
}

response = requests.post(token_url, data=data)

if response.status_code == 200:
    print("Token obtained:", response.json())
else:
    print("Failed to obtain token:", response.json())
