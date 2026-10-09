import React, {useEffect, useRef, useState} from 'react';
import {createRoot} from 'react-dom/client';
import {marked} from 'marked';
import DOMPurify from 'dompurify';
import {PanelLeft, Plus, MessageSquare, Library, FileText, Search, ArrowUp, Square, RefreshCw, ChevronRight, ChevronDown, X, Code2, FlaskConical, ClipboardList, Check, Copy, Download, BookOpen, CircleHelp, Loader2, FolderGit2, ExternalLink, Sparkles, Save} from 'lucide-react';
import './style.css';

const MODES = [{id:'ask',label:'自由提问',icon:MessageSquare},{id:'requirement',label:'需求分析',icon:ClipboardList},{id:'code',label:'代码分析',icon:Code2},{id:'test',label:'测试设计',icon:FlaskConical}];
const KINDS={requirement:'现状需求',code:'源代码',test:'测试代码',reference:'参考文档'};
const MODULES={account:'账户与身份',security:'安全与风控',assets:'资产与钱包',exchange:'兑换与闪兑',trading:'现货与市场',margin:'杠杆与借贷',perpetual:'合约',p2p:'法币与 P2P',investment:'理财与策略',operation:'运营与消息',platform:'平台与其他'};
const PROMPTS=[
 {icon:ClipboardList,mode:'requirement',title:'梳理现有业务规则',text:'根据现有代码，梳理兑换订单的业务规则和待确认需求。'},
 {icon:Code2,mode:'code',title:'读懂一段业务实现',text:'兑换订单如何处理并发请求？请找到代码和已有测试依据。'},
 {icon:FlaskConical,mode:'test',title:'补齐关键测试场景',text:'为安全资料重置流程设计测试用例，区分现有行为和待确认预期。'},
];
async function api(path, options={}) {
 const response=await fetch('/api'+path,{...options,headers:{'Content-Type':'application/json',...options.headers}});
 const data=await response.json(); if(!response.ok) throw new Error(typeof data.detail==='string'?data.detail:'请求失败，请重试'); return data;
}
function download(name, text){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([text],{type:'text/markdown;charset=utf-8'}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);}
function Markdown({text, sources=[], onSource}) {
 const content=text.replace(/\[S(\d+)\]/g,(all,n)=>sources[Number(n)-1]?`[${all.slice(1,-1)}](#source-${Number(n)-1})`:all);
 const html=DOMPurify.sanitize(marked.parse(content),{FORBID_TAGS:['img','iframe','style'],FORBID_ATTR:['style'],ADD_ATTR:['target']});
 return <div className="markdown" onClick={e=>{const link=e.target.closest('a');if(!link)return;const href=link.getAttribute('href')||'';if(href.startsWith('#source-')){e.preventDefault();onSource?.(sources[Number(href.slice(8))]);}else if(href.startsWith('/api/sources/')){e.preventDefault();onSource?.({source_id:href.split('/').pop()});}else if(!href.startsWith('https://')&&!href.startsWith('http://')){e.preventDefault();}else{e.preventDefault();window.open(href,'_blank','noopener,noreferrer');}}} dangerouslySetInnerHTML={{__html:html}}/>;
}
function App(){
 const [status,setStatus]=useState(null),[conversations,setConversations]=useState([]),[current,setCurrent]=useState(null),[cid,setCid]=useState(null);
 const [page,setPage]=useState('chat'),[mode,setMode]=useState('ask'),[text,setText]=useState(''),[sending,setSending]=useState(false),[toast,setToast]=useState('');
 const [sidebar,setSidebar]=useState(()=>window.innerWidth>=760),[source,setSource]=useState(null),[sourceLoading,setSourceLoading]=useState(false),[highlight,setHighlight]=useState(null),[help,setHelp]=useState(false);
 const [syncJob,setSyncJob]=useState(null),[items,setItems]=useState([]),[total,setTotal]=useState(0),[query,setQuery]=useState(''),[kind,setKind]=useState(''),[module,setModule]=useState(''),[loading,setLoading]=useState(false),[searching,setSearching]=useState(false);
 const bottom=useRef(null),input=useRef(null),activeId=useRef(null),sourceSeq=useRef(0);
 const job=current?.job, busy=job&&['running','queued'].includes(job.status);
 function notify(message){setToast(message);}
 useEffect(()=>{if(!toast)return;const t=setTimeout(()=>setToast(''),4500);return()=>clearTimeout(t);},[toast]);
 async function refreshStatus(){try{const s=await api('/status');setStatus(s);const sync=s.jobs.find(j=>j.kind==='sync');if(sync)setSyncJob(sync);}catch(e){notify(e.message);}}
 async function refreshConversations(){setConversations(await api('/conversations'));}
 async function loadConversation(id){const c=await api('/conversations/'+id);if(activeId.current===id)setCurrent(c);return c;}
 useEffect(()=>{refreshStatus();refreshConversations().catch(e=>notify(e.message));},[]);
 useEffect(()=>{activeId.current=cid;if(cid){setCurrent(null);loadConversation(cid).catch(e=>notify(e.message));}else setCurrent(null);},[cid]);
 useEffect(()=>{bottom.current?.scrollIntoView({behavior:'smooth'});},[current?.messages?.length,job?.stage]);
 useEffect(()=>{
  if(!busy)return;
  const event=new EventSource('/api/jobs/'+job.id+'/events');
  event.onmessage=e=>{const next=JSON.parse(e.data);setCurrent(c=>c?.id===cid?{...c,job:next}:c);if(!['running','queued'].includes(next.status)){event.close();loadConversation(cid).catch(e=>notify(e.message));refreshConversations().catch(()=>{});}};
  event.onerror=()=>{event.close();loadConversation(cid).catch(e=>notify(e.message));};
  const fallback=setInterval(()=>loadConversation(cid).catch(()=>{}),5000);
  return()=>{event.close();clearInterval(fallback);};
 },[job?.id,busy,cid]);
 useEffect(()=>{
  if(!syncJob||!['queued','running'].includes(syncJob.status))return;
  const t=setInterval(async()=>{try{const j=await api('/jobs/'+syncJob.id);setSyncJob(j);if(!['running','queued'].includes(j.status)){await refreshStatus();if(j.status==='done'){notify('知识库已更新');setQuery(q=>q+' ');}else notify(j.error||'同步失败');}}catch(e){notify(e.message);}},1800);
  return()=>clearInterval(t);
 },[syncJob?.id,syncJob?.status]);
 useEffect(()=>{
  if(!['library','requirements'].includes(page))return;
  let stale=false;const timer=setTimeout(async()=>{setLoading(true);try{
    const params=new URLSearchParams({q:query.trim(),kind:page==='requirements'?'requirement':kind,module,limit:'100'});
    const result=await api((searching?'/search?':'/sources?')+params);if(!stale){setItems(result.items);setTotal(searching?result.items.length:result.total);}
  }catch(e){if(!stale)notify(e.message);}finally{if(!stale)setLoading(false);}},200);
  return()=>{stale=true;clearTimeout(timer);};
 },[page,query,kind,module,searching,status?.sync?.synced_at]);
 useEffect(()=>{function key(e){if(e.key==='Escape'){setSource(null);setHelp(false);}if((e.metaKey||e.ctrlKey)&&e.key==='k'){e.preventDefault();setPage('library');setQuery('');}if((e.metaKey||e.ctrlKey)&&e.key==='Enter'){e.preventDefault();setCid(null);setCurrent(null);setText('');setPage('chat');setSource(null);}}window.addEventListener('keydown',key);return()=>window.removeEventListener('keydown',key);},[]);
 async function openSource(item){if(!item)return;const seq=++sourceSeq.current;setSourceLoading(true);setSource(null);setHighlight(item.start_line?{start:item.start_line,end:item.end_line}:null);try{const s=await api('/sources/'+(item.source_id||item.id));if(seq===sourceSeq.current)setSource(s);}catch(e){notify(e.message);}finally{if(seq===sourceSeq.current)setSourceLoading(false);}}
 useEffect(()=>{if(source&&highlight)setTimeout(()=>document.querySelector('.source-line.highlight')?.scrollIntoView({block:'center'}),80);},[source]);
 function navigate(next){setPage(next);setQuery('');setKind('');setModule('');setSearching(false);setSource(null);if(window.innerWidth<760)setSidebar(false);}
 function fresh(){setCid(null);setCurrent(null);setText('');navigate('chat');setTimeout(()=>input.current?.focus(),100);}
 async function send(value=text, nextMode=mode){
  if(!value.trim()||sending||busy)return;setSending(true);setPage('chat');
  try{let id=cid;if(!id){const c=await api('/conversations',{method:'POST',body:JSON.stringify({mode:nextMode})});id=c.id;activeId.current=id;setCid(id);}
   await api('/conversations/'+id+'/messages',{method:'POST',body:JSON.stringify({content:value,mode:nextMode})});setText('');setMode(nextMode);await loadConversation(id);await refreshConversations();
  }catch(e){notify(e.message);}finally{setSending(false);}
 }
 async function sync(){try{const j=await api('/sync',{method:'POST',body:'{}'});setSyncJob({...j,status:'queued'});}catch(e){notify(e.message);}}
 function searchContent(){if(query.trim())setSearching(true);}
 async function loadMore(){setLoading(true);try{const r=await api('/sources?'+new URLSearchParams({q:query.trim(),kind:page==='requirements'?'requirement':kind,module,limit:'100',offset:String(items.length)}));setItems(old=>[...old,...r.items]);setTotal(r.total);}catch(e){notify(e.message);}finally{setLoading(false);}}
 async function saveMessage(m){try{const r=await api('/messages/'+m.id+'/save',{method:'POST',body:JSON.stringify({title:current.title})});notify('已保存为知识库草稿');await refreshStatus();openSource({id:r.id});}catch(e){notify(e.message);}}
 const syncing=syncJob&&['queued','running'].includes(syncJob.status);
 const counts=status?.counts||{};
 const sourcePanel=source||sourceLoading;
 return <div className={'app '+(!sidebar?'collapsed ':'')+(sourcePanel?'has-source':'')}>
  {sidebar&&<aside className="sidebar">
   <div className="brand"><div className="brand-mark"><BookOpen size={21}/></div><span>知间<span className="brand-sub">研发知识库</span></span><button className="icon-button collapse" title="收起侧栏" onClick={()=>setSidebar(false)}><PanelLeft size={18}/></button></div>
   <button className="new-chat" onClick={fresh}><Plus size={17}/>新对话<span>⌘ ↵</span></button>
   <nav><button className={page==='chat'?'active':''} onClick={()=>navigate('chat')}><MessageSquare size={17}/>对话分析</button><button className={page==='library'?'active':''} onClick={()=>navigate('library')}><Library size={17}/>知识库<span className="count">{Object.values(counts).reduce((a,b)=>a+b,0)||'—'}</span></button><button className={page==='requirements'?'active':''} onClick={()=>navigate('requirements')}><FileText size={17}/>现状需求<span className="count">{counts.requirement||'—'}</span></button></nav>
   <div className="history-label">最近对话</div><div className="history">{!conversations.length?<p>从一个业务问题开始</p>:conversations.map(c=><button key={c.id} className={cid===c.id&&page==='chat'?'selected':''} onClick={()=>{setCid(c.id);setMode(c.mode);navigate('chat');}} title={c.title}>{c.title}</button>)}</div>
   <div className="sidebar-bottom"><div className="project-card"><FolderGit2 size={17}/><div><strong>coinex_backend</strong><span>{status?.sync?'本地代码已连接':'等待同步代码'}</span></div><span className="project-tag">只读</span></div><button className="help-button" onClick={()=>setHelp(true)}><CircleHelp size={16}/>关于这个工作台</button></div>
  </aside>}
  {sidebar&&<div className="mobile-overlay" onClick={()=>setSidebar(false)}/>}
  <main>
   <header><div className="breadcrumb">{!sidebar&&<button className="icon-button" aria-label="展开侧栏" onClick={()=>setSidebar(true)}><PanelLeft size={19}/></button>}<span>coinex_backend</span><ChevronRight size={13}/><strong>{page==='chat'?'对话分析':page==='library'?'知识库':'现状需求'}</strong></div><div className="header-right"><span className={'connection '+(status?.codex.ready?'ready':'')}><i/>{status?status.codex.ready?'Codex 已连接':'Codex 未连接':'正在连接'}</span><button className="icon-button" title="刷新连接状态" onClick={refreshStatus}><RefreshCw size={15}/></button></div></header>
   {page==='chat'?<>
    <div className={'conversation '+(!current?.messages?.length?'empty':'')}>
     {!current?.messages?.length?<div className="welcome"><div className="welcome-icon"><BookOpen size={29} strokeWidth={1.6}/></div><div className="eyebrow">代码里的知识，团队的共同语言</div><h1>今天想了解哪个业务？</h1><p>从需求到实现，让每一个回答都有据可查。</p><div className="suggestions">{PROMPTS.map(p=><button key={p.mode} onClick={()=>{setMode(p.mode);setText(p.text);input.current?.focus();}}><p.icon size={19} strokeWidth={1.6}/><strong>{p.title}</strong><span>{p.text}</span><ChevronRight size={15} className="suggestion-arrow"/></button>)}</div><div className="knowledge-note"><span className="mini-dot"/>已连接项目知识{status?.sync&&<><span>·</span>{counts.requirement||0} 份需求草稿<span>·</span>{(counts.code||0)+(counts.test||0)} 个代码文件</>}</div>{status&&!status.sync&&<button className="primary" onClick={sync} disabled={syncing}>{syncing?'正在建立知识库…':'建立知识库'}</button>}</div>:
      <div className="messages">{current.messages.map(m=><article key={m.id} className={'message '+m.role}>{m.role==='user'?<div className="user-content">{m.content}</div>:<><div className="assistant-label"><div className="assistant-mark"><BookOpen size={16}/></div><strong>知间</strong><span>基于项目知识</span></div><Markdown text={m.content} sources={m.sources} onSource={openSource}/>{m.sources.length>0&&<details className="citations"><summary><Library size={14}/>{m.sources.length} 处检索依据<ChevronDown size={14}/></summary><div>{m.sources.map((s,i)=><button key={i} onClick={()=>openSource(s)}><span>S{i+1}</span><Code2 size={13}/><span>{s.path}:{s.start_line}</span><ChevronRight size={13}/></button>)}</div></details>}<div className="message-actions"><button onClick={()=>navigator.clipboard.writeText(m.content).then(()=>notify('已复制')).catch(()=>notify('复制失败，请手动选择文本'))}><Copy size={14}/>复制</button><button onClick={()=>saveMessage(m)}><Save size={14}/>存为知识草稿</button><button onClick={()=>download(current.title+'.md',m.content+'\n\n'+m.sources.map((s,i)=>`[S${i+1}] ${s.path}:${s.start_line} · ${s.version}`).join('\n'))}><Download size={14}/>导出</button></div></>}</article>)}
      {busy&&<div className="working" role="status"><Loader2 size={17} className="spin"/><div><strong>{job.stage}</strong><span>读取已索引的资料，核对代码与业务规则</span></div></div>}
      {job?.status==='error'&&<div className="error-box" role="alert"><strong>{job.stage}</strong><p>{job.error}</p><button onClick={()=>send([...current.messages].reverse().find(m=>m.role==='user')?.content||'')}>重新分析</button></div>}
      {job?.status==='cancelled'&&<div className="stopped">本次分析已停止。可以修改问题后再次发送。</div>}<div ref={bottom}/></div>}
    </div>
    <div className="composer-wrap"><form className={'composer '+(busy?'is-busy':'')} onSubmit={e=>{e.preventDefault();send();}}><textarea ref={input} rows={2} value={text} onChange={e=>setText(e.target.value)} placeholder="询问业务规则、分析代码，或描述一个新需求…" aria-label="输入问题" onKeyDown={e=>{if(e.key==='Enter'&&!e.shiftKey&&!e.nativeEvent.isComposing){e.preventDefault();send();}}}/><div className="composer-toolbar"><div className="modes">{MODES.map(m=><button key={m.id} type="button" className={mode===m.id?'selected':''} onClick={()=>setMode(m.id)} disabled={busy}><m.icon size={14}/><span>{m.label}</span></button>)}</div>{busy?<button type="button" className="send stop" aria-label="停止分析" onClick={()=>api('/jobs/'+job.id+'/cancel',{method:'POST',body:'{}'}).then(()=>loadConversation(cid)).catch(e=>notify(e.message))}><Square size={15} fill="currentColor"/></button>:<button className="send" type="submit" aria-label="发送问题" disabled={!text.trim()||sending||!status?.sync}>{sending?<Loader2 className="spin" size={19}/>:<ArrowUp size={20}/>}</button>}</div></form><div className="composer-note"><span>回答附代码依据 · 需求文档为待确认草稿</span><span>Enter 发送 · Shift + Enter 换行</span></div></div>
   </>:<section className="library-page"><div className="page-heading"><div><div className="eyebrow">{page==='library'?'PROJECT KNOWLEDGE':'AS-BUILT REQUIREMENTS'}</div><h1>{page==='library'?'团队的知识，放在一起。':'从实现出发，梳理业务。'}</h1><p>{page==='library'?'检索需求、业务代码与测试，回到每个结论的出处。':'根据当前代码反推的需求草稿，保留依据和待确认事项。'}</p></div><button className="secondary" onClick={sync} disabled={syncing}><RefreshCw size={15} className={syncing?'spin':''}/>{syncing?'同步中…':'同步知识库'}</button></div>
    <div className="library-stats"><div><span>需求草稿</span><strong>{counts.requirement||0}<small>份</small></strong></div><div><span>业务代码</span><strong>{counts.code||0}<small>个文件</small></strong></div><div><span>测试代码</span><strong>{counts.test||0}<small>个文件</small></strong></div><div className="snapshot"><span>当前快照</span><strong>{status?.sync?.commit?.slice(0,8)||'未同步'}</strong><small>{status?.sync?.synced_at?new Date(status.sync.synced_at).toLocaleString('zh-CN',{month:'short',day:'numeric',hour:'2-digit',minute:'2-digit'}):'点击同步建立索引'}</small></div></div>
    {page==='requirements'&&<div className="draft-banner"><ClipboardList size={18}/><p><strong>现状 ≠ 已确认的产品规则</strong><span>模块清单来自静态提取；兑换、安全重置另有详细规则与验收建议。所有文档均待评审。</span></p></div>}
    <div className="filters"><div className="search-input"><Search size={17}/><input value={query} onChange={e=>{setQuery(e.target.value);setSearching(false);}} onKeyDown={e=>{if(e.key==='Enter')searchContent();}} placeholder="搜索名称，按 Enter 检索正文" aria-label="搜索知识库"/>{query&&<button aria-label="清除搜索" onClick={()=>{setQuery('');setSearching(false);}}><X size={14}/></button>}</div>{page==='library'&&<select aria-label="资料类型" value={kind} onChange={e=>setKind(e.target.value)}><option value="">全部类型</option>{Object.entries(KINDS).map(([k,v])=><option value={k} key={k}>{v}</option>)}</select>}<select aria-label="业务模块" value={module} onChange={e=>setModule(e.target.value)}><option value="">全部模块</option>{Object.entries(MODULES).map(([k,v])=><option value={k} key={k}>{v}</option>)}</select></div>
    <div className="results-label">{searching?'正文检索结果':'知识条目'}<span>{total} {searching?'处匹配':'个条目'}{total>items.length?' · 当前显示 '+items.length+' 个':''}</span></div>
    <div className="source-list">{loading?<div className="list-empty"><Loader2 className="spin" size={20}/>正在查找资料…</div>:!items.length?<div className="list-empty"><Search size={24}/><strong>没有找到相关资料</strong><span>试试业务名称或函数名，如“兑换”、swap。</span>{query&&<button className="secondary" onClick={searchContent}>检索正文</button>}</div>:items.map((s,i)=><button className="source-row" key={s.id||s.chunk_id||i} onClick={()=>openSource(s)}><div className={'file-icon '+s.kind}>{s.kind==='requirement'?<FileText size={20}/>:s.kind==='test'?<FlaskConical size={20}/>:<Code2 size={20}/>}</div><div className="source-info"><strong>{s.title}{s.kind==='requirement'&&<em>草稿</em>}</strong><span>{searching?s.symbol+' · '+s.path+':'+s.start_line:s.path}</span></div><span className="module-tag">{MODULES[s.module]}</span><span className="kind-label">{KINDS[s.kind]}</span><ChevronRight size={16}/></button>)}</div>
    {!searching&&items.length<total&&<div className="load-more"><button className="secondary" onClick={loadMore} disabled={loading}>加载更多资料</button></div>}
    <div className="library-foot">源仓库保持只读 · 同步不执行项目代码或连接业务数据库</div>
   </section>}
  </main>
  {sourcePanel&&<aside className="source-panel"><div className="source-panel-header"><span><BookOpen size={16}/>来源阅读</span><button className="icon-button" aria-label="关闭来源" onClick={()=>{sourceSeq.current++;setSource(null);setSourceLoading(false);}}><X size={19}/></button></div>{sourceLoading?<div className="list-empty"><Loader2 className="spin"/>正在打开来源…</div>:<><div className="source-meta"><span className="source-kind">{KINDS[source.kind]}</span>{!source.active&&<span className="old-version">历史快照</span>}<h2>{source.title}</h2><p>{source.path}</p><span>{source.version}</span><button className="icon-button" title="导出原文" onClick={()=>download(source.title+(source.title.includes('.')?'':'.md'),source.content)}><Download size={15}/></button></div><div className="source-body">{['requirement','reference'].includes(source.kind)?<Markdown text={source.content} onSource={openSource}/>:<pre className="code-view">{source.content.split('\n').map((line,i)=><div className={'source-line '+(highlight&&i+1>=highlight.start&&i+1<=highlight.end?'highlight':'')} key={i}><span>{i+1}</span><code>{line||' '}</code></div>)}</pre>}</div><div className="source-panel-footer"><button onClick={()=>{const q=`请分析 ${source.path} 的业务规则、实现边界和待确认事项。`;setText(q);setPage('chat');setMode('code');if(window.innerWidth<1000)setSource(null);input.current?.focus();}}><MessageSquare size={15}/>围绕这份资料提问</button></div></>}</aside>}
  {help&&<div className="modal-backdrop" onClick={()=>setHelp(false)}><section className="help-modal" role="dialog" aria-modal="true" aria-labelledby="help-title" onClick={e=>e.stopPropagation()}><button className="icon-button close-help" aria-label="关闭说明" onClick={()=>setHelp(false)}><X size={20}/></button><BookOpen size={30}/><h2 id="help-title">一个轻量的研发知识空间</h2><p>产品、研发和测试从同一份项目知识出发。用自然语言提问，查看代码依据，把有价值的分析存成草稿。</p><ul><li>模型使用本机 Codex 登录，分析会消耗该账号额度。</li><li>知识来自代码快照与反推文档；请先同步再分析最新改动。</li><li>第一版仅在本机运行，尚未加入团队账号和权限管理。</li><li>检索使用中英文关键词和业务别名，不需要向量模型 Key。</li><li>不执行源仓库代码，不自动修改业务代码。</li></ul><div className="help-status">{status?.codex.message||'正在检查连接'}</div><button className="primary" onClick={()=>setHelp(false)}>知道了</button></section></div>}
  {toast&&<div className="toast" role="status">{toast}</div>}
 </div>;
}
createRoot(document.getElementById('root')).render(<App/>);
