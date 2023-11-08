from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(10)
    return "Finished"

if __name__ == '__main__':
    app.run()
