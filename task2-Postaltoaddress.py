import requests

pincode = input("Enter the pincode: ")
response = requests.get(f"https://api.postalpincode.in/pincode/{pincode}")