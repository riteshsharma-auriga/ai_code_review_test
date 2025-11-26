from flask import Flask

app = Flask(__name__)

# The @app.route('/') decorator associates the URL '/' (the root) with the function immediately below it.
@app.route('/')
def hello_world():
    """
    This function is executed when a user navigates to the root URL.
    """
    return 'Hello, World! This is my first Flask application.'

if __name__ == '__main__':
    # Run the application in debug mode for easier development
    app.run(debug=True)
