from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from egame import Game

account_sid = 'AC7129f692edfb436fe3827c984d535d69'
auth_token = 'e5f94e6cd91d078f6f44e64a67b4699f'

num_reply = dict()

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])

def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    num_reply[request.form['From']] = request.form['Body']
    # Add a message
    resp.message("Response Received")

    return str(resp)


if __name__ == "__main__":
    #game = Game()
    #game.start()
    app.run(debug=True)