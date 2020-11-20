import requests,json,re
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
ses = requests.session()
cookies = open('cookies.txt').read().splitlines()
for line in cookies:
  ses.cookies['.ROBLOSECURITY'] = line
  x = ses.post('https://auth.roblox.com')
  token = x.headers['x-csrf-token']
  #print(token)
  r = ses.get('https://www.roblox.com/mobileapi/userinfo')
  w = r.text
  remove_html_tags(w)
  o = open('output.txt','a')
  o.write('\n' + w + ses.cookies['.ROBLOSECURITY'])
print('All done!!')
