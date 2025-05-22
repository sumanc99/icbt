# importing the flask app created
from app import create_app
# importing qrcode library to create qrcode
import qrcode

# img = qrcode.make("http://192.168.43.1:5000")
# img.save("app/static/images/test_ui.png")

# holding the app in a variable
app = create_app()

# ensuring the file is being run directly
if __name__ == "__main__":
    # starting the app
    app.run(debug=True, host="0.0.0.0", port=5000)
    # app.run(debug=True)