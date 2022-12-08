from flask import Flask, jsonify, request
from data_fetcher import scrap



app = Flask(__name__)

@app.route('/')
def test():
 return 'paste a url to get the data'

@app.route("/<path:url>")
def get_data(url):
 new_url = request.full_path
 result = scrap(new_url[1:])
 return jsonify(result)




if __name__ == '__main__':
 app.run(debug=True)