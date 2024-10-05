from flask import Flask ,render_template ,request , redirect , url_for
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cat")
def cat():
    url = "https://api.thecatapi.com/v1/images/search"
    res = requests.get(url)
    data = res.json()[0]['url']
    print(res.json())
    return render_template("cat.html", data = data)

@app.route("/dog")
def dog():
    url = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(url)
    data = res.json()['message']
    return render_template("dog.html", data = data)

@app.route("/pincode" , methods = ["GET" , "POST"])
def pincode():
    if request.method == "POST":
        pincode = request.form.get("pincode")
        return redirect(url_for('results', pincode=pincode))
    return render_template("pincode.html")

@app.route("/results" , methods = ["GET"])
def results():
    pincode = request.args.get("pincode")
    res = requests.get(f"https://api.postalpincode.in/pincode/{pincode}")
    data = res.json()
    print("This is data parrrttt", data)
    if data[0]['Status'] == "404":
        url = "https://api.thecatapi.com/v1/images/search"
        res = requests.get(url)
        date = res.json()[0]['url']
        return render_template("error.html" , date = date)
    else:
        address = data[0]["PostOffice"][0]["Name"]
        print("This is the address", address)
        return render_template("results.html" , address = address)  

if __name__ == '__main__':
    app.run(debug=True)