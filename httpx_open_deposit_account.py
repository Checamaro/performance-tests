import httpx
import time

base_url = "http://localhost:8003/api/v1"
create_user_payload = {
    "email": f"user{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post(f"{base_url}/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Create user response:", create_user_response_data)
print("Status Code:", create_user_response.status_code)

create_account_payload = {
    "userId": create_user_response_data['user']['id']
}

create_account_response = httpx.post(
    f"{base_url}/accounts/open-deposit-account", json=create_account_payload)
create_account_response_data = create_account_response.json()

print("Create account response:", create_account_response_data)
print("Status Code:", create_account_response.status_code)
