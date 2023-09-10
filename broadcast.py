from global_functions import * 
from daily_challenge import load 

def send_messages_to_everyone():
    all_numbers = get_all_numbers()
    msg, _ = load()
    for number in all_numbers:
    # Check if this user has sent us a text today: 
        if not user_sent_message_today(number):
            # message_body = "Hello, this is a broadcast message."
            message_from = "+18559593981" 
            message_to = number
            send_message(msg, message_from, message_to) 

