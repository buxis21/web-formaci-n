/* ================= Ficha de curso: comportamiento común =================
   Menú, cabecera, barra de progreso, aparición, pestañas, formularios,
   FAQ, navegación por anclas y cielo de estrellas del hero. */
(function(){
const $=(s,c=document)=>c.querySelector(s), $$=(s,c=document)=>[...c.querySelectorAll(s)];
const body=document.body;

/* Menú */
const ham=$('.hamburguesa');
if(ham) ham.addEventListener('click',()=>{const a=body.classList.toggle('menu-abierto');ham.setAttribute('aria-expanded',a);});
$$('.con-mega').forEach(li=>{
  const btn=$('button',li);
  btn.addEventListener('click',e=>{e.stopPropagation();const a=li.classList.toggle('abierto');btn.setAttribute('aria-expanded',a);});
  li.addEventListener('mouseenter',()=>{if(innerWidth>900){li.classList.add('abierto');btn.setAttribute('aria-expanded',true);}});
  li.addEventListener('mouseleave',()=>{if(innerWidth>900){li.classList.remove('abierto');btn.setAttribute('aria-expanded',false);}});
});
document.addEventListener('click',e=>{if(!e.target.closest('.con-mega'))$$('.con-mega').forEach(li=>li.classList.remove('abierto'));});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){body.classList.remove('menu-abierto');$$('.con-mega').forEach(li=>li.classList.remove('abierto'));}});
$$('.menu a').forEach(a=>a.addEventListener('click',()=>body.classList.remove('menu-abierto')));
const cab=$('#cabecera');
addEventListener('scroll',()=>cab&&cab.classList.toggle('scroll',scrollY>10),{passive:true});

/* Pestañas: [role=tablist] con botones aria-controls */
$$('[role="tablist"]').forEach(lista=>{
  const tabs=$$('[role="tab"]',lista);
  const activar=t=>{tabs.forEach(o=>{const on=o===t;o.setAttribute('aria-selected',on);o.tabIndex=on?0:-1;const p=document.getElementById(o.getAttribute('aria-controls'));if(p)p.hidden=!on;});};
  tabs.forEach((t,i)=>{
    t.addEventListener('click',()=>activar(t));
    t.addEventListener('keydown',e=>{
      const d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0; if(!d) return;
      e.preventDefault(); const n=tabs[(i+d+tabs.length)%tabs.length]; activar(n); n.focus();
    });
  });
});
/* Enlaces que abren una pestaña concreta: data-abre="id-del-tab" */
$$('[data-abre]').forEach(a=>a.addEventListener('click',()=>{const t=document.getElementById(a.dataset.abre);if(t)t.click();}));

/* Formularios: se envían a Web3Forms (data-endpoint del <form>), que manda un correo con los datos.
   1) Se envían en segundo plano como formulario normal (FormData), sin consulta previa del navegador.
   2) Si el entorno no deja conectar (red o seguridad del navegador), se hace el envío clásico del
      formulario: la página va a Web3Forms y muestra su confirmación.
   Mientras envía, el botón dice «Enviando…»; si falla, sale un aviso con el motivo. */
$$('form[data-form]').forEach(f=>{
  const btn=$('button[type="submit"]',f), aviso=$('.form-error',f), textoBtn=btn.innerHTML;
  const error=(msg,detalle)=>{if(!aviso)return;aviso.textContent=msg;if(detalle){const s=document.createElement('small');s.style.cssText='display:block;opacity:.7;margin-top:4px';s.textContent='Detalle: '+detalle;aviso.append(s);}aviso.hidden=false;};
  const extra=(k,v)=>{let i=f.querySelector(`input[type=hidden][name="${k}"]`);if(!i){i=document.createElement('input');i.type='hidden';i.name=k;f.append(i);}i.value=v;};
  f.addEventListener('input',()=>{if(aviso)aviso.hidden=true;});
  f.addEventListener('submit',async e=>{
    e.preventDefault();
    if(!f.checkValidity()){f.reportValidity();error('Revisa los campos: falta alguno o no está bien escrito.');return;}
    if(f.botcheck&&f.botcheck.checked) return;      /* trampa para bots: un humano no la marca */
    const nombre=[f.nombre&&f.nombre.value,f.apellidos&&f.apellidos.value].filter(Boolean).join(' ');
    extra('curso',document.body.dataset.curso||document.title);
    extra('formulario',f.dataset.form);
    if(nombre) extra('name',nombre);
    const datos=new FormData(f); datos.delete('botcheck');
    btn.disabled=true; btn.textContent='Enviando…'; if(aviso)aviso.hidden=true;
    const corta=new AbortController(), reloj=setTimeout(()=>corta.abort(),15000);
    try{
      if(f.dataset.endpoint){
        const r=await fetch(f.dataset.endpoint,{method:'POST',headers:{'Accept':'application/json'},body:datos,signal:corta.signal});
        const res=await r.json().catch(()=>({}));
        if(!r.ok||res.success===false){const e2=new Error(res.message||('respuesta '+r.status));e2.servidor=true;throw e2;}
      }
      f.closest('.ins-panel').classList.add('enviado');
      f.closest('.inscripcion').scrollIntoView({behavior:'smooth',block:'start'});
    }catch(err){
      console.error('Envío del formulario:',err);
      if(!err.servidor&&err.name!=='AbortError'&&f.dataset.endpoint){
        /* No se ha podido conectar en segundo plano: envío clásico del formulario */
        f.action=f.dataset.endpoint; f.method='post';
        setTimeout(()=>{btn.disabled=false;btn.innerHTML=textoBtn;error('No hemos podido enviar el formulario. Inténtalo de nuevo o escríbenos a gerard@westlabs.es.','sin conexión con el servicio de formularios ('+err.message+')');},6000);
        HTMLFormElement.prototype.submit.call(f);
        return;
      }
      btn.disabled=false; btn.innerHTML=textoBtn;
      error('No hemos podido enviar el formulario. Inténtalo de nuevo o escríbenos a gerard@westlabs.es.',err.name==='AbortError'?'el servicio tarda demasiado en responder':err.message);
    }finally{clearTimeout(reloj);}
  });
});
/* Precio de particulares según la modalidad elegida */
$$('[data-precio-op]').forEach(op=>op.addEventListener('change',()=>{
  const p=$('#precio-part'); if(!p) return;
  $('b',p).textContent=op.dataset.precioOp; $('span',p).innerHTML=op.dataset.precioNota;
}));

/* Expandir / contraer acordeones */
$$('[data-acordeon]').forEach(b=>b.addEventListener('click',()=>{
  $$(`#${b.dataset.acordeon} details`).forEach(d=>d.open=b.dataset.accion==='abrir');
}));

/* Aparición suave */
const io='IntersectionObserver' in window?new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visto');io.unobserve(e.target);}}),{threshold:.12}):null;
$$('.reveal').forEach(el=>io?io.observe(el):el.classList.add('visto'));
const anio=$('#anio'); if(anio) anio.textContent=new Date().getFullYear();

/* Ancla activa en la barra de navegación del curso */
const anclas=$$('.anclas a[href^="#"]:not(.apunta)');
if(anclas.length&&'IntersectionObserver' in window){
  const secs=anclas.map(a=>document.querySelector(a.getAttribute('href'))).filter(Boolean);
  const ob=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){anclas.forEach(a=>a.classList.toggle('activa',a.getAttribute('href')==='#'+e.target.id));}}),{rootMargin:'-45% 0px -50% 0px'});
  secs.forEach(s=>ob.observe(s));
}

/* Barra de progreso e inclinación de tarjetas */
const bar=$('.progreso');
if(bar){const upd=()=>{const h=document.documentElement.scrollHeight-innerHeight;bar.style.transform=`scaleX(${h>0?scrollY/h:0})`;};addEventListener('scroll',upd,{passive:true});upd();}
if(!matchMedia('(prefers-reduced-motion:reduce)').matches&&matchMedia('(hover:hover)').matches){
  document.addEventListener('mousemove',e=>{
    const c=e.target.closest('.curso,.mf'); $$('.tilt').forEach(t=>{if(t!==c){t.style.transform='';t.classList.remove('tilt');}});
    if(!c) return;
    const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
    c.classList.add('tilt');c.style.transform=`perspective(900px) rotateX(${(-y*6).toFixed(2)}deg) rotateY(${(x*8).toFixed(2)}deg) translateY(-6px)`;
  });
}

/* Cielo de estrellas del hero */
const cv=$('.hero .cielo'); if(!cv) return;
const ctx=cv.getContext('2d'), quieto=matchMedia('(prefers-reduced-motion:reduce)').matches;
let W,H,estrellas=[],fugaces=[],t0=performance.now(),ultimo=t0,proxFugaz=t0+2500,activo=true;
function crear(){
  const dpr=Math.min(devicePixelRatio||1,2);
  W=cv.clientWidth;H=cv.clientHeight;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
  estrellas=Array.from({length:Math.round(W*H/5200)},()=>{const capa=Math.random(),brillo=Math.random()<.05;return{
    x:Math.random()*W,y:Math.random()*H,r:brillo?1.1+Math.random()*.7:.3+capa*.8,max:brillo?.9:.2+capa*.5,
    vel:.3+Math.random()*1.1,fase:Math.random()*6.28,dx:(4+capa*10)/1000,inicio:Math.random()*5000,brillo};});
}
function pintar(ahora){
  const dt=Math.min(50,ahora-ultimo); ultimo=ahora; const t=quieto?1e5:ahora-t0;
  ctx.clearRect(0,0,W,H);
  for(const e of estrellas){
    if(!quieto){e.x-=e.dx*dt; if(e.x<-4) e.x=W+4;}
    const entra=Math.min(1,Math.max(0,(t-e.inicio)/2000)); if(!entra) continue;
    const a=e.max*entra*(quieto?.8:.35+.65*Math.pow((Math.sin(e.fase+t/1000*e.vel)+1)/2,2));
    if(e.brillo){const g=ctx.createRadialGradient(e.x,e.y,0,e.x,e.y,e.r*7);g.addColorStop(0,`rgba(160,215,255,${a*.45})`);g.addColorStop(1,'rgba(160,215,255,0)');ctx.fillStyle=g;ctx.beginPath();ctx.arc(e.x,e.y,e.r*7,0,6.28);ctx.fill();}
    ctx.fillStyle=`rgba(235,245,255,${a})`;ctx.beginPath();ctx.arc(e.x,e.y,e.r,0,6.28);ctx.fill();
  }
  if(quieto) return;
  if(ahora>proxFugaz){const ang=Math.PI*(.78+Math.random()*.1);fugaces.push({x:W*(.2+Math.random()*.7),y:H*Math.random()*.45,vx:Math.cos(ang)*.9,vy:Math.sin(ang)*.9,vida:0,dur:900+Math.random()*500});proxFugaz=ahora+5000+Math.random()*6000;}
  fugaces=fugaces.filter(f=>{
    f.vida+=dt; const p=f.vida/f.dur; if(p>=1) return false;
    const hx=f.x+f.vx*f.vida,hy=f.y+f.vy*f.vida,L=120,op=Math.sin(p*Math.PI)*.8;
    const g=ctx.createLinearGradient(hx,hy,hx-f.vx*L,hy-f.vy*L);g.addColorStop(0,`rgba(220,240,255,${op})`);g.addColorStop(1,'rgba(220,240,255,0)');
    ctx.strokeStyle=g;ctx.lineWidth=1.3;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(hx,hy);ctx.lineTo(hx-f.vx*L,hy-f.vy*L);ctx.stroke();return true;});
  if(activo) requestAnimationFrame(pintar);
}
crear();requestAnimationFrame(pintar);
let rz;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(()=>{crear();if(quieto)pintar(performance.now());},150);});
if('IntersectionObserver' in window&&!quieto) new IntersectionObserver(([en])=>{const antes=activo;activo=en.isIntersecting;if(activo&&!antes){ultimo=performance.now();requestAnimationFrame(pintar);}}).observe(cv);
})();
