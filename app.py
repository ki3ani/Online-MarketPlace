from flask import Flask, jsonify, request
import recommendation

# Load datasets
data = recommendation.load_datasets(recommendation.file_paths)

app = Flask(__name__)

@app.route('/recommend_items/<user_id>', methods=['GET'])
def recommend_items_route(user_id):
    user_id = float(user_id)
    recommended_items = recommendation.recommend_items(user_id, data)
    return jsonify(recommended_items=recommended_items)

@app.route('/get_similar_items/<product_id>', methods=['GET'])
def get_similar_items_route(product_id):
    product_id = float(product_id)
    similar_items = recommendation.get_similar_items(product_id, data)
    return jsonify(similar_items=similar_items)

if __name__ == '__main__':
    app.run(debug=True)