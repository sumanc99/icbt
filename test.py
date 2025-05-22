from app import create_app
import os
import threading

app = create_app()

def open_browser():
    # This opens the URL in the Android browser using Termux
    os.system("am start -a android.intent.action.VIEW -d http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start() # open browser after just one second
    app.run(debug=True, host="0.0.0.0")  # Make it accessible from your phone browser
