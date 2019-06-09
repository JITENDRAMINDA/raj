from pyrogram import Client, Filters
app = Client('my_account',891273,"de8204ec84cb49ff02e1652325adf332")

u = '-1001115051772'
s = '-1001378725482'
@app.on_message(Filters.chat(int(s)) & Filters.text & ~ Filters.edited)
def forawrd(client, message):
   client.send_message(int(u),message.text.replace('🎾' , '🥎'))
           

@app.on_message(Filters.chat(int(s)) & Filters.edited & Filters.text)
def edit(client, message):
    mess = client.iter_history(int(u), limit=15)
    for i in mess:
        x = ' '.join(i.text.split(' ')[0:2]) 
        y = ' '.join(message.text.split(' ')[0:2])

        if x.casefold() in y.casefold():
          text = message.text
          f = False
          words = ['lund','dekho','fix','fixer','👆','👇','sab','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔']
          for word in words:
            if word.casefold() in text.casefold():
              f = True
          if not f:       
           if '🖲' in text:
            i.edit(message.text.replace('🖲' , '**💘'))
           elif '📟' in text:
            i.edit(message.text.replace('📟' , '🏝'))
           elif 'Runs Scored:' in text:
            i.edit(message.text.replace('Runs Scored:' , '**Runs Scored:**'))
           elif 'RUNS SCORED:' in text:
            i.edit(message.text.replace('RUNS SCORED:' , '**Runs Scored:**'))
           elif '🎾' in text:
            i.edit(message.text.replace('🎾' , '🥎'))
           else:
            i.edit(message.text)



        elif y.casefold() in x.casefold():
          text = message.text
          f = False
          words = ['lund','dekho','fix','fixer','👆','👇','sab','karvana','link','loss','audio','varna','pura','puri','open','paid','contact','baazigar','whatsapp','timepass','kamma','book','teenpatti','diya','bhai','🥺','members','🖕','member','only','chut','lund','gand','ma','maa','bhosdi','bahan','loude','lode','lavde','chutiya','🤞','🤟','☝️','mkc','bkc','mc','bc','madarchod','bahanchod','bahnchod','gandu','❓','kya','wbt','line','who',"https://",'joinchat','bullet','fuck','🤔']
          for word in words:
            if word.casefold() in text.casefold():
              f = True
          if not f:       
           if '🖲' in text:
            i.edit(message.text.replace('🖲' , '**💘'))
           elif '📟' in text:
            i.edit(message.text.replace('📟' , '🏝'))
           elif 'Runs Scored:' in text:
            i.edit(message.text.replace('Runs Scored:' , '**Runs Scored:**'))
           elif 'RUNS SCORED:' in text:
            i.edit(message.text.replace('RUNS SCORED:' , '**Runs Scored:**'))
           elif '🎾' in text:
            i.edit(message.text.replace('🎾' , '🥎'))
           else:
            i.edit(message.text)
  
        

app.run()
