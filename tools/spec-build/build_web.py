"""Build the designed web page (HTML) for a specification from its Markdown source.

Usage: python3 build_web.py phase1
The header block (title, dates, at-a-glance facts) lives in CFG below: update it if you change those facts in the Markdown.
"""
import re, subprocess, html, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
cfg_name = sys.argv[1]
CFG = {
 'phase1': dict(
   src=os.path.join(ROOT, 'bid-phase1', 'MosquitoAlert_Website_Phase1_Specifications.md'),
   out='mosquitoalert-phase1-spec.html',
   title='Mosquito Alert Website Phase 1 Specification',
   header='''<header class="masthead">
  <div class="stripe" aria-hidden="true"></div>
  <p class="eyebrow">Specification for quotation <span class="draft">Phase 1</span></p>
  <h1>Mosquito Alert website: migration from WordPress to Hugo</h1>
  <p class="lede">Move the public website www.mosquitoalert.com, with its 600 blog posts, 200 pages, FAQ and media in Spanish, Catalan and English, from WordPress to a static Hugo site on GitHub Pages, keeping its URLs, navigation and content on a plain theme, so that the project team can maintain it from a Git repository and redesign it in Phase 2 before it goes live.</p>
  <dl class="meta">
    <div><dt>Client</dt><dd>Mosquito Alert · Universitat Pompeu Fabra (UPF)</dd></div>
    <div><dt>Contact</dt><dd>John Palmer · <a href="mailto:john.palmer@upf.edu">john.palmer@upf.edu</a></dd></div>
    <div><dt>Quotations due</dt><dd>Fri 13 Nov 2026, 12:00 CET (<a href="#how-to-submit-a-quotation">§12</a>)</dd></div>
    <div><dt>Work period</dt><dd>WP1–2: Tue 17 Nov – Fri 11 Dec 2026, invoiced by 18 Dec · WP3: Jan–Feb 2027, separate request · WP4 (launch): after Phase 2</dd></div>
  </dl>
  <div class="glance" role="list" aria-label="At a glance">
    <div role="listitem"><span class="k">Hosting</span><span class="v">GitHub Pages · GPL-3.0</span></div>
    <div role="listitem"><span class="k">Design</span><span class="v">Plain theme · redesign in Phase 2</span></div>
    <div role="listitem"><span class="k">Content</span><span class="v">607 posts · 206 pages · 1 GB media</span></div>
    <div role="listitem"><span class="k">Languages</span><span class="v">Spanish · Catalan · English</span></div>
    <div role="listitem"><span class="k">Requirements</span><span class="v num">{{MUST}} must · {{SHOULD}} should · {{OPTS}} opt.</span></div>
  </div>
</header>''',
   tocnote='<p class="toc-note">Attachments: <code>url_inventory.csv</code> (the 2,204 public URLs of the current site) and the optional scaffold on the <code>scaffold-2025</code> branch of <code>github.com/Mosquito-Alert/website</code>.</p>'),
}[cfg_name]

body = subprocess.run(['pandoc', CFG['src'], '-t', 'html5', '--wrap=none'], capture_output=True, text=True, check=True).stdout
body = body[body.index('<h2'):]
ack_i = body.rfind('<p><em>Mosquito Alert is coordinated')
if ack_i > 0: body = body[:ack_i]
body = body.replace('<hr />', '')

toc = []
def h2(m):
    hid, num, text = m.group(1), m.group(2), m.group(3)
    num = num.replace('Appendix ', '')
    toc.append((hid, num, re.sub('<[^>]+>', '', text)))
    return f'<h2 id="{hid}"><span class="secno">{num}</span><span>{text}</span></h2>'
body = re.sub(r'<h2 id="([^"]+)">(\d+|Appendix [A-Z])\. (.*?)</h2>', h2, body)
body = re.sub(r'<h3 id="([^"]+)">([A-Z]?\d*\.\d+) (.*?)</h3>', r'<h3 id="\1"><span class="subno">\2</span> \3</h3>', body)

must = len(re.findall(r'<td>MUST</td>', body))
should = len(re.findall(r'<td>SHOULD</td>', body))
opts = len(set(re.findall(r'<td>(?:<strong>)?(OPT-\d\d)(?:</strong>)?</td>', body)))

body = re.sub(r'<td>(MUST|SHOULD)</td>', lambda m: f'<td class="pri"><span class="pill pill-{m.group(1).lower()}">{m.group(1)}</span></td>', body)
body = re.sub(r'<td>(?:<strong>)?((?:[A-Z0-9]{2,5}-\d\d)|D-\d\d)(?:</strong>)?</td>', r'<td class="rid"><span class="rid-chip">\1</span></td>', body)
body = body.replace('<li><strong>MUST</strong>:', '<li><span class="pill pill-must">MUST</span>')
body = body.replace('<li><strong>SHOULD</strong>:', '<li><span class="pill pill-should">SHOULD</span>')

body = re.sub(r'<colgroup>.*?</colgroup>', '', body, flags=re.S)
def wrap_table(m):
    t = m.group(0)
    kind = 'req' if '<th>ID</th>' in t and '<th>Priority</th>' in t else ('ids' if '<th>ID</th>' in t else 'plain')
    return f'<div class="table-wrap"><table class="t-{kind}">' + t[len('<table>'):] + '</div>'
body = re.sub(r'<table>(?:(?!</table>).)*?<th>At a glance</th>.*?</table>', '', body, flags=re.S)
body = re.sub(r'<table>.*?</table>', wrap_table, body, flags=re.S)

toc_html = ''.join(f'<li><a href="#{i}"><span class="toc-no">{n}</span>{html.escape(t)}</a></li>' for i, n, t in toc)
tpl = open(os.path.join(HERE, 'template.html')).read()
out = (tpl.replace('{{HEADER}}', CFG['header']).replace('{{TOCNOTE}}', CFG['tocnote']).replace('{{TITLE}}', CFG['title'])
          .replace('{{BODY}}', body).replace('{{TOC}}', toc_html)
          .replace('{{MUST}}', str(must)).replace('{{SHOULD}}', str(should)).replace('{{OPTS}}', str(opts)))
assert '{{' not in out, re.findall(r'\{\{\w+\}\}', out)
open(os.path.join(OUT, CFG['out']), 'w').write(out)
print(cfg_name, 'must', must, 'should', should, 'opts', opts, 'toc', len(toc), 'bytes', len(out))
