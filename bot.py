from pyrogram import Client, Filters
app = Client('485505720:AAGQHhdDGWlEnzPUNcJlX8wBSdVneBjnUXc')

u = '-1001115051772'
@app.on_message(Filters.chat(-1001369162545) & Filters.text)
def forawrd(client, message):
    file = open("text.txt" , "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        if '🖲' in message.text :
            client.send_message(int(u),message.text.replace('🖲' , '💘'))
        else:
          if '📟' in message.text :
            client.send_message(int(u),message.text.replace('📟' , '🏝'))
          else:
            if message.text == '6' :
               client.send_sticker(int(u),'CAADBQADagIAAlrCoBLZsv2I8bOyAAEC')
               client.send_message(int(u),message.text.replace('🎾' , '🥎'))
            else:
              if message.text == '4' :
               client.send_sticker(int(u),'CAADBQADaQIAAlrCoBIcPTv3oa81RgI')
               client.send_message(int(u),message.text.replace('🎾' , '🥎'))
              else:
                if message.text == 'WD' :
                  client.send_message(int(u),message.text.replace('WD' , 'WIDE BALL 🙅‍♂️'))
                else:
                   if message.text == 'WKT' :
                    client.send_sticker(int(u),'CAADBQADawIAAlrCoBKKtko8XZuaqgI')
                    client.send_message(int(u),message.text.replace('WKT' , '🚾 Wicket Wicket Wicket 🚾 '))
                   else:
                    client.send_message(int(u),message.text.replace('🎾' , '🥎'))
                 



@app.on_message(Filters.command('status'))
def main(client, message) :
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")
    if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
      file = open("text.txt" , "r")
      lines = file.readlines()
      file.close()
      for line in lines:
        if line == "started":
           message.reply("line is on ! ")
        if line == "closed":
           message.reply("line is stopped ! ")        
@app.on_message(Filters. private)
def ran( client, message) :
  client.forward_messages(-1001250871922, message.chat.id ,[message.message_id])
@app.on_message(Filters.command('offline'))
def main(client, message) :
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("line is off ! ")
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("text.txt" , "w")
    file.write("closed")
    file.close()
    message.reply("line is off ! ")
@app.on_message(Filters.command('online'))
def main(client, message) :
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'administrator':
    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("line is on !")
   if client.get_chat_member(message.chat.id , message.from_user.id).status == 'creator':
    file = open("text.txt" , "w")
    file.write("started")
    file.close()
    message.reply("line is on !")
app.run()
