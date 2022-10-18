import cantools
from can.message import Message

db = cantools.db.load_file('/home/kevin/Documents/Test_2/motohawk.dbc')

# Print Content of dbc
print(db)

# print particular message in dbc
msg = db.get_message_by_name('ExampleMessage')
print(msg)
msg_data = msg.encode({'Enable':1, 'AverageRadius': 1, 'Temperature': 251})
print(msg_data)