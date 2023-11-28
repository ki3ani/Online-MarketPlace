from flask import Flask, jsonify, request
import pandas as pd
from scipy.stats import zscore
import numpy as np
import scipy.stats as stats
from scipy.stats import kruskal
import scikit_posthocs as sp
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from recommendation import load_datasets, get_similar_items, recommend_items
from recommendation import file_paths


# Your existing code here...

app = Flask(__name__)

@app.route('/load_datasets', methods=['GET'])
def load_datasets_route():
    data = load_datasets(file_paths)
    return jsonify(success=True)

@app.route('/get_similar_items/<product_id>', methods=['GET'])
def get_similar_items_route(product_id):
    similar_items = get_similar_items(int(product_id))
    return jsonify(similar_items=similar_items.tolist())

@app.route('/recommend_items/<user_id>', methods=['GET'])
def recommend_items_route(user_id):
    recommended_items = recommend_items(float(user_id))
    return jsonify(recommended_items=recommended_items.tolist())

if __name__ == '__main__':
    app.run(debug=True)