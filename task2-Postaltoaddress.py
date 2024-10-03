import requests

pincode = input("Enter the pincode: ")
response = requests.get(f"https://api.postalpincode.in/pincode/{pincode}")

if response.json()[0]["Status"] == "Error":
    print("Invalid Pincode")
else:
    print(response.json()[0]["PostOffice"][0]["Name"])