import json,pathlib
h=pathlib.Path(__file__).parent
a=json.load(open(h/'_assets.json'))
s=(h/'_src.html').read_text(encoding='utf-8')
for k,v in a.items(): s=s.replace('{{'+k+'}}',v)
(h/'index.html').write_text(s,encoding='utf-8');print(len(s)//1024,'KB')
