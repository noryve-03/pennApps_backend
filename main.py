from twilio.rest import Client

from global_functions import *  
import random 
import daily_challenge 

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

msg, index = daily_challenge.load("data.pickle") 

from flask import Flask, request

app = Flask(__name__)
message = client.messages.create(
    body = msg,
    from_ = 'NUMBER',
    to = 'NUMBER'
)

@app.route('/webhooks', methods=['POST'])
def webhook():
    user_response = request.form['Body']
    user_number = request.form['From']
    
    if user_response == str(index):
        print(user_number)
        congratulation_message = "Congratulations! You chose the correct answer!"
        message = client.messages.create(
            body=congratulation_message,
            from_='+18559593981',
            to='+14752879371',
            status_callback='https://5677-2607-f470-34-2101-af65-57c-8243-9691.ngrok-free.app/'
        )
    else: 
        congratulation_message = "Better Luck Tomorrow!"
        message = client.messages.create(
            body=congratulation_message,
            from_='+NUMBER',
            to='+NUMBER'
        )
    return '', 200

@app.route('/', methods=['POST'])
def other_webhook():
    print(request.form)
    user_response = request.form['Body']
    if user_response == str(index):
        congratulation_message = "Congratulations! You chose the correct answer!"
        message = client.messages.create(
            body=congratulation_message,
            from_='+NUMBER',
            to='+NUMBER',
            status_callback='https://5677-2607-f470-34-2101-af65-57c-8243-9691.ngrok-free.app/'
        )
    else: 
        congratulation_message = "Better Luck Tomorrow!"
        message = client.messages.create(
            body=congratulation_message,
            from_='+18559593981',
            to='+14752879371'
        )
    return '', 200

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=8080)



# # message = client.messages('SM36a1bc37e9da8bacff2ef83a2db8d667').fetch()

# print(message.body)
# messages = client.messages.list(limit=20)

# for record in messages:
#     print(record)`
