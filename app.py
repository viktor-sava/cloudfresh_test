from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test_endpoint():
    response = {
        "message": "Cloudfresh test task"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
