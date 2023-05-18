from twilio.rest import Client

account_sid = 'AC6c50766d6c97538ff1221e8f281421e9'
auth_token = '421452b1aabf2968f47a5ece3f913990'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Helloooo!!!!",
    from_="+18885022084",
    to="+3333333333"
)

print(message.sid)
