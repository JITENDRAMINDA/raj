from pyrogram import Client, Filters
app = Client('my_account',891273,"de8204ec84cb49ff02e1652325adf332")

u = '-1001115051772'
s = '-1001378725482'
@app.on_message(Filters.chat(int(s)) & Filters.text & ~ Filters.edited)
def forawrd(client, message):
   client.send_message(int(u),message.text.replace('🎾' , '🥎'))
           

@app.on_message(Filters.chat(int(s)) & Filters.edited & Filters.text)
def edit(client, message):
    mess = client.iter_history(int(u), limit=30)
    for i in mess:
        if ' '.join(i.text.split(' ')[0:8]) in message.text:
            i.edit(message.text)
        elif message.text in ' '.join(i.text.split(' ')[0:8]):
            i.edit(message.text)
        

app.run()
