from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
    'id' : 1,
    'title': u'Buy Groceries',
    'description': u'Milk, Cheese, Pizza, Fruits',
    'done': False
    },
    {
    'id' : 2,
    'title': u'Furniture',
    'description': u'Bed, Sofa, Chair',
    'done': False
    }
]

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        }, 400)
    
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({
            "status":"Success",
            "message": "Task added successfully"
        }, 400)
    


@app.route("/get-data")
def get_data():
    return jsonify({
        'data':tasks
    })


@app.route("/")
def hello_world():
    return "Hello World!"

if(__name__ == '__main__'):
    app.run(debug = True)

