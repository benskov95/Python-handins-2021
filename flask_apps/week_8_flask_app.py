from flask import Flask, jsonify, abort, request
import mysql.connector as mysql

app = Flask(__name__)
connection = mysql.connect(host="db", user="root", passwd="root", db="db")
cursor = connection.cursor(prepared=True)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/chuck/api/joke', methods=['GET'])
def get_all_jokes():
    query = "select * from chuckJoke"
    cursor.execute(query)
    result = cursor.fetchall()

    jokes = []
    for joke in result:
        jokes.append({"id": joke[0], "text": joke[1], "value": joke[2]})
        
    return jsonify(jokes)



@app.route('/chuck/api/joke', methods=['POST'])
def add_joke():
    joke = request.json
    query = "insert into chuckJoke (text, value) values (%s, %s)"
    cursor.execute(query, (joke["text"], joke["value"],))
    connection.commit()
    joke["id"] = cursor.lastrowid
            
    return jsonify(joke)