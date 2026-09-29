import json,subprocess,re,urllib.parse,sys,time
def decode(link):
    if 'news.google.com' not in link: return link
    aid=link.split('/articles/')[1].split('?')[0]
    html=subprocess.run(['curl','-s','-L','-m','20','-A','Mozilla/5.0',f'https://news.google.com/rss/articles/{aid}?oc=5'],capture_output=True,text=True).stdout
    sg=re.search(r'data-n-a-sg="([^"]+)"',html); ts=re.search(r'data-n-a-ts="([^"]+)"',html)
    if not (sg and ts): return None
    req=[[["Fbv4je",json.dumps(["garturlreq",[["X","X",["X","X"],None,None,1,1,"US:en",None,1,None,None,None,None,None,0,1],"X","X",1,[1,1,1],1,1,None,0,0,None,0],aid,int(ts.group(1)),sg.group(1)]),None,"generic"]]]
    body='f.req='+urllib.parse.quote(json.dumps(req))
    r=subprocess.run(['curl','-s','-m','20','-A','Mozilla/5.0','-H','Content-Type: application/x-www-form-urlencoded;charset=UTF-8','--data',body,'https://news.google.com/_/DotsSplashUi/data/batchexecute'],capture_output=True,text=True).stdout
    i=r.find('garturlres')
    if i<0: return None
    m=re.search(r'(https?://.*?)\\+"', r[i:])
    if not m: return None
    u=m.group(1)
    u=re.sub(r'\\+u([0-9a-fA-F]{4})', lambda x: chr(int(x.group(1),16)), u)
    u=re.sub(r'\\+/', '/', u)
    return u
if __name__=='__main__':
    for a in sys.argv[1:]:
        u=None
        for i in range(3):
            u=decode(a)
            if u: break
            time.sleep(3)
        print(u)
