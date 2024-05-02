from flask import Flask, jsonify

app = Flask(__name__)

activity = dict()
activity["date"] = "2021-09-01"
activity["time"] = "morning"
activity["description"] = "visit the zoo"

@app.route('/test')
def test():
    return jsonify(activity)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
