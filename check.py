from pathlib import Path
import re,json,urllib.parse,xml.etree.ElementTree as ET
r=Path(__file__).parent;d=r/'dist';errors=[];titles=[];descs=[];files=list(d.rglob('index.html'))
for p in files:
 t=p.read_text();path='/'+str(p.relative_to(d)).replace('index.html','');
 if 'http-equiv="refresh"' in t:continue
 def need(pattern,label):
  a=re.findall(pattern,t,re.S); 
  if len(a)!=1:errors.append(f'{path}: {label} count {len(a)}')
  return a[0] if a else ''
 titles.append(need(r'<title>(.*?)</title>','title'));descs.append(need(r'<meta name="description" content="([^"]+)"','description'))
 need(r'<h1.*?>.*?</h1>','H1');canon=need(r'<link rel="canonical" href="([^"]+)"','canonical')
 if canon!='https://wellness-origin-seo-preview.bmaq12.chatgpt.site'+path:errors.append(path+' canonical mismatch '+canon)
 if 'noindex,follow' not in t:errors.append(path+' missing intentional preview noindex')
 try:graph=json.loads(need(r'<script type="application/ld\+json">(.*?)</script>','schema'))
 except Exception as ex:errors.append(path+' schema '+str(ex))
 if 'darkblue-scorpion' in t:errors.append(path+' staging name')
 for attr,u in re.findall(r'\b(href|src)="([^"]+)"',t):
  if not u.startswith('/'):continue
  route=urllib.parse.urlparse(u).path;f=d/route.lstrip('/');f=f/'index.html' if route.endswith('/') else f
  if not f.is_file():errors.append(path+' broken '+u)
 for im in re.findall(r'<img[^>]*>',t):
  for a in ['alt=','width=','height=']:
   if a not in im:errors.append(path+' image missing '+a)
for label,values in [('title',titles),('description',descs)]:
 dup=[x for x in set(values) if values.count(x)>1]
 if dup:errors.append('duplicate '+label+':'+str(dup))
for rel,expected in [('index.html',12),('spa-services/index.html',12)]:
 count=len(re.findall(r'<img class="service-thumb"', (d/rel).read_text()))
 if count!=expected:errors.append(rel+' service images: '+str(count))
for f in ['sitemap.xml']:
 root=ET.parse(d/f).getroot()
 if len(root)!=0:errors.append('Preview sitemap should be empty because pages noindex')
root=ET.parse(r/'production-sitemap.xml').getroot()
if len(root)!=29:errors.append('Production sitemap missing paths')
for p in json.load(open(r/'page-inventory.json')):
 if not (d/p['path'].strip('/')/'index.html').is_file():errors.append('Missing '+p['path'])
print(json.dumps({'page_count':len(titles),'preserved_sitemap_paths':29,'asset_bytes':sum(p.stat().st_size for p in (d/'assets').iterdir()),'css_bytes':(d/'styles.css').stat().st_size,'js_bytes':(d/'app.js').stat().st_size,'service_photos':{'homepage':12,'directory':12},'errors':errors},indent=2))
raise SystemExit(bool(errors))
