from pyrogram import Client, Filters


app = Client('765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc')

string = 'xcx'


@app.on_message(Filters.chat(-1001309160459) & Filters.text & ~ Filters.regex('👇'))
def forawrd(client, message):
  if string = 'xcx' 
      client.forward_messages(-1001344956857, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )
      client.forward_messages(-1001356076506, -1001309160459, [message.message_id], 'bool = None ', 'bool = True' , 'bool = True' )

@app.on_message(Filters.command('zeet'))
    file = open("text.txt" , "r")
    lines = readlines()
     file.close()

    for line in lines:
      message.reply(line)

app.run()

