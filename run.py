# importing the flask app created
from app import create_app

# holding the app in a variable
app = create_app()

# ensuring the file is being run directly
if __name__ == "__main__":
    # starting the app
    app.run(debug=True)