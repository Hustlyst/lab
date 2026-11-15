"""Renders the hub page (index.html). Called by build.py."""
import html

REPO = 'https://github.com/Hustlyst/lab'
GH = ('<svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>')

# slug: (sample result shown on the card, what you need as filter keys, time label, one-line tagline)
# Sample results are made-up examples, never real data.
CARD = {
 'meeting-receipt': ('$1,840', ['calendar'], '1 min', 'What your meetings really cost.'),
 'work-wrapped': ('408 h', ['calendar'], '1 min', 'Your year in meetings, wrapped.'),
 'calendar-horoscope': ('The Marathoner', ['calendar'], '1 min', 'Your work personality and lucky hour.'),
 'could-it-be-an-email': ('42%', ['calendar'], '1 min', 'How much of your calendar was an email?'),
 'binge-receipt': ('6.9 days', ['netflix'], '1 min', 'Your Netflix binge, itemised.'),
 'listening-receipt': ('166 h', ['spotify'], '1 min', 'Hours, artists and late-night plays.'),
 'shelf-receipt': ('31 books', ['goodreads', 'letterboxd'], '1 min', 'Your reading or film year.'),
 'inbox-receipt': ('4.2 h', ['gmail'], '1 min', 'The Reply-All Tax on your inbox.'),
 'chat-awards': ('The Ghost', ['whatsapp'], '1 min', 'Who is the Ghost? The Night Owl?'),
 'linkedin-wrapped': ('+212', ['linkedin'], '1 min', 'Your LinkedIn year, totals only.'),
 'fitness-wrapped': ('1,240 km', ['strava', 'apple health'], '1 min', 'Your year of movement.'),
 'meeting-bingo': ('BINGO', [], 'instant', 'Bingo for the meeting you are in.'),
 'buzzword-decoder': ('4/5', [], 'instant', 'Corporate speak, translated.'),
 'daily-guess': ('11/15', [], 'instant', 'Five guesses a day.'),
 'dither-booth': ('[you]', ['a photo'], '1 min', 'Print your face on a receipt.'),
 'receipt-of-me': ('TOTAL', [], 'instant', 'A joke receipt of your week.'),
}
SECTIONS = [
 ('The calendar bench', ['meeting-receipt', 'work-wrapped', 'calendar-horoscope', 'could-it-be-an-email']),
 ('The streaming shelf', ['binge-receipt', 'listening-receipt', 'shelf-receipt']),
 ('Inbox, chats and feeds', ['inbox-receipt', 'chat-awards', 'linkedin-wrapped', 'fitness-wrapped']),
 ('Play and make', ['meeting-bingo', 'buzzword-decoder', 'daily-guess', 'dither-booth', 'receipt-of-me']),
]
# Experiment numbers follow this order. A new tool goes at the end so existing numbers never change.
ORDER = ['meeting-receipt', 'work-wrapped', 'calendar-horoscope', 'could-it-be-an-email', 'binge-receipt', 'listening-receipt', 'shelf-receipt', 'inbox-receipt', 'chat-awards', 'linkedin-wrapped', 'fitness-wrapped', 'meeting-bingo', 'buzzword-decoder', 'daily-guess', 'dither-booth', 'receipt-of-me']
NEWEST = 'linkedin-wrapped'
NOFILE = 'meeting-bingo'
CHIPS = ['calendar', 'netflix', 'spotify', 'goodreads', 'letterboxd', 'whatsapp', 'gmail', 'linkedin', 'strava', 'apple health', 'a photo', 'nothing needed']

CSS = '''
:root{--bg:#F4EEE3;--grid:rgba(0,127,157,.11);--card:#fff;--ink:#191512;--ink2:#4B443D;--mute:#6F6456;--line:#191512;--ac:#007F9D;--dash:#cfc7b8;--sticker:#FFD66B;--wave:#FF8A6B;--shadow:#191512;--rule:#d9ecf1;--on-ink:#FFF6E3}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#161513;--grid:rgba(98,196,220,.08);--card:#1f1e1b;--ink:#ece8de;--ink2:#cfc6b8;--mute:#9a9486;--line:#ece8de;--ac:#62C4DC;--dash:#4a463e;--shadow:#000;--rule:rgba(98,196,220,.12);--on-ink:#161513}}
:root[data-theme=dark]{--bg:#161513;--grid:rgba(98,196,220,.08);--card:#1f1e1b;--ink:#ece8de;--ink2:#cfc6b8;--mute:#9a9486;--line:#ece8de;--ac:#62C4DC;--dash:#4a463e;--shadow:#000;--rule:rgba(98,196,220,.12);--on-ink:#161513;color-scheme:dark}
:root[data-theme=light]{color-scheme:light}
*{box-sizing:border-box}
body{margin:0;font:16px/1.5 "Trebuchet MS",-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:28px 28px}
.w{max-width:1120px;margin:0 auto;padding:0 28px}a{color:inherit}
:focus-visible{outline:3px solid var(--ac);outline-offset:2px}
.rnd{font-family:"Arial Rounded MT Bold","Trebuchet MS",-apple-system,Helvetica,sans-serif}.mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.top{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:20px 0}
.logo{font:900 20px "Arial Rounded MT Bold","Trebuchet MS",sans-serif;color:var(--ac);letter-spacing:.02em;text-decoration:none}
.gh{display:inline-flex;gap:8px;align-items:center;border:2px solid var(--line);background:var(--card);color:var(--ink);border-radius:10px;padding:8px 14px;font-weight:800;text-decoration:none;font-size:15px}
.gh:hover{border-color:var(--ac)}
h1{font:900 clamp(40px,5.4vw,64px)/1.03 "Arial Rounded MT Bold","Trebuchet MS",sans-serif;margin:24px 0 28px}
h1 u{text-decoration:underline wavy var(--wave);text-underline-offset:9px}
.sub{font-size:19px;max-width:54ch;margin:0 0 18px}
.btn{display:block;background:var(--ink);color:var(--on-ink);border:0;border-radius:12px;padding:11px 20px;font:900 16px "Arial Rounded MT Bold","Trebuchet MS",sans-serif;text-decoration:none;text-align:center;cursor:pointer;width:100%}
.btn.p{background:var(--ac);color:#fff}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 4px}
.chip{border:2px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:6px 14px;font:700 14px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;cursor:pointer}
.chip[aria-pressed=true]{background:var(--ink);color:var(--on-ink)}
.note{font:13px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:var(--mute);margin:8px 0 18px}
.layout{display:grid;grid-template-columns:250px 1fr;gap:30px;align-items:start}
.nb{background:var(--card);border:2px solid var(--line);border-radius:12px;padding:20px 16px 20px 32px;position:relative;background-image:linear-gradient(var(--rule) 1px,transparent 1px);background-size:100% 26px}
.nb.first{box-shadow:5px 5px 0 var(--shadow)}.nb+.nb{margin-top:22px}
.nb:before{content:"";position:absolute;left:13px;top:10px;bottom:10px;border-left:3px dotted var(--line)}
.nb small{font:800 11px ui-monospace,Menlo,monospace;letter-spacing:.08em;color:var(--ac)}
.nb h3{font:900 20px "Arial Rounded MT Bold","Trebuchet MS",sans-serif;margin:2px 0 4px}.nb p{margin:4px 0 12px;font-size:14px}
.nb .btn+.btn{margin-top:10px}.nb a.plain{text-decoration:none;color:inherit;display:block}
.sec{font:800 14px ui-monospace,Menlo,monospace;letter-spacing:.08em;color:var(--ac);margin:30px 0 16px;text-transform:uppercase}.bench:first-child .sec{margin-top:2px}
.g{display:grid;grid-template-columns:repeat(3,1fr);gap:24px 22px}
.e{background:var(--card);border:2px solid var(--line);border-radius:12px;padding:16px;position:relative;text-decoration:none;color:inherit;display:block;transition:transform .12s}
.e:hover{transform:translate(-2px,-2px);box-shadow:4px 4px 0 var(--ac)}
.tag{font:800 11px ui-monospace,Menlo,monospace;letter-spacing:.08em;color:var(--ac)}
.st{position:absolute;top:-12px;right:12px;font:800 12px ui-monospace,Menlo,monospace;border:2px solid var(--line);border-radius:999px;padding:2px 10px;transform:rotate(3deg);background:var(--sticker);color:#191512}
.stat{font:900 28px "Arial Rounded MT Bold","Trebuchet MS",sans-serif;margin:8px 0 0}
.e h4{margin:6px 0 3px;font-size:18px}.e p{margin:0 0 10px;font-size:14px;color:var(--ink2)}
.need{font:12px ui-monospace,Menlo,monospace;color:var(--mute);border-top:2px dashed var(--dash);padding-top:8px}
.idea{background:var(--card);border:2px solid var(--line);border-radius:14px;padding:24px 26px;display:flex;justify-content:space-between;align-items:center;gap:20px;margin:34px 0 20px;box-shadow:6px 6px 0 var(--ac)}
.idea h3{margin:0;font:900 26px "Arial Rounded MT Bold","Trebuchet MS",sans-serif}.idea p{margin:4px 0 0}
.row{display:flex;gap:10px;flex-wrap:wrap}.idea .btn{width:auto;background:var(--sticker);color:#191512;border:2px solid var(--line)}
footer{padding:0 0 40px;font-weight:700;font-size:14px;color:var(--ink2)}
.theme{position:fixed;bottom:14px;right:14px;z-index:5;background:var(--card);color:var(--ink);border:2px solid var(--line);border-radius:999px;padding:6px 12px;font:inherit;font-size:13px;cursor:pointer}
[hidden]{display:none!important}
@media(max-width:820px){.layout{grid-template-columns:1fr}.g{grid-template-columns:repeat(2,1fr)}.idea{flex-direction:column;align-items:flex-start}.w{padding:0 16px}}
@media(max-width:560px){.g{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){.e{transition:none}.e:hover{transform:none}}
'''

JS = '''
(function(){
var cards=[].slice.call(document.querySelectorAll('.e')),chips=[].slice.call(document.querySelectorAll('.chip')),secs=[].slice.call(document.querySelectorAll('.bench'));
function apply(k){
  cards.forEach(function(c){var ks=c.getAttribute('data-k').split('|');c.hidden=!(k==='all'||(k==='nothing needed'?c.getAttribute('data-k')==='':ks.indexOf(k)>-1))});
  secs.forEach(function(s){s.hidden=!s.querySelector('.e:not([hidden])')});
  chips.forEach(function(c){c.setAttribute('aria-pressed',String(c.getAttribute('data-k')===k))});
  var n=cards.filter(function(c){return !c.hidden}).length;document.getElementById('count').textContent=k==='all'?'':'Showing '+n+(n===1?' experiment':' experiments')+' for '+k+'.';
}
chips.forEach(function(c){c.addEventListener('click',function(){var k=c.getAttribute('data-k');apply(c.getAttribute('aria-pressed')==='true'&&k!=='all'?'all':k)})});
var day=Math.floor(Date.now()/864e5),t=cards[day%cards.length];
var link=document.getElementById('today');
if(t){link.href=t.getAttribute('href');document.getElementById('today-name').textContent=t.querySelector('h4').textContent;document.getElementById('today-desc').textContent=t.querySelector('p').textContent}
document.getElementById('surprise').addEventListener('click',function(){var vis=cards.filter(function(c){return !c.hidden});location.href=vis[Math.floor(Math.random()*vis.length)].getAttribute('href')});
})();
'''

def render(meta, root_exists, theme_init, theme_js, og):
    slugs = [s for _, ss in SECTIONS for s in ss]
    assert sorted(slugs) == sorted(meta) == sorted(CARD) == sorted(ORDER), 'every tool must be in SECTIONS, CARD, ORDER and META'
    num = {s: i + 1 for i, s in enumerate(ORDER)}
    def card(s):
        title = meta[s][0]
        stat, keys, mins, pitch = CARD[s]
        need = ', '.join(keys) if keys else 'none'
        return ('<a class="e" href="%s/index.html" data-k="%s"><div class="tag">EXPERIMENT %02d</div><div class="st">%s</div>'
                '<div class="stat">%s</div><h4>%s</h4><p>%s</p><div class="need">Ingredients: %s</div></a>'
                % (s, '|'.join(keys), num[s], mins, html.escape(stat), html.escape(title), html.escape(pitch), html.escape(need)))
    secs = ''.join('<section class="bench"><h2 class="sec">%s</h2><div class="g">%s</div></section>'
                   % (name, ''.join(card(s) for s in ss if root_exists(s))) for name, ss in SECTIONS)
    chips = '<button type="button" class="chip" data-k="all" aria-pressed="true">all</button>' + ''.join(
        '<button type="button" class="chip" data-k="%s" aria-pressed="false">%s</button>' % (c, c) for c in CHIPS)
    nb = lambda s: '<a class="plain" href="%s/index.html"><h3>%s</h3><p>%s</p></a>' % (s, html.escape(meta[s][0]), html.escape(CARD[s][3]))
    desc = 'Small experiments that turn your own data into something worth sharing. Everything runs in your browser.'
    return ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>The Lab</title><meta name="description" content="%s">%s%s\n<style>%s</style></head>\n<body><div class="w">'
        '<div class="top"><a class="logo" href="./">HUSTLYST LAB</a><a class="gh" href="%s">%s GitHub</a></div>'
        '<h1>The Lab <u>notebook.</u></h1>'
        '<p class="sub">Small experiments on your own data. Pick what you have in your data drawer, drop in a file, see what pops out. Nothing leaves your browser.</p>'
        '<div class="chips" role="group" aria-label="Filter by what you have">%s</div>'
        '<p class="note">The numbers on the cards are examples. <span id="count" aria-live="polite"></span></p>'
        '<div class="layout"><div>'
        '<div class="nb first"><small>TODAY\'S EXPERIMENT</small><a class="plain" id="today" href="work-wrapped/index.html"><h3 id="today-name">Work Wrapped</h3><p id="today-desc">Your year in meetings, wrapped.</p></a>'
        '<a class="btn p" href="#" id="todaybtn" onclick="location.href=document.getElementById(\'today\').href;return false">Try it</a><button type="button" class="btn" id="surprise">Surprise me</button></div>'
        '<div class="nb"><small>NEWEST</small>%s</div><div class="nb"><small>NO FILE NEEDED</small>%s</div></div>'
        '<div>%s</div></div>'
        '<div class="idea"><div><h3>The next experiment could be yours.</h3><p>Pitch a daft idea, or help us build one.</p></div>'
        '<div class="row"><a class="btn" href="%s/issues/new?template=idea.yml">Submit an idea</a><a class="gh" href="%s/blob/main/CONTRIBUTING.md">%s Contribute</a></div></div>'
        '<footer>Free and open source. No accounts, no tracking. Nothing leaves your browser.<br><a href="https://hustlyst.com?ref=lab">Hustlyst</a> shows people who do not code how to use AI at work, one task at a time.</footer></div>'
        '<script>%s</script><script>(function(){%s})()</script></body></html>\n'
        % (html.escape(desc, True), og('The Lab', desc), theme_init, CSS, REPO, GH, chips, nb(NEWEST), nb(NOFILE), secs, REPO, REPO, GH, JS, theme_js))
