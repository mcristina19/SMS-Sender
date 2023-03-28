from twilio.rest import Client

account_sid = 'AC6c50766d6c9932ru8dby237283u29'
auth_token = '409fnu398v3bcu3rh4888332904n94n8'
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Helloooo!!!!",
  from_="+18881231234",
  to="+10001231234"
)

print(message.sid)