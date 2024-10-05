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

if __name__ == '__main__':
    app.run(debug=True)