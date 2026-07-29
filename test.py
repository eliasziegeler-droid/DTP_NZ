from flask import Flask,

app = Flask(__name__)

@app.route
def get_data():
    return {"message": "Hello, World!"}

if __name__ == '__main__':
    app.run(debug=True)