from ps6 import *

# text = "Hello, my friend!"
# myMessage = Message(text)
# print(myMessage.build_shift_dict(0))
# print(myMessage.apply_shift(2))

plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
plaintext.change_shift(26)
print('Actual Output2:', plaintext.get_message_text_encrypted())
