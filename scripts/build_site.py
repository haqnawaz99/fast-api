"""Build the static teaching website from Markdown and runnable Python files."""
from pathlib import Path
from html import escape
import re
import shutil
import zipfile
import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs'
NOTES = sorted((ROOT / 'notes').glob('lecture_*.md'))

def render(text):
    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc'], extension_configs={'toc': {'permalink': True}})
    body = md.convert(text)
    body = re.sub(r'href="\.\./(lecture_\d+\.md)(#[^"]*)?"', lambda m: f'href="{Path(m[1]).stem}.html{m[2] or ""}"', body)
    body = re.sub(r'href="\.\./README\.md(?:#[^"]*)?"', 'href="setup.html"', body)
    body = re.sub(r'href="\.\./([^"/]+\.py)"', r'href="downloads/\1"', body)
    return body, md.toc

def page(title, body, toc='', active=''):
    nav = '<a href="index.html">Course overview</a><a href="setup.html">Start here / setup</a>'
    for note in NOTES:
        name = note.read_text(encoding='utf-8').splitlines()[0].lstrip('# ')
        nav += f'<a {"aria-current=page" if active == note.stem else ""} href="{note.stem}.html">{escape(name)}</a>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · FastAPI classroom</title><meta name="description" content="Learn FastAPI in small runnable steps, with explained code and practice exercises.">
<link rel="stylesheet" href="assets/style.css"><script src="assets/site.js" defer></script></head>
<body><a class="skip" href="#content">Skip to lesson</a><header><a class="brand" href="index.html"><span>F /</span> FastAPI classroom</a><a href="downloads/examples.zip">Download examples ↓</a></header>
<div class="layout"><aside><p class="eyebrow">YOUR LEARNING PATH</p><nav aria-label="Course">{nav}</nav><details><summary>On this page</summary>{toc}</details><p class="aside-note">Small steps. Real code.<br>Learn at your own pace.</p></aside><main id="content">{body}<footer>FastAPI classroom · Python + Windows PowerShell · <a href="https://github.com/haqnawaz99/fast-api">Source on GitHub</a></footer></main></div><p id="copy-status" role="status" aria-live="polite"></p></body></html>'''

def build():
    OUT.mkdir(exist_ok=True)
    (OUT/'downloads').mkdir(exist_ok=True)
    (OUT/'assets').mkdir(exist_ok=True)
    for asset in (ROOT/'site-assets').iterdir():
        shutil.copyfile(asset, OUT/'assets'/asset.name)
    files = [ROOT/'main.py', ROOT/'mock.py', ROOT/'requirements.txt', *sorted(ROOT.glob('lecture_*.py'))]
    for file in files:
        shutil.copyfile(file, OUT/'downloads'/file.name)
    with zipfile.ZipFile(OUT/'downloads/examples.zip', 'w', zipfile.ZIP_DEFLATED) as bundle:
        for file in files:
            bundle.write(file, file.name)
    setup = '''# Start here: set up your classroom workspace

You need Python installed on your computer and a text editor such as VS Code. These instructions use Windows PowerShell.

## 1. Get the files

[Download all examples](downloads/examples.zip), extract the ZIP into a folder, then open that folder in VS Code. Open a PowerShell terminal in the same folder. Keep `mock.py` beside the Lecture 03 files.

## 2. Create the environment once

```powershell
py -m venv .venv
.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt
```

A virtual environment keeps this project's packages separate. These commands use its Python directly, so activation is not required. If `py` is unavailable, check that Python is installed and restart your terminal.

## 3. Check the installation

```powershell
.\\.venv\\Scripts\\python.exe main.py
```

Expected output: `0.141.1` with the supplied requirements.

## 4. Run a server example

```powershell
.\\.venv\\Scripts\\fastapi.exe dev lecture_02_01.py
```

Keep this terminal open. Visit <http://127.0.0.1:8000/> for the welcome message and <http://127.0.0.1:8000/docs> for interactive API documentation. Press `Ctrl+C` to stop the server before starting another example.

## How to use each lesson

Read the explanation, copy the complete file from the lesson's runnable-files section, save it with the displayed filename, and run the command below it. Short snippets in the notes explain one part of a program; the runnable-files section contains complete programs.

The website hosts reading material and downloads. Python runs on your own computer; GitHub Pages does not run the FastAPI server.
'''
    body,toc=render(setup)
    (OUT/'setup.html').write_text(page('Setup',body,toc),encoding='utf-8')
    cards=''
    for index,note in enumerate(NOTES):
        source=note.read_text(encoding='utf-8')
        title=source.splitlines()[0].lstrip('# ')
        body,toc=render(source)
        number=note.stem.split('_')[1]
        examples=[ROOT/'main.py'] if number=='01' else sorted(ROOT.glob(f'lecture_{number}*.py'))
        if any('from mock import' in f.read_text(encoding='utf-8') for f in examples):
            examples.insert(0,ROOT/'mock.py')
        runnable='## Complete runnable files\n\nCopy each file into the same project folder, or [download the full bundle](downloads/examples.zip). Complete files below include all imports and earlier endpoints. Read [setup](setup.html) first.\n\n'
        for file in examples:
            runnable+=f'### {file.name}\n\n[Download this file](downloads/{file.name})\n\n```python\n{file.read_text(encoding="utf-8").rstrip()}\n```\n\n'
            if file.name=='mock.py':
                runnable+='This data file is imported by Lecture 03 examples. Save it beside them; it does not start a server.\n\n'
            else:
                command = '.\\.venv\\Scripts\\python.exe main.py' if file.name=='main.py' else f'.\\.venv\\Scripts\\fastapi.exe dev {file.name}'
                runnable+=f'Run from the project folder (stop any previous server first):\n\n```powershell\n{command}\n```\n\n'
        combined,toc=render(source+'\n\n'+runnable)
        lead='<div class="notice"><strong>Before you begin</strong> · <a href="setup.html">Set up your environment</a>. Read the notes, then <a href="#complete-runnable-files">copy a complete runnable file</a>.</div>'
        nextlinks='<div class="lesson-nav"><a href="index.html">← All lessons</a>'
        if index+1<len(NOTES): nextlinks+=f'<a href="{NOTES[index+1].stem}.html">Next lesson →</a>'
        nextlinks+='</div>'
        (OUT/f'{note.stem}.html').write_text(page(title,lead+combined+nextlinks,toc,note.stem),encoding='utf-8')
        cards+=f'<a class="card" href="{note.stem}.html"><span class="eyebrow">LESSON {number}</span><h2>{escape(title.split(": ",1)[-1])}</h2><p>Explained examples, expected results, troubleshooting, and practice.</p><span>Open lesson →</span></a>'
    hero=f'''<section class="hero"><p class="eyebrow">A PRACTICAL INTRODUCTION</p><h1>Build your first API.<br><em>One small step at a time.</em></h1><p class="intro">Read a little. Run some code. Understand what happens.<br>A hands-on FastAPI course with copy-ready examples.</p><a class="primary" href="setup.html">Set up & start learning →</a><p class="meta">{len(NOTES):02d} lessons · Beginner friendly · Python + FastAPI</p></section><section><p class="eyebrow">THE COURSE</p><div class="cards">{cards}</div></section><section class="notice"><h2>Your learning rhythm</h2><p><strong>01 Read</strong> the explanation. <strong>02 Copy</strong> a complete file. <strong>03 Run</strong> it locally. <strong>04 Experiment</strong> with the practice exercises.</p></section>'''
    (OUT/'index.html').write_text(page('Learn FastAPI',hero),encoding='utf-8')
    (OUT/'.nojekyll').write_text('',encoding='utf-8')
    print(f'Built {len(NOTES)} lessons plus index and setup in {OUT}')

if __name__=='__main__':
    build()
