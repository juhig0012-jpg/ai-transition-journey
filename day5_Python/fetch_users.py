# fetch_users.py

import requests

# Fetch users data from API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# Convert response to JSON
users = response.json()

# Print emails
print("User Emails:")
for user in users:
    print(user["email"])

print("\nCompany Names:")
# Print company names
for user in users:
    print(user["company"]["name"])

# Find users by city
search_city = "South Christy"

print(f"\nUsers from city: {search_city}")
for user in users:
    if user["address"]["city"].lower() == search_city.lower():
        print(user["name"])