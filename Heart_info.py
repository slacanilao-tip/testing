from flask import Flask, jsonify, request
from flask.helpers import make_response
app = Flask (__name__)
hearts = [{
    "heart_id": "0",
    "date": "11/27/21",
    "heart_rate": "89"},
{
    "heart_id": "1",
    "date": "11/27/21",
    "heart_rate": "98"},
{
    "heart_id": "2",
    "date": "11/27/21",
    "heart_rate": "101"},
]
@app.route('/hearts', methods=['GET'])
def getHearts():
    return jsonify(hearts)

@app.route('/hearts/<index>', methods=['GET'])
def get_oneHeart(index):
    return jsonify(hearts[int(index)-1]), 200

@app.route('/hearts', methods=['POST'])
def add_hearts():
    heart = request.get_json()
    hearts.append(heart)
    return {'id': len(hearts)}, 200

@app.route('/hearts/<index>', methods=['PUT'])
def update_heart(index):
    heart = request.get_json()
    if index in hearts:
        hearts[index] = heart
        return "none"
    hearts[int(index)] = heart
    return "none"

@app.route('/hearts/<index>', methods=['DELETE'])
def delete_hearts(index):
    counter = 0
    for i in hearts:
        if i["heart_id"]==(index):
            hearts.pop(counter)
            return jsonify(hearts)
        counter += 1
    return "none"

if __name__ == '__main__':
    app.run() #run our Flask app