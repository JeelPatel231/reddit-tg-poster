import requests, time, subprocess

subreddit='dankmemes'
bot_token='' #add bot token here
chat_id='' #add your chat id here, like, where is the bot going to be posting memes

def getnewpage():
    newpage = requests.get('https://www.reddit.com/r/' + subreddit + '/new/.json').json()
    
    if 'error' in newpage.keys():
        print('retry?')
        time.sleep(1)
        getnewpage()
    else:
        imageurl = newpage['data']['children'][0]['data']['url_overridden_by_dest']
        imagetitle = newpage['data']['children'][0]['data']['title']
        postlonk = 'www.reddit.com' + newpage['data']['children'][0]['data']['permalink']
        print(imageurl, imagetitle, postlonk)
        subprocess.run(['bash','-c',f'curl -s "https://api.telegram.org/bot{bot_token}/sendPhoto" -d photo=\'{imageurl}\' -d caption="<a href=\'{postlonk}\'>{imagetitle}</a>" -d chat_id="{chat_id}" -d parse_mode=HTML'])
        def whileloopcheck():
          print('checking')
          newcheck = requests.get('https://www.reddit.com/r/' + subreddit + '/new/.json').json()
          if 'error' in newcheck.keys():
              print('retrywhile?')
              time.sleep(1)
              whileloopcheck()
          else:
              if imageurl == newcheck['data']['children'][0]['data']['url_overridden_by_dest']:
                  print('same..')
                  time.sleep(10)
                  whileloopcheck()
              else:
                    getnewpage()
        whileloopcheck()
        print(imageurl, imagetitle, postlonk)
    getnewpage()


getnewpage()