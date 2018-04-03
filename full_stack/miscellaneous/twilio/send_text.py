from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7307ee90dae4c5839316ae6787826212"
# Your Auth Token from twilio.com/console
auth_token  = "8071d888b3e14d84cb1d22107d7430cb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17708642946",
    from_="+14704357668",
    body="Hello from Python!")

print(message.sid)
