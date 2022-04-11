#Signing New Users
import requests

SHEETY_URL = "https://api.sheety.co/35a6ae652c21441f2472693f713b27de/flightDeals/users"

print("Welcome to Abhishek's Flight Club")
print("We find the best flight deals for you")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
confirm_email = input("Please confirm your email.\n")

if (email != confirm_email):
  print("Email mismatch!")
else:
  new_data = {
    "user": {
      "firstName": first_name,
      "lastName": last_name,
      "email": email
    }
  }
  response = requests.post(url=SHEETY_URL, json=new_data)
  if (response.status_code == 200):
    print("You are a member of the club")
  else:
    print(response.text)