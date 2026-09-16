"""Check generated links, anchors, downloads, and code fidelity."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import zipfile
ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.links=[]; self.ids=set(); self.codes=[]; self.code=None; self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for key in ('href','src'):
            if key in attrs: self.links.append(attrs[key])
        if tag=='code': self.code=''
    def handle_data(self, data):
        if self.code is not None: self.code+=data
    def handle_endtag(self, tag):
        if tag=='code' and self.code is not None: self.codes.append(self.code); self.code=None
pages={p:Page(p.read_text(encoding='utf-8')) for p in SITE.glob('*.html')}
for file,page in pages.items():
    for link in page.links:
        url=urlsplit(link)
        if url.scheme or url.netloc: continue
        target=(file.parent / unquote(url.path)).resolve() if url.path else file
        assert target.is_relative_to(SITE), (file,link)
        assert target.exists(), (file,link)
        if url.fragment and target in pages: assert unquote(url.fragment) in pages[target].ids, (file,link)
for source in [ROOT/'main.py',ROOT/'mock.py',*ROOT.glob('lecture_*.py')]:
    assert (SITE/'downloads'/source.name).read_bytes()==source.read_bytes(), source
    assert any(source.read_text(encoding='utf-8').rstrip()+'\n' in page.codes for page in pages.values()), source
with zipfile.ZipFile(SITE/'downloads/examples.zip') as bundle:
    for name in bundle.namelist(): assert bundle.read(name)==(ROOT/name).read_bytes(),name
assert len(pages)==len(list((ROOT/'notes').glob('lecture_*.md')))+2
print('PASS: all local links, anchors, complete code blocks, downloads, and ZIP contents')
