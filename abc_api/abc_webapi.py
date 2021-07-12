from flask import Flask, json, jsonify, render_template
from flask_restful import Api, Resource, reqparse
from ecommerce_data import *

app = Flask(__name__)
api = Api(app)

@app.route("/ecommerceData", methods=['GET'])
def get_ecommerce_data():
    ecommerceData = read_ecommerce_data()
    return jsonify(ecommerceData)

@app.route("/summarizedEcommerceData", methods=['GET'])
def get_summarized_ecommerce_data():
    summarizedEcommerceData = summarize_ecommerce_data()
    return jsonify(summarizedEcommerceData)

if __name__ == '__main__':
    app.run(debug=True)