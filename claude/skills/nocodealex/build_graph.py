"""Render graph.html from atoms.jsonl + edges.jsonl. Generated, never hand-edited.

Force-directed canvas: nodes coloured by topic, sized by edge degree; hover shows the atom
text / type / confidence and a link to its source (YouTube short, chen.media guide, or GitHub
repo). Filter by topic, type, confidence, source kind, or free text. Repulsion uses a spatial
hash so thousands of atoms stay interactive, and the layout cools to a stop.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
PALETTE = ["#7aa2ff", "#ff9e64", "#9ece6a", "#f7768e", "#bb9af7", "#e0af68", "#2ac3de"]


def load(name: str) -> list[dict]:
    p = HERE / name
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()] if p.exists() else []


def main() -> None:
    atoms, edges = load("atoms.jsonl"), load("edges.jsonl")
    manifest = json.loads((HERE / "sources" / "manifest.json").read_text(encoding="utf-8"))
    url = {it["id"]: (it["url"], it["kind"]) for it in manifest["items"]}
    ids = {a["id"] for a in atoms}
    edges = [e for e in edges if e["from"] in ids and e["to"] in ids]
    topics = sorted({a["topic"] for a in atoms})
    colour = {t: PALETTE[i % len(PALETTE)] for i, t in enumerate(topics)}

    nodes = []
    for a in atoms:
        src = (a.get("sources") or [""])[0]
        link, kind = url.get(src, ("", ""))
        nodes.append({"id": a["id"], "t": a["type"], "tp": a["topic"], "c": a["confidence"],
                      "x": a["text"], "u": link, "k": kind, "col": colour[a["topic"]]})
    links = [{"s": e["from"], "t": e["to"], "r": e["rel"]} for e in edges]

    html = """<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>nocodealex brain — atom graph</title>
<style>
 :root{color-scheme:dark;--bg:#0b0c10;--panel:#14161dcc;--line:#2a2e3d;--ink:#d6dbea;--mute:#8a91a8;--hot:#ff9e64}
 body{margin:0;background:var(--bg);color:var(--ink);font:13px/1.5 ui-sans-serif,system-ui,-apple-system,Segoe UI}
 #bar{position:fixed;inset:0 0 auto 0;padding:10px 14px;background:var(--panel);backdrop-filter:blur(14px) saturate(1.4);
      border-bottom:1px solid var(--line);display:flex;gap:8px;align-items:center;flex-wrap:wrap;z-index:9}
 #bar b{letter-spacing:.02em;margin-right:6px}
 select,input{background:#1b1e28;color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:5px 9px;font:inherit}
 canvas{display:block;cursor:grab} canvas:active{cursor:grabbing}
 #tip{position:fixed;max-width:400px;padding:12px 14px;background:#161925f2;border:1px solid #3a3f55;border-radius:12px;
      box-shadow:0 18px 40px #0008;pointer-events:none;opacity:0;transition:opacity .12s;font-size:12.5px;z-index:20}
 #tip b{color:var(--hot)} #tip a{color:#7aa2ff}
 #stat{margin-left:auto;color:var(--mute)}
</style>
<div id=bar><b>nocodealex</b>
 <select id=topic></select><select id=type></select><select id=conf></select><select id=kind></select>
 <input id=q placeholder="search atoms…" size=24><span id=stat></span></div>
<canvas id=c></canvas><div id=tip></div>
<script>
const NODES=__NODES__, LINKS=__LINKS__;
const deg={}; LINKS.forEach(l=>{deg[l.s]=(deg[l.s]||0)+1;deg[l.t]=(deg[l.t]||0)+1});
const byId={}; NODES.forEach(n=>{n.d=deg[n.id]||0;n.r=3+Math.min(10,Math.sqrt(n.d)*2.2);byId[n.id]=n});
const c=document.getElementById('c'),g=c.getContext('2d'),dpr=devicePixelRatio||1;
let W,H; function size(){W=innerWidth;H=innerHeight;c.width=W*dpr;c.height=H*dpr;c.style.width=W+'px';c.style.height=H+'px'} size();
addEventListener('resize',size);
NODES.forEach((n,i)=>{const a=i*2.399,r=Math.sqrt(i)*9;n.px=W/2+r*Math.cos(a);n.py=H/2+r*Math.sin(a);n.vx=0;n.vy=0});
function fill(id,vals,label){document.getElementById(id).innerHTML='<option value="">'+label+'</option>'+vals.map(v=>`<option>${v}</option>`).join('')}
const uniq=k=>[...new Set(NODES.map(n=>n[k]))].filter(Boolean).sort();
fill('topic',uniq('tp'),'all topics');fill('type',uniq('t'),'all types');fill('conf',['CORE','STATED','INFERRED'],'all confidence');fill('kind',uniq('k'),'all sources');
let vis=new Set();
function refilter(){const f={tp:topic.value,t:type.value,c:conf.value,k:kind.value},qq=q.value.toLowerCase();
 vis=new Set(NODES.filter(n=>Object.entries(f).every(([k,v])=>!v||n[k]==v)&&(!qq||n.x.toLowerCase().includes(qq))).map(n=>n.id));
 stat.textContent=vis.size+' / '+NODES.length+' atoms · '+LINKS.length+' edges'}
['topic','type','conf','kind','q'].forEach(id=>document.getElementById(id).oninput=refilter); refilter();
let cam={x:0,y:0,z:.8},drag=null,heat=1;
c.onmousedown=e=>drag={x:e.clientX,y:e.clientY,cx:cam.x,cy:cam.y}; onmouseup=()=>drag=null;
c.onwheel=e=>{e.preventDefault();cam.z=Math.max(.08,Math.min(6,cam.z*(e.deltaY<0?1.12:.89)))};
const tip=document.getElementById('tip'), toWorld=(x,y)=>[(x-W/2)/cam.z-cam.x+W/2,(y-H/2)/cam.z-cam.y+H/2];
let hover=null;
c.onmousemove=e=>{ if(drag){cam.x=drag.cx+(e.clientX-drag.x)/cam.z;cam.y=drag.cy+(e.clientY-drag.y)/cam.z;return}
 const [mx,my]=toWorld(e.clientX,e.clientY); hover=null;
 for(const n of NODES){if(!vis.has(n.id))continue;if((n.px-mx)**2+(n.py-my)**2<(n.r+3)**2){hover=n;break}}
 if(hover){tip.style.opacity=1;tip.style.left=Math.min(W-420,e.clientX+16)+'px';tip.style.top=Math.min(H-160,e.clientY+16)+'px';
  tip.innerHTML=`<b>${hover.t}</b> · ${hover.c} · ${hover.tp}<br><br>${hover.x}`+(hover.u?`<br><br><a href="${hover.u}" target=_blank>${hover.u.replace('https://','')}</a>`:'')}
 else tip.style.opacity=0};
c.onclick=()=>{if(hover&&hover.u)open(hover.u,'_blank')};
const CELL=60;
function step(){
 if(heat>0.02){const grid=new Map();
  for(const n of NODES){const k=((n.px/CELL)|0)+','+((n.py/CELL)|0);(grid.get(k)||grid.set(k,[]).get(k)).push(n)}
  for(const n of NODES){const gx=(n.px/CELL)|0,gy=(n.py/CELL)|0;
   for(let dx=-1;dx<=1;dx++)for(let dy=-1;dy<=1;dy++){const cell=grid.get((gx+dx)+','+(gy+dy));if(!cell)continue;
    for(const m of cell){if(m===n)continue;const ddx=n.px-m.px,ddy=n.py-m.py,d2=ddx*ddx+ddy*ddy||1;const f=90/d2;n.vx+=ddx*f;n.vy+=ddy*f}}}
  for(const l of LINKS){const a=byId[l.s],b=byId[l.t];const dx=b.px-a.px,dy=b.py-a.py,d=Math.hypot(dx,dy)||1,f=(d-34)*.004;
   a.vx+=dx*f;a.vy+=dy*f;b.vx-=dx*f;b.vy-=dy*f}
  for(const n of NODES){n.vx+=(W/2-n.px)*.0006;n.vy+=(H/2-n.py)*.0006;n.px+=(n.vx*=.82)*heat;n.py+=(n.vy*=.82)*heat}
  heat*=.996}
 g.setTransform(dpr,0,0,dpr,0,0);g.fillStyle='#0b0c10';g.fillRect(0,0,W,H);
 g.setTransform(cam.z*dpr,0,0,cam.z*dpr,dpr*(W/2-cam.z*(W/2-cam.x)),dpr*(H/2-cam.z*(H/2-cam.y)));
 g.strokeStyle='#2a2e3d';g.lineWidth=.6/cam.z;g.beginPath();
 for(const l of LINKS){if(!vis.has(l.s)||!vis.has(l.t))continue;const a=byId[l.s],b=byId[l.t];g.moveTo(a.px,a.py);g.lineTo(b.px,b.py)}
 g.stroke();
 for(const n of NODES){g.globalAlpha=vis.has(n.id)?1:.06;g.beginPath();g.arc(n.px,n.py,n.r,0,6.283);g.fillStyle=n.col;g.fill()}
 g.globalAlpha=1;requestAnimationFrame(step)}
step();
</script>"""
    html = html.replace("__NODES__", json.dumps(nodes, ensure_ascii=False)).replace("__LINKS__", json.dumps(links))
    (HERE / "graph.html").write_text(html, encoding="utf-8")
    print(f"graph.html: {len(nodes)} nodes, {len(links)} edges")


if __name__ == "__main__":
    main()
