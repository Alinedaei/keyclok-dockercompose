import requests

# Configuration
KEYCLOAK_URL = "http://kiclocktest.com:8080/auth"  # Correct base URL
REALM = "master"  # Replace with your actual realm name
CLIENT_ID = "sso"  # Replace with your actual client ID
CLIENT_SECRET = "vYUlC5hXnXp0RISx5N2PXyyF62SqDVtH"  # Include this if the client is confidential
USERNAME = "admin"  # Replace with your actual username
PASSWORD = "admin"  # Replace with your actual password

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
