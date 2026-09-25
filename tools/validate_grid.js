/* ── canonical eras ─────────────────────────────────────────── */
const ERAS = [
  {id:'before-1500', label:'Before 1500',  a:'',     b:'1500'},
  {id:'1500s',       label:'The 1500s',    a:'1500', b:'1600'},
  {id:'1600s',       label:'The 1600s',    a:'1600', b:'1700'},
  {id:'1700-1750',   label:'1700 to 1750', a:'1700', b:'1750'},
  {id:'1750-1800',   label:'1750 to 1800', a:'1750', b:'1800'},
  {id:'1800-1850',   label:'1800 to 1850', a:'1800', b:'1850'},
  {id:'1850-1900',   label:'1850 to 1900', a:'1850', b:'1900'},
  {id:'1900-1950',   label:'1900 to 1950', a:'1900', b:'1950'},
  {id:'1950-2000',   label:'1950 to 2000', a:'1950', b:'2000'},
  {id:'2000-today',  label:'2000 to Today',a:'2000', b:'now'}
];
const ERA_IX = Object.fromEntries(ERAS.map((e,i)=>[e.id,i]));

/* ── era drift: sepia & earthen → cool & clean ──────────────── */
const DRIFT = [
  {p:'#EBDCBC', i:'#33281B', r:'#C4AC84', a:'#8A5A2B', t:'#E6D4AE'},
  {p:'#ECDEC0', i:'#322718', r:'#C5AE88', a:'#8F5730', t:'#E7D6B3'},
  {p:'#EDE0C5', i:'#302619', r:'#C6B08C', a:'#94512F', t:'#E8D9B9'},
  {p:'#EEE2CA', i:'#2E2519', r:'#C6B290', a:'#9A4C2E', t:'#E9DBBF'},
  {p:'#EFE4CF', i:'#2C241A', r:'#C6B494', a:'#9C4A2F', t:'#EADEC5'},
  {p:'#F0E6D4', i:'#2A2319', r:'#C5B698', a:'#8E4A38', t:'#EBE0CB'},
  {p:'#F0E8D9', i:'#28231A', r:'#C4B79C', a:'#7A4E45', t:'#EBE2D1'},
  {p:'#F1EADD', i:'#26231B', r:'#C2B8A1', a:'#5F5257', t:'#ECE4D7'},
  {p:'#F1ECE2', i:'#24231D', r:'#BFB8A5', a:'#48546A', t:'#ECE6DC'},
  {p:'#F2EEE7', i:'#22231F', r:'#BCB8A9', a:'#33456B', t:'#EDE8E1'}
];

/* ── world metrics ──────────────────────────────────────────── */
let   COL_W  = 700;
let   GUT    = 96;
const HEAD_H = 86;
const PAGE_GAP = 54;
const MIN_ROW  = 360;
const ZMAX   = 2.2;
const FAR    = 0.38;

/* ══════════════════════════════════════════════════════════════
   1 · PARSER
   ══════════════════════════════════════════════════════════════ */
const RE_MARK = /^\s*<!--\s*(\/?)(hb-[a-z]+)(:start|:end)?\s*([\s\S]*?)\s*-->\s*$/;
const RE_ATTR = /([\w-]+)\s*=\s*"([^"]*)"/g;

function attrs(s){
  const o={}; let m; RE_ATTR.lastIndex=0;
  while((m=RE_ATTR.exec(s))) o[m[1]]=m[2];
  return o;
}

function parseGrid(text, srcName){
  const lines = text.replace(/\r\n?/g,'\n').split('\n');
  const errs = [], chapters = [];
  let book=null, ch=null, era=null, blk=null, note=null, buf=[];
  const stack=[];

  const flushBlk = ()=>{
    if(!blk) return;
    blk.md = buf.join('\n').trim();
    buf=[];
    if(era) era.blocks.push(blk);
    blk=null;
  };

  for(let i=0;i<lines.length;i++){
    const ln=lines[i], no=i+1;
    const m = ln.match(RE_MARK);

    if(!m){
      if(blk||note) buf.push(ln);
      continue;
    }
    const [,slash,name,se,tail]=m;
    if(!name.startsWith('hb-')){ if(blk||note) buf.push(ln); continue; }
    const A = attrs(tail);
    const opening = se===':start' || (!se && !slash && (name==='hb-note'||name==='hb-zoom'));
    const closing = se===':end'   || (!!slash);

    if(name==='hb-chapter'){
      flushBlk();
      ch = {id:A.id||String(chapters.length+1).padStart(2,'0'), slug:A.slug||('lens-'+chapters.length),
            title:A.title||A.slug||'Untitled', mode:A.mode||'prose', note:'', eras:{}, line:no};
      const prev = chapters.find(c=>c.slug===ch.slug);
      if(prev){ ch=prev; }              // part files merge by slug
      else chapters.push(ch);
      continue;
    }

    if(name==='hb-note'){
      if(opening){ note={line:no}; buf=[]; stack.push('note'); }
      else{
        const txt = buf.join('\n').trim(); buf=[];
        if(ch && !era) ch.note = (ch.note?ch.note+'\n\n':'')+txt;
        else if(!ch)   book = (book?book+'\n\n':'')+txt;
        else if(era)   era.note = txt;
        note=null; stack.pop();
      }
      continue;
    }

    if(name==='hb-time'){
      if(opening){
        flushBlk();
        const id=A.id;
        if(!(id in ERA_IX)) errs.push(`L${no}: unknown era id "${id}"`);
        if(A.chapter && ch && A.chapter!==ch.slug)
          errs.push(`L${no}: hb-time chapter="${A.chapter}" inside chapter "${ch.slug}"`);
        era={id, order:A.order, label:A.label||(ERAS[ERA_IX[id]]||{}).label||id,
             state:A.state||'full', progress:A.progress||'', blocks:[], note:'', line:no};
        if(!['full','thin','empty'].includes(era.state))
          errs.push(`L${no}: state="${era.state}" is not full / thin / empty`);
        if(ch) ch.eras[id]=era;
        stack.push('time');
      }else{
        flushBlk();
        if(A.id && era && A.id!==era.id) errs.push(`L${no}: hb-time:end id="${A.id}" closes "${era.id}"`);
        era=null; stack.pop();
      }
      continue;
    }

    if(name==='hb-zoom'){
      if(opening){
        flushBlk();
        const lv=A.level||'era';
        if(!['era','span'].includes(lv)) errs.push(`L${no}: zoom level="${lv}" is not era / span`);
        blk={type:'zoom', level:lv, label:A.label||'', line:no};
        buf=[];
      }else flushBlk();
      continue;
    }

    if(name==='hb-story'){
      if(opening){
        flushBlk();
        blk={type:'story', slug:A.slug||'', name:A.name||'', movie:A.movie||'',
             kind:A.kind||'', status:A.status||'', line:no};
        buf=[];
      }else{
        if(A.slug && blk && A.slug!==blk.slug) errs.push(`L${no}: hb-story:end slug mismatch`);
        flushBlk();
      }
      continue;
    }
  }
  if(stack.length) errs.push(`${stack.length} block(s) never closed: ${stack.join(', ')}`);

  /* completeness + slug uniqueness */
  const seen={};
  chapters.forEach(c=>{
    const miss = ERAS.filter(e=>!c.eras[e.id]).map(e=>e.id);
    // A PART FILE legitimately holds only some eras; the viewer merges parts by slug.
    // Reporting that as an error taught agents to ignore errors, so --part suppresses
    // THIS check only. Every other check still applies at full strictness.
    if(miss.length && !global.__HB_PART_MODE)
      errs.push(`${c.slug}: missing ${miss.length} era(s) — ${miss.join(', ')}`);
    ERAS.forEach(e=>{
      const E=c.eras[e.id]; if(!E) return;
      E.blocks.forEach(b=>{
        if(b.type!=='story') return;
        if(!b.slug) return;
        if(seen[b.slug]) errs.push(`story slug "${b.slug}" used in ${seen[b.slug]} and ${c.slug}`);
        else seen[b.slug]=c.slug;
      });
    });
  });
  if(!chapters.length) errs.push('No hb-chapter declaration found — is this a grid file?');

  chapters.sort((a,b)=> (a.id||'').localeCompare(b.id||''));
  return {book, chapters, errs, src:srcName||''};
}


const fs=require('fs');
// --part: this file is one part of a multi-file chapter, so do not require all ten
// eras. Nothing else is relaxed. Without this flag a part file always reported a
// false error, which is how agents learned to wave errors through.
let args = process.argv.slice(2);
global.__HB_PART_MODE = args.includes('--part');
args = args.filter(a => a !== '--part');
let totalErrs=0;
for(const f of args){
  const g=parseGrid(fs.readFileSync(f,'utf8'), f);
  const stories=g.chapters.reduce((n,c)=>n+Object.values(c.eras).reduce((m,e)=>m+e.blocks.filter(b=>b.type==='story').length,0),0);
  console.log(`\n=== ${f.split(/[\/]/).pop()} : ${g.chapters.length} chapters, ${stories} stories, ${g.errs.length} errors`);
  g.errs.slice(0,25).forEach(e=>console.log('  ERR:', e));
  totalErrs += g.errs.length;
}
// Exit non-zero when anything failed, so loops and CI cannot silently pass.
// (Until 2026-09-06 this script always exited 0 - see control/RESUME.md.)
process.exit(totalErrs > 0 ? Math.min(totalErrs, 100) : 0);
