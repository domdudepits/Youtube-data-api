from flask import Flask, jsonify, request
from data_fetcher import scrap
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Data(Resource):
  def get(self, url):
    new_url = request.full_path
    result = scrap(new_url[1:])
    return jsonify(result)
    return result

    

api.add_resource(Data, '/<path:url>', methods=['GET'])


@app.route('/')
def welcome():
  return "<h1> Add a YouTube URL as an ENDPOINT </h1>"
  


if __name__ == '__main__':
 app.run(debug=True)
