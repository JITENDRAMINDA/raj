from pyrogram import Client, Filters




app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')

@app.on_message(Filters.chat('-1001309160459'))
def forawrd(client, message):
    client.forward_messages('-1001356076506', '-1001309160459', [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
    client.edit_message_text('-1001356076506', '2344', [message] )

app.run()

