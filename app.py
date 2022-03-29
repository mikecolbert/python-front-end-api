from flask import Flask, render_template
import urllib.request as request
import json
import ssl
import os

app = Flask(__name__)

api_key = os.environ.get("TMDB_API_KEY")
print(api_key)
url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(api_key)

@app.route("/")
def home():
    ssl._create_default_https_context = ssl._create_unverified_context
    response = request.urlopen(url)
    data = response.read()
    json_data = json.loads(data)

    return render_template ("index.html", data=json_data["results"])

if __name__ == '__main__':
    app.run(debug=True)