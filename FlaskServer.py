from flask import Flask, request

import os

import datetime



app = Flask(__name__)



@app.route("/", methods=["POST"])

def receive_screenshot():

    data = request.get_data()

    if data:

        # Generate a unique filename using the current timestamp

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"/media/sf_exceptions/RTOMaldev/screenshots/screenshot_{timestamp}.png"

        

        with open(filename, "wb") as f:

            f.write(data)

        return "Received and saved screenshot", 200

    else:

        return "No data received", 400



if __name__ == "__main__":

    port = int(os.environ.get('PORT', 80))

    app.run(host='0.0.0.0', port=port)

