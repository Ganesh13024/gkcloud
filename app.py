# Importing Flask
from flask import Flask, render_template

# Creating an instance of the Flask class
app = Flask(__name__)

# Creating a new endpoint with this instance as a function decorator
@app.route('/')
def home():
    return render_template('index.html')


# Starting the Server
if __name__ == '__main__':
    app.run()
