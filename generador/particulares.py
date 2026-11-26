# -*- coding: utf-8 -*-
"""
PÁGINAS DE PARTICULARES (carpeta particulares/)
Se generan con  python3 generador/generar.py  (este archivo lo llama al final).
  particulares/claude-esencial.html   ┐
  particulares/claude-avanzado.html   ├ una página por nivel: es donde se compra
  particulares/claude-completo.html   ┘
  particulares/como-funciona.html     el campus, la mentoría, subir de nivel y el pago
  particulares/certificado.html       el certificado y el artículo 4 del AI Act
Textos en generador/datos_particulares.py; precios en generador/datos.py (PACKS).
Estilos en assets/css/particulares.css; el pago en assets/js/pago.js.
"""
import os, html, math
from datos import PACKS
from datos_particulares import PART, RECORRIDO, FAQ_COMUN, PASOS, STRIPE_PK

DIR = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(DIR)
leer = lambda f: open(os.path.join(DIR, 'parciales', f), encoding='utf-8').read()
ICONOS, CABECERA, PIE = leer('iconos.html'), leer('cabecera.html'), leer('pie.html')
WEB3FORMS = 'ab432877-6901-4527-b6b2-86e117e9f28f'
e = lambda t: html.escape(str(t), quote=True)
ARROW = '<svg class="i fl"><use href="#i-arrow"/></svg>'
WHATSAPP = 'https://wa.me/34636875779?text=Hola%20Gerard%2C%20tengo%20una%20duda%20sobre%20los%20cursos%20de%20Claude'
NIVELES = list(PACKS.keys())          # ['claude-esencial', 'claude-avanzado', 'claude-completo']


def euros(n):
    s = f'{n:.2f}'.replace('.', ',')
    return (s[:-3] if s.endswith(',00') else s) + ' €'

def precio(slug):
    return float(PACKS[slug]['normal'].replace(' €', '').replace(',', '.'))

def plazo(slug):
    return euros(precio(slug) / 3)

def ico(i):
    return f'<span class="logo-tile"><svg><use href="#{i}"/></svg></span>'


# ---------------------------------------------------------------- dibujos (SVG en línea)
DEFS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <linearGradient id="pg-a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1B3F94"/><stop offset=".6" stop-color="#2563EB"/><stop offset="1" stop-color="#3BA8F5"/></linearGradient>
  <linearGradient id="pg-b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3B8EF5"/><stop offset="1" stop-color="#5BC8F5"/></linearGradient>
  <linearGradient id="pg-n" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E1B45"/><stop offset="1" stop-color="#1B3F94"/></linearGradient>
</defs></svg>
'''
FONDO = '<rect width="240" height="150" rx="22" fill="#EAF3FC"/><circle cx="214" cy="20" r="44" fill="#DDEBFA"/><circle cx="20" cy="142" r="36" fill="#E0EFFA"/>'
VENT = lambda x, y, w, h: (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" stroke="#D6DDE8"/>'
                           f'<circle cx="{x+13}" cy="{y+11}" r="3.2" fill="#F6B4B0"/><circle cx="{x+23}" cy="{y+11}" r="3.2" fill="#F8D99A"/><circle cx="{x+33}" cy="{y+11}" r="3.2" fill="#A9DDB4"/>'
                           f'<line x1="{x}" y1="{y+22}" x2="{x+w}" y2="{y+22}" stroke="#E6ECF4"/>')
BARRA = lambda x, y, w, c='#C5D4EA': f'<rect x="{x}" y="{y}" width="{w}" height="5" rx="2.5" fill="{c}"/>'
CHISPA = lambda x, y, s=1, c='#5BC8F5': f'<path transform="translate({x} {y}) scale({s})" d="M0-9l2.6 6.4L9 0l-6.4 2.6L0 9l-2.6-6.4L-9 0l6.4-2.6z" fill="{c}"/>'
CHECK = lambda x, y, r=18: (f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#pg-a)"/>'
                            f'<path d="M{x-r*.4:.1f} {y:.1f}l{r*.28:.1f} {r*.28:.1f} {r*.5:.1f}-{r*.55:.1f}" fill="none" stroke="#fff" stroke-width="{r*.2:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')

def estrellas(cx, cy, r, n=12, tam=3.2):
    return ''.join(f'<circle cx="{cx + r*math.cos(2*math.pi*i/n):.1f}" cy="{cy + r*math.sin(2*math.pi*i/n):.1f}" r="{tam}" fill="#FFD54A"/>' for i in range(n))

def qr(x, y, t=4):
    # Un QR dibujado (decorativo), de 7x7 módulos
    patron = ['1111101', '1000101', '1011101', '0010010', '1101011', '0100110', '1011101']
    out = [f'<rect x="{x-3}" y="{y-3}" width="{7*t+6}" height="{7*t+6}" rx="3" fill="#fff"/>']
    for f, fila in enumerate(patron):
        for c, v in enumerate(fila):
            if v == '1': out.append(f'<rect x="{x+c*t}" y="{y+f*t}" width="{t}" height="{t}" fill="#0E1B45"/>')
    return ''.join(out)

ILUS = {
 'chat': VENT(38, 18, 164, 116) + '<rect x="100" y="50" width="90" height="22" rx="11" fill="url(#pg-a)"/>' + BARRA(112, 58.5, 56, '#fff')
         + '<rect x="50" y="80" width="116" height="42" rx="12" fill="#EEF4FC"/>' + BARRA(60, 89, 82, '#9DB6DA') + BARRA(60, 99, 94) + BARRA(60, 109, 60)
         + CHISPA(184, 100) + CHISPA(198, 84, .6, '#3B8EF5'),
 'ajustes': VENT(46, 18, 148, 116)
         + BARRA(60, 50, 64) + '<rect x="146" y="44" width="34" height="18" rx="9" fill="url(#pg-a)"/><circle cx="171" cy="53" r="6.5" fill="#fff"/>'
         + BARRA(60, 75, 50) + '<rect x="146" y="69" width="34" height="18" rx="9" fill="url(#pg-a)"/><circle cx="171" cy="78" r="6.5" fill="#fff"/>'
         + BARRA(60, 100, 72) + '<rect x="146" y="94" width="34" height="18" rx="9" fill="#D6DDE8"/><circle cx="155" cy="103" r="6.5" fill="#fff"/>'
         + '<rect x="60" y="120" width="120" height="4" rx="2" fill="#E2E9F3"/><rect x="60" y="120" width="78" height="4" rx="2" fill="url(#pg-b)"/><circle cx="138" cy="122" r="6" fill="#fff" stroke="#2563EB" stroke-width="2.5"/>'
         + CHISPA(204, 40, .8),
 'escudo': '<path d="M120 16l50 17v36c0 34-22 54-50 66-28-12-50-32-50-66V33z" fill="url(#pg-a)"/>'
         + '<path d="M120 28l38 13v28c0 26-17 42-38 52-21-10-38-26-38-52V41z" fill="#fff" opacity=".12"/>'
         + estrellas(120, 72, 30, 12, 3) + '<path d="M106 73l10 10 19-21" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
         + CHISPA(190, 40) + CHISPA(50, 110, .7, '#3B8EF5'),
 'proyecto': '<g transform="rotate(-9 104 78)"><rect x="84" y="36" width="44" height="56" rx="6" fill="#fff" stroke="#D6DDE8"/>' + BARRA(92, 48, 26) + BARRA(92, 58, 20) + '</g>'
         + '<g transform="rotate(7 134 74)"><rect x="112" y="34" width="44" height="56" rx="6" fill="#fff" stroke="#D6DDE8"/>' + BARRA(120, 46, 28, '#9DB6DA') + BARRA(120, 56, 22) + BARRA(120, 66, 26) + '</g>'
         + '<path d="M70 66h30l9 9h53a7 7 0 0 1 7 7v40a7 7 0 0 1-7 7H70a7 7 0 0 1-7-7V73a7 7 0 0 1 7-7z" fill="url(#pg-a)"/>'
         + '<path d="M40 52L78 84M200 46L162 84" stroke="#3B8EF5" stroke-width="2" stroke-dasharray="4 5"/>'
         + '<rect x="18" y="34" width="40" height="28" rx="6" fill="#fff" stroke="#D6DDE8"/><path d="M22 40l16 11 16-11" fill="none" stroke="#2563EB" stroke-width="2.4" stroke-linecap="round"/>'
         + '<rect x="184" y="26" width="38" height="34" rx="6" fill="#fff" stroke="#D6DDE8"/><rect x="184" y="26" width="38" height="10" rx="5" fill="url(#pg-b)"/>'
         + ''.join(f'<rect x="{190+c*9}" y="{41+f*8}" width="5" height="4" rx="1" fill="{"#2563EB" if (f, c) == (1, 2) else "#C5D4EA"}"/>' for f in range(2) for c in range(3)),
 'skills': '<rect x="66" y="40" width="104" height="76" rx="12" fill="#C9DCF5" transform="rotate(-9 118 78)"/>'
         + '<rect x="66" y="40" width="104" height="76" rx="12" fill="#DDE9F9" transform="rotate(-3 118 78)"/>'
         + '<rect x="68" y="38" width="106" height="78" rx="12" fill="#fff" stroke="#D6DDE8"/>' + BARRA(82, 54, 54, '#9DB6DA') + BARRA(82, 66, 76) + BARRA(82, 78, 64) + BARRA(82, 90, 70) + BARRA(82, 102, 40)
         + '<circle cx="172" cy="40" r="20" fill="url(#pg-a)"/><path d="M175 27l-11 15h8l-2 12 11-16h-8z" fill="#fff"/>' + CHISPA(42, 44) + CHISPA(206, 118, .7, '#3B8EF5'),
 'auto': '<rect x="40" y="26" width="116" height="100" rx="14" fill="#fff" stroke="#D6DDE8"/><path d="M40 40a14 14 0 0 1 14-14h88a14 14 0 0 1 14 14v12H40z" fill="url(#pg-a)"/>'
         + '<rect x="62" y="18" width="6" height="16" rx="3" fill="#0E1B45"/><rect x="128" y="18" width="6" height="16" rx="3" fill="#0E1B45"/>'
         + ''.join(f'<rect x="{54+c*24}" y="{62+f*20}" width="16" height="12" rx="3" fill="{"url(#pg-b)" if (f, c) in ((0, 0), (1, 0), (2, 0)) else "#E3EBF6"}"/>' for f in range(3) for c in range(4))
         + '<circle cx="172" cy="100" r="30" fill="#fff" stroke="url(#pg-a)" stroke-width="5"/><path d="M172 84v16l11 7" fill="none" stroke="#0E1B45" stroke-width="4" stroke-linecap="round"/>'
         + CHISPA(206, 52, .8),
 'revision': '<rect x="66" y="16" width="100" height="120" rx="10" fill="#fff" stroke="#D6DDE8"/>' + BARRA(80, 32, 50, '#9DB6DA') + BARRA(80, 46, 72) + BARRA(80, 58, 64) + BARRA(80, 70, 70) + BARRA(80, 82, 48) + BARRA(80, 96, 66) + BARRA(80, 108, 40)
         + '<ellipse cx="112" cy="84" rx="38" ry="9" fill="none" stroke="#E25555" stroke-width="2"/><path d="M152 56l8 6" stroke="#E25555" stroke-width="2.5" stroke-linecap="round"/>'
         + '<path d="M34 120l46-46 8 8-46 46-12 4z" fill="url(#pg-b)"/>' + CHECK(172, 112, 22) + CHISPA(196, 40),
 'miniapp': VENT(36, 18, 168, 116) + '<rect x="37" y="41" width="36" height="92" fill="#F1F5FB"/>' + BARRA(45, 54, 20, '#9DB6DA') + BARRA(45, 68, 20) + BARRA(45, 82, 20)
         + ''.join(f'<rect x="{86+i*20}" y="{120-hh}" width="12" height="{hh}" rx="3" fill="url(#pg-a)"/>' for i, hh in enumerate([26, 40, 32, 56, 70]))
         + '<rect x="146" y="50" width="48" height="30" rx="8" fill="#EEF4FC"/>' + BARRA(152, 58, 26, '#9DB6DA') + '<rect x="152" y="67" width="34" height="7" rx="3.5" fill="#2563EB"/>' + CHISPA(212, 120, .8),
 'agente': '<path d="M58 40L104 70M182 40L136 70M58 118L104 92M182 118L136 92" stroke="#3B8EF5" stroke-width="2" stroke-dasharray="4 5"/>'
         + '<rect x="92" y="50" width="56" height="50" rx="16" fill="url(#pg-a)"/><circle cx="108" cy="74" r="6" fill="#fff"/><circle cx="132" cy="74" r="6" fill="#fff"/>'
         + '<path d="M110 88q10 7 20 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M120 50V38" stroke="#1B3F94" stroke-width="3"/><circle cx="120" cy="34" r="5" fill="url(#pg-b)"/>'
         + ''.join(f'<circle cx="{x}" cy="{y}" r="17" fill="#fff" stroke="#D6DDE8"/><use href="#{i}" x="{x-10}" y="{y-10}" width="20" height="20"/>'
                   for x, y, i in [(46, 34, 'i-mail'), (194, 34, 'i-doc'), (46, 122, 'i-form'), (194, 122, 'i-chart')]),
 'cohete': '<path d="M120 18c24 16 32 44 27 76h-54c-5-32 3-60 27-76z" fill="url(#pg-a)"/><circle cx="120" cy="56" r="11" fill="#fff"/><circle cx="120" cy="56" r="6" fill="url(#pg-b)"/>'
         + '<path d="M93 76l-18 22 20-2zM147 76l18 22-20-2z" fill="#1B3F94"/><path d="M106 96h28l-6 22-8 12-8-12z" fill="url(#pg-b)"/><path d="M114 96h12l-3 14-3 6-3-6z" fill="#fff" opacity=".7"/>'
         + CHISPA(54, 40) + CHISPA(190, 50, .8, '#3B8EF5') + CHISPA(186, 116, .6),
 'mentoria': VENT(26, 20, 188, 112) + '<rect x="36" y="50" width="82" height="64" rx="10" fill="#DCEBFA"/><rect x="122" y="50" width="82" height="64" rx="10" fill="#D3E7F7"/>'
         + '<circle cx="77" cy="74" r="11" fill="url(#pg-a)"/><path d="M57 114a20 18 0 0 1 40 0z" fill="url(#pg-a)"/>'
         + '<circle cx="163" cy="74" r="11" fill="url(#pg-n)"/><path d="M143 114a20 18 0 0 1 40 0z" fill="url(#pg-n)"/>'
         + '<rect x="144" y="54" width="40" height="12" rx="6" fill="#fff"/>' + BARRA(150, 57.5, 28, '#9DB6DA') + CHISPA(204, 30, .7),
 'certificado': '<rect x="40" y="22" width="150" height="108" rx="8" fill="#fff" stroke="#D6DDE8" transform="rotate(-4 115 76)"/>'
         + '<rect x="46" y="20" width="150" height="108" rx="8" fill="#fff" stroke="#D6DDE8"/><rect x="54" y="28" width="134" height="92" rx="4" fill="none" stroke="#C9D7EC"/>'
         + BARRA(96, 40, 50, '#9DB6DA') + '<rect x="78" y="54" width="86" height="7" rx="3.5" fill="#0E1B45"/>' + BARRA(84, 70, 74) + BARRA(92, 80, 58) + qr(64, 92, 3.2)
         + '<circle cx="178" cy="108" r="18" fill="url(#pg-b)"/><path d="M170 124l-4 18 12-6 12 6-4-18" fill="#2563EB"/>' + estrellas(178, 108, 11, 8, 1.6) + CHISPA(214, 34, .8),
 'campus': '<rect x="40" y="22" width="160" height="96" rx="10" fill="url(#pg-n)"/><rect x="48" y="30" width="144" height="80" rx="4" fill="#1B3F94"/>'
         + '<rect x="48" y="30" width="144" height="80" rx="4" fill="url(#pg-a)" opacity=".7"/><circle cx="120" cy="70" r="16" fill="#fff"/><path d="M115 62l13 8-13 8z" fill="#2563EB"/>'
         + '<rect x="58" y="100" width="124" height="4" rx="2" fill="#fff" opacity=".3"/><rect x="58" y="100" width="70" height="4" rx="2" fill="#5BC8F5"/>'
         + '<path d="M24 118h192l-10 14H34z" fill="#C9D7EC"/><rect x="104" y="118" width="32" height="5" rx="2.5" fill="#9DB6DA"/>' + CHISPA(212, 34, .8),
}

def ilus(nombre, clase='ilus'):
    return f'<svg class="{clase}" viewBox="0 0 240 150" role="presentation" aria-hidden="true">{FONDO}{ILUS[nombre]}</svg>'


# ---------------------------------------------------------------- piezas comunes
def pagina(titulo, desc, curso, contenido, pago=False, slug_pago=''):
    scripts = '<script src="../assets/js/curso.js"></script>' + ('\n<script src="../assets/js/pago.js"></script>' if pago else '')
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="../assets/logo/icono-westlabs.png">
<link rel="stylesheet" href="../assets/css/base.css">
<link rel="stylesheet" href="../assets/css/curso.css">
<link rel="stylesheet" href="../assets/css/particulares.css">
</head>
<!-- Página generada con generador/generar.py (generador/particulares.py). No la edites a mano. -->
<body class="part" data-curso="{e(curso)}"{f' data-stripe-pk="{e(STRIPE_PK)}"' if pago else ''}>
{ICONOS}{DEFS}<div class="progreso" aria-hidden="true"></div>
<a class="skip" href="#contenido">Ir al contenido</a>

{CABECERA}<main id="contenido">
{contenido}
</main>

{PIE}{scripts}
</body>
</html>
'''

def hero(migas, pre, h1, sub, intro, chips, derecha, extra=''):
    chips_html = ''.join(f'<span class="chip-h{" dest" if i == 0 else ""}"><svg class="i"><use href="#i-check"/></svg>{e(t)}</span>' for i, t in enumerate(chips))
    migas_html = '<a href="../">Inicio</a><span>/</span><a href="../particulares.html">Particulares</a>' + ''.join(f'<span>/</span>{e(m)}' for m in migas)
    return f'''<section class="hero hero-curso oscuro" id="top">
  <canvas class="cielo" aria-hidden="true"></canvas>
  <div class="wrap">
    <nav class="migas" aria-label="Estás en">{migas_html}</nav>
    <div class="grid">
      <div>
        <div class="pre">{e(pre)}</div>
        <h1>{e(h1)}</h1>
        <span class="sub">{e(sub)}</span>
        <p class="intro">{intro}</p>
        <div class="chips">{chips_html}</div>{extra}
      </div>
{derecha}
    </div>
  </div>
  <svg class="ola" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 80V40C240 0 480 0 720 30s480 40 720 0v50z" fill="#fff"/></svg>
</section>'''

def cab(pre, t1, t2, intro='', centro=True):
    return (f'<div class="cab-sec reveal">\n      <div class="pre">{e(pre)}</div>\n      <h2>{e(t1)} <span class="acento">{e(t2)}</span></h2>'
            + (f'\n      <p class="intro">{intro}</p>' if intro else '') + '\n    </div>')

def faq_sec(preguntas, intro):
    det = ''.join(f'\n      <details><summary>{e(p)}</summary><div class="cuerpo">{r}</div></details>' for p, r in preguntas)
    return f'''<section class="faq" id="faqs">
  <div class="wrap">
    <div class="faq-cab reveal">
      <div class="pre">Dudas</div>
      <h2>Preguntas <span class="acento">frecuentes</span></h2>
      <p class="intro">{intro}</p>
      <div class="faq-acciones"><button type="button" data-acordeon="faq-lista" data-accion="abrir">Expandir todo</button><button type="button" data-acordeon="faq-lista" data-accion="cerrar">Contraer todo</button></div>
      <div class="faq-contacto"><b>¿No encuentras tu respuesta?</b><span>Escríbenos a <a href="mailto:gerard@westlabs.es">gerard@westlabs.es</a> o por WhatsApp al <a href="{WHATSAPP}" target="_blank" rel="noopener">636 875 779</a>.</span></div>
    </div>
    <div class="acordeon reveal" id="faq-lista">{det}
    </div>
  </div>
</section>'''

def niveles_mini(actual=None, titulo=('Elige tu', 'nivel de Claude')):
    """Las tres tarjetas de nivel, cada una enlaza a su página (donde se compra)."""
    cards = []
    for slug in NIVELES:
        P = PACKS[slug]; es = slug == actual
        clase = 'esc actual' if (es or (actual is None and P.get('completo'))) else 'esc e2'
        marca = '<span class="aqui">Estás aquí</span>' if es else ('<span class="aqui">Curso completo</span>' if actual is None and P.get('completo') else '')
        boton = ('<a href="#compra" class="btn btn-claro">Comprar ' + ARROW + '</a>') if es else f'<a href="{slug}.html" class="btn {"btn-claro" if "actual" in clase else "btn-primario"}">Ver el curso {ARROW}</a>'
        cards.append(f'''      <article class="{clase} reveal">{marca}
        <img class="medalla-e" src="../assets/3d/medalla-{P['medalla']}.png" alt="">
        <span class="et">{e(P['et'])}</span>
        <h3>{e(P['nombre'])}</h3>
        <div class="px">{e(P['normal'])}<small>IVA incluido</small></div>
        <p class="plazos">o 3 plazos de {plazo(slug)} sin intereses</p>
        <p>{e(P['txt'])}</p>
        <ul>{''.join(f'<li>{e(x)}</li>' for x in P['lista'])}</ul>
        <div class="esc-btns">{boton}</div>
      </article>''')
    return f'''<section class="escalera" id="niveles">
  <div class="wrap">
    {cab('Tres niveles', titulo[0], titulo[1], 'Cada nivel incluye el anterior. Si empiezas por uno y luego quieres más, pagas solo la diferencia.')}
    <div class="escalones">
{chr(10).join(cards)}
    </div>
  </div>
</section>'''

def cert_papel(nombre_curso, aria):
    return f'''<div class="cert-wrap" role="img" aria-label="{e(aria)}">
        <div class="paper back"></div>
        <div class="paper mid"></div>
        <div class="paper front"><div class="frame">
          <img class="cl" src="../assets/logo/westlabs-ai-school.png" alt="">
          <div class="ct">FORMACIÓN EN IA</div>
          <div class="ch">Certificado de formación</div>
          <div class="cs">Se certifica que</div>
          <div class="cn">Nombre del participante</div>
          <div class="cd">ha completado el curso <b>{e(nombre_curso)}</b>, con horas y contenidos, incluida la alfabetización en IA del <b>art. 4 del Reglamento Europeo de IA</b>.</div>
          <div class="cfoot">
            <div class="csig"><i>Verificable</i>Código QR</div>
            <div class="csig r"><i>Westlabs</i>Entidad formadora</div>
          </div>
          <div class="seal"><div><span>AI ACT</span><b>ART. 4</b></div></div>
        </div></div>
      </div>'''

def cta_final(t1, t2, texto, botones):
    return f'''<section class="cta-final">
  <div class="wrap">
    <div class="caja oscuro reveal">
      <div>
        <h2>{e(t1)} <span class="acento">{e(t2)}</span></h2>
        <p class="intro">{e(texto)}</p>
      </div>
      <div class="botones">
        {botones}
      </div>
    </div>
  </div>
</section>'''


# ---------------------------------------------------------------- página de curso
def compra_card(slug):
    P = PACKS[slug]
    return f'''      <div class="inscripcion compra" id="compra">
        <div class="ins-panel">
          <div class="compra-cab"><img src="../assets/3d/medalla-{P['medalla']}.png" alt=""><div><span class="compra-et">Teleformación{' con mentoría' if P['mentoria'] else ''}</span><h2>{e(P['nombre'])}</h2></div></div>
          <div class="precio"><b>{e(P['normal'])}</b><span>IVA incluido<br>o 3 plazos de {plazo(slug)} sin intereses</span></div>
          <ul class="pack-lista">{''.join(f'<li>{e(x)}</li>' for x in P['lista'])}</ul>
          <div class="cod-mini">
            <label for="cod-desc">¿Tienes un código de descuento?</label>
            <div class="cod-fila"><input id="cod-desc" type="text" autocomplete="off" autocapitalize="characters" spellcheck="false" placeholder="Escríbelo aquí (opcional)"><svg class="i"><use href="#i-check"/></svg></div>
          </div>
          <a href="#reserva" class="btn btn-primario full" data-pack="{e(P['nombre'])}" data-curso="{slug}">Comprar {ARROW}</a>
          <p class="compra-seg"><svg class="i"><use href="#i-shield"/></svg>Pago seguro con Stripe: tarjeta, Apple Pay, Google Pay o 3 plazos con Klarna. Empiezas hoy.</p>
        </div>
      </div>'''

def recorrido(nivel):
    """Mapa visual de los 10 módulos de los tres niveles. Los incluidos en este nivel se ven en color."""
    grupos = []
    n = 0
    for lv, slug in enumerate(NIVELES, 1):
        mods = [m for m in RECORRIDO if m['nivel'] == lv]
        incl = lv <= nivel
        paradas = []
        for m in mods:
            n += 1
            paradas.append(f'<li class="parada"><span class="pn">{n}</span><svg class="pi" viewBox="0 0 240 150" aria-hidden="true">{ILUS[m["ilus"]]}</svg><b>{e(m["t"])}</b><small>{e(m["sub"])}</small></li>')
        etiqueta = (f'Nivel {lv} · {PACKS[slug]["nombre"]}' + ('' if incl else ''))
        extra = '' if incl else f'<a href="{slug}.html" class="rec-mas">Está en {e(PACKS[slug]["nombre"])} {ARROW}</a>'
        grupos.append(f'<div class="rec-grupo{"" if incl else " fuera"}"><div class="rec-et"><img src="../assets/3d/medalla-{lv}.png" alt=""><span>{e(etiqueta)}</span>{"<em>Incluido</em>" if incl else ""}</div><ol class="rec-paradas">{"".join(paradas)}</ol>{extra}</div>')
    total = sum(1 for m in RECORRIDO if m['nivel'] <= nivel)
    return f'''<section class="recorrido" id="recorrido">
  <div class="wrap">
    {cab('Tu recorrido', 'Dónde estás', 'y hasta dónde llegas', f'Los tres niveles de Claude son un mismo camino. Con {e(PACKS[NIVELES[nivel-1]]["nombre"])} haces {total} de los 10 módulos{"" if nivel == 3 else "; los demás, si quieres, los sumas después pagando solo la diferencia"}.')}
    <div class="rec reveal">
      {''.join(grupos)}
    </div>
  </div>
</section>'''

def temario_part(nivel):
    out = []; n = 0
    for lv, slug in enumerate(NIVELES[:nivel], 1):
        out.append(f'          <p class="tem-grupo">Nivel {lv} · {e(PACKS[slug]["nombre"])}</p>')
        for m in [x for x in RECORRIDO if x['nivel'] == lv]:
            n += 1
            puntos = ''.join(f'<li>{e(p)}</li>' for p in m['puntos'])
            out.append(f'''          <details{' open' if n == 1 else ''}><summary><span class="num">{n}</span><span class="t">{e(m['t'])}<small>{e(m['sub'])}</small></span></summary><div class="cuerpo"><ul>{puntos}</ul><p class="entregable"><b>Te llevas:</b> {e(m['llevas'])}</p></div></details>''')
    fin = 'test final' if nivel == 1 else 'entrega de tu proyecto'
    out.append(f'''          <details><summary><span class="num">✓</span><span class="t">Certificado<small>Al acabar</small></span></summary><div class="cuerpo"><ul><li>Con el {fin} descargas tu certificado nominativo y verificable</li><li>Incluye la alfabetización en IA del artículo 4 del Reglamento Europeo de IA</li></ul></div></details>''')
    return '        <div class="acordeon" id="tem-part">\n' + '\n'.join(out) + '\n        </div>'

def campus_mock(nivel):
    mods = [m['t'] for m in RECORRIDO if m['nivel'] <= nivel][:6]
    filas = ''.join(f'<li class="{"hecho" if i < 2 else ("ahora" if i == 2 else "")}"><span></span>{e(t)}</li>' for i, t in enumerate(mods))
    return f'''<div class="campus-mock" role="img" aria-label="Así se ve una lección en el campus de Westlabs">
          <div class="cm-barra"><i></i><i></i><i></i><span>westlabscampus.es</span></div>
          <div class="cm-cuerpo">
            <aside><b>Tu curso</b><div class="cm-prog"><span style="width:{28 if nivel > 1 else 45}%"></span></div><ol>{filas}</ol></aside>
            <div class="cm-main">
              <div class="cm-video"><span class="cm-play"></span><em>3:42</em></div>
              <b>Módulo 3 · IA segura y legal</b>
              <div class="cm-ej"><span class="logo-tile"><svg><use href="#i-doc"/></svg></span><div><b>Ejercicio</b><small>Pasa tu documento por el semáforo de datos</small></div><i>Entregar</i></div>
            </div>
          </div>
        </div>'''

def comparativa(actual):
    filas = [('Vídeos y ejercicios en el campus', '✓', '✓', '✓'), ('Prompting, configuración y memoria', '✓', '✓', '✓'),
             ('IA segura y legal (artículo 4)', '✓', '✓', '✓'), ('Proyectos y conectores', '✓', '✓', '✓'),
             ('Skills y Claude en Excel, Word y correo', '—', '✓', '✓'), ('Automatizaciones y Claude en Chrome', '—', '✓', '✓'),
             ('Artefactos y miniaplicaciones', '—', '—', '✓'), ('Agentes', '—', '—', '✓'),
             ('Mentoría 1 a 1', '—', '2 h', '3 h'), ('Proyectos corregidos', '—', '1', '2'),
             ('Certificado verificable', '✓', '✓', '✓'), ('Acceso al campus', '12 meses', '12 meses', '12 meses'),
             ('Cuenta de Claude', 'Gratuita', 'Pro', 'Pro'),
             ('Precio con IVA', *[PACKS[s]['normal'] for s in NIVELES])]
    col = NIVELES.index(actual)
    ACT = ' class="act"'
    th = ''.join(f'<th scope="col"{ACT if i == col else ""}><img src="../assets/3d/medalla-{i+1}.png" alt=""><a href="{s}.html">{e(PACKS[s]["nombre"])}</a></th>' for i, s in enumerate(NIVELES))
    def celda(v, i):
        cls = (' class="act"' if i == col else '')
        if v == '✓': return f'<td{cls}><span class="si" aria-label="Sí">✓</span></td>'
        if v == '—': return f'<td{cls}><span class="no" aria-label="No">—</span></td>'
        return f'<td{cls}>{e(v)}</td>'
    tb = ''.join(f'<tr><th scope="row">{e(f[0])}</th>{"".join(celda(v, i) for i, v in enumerate(f[1:]))}</tr>' for f in filas)
    pie = ''.join((f'<td class="act"><a href="#compra" class="btn btn-primario btn-sm">Comprar</a></td>' if i == col else f'<td><a href="{s}.html" class="btn btn-borde-osc btn-sm">Ver</a></td>') for i, s in enumerate(NIVELES))
    return f'''<section class="comparar" id="comparar">
  <div class="wrap">
    {cab('Compara', 'Los tres niveles', 'de un vistazo', 'Cada nivel incluye todo lo del anterior. Si subes de nivel más adelante, pagas solo la diferencia.')}
    <div class="tabla-wrap reveal">
      <table class="tabla-niv">
        <thead><tr><td></td>{th}</tr></thead>
        <tbody>{tb}</tbody>
        <tfoot><tr><td></td>{pie}</tr></tfoot>
      </table>
    </div>
  </div>
</section>'''

def reserva(slug):
    if STRIPE_PK: return ''
    P = PACKS[slug]
    return f'''<section class="reserva" id="reserva">
  <div class="wrap">
    <div class="inscripcion reserva-card reveal">
      <div class="ins-panel">
        <h2>Reserva tu plaza en {e(P['nombre'])}</h2>
        <p class="ayuda">Déjanos tus datos y te enviamos hoy el enlace de pago y el acceso al campus.</p>
        <form class="form" data-form="particulares" data-endpoint="https://api.web3forms.com/submit" novalidate>
          <input type="hidden" name="access_key" value="{WEB3FORMS}">
          <input type="hidden" name="subject" value="Particular · reserva de {e(P['nombre'])}">
          <input type="hidden" name="from_name" value="Web Westlabs AI School">
          <input type="checkbox" name="botcheck" class="sr" tabindex="-1" autocomplete="off" aria-hidden="true">
          <input type="hidden" id="r-pack" name="curso_elegido" value="{e(P['nombre'])} · {e(P['normal'])}">
          <div class="campo full"><label for="r-codigo">Código de descuento <small>(opcional)</small></label><input id="r-codigo" name="codigo_descuento" type="text" autocomplete="off" placeholder="Si tienes uno"></div>
          <div class="campo full"><span class="grupo-t" id="r-pago-t">Pago</span>
            <div class="opciones dos" role="radiogroup" aria-labelledby="r-pago-t">
              <label class="op"><input type="radio" name="pago" value="De una vez" checked><span>De una vez · {e(P['normal'])}</span></label>
              <label class="op"><input type="radio" name="pago" value="En 3 plazos"><span>3 plazos de {plazo(slug)}</span></label>
            </div></div>
          <div class="campo"><label for="r-nombre">Nombre</label><input id="r-nombre" name="nombre" autocomplete="given-name" required></div>
          <div class="campo"><label for="r-apellidos">Apellidos</label><input id="r-apellidos" name="apellidos" autocomplete="family-name" required></div>
          <div class="campo"><label for="r-email">Email</label><input id="r-email" name="email" type="email" autocomplete="email" required></div>
          <div class="campo"><label for="r-tel">Teléfono</label><input id="r-tel" name="telefono" type="tel" autocomplete="tel" required></div>
          <label class="legal full"><input type="checkbox" name="privacidad" value="Aceptada" required><span>He leído y acepto la <a href="../privacidad.html">política de privacidad</a>.</span></label>
          <p class="form-error full" role="alert" hidden></p>
          <button type="submit" class="btn btn-primario full">Reservar mi plaza {ARROW}</button>
        </form>
        <div class="form-ok" role="status"><div class="ok">✓</div><h3>¡Ya casi está!</h3><p>Te escribimos con el enlace de pago y el acceso al campus.</p></div>
      </div>
    </div>
  </div>
</section>'''

DIALOGO = '''<dialog class="pago" id="pago" aria-labelledby="pago-titulo">
  <div class="pago-cab">
    <div><span class="pago-pre">Pago seguro con Stripe</span><h2 id="pago-titulo">Tu curso</h2></div>
    <button type="button" class="pago-cerrar" id="pago-cerrar" aria-label="Cerrar el pago">&times;</button>
  </div>
  <div class="pago-aviso" id="pago-aviso" role="alert" hidden></div>
  <div id="pago-form"></div>
</dialog>'''

def pagina_curso(slug):
    P = PACKS[slug]; D = PART[slug]; nv = D['nivel']
    anclas = [('consigues', 'Qué consigues'), ('recorrido', 'Recorrido'), ('temario', 'Temario'), ('como', 'Cómo estudias'),
              ('certificado', 'Certificado'), ('comparar', 'Comparar niveles'), ('faqs', 'Preguntas')]
    nav = '<nav class="anclas" aria-label="Secciones del curso">\n  <div class="wrap">\n' + ''.join(f'    <a href="#{a}">{t}</a>\n' for a, t in anclas) + '    <a href="#compra" class="apunta">Comprar</a>\n  </div>\n</nav>'
    para = ''.join(f'<div class="pq">{ico(i)}<div><b>{e(t)}</b><span>{e(d)}</span></div></div>' for i, t, d in D['para'])
    logros = ''.join(f'<article class="logro reveal">{ilus(il)}<h3>{e(t)}</h3><p>{e(d)}</p></article>' for il, t, d in D['logros'])
    ej = D['ejemplo']
    mentoria = ''
    if P['mentoria']:
        h = int(P['mentoria'].split()[0])
        trozos = ''.join('<span class="tz">30 min</span>' if i % 2 == 0 else '<span class="tz l">1 h</span>' for i in range(h + 1))
        mentoria = f'''
        <div class="mentor-caja reveal">
          {ilus('mentoria', 'ilus pequena')}
          <div>
            <b>{e(P['mentoria'])} de mentoría 1 a 1</b>
            <p>Por videollamada, cuando tú quieras durante los 12 meses. Todas juntas o repartidas, por ejemplo así:</p>
            <div class="trozos">{trozos}</div>
            <ul class="lista-ok"><li>Al empezar: definimos tu caso y qué quieres conseguir.</li><li>A mitad: resolvemos dudas y desbloqueamos lo que no te sale.</li><li>Al acabar: revisamos tu proyecto y los siguientes pasos.</li></ul>
          </div>
        </div>'''
    preguntas = D['faq_extra'] + FAQ_COMUN
    contenido = f'''
<!-- ============ HERO + COMPRA ============ -->
{hero([P['nombre']], P['et'], D['h1'], D['sub'], f'<b>{e(D["lead"])}</b> {e(D["intro"])}', D['chips'], compra_card(slug))}

<!-- ============ NAVEGACIÓN ============ -->
{nav}

<!-- ============ PARA QUIÉN ============ -->
<section class="para-part" aria-label="Para quién es">
  <div class="wrap"><div class="para-quien reveal">{para}</div></div>
</section>

<!-- ============ QUÉ CONSIGUES ============ -->
<section class="consigues" id="consigues">
  <div class="wrap">
    {cab('Qué consigues', 'Al acabar', 'vas a saber', e(D['sale']))}
    <div class="logros">{logros}</div>
    <div class="ejemplo reveal">
      <div class="ej-txt">
        <div class="pre">Un ejemplo</div>
        <h3>{e(ej['titulo'])}</h3>
        <p>{e(ej['nota'])}</p>
      </div>
      <div class="ej-chat" role="img" aria-label="Ejemplo de conversación con Claude">
        <div class="ej-yo"><span>Tú</span><p>{e(ej['pide'])}</p></div>
        <div class="ej-cl"><img src="../assets/herramientas/claude.svg" alt=""><p>{e(ej['responde'])}</p></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ RECORRIDO ============ -->
{recorrido(nv)}

<!-- ============ TEMARIO ============ -->
<section class="temario" id="temario">
  <div class="wrap tem-grid">
    <div class="tem-lado reveal">
      <div class="pre">Temario</div>
      <h2>Qué vas a ver <span class="acento">módulo a módulo</span></h2>
      <p class="intro">Cada módulo son vídeos cortos y un ejercicio con tus propios documentos. Lo haces a tu ritmo, en el orden que te vaya mejor.</p>
      <div class="tem-sale"><span class="logo-tile"><svg><use href="#i-shield"/></svg></span><div><b>Te llevas</b><p>{e(D['sale'])}</p></div></div>
    </div>
    <div>
      <div class="tem-cab">
        <p class="tem-total"><b>{sum(1 for m in RECORRIDO if m['nivel'] <= nv)} módulos y certificado</b> · {e(P['cuenta'])}</p>
        <div class="faq-acciones"><button type="button" data-acordeon="tem-part" data-accion="abrir">Expandir todo</button><button type="button" data-acordeon="tem-part" data-accion="cerrar">Contraer todo</button></div>
      </div>
{temario_part(nv)}
    </div>
  </div>
</section>

<!-- ============ CÓMO ESTUDIAS ============ -->
<section class="como-est" id="como">
  <div class="wrap">
    <div class="dos-col">
      <div class="reveal">
        <div class="pre">Cómo estudias</div>
        <h2>En el campus, <span class="acento">a tu ritmo</span></h2>
        <p class="intro">Entras el mismo día que compras y tienes 12 meses para hacerlo. Desde el ordenador o el móvil, en el orden que quieras.</p>
        <ul class="lista-check">
          <li><span><b>Vídeos cortos</b> que puedes ver y repetir cuando quieras.</span></li>
          <li><span><b>Ejercicios con tus documentos</b>: practicas con tu trabajo real, no con ejemplos inventados.</span></li>
          <li><span><b>Guías descargables</b> para tenerlas a mano cuando uses Claude.</span></li>
          <li><span>{'<b>Proyecto corregido</b> por una formadora, con sus comentarios.' if nv > 1 else '<b>Test final</b> corto para descargar tu certificado.'}</span></li>
        </ul>
        <a href="como-funciona.html" class="btn btn-primario">Cómo funciona paso a paso {ARROW}</a>
      </div>
      <div class="reveal">{campus_mock(nv)}</div>
    </div>{mentoria}
  </div>
</section>

<!-- ============ CERTIFICADO ============ -->
<section class="aiact" id="certificado">
  <div class="wrap dos-col">
    <div class="cert-caja reveal">
      {cert_papel(P['nombre'], 'Ejemplo de certificado del curso ' + P['nombre'])}
    </div>
    <div class="reveal">
      <div class="pre">Certificado</div>
      <h2>Un certificado alineado con <span class="acento">el AI Act</span></h2>
      <p class="intro">El artículo 4 del Reglamento Europeo de IA pide a quien usa IA en su trabajo que se forme para usarla bien. Tu certificado deja constancia de esa formación, con tu nombre, las horas y los contenidos.</p>
      <ul class="lista-check">
        <li><span><b>Nominativo y verificable:</b> lleva un QR que abre una página de Westlabs con tu nombre, el curso, las horas y la fecha.</span></li>
        <li><span><b>Alineado con el artículo 4</b> del Reglamento Europeo de IA: el curso incluye el módulo de IA segura y legal.</span></li>
        <li><span>El modelo de certificado y el programa están <b>protocolizados ante notario</b>.</span></li>
        <li><span>Lo puedes añadir a tu perfil de LinkedIn y enseñarlo a tu empresa o a tus clientes.</span></li>
      </ul>
      <a href="certificado.html" class="btn btn-primario">Todo sobre el certificado {ARROW}</a>
    </div>
  </div>
</section>

<!-- ============ COMPARAR ============ -->
{comparativa(slug)}

<!-- ============ FAQ ============ -->
{faq_sec(preguntas, 'Lo que más nos preguntan sobre ' + e(P['nombre']) + '.')}

<!-- ============ CTA FINAL ============ -->
{cta_final('Empieza hoy', P['nombre'], f"{P['normal']} con IVA, o 3 plazos de {plazo(slug)} sin intereses. Acceso al campus el mismo día.",
           f'<a href="#compra" class="btn btn-claro">Comprar {ARROW}</a>' + chr(10) + f'        <a href="{WHATSAPP}" target="_blank" rel="noopener" class="btn btn-borde">Tengo una duda</a>')}

{reserva(slug)}
{DIALOGO}
'''
    return pagina(f'{P["nombre"]} · Curso de Claude para particulares · Westlabs', D['desc'], P['nombre'], contenido, pago=True)


# ---------------------------------------------------------------- cómo funciona
def pagina_como():
    pasos = ''.join(f'<li class="reveal"><span class="pn">{i}</span>{ico(ic)}<b>{e(t)}</b><span>{e(d)}</span></li>' for i, (ic, t, d) in enumerate(PASOS, 1))
    p1, p2, p3 = (precio(s) for s in NIVELES)
    subir = f'''<div class="subir reveal" role="img" aria-label="Si subes de nivel pagas solo la diferencia">
          <div class="sb n1"><img src="../assets/3d/medalla-1.png" alt=""><b>{e(PACKS[NIVELES[0]]['nombre'])}</b><span>{euros(p1)}</span></div>
          <div class="sb-flecha"><span>+ {euros(p2 - p1)}</span></div>
          <div class="sb n2"><img src="../assets/3d/medalla-2.png" alt=""><b>{e(PACKS[NIVELES[1]]['nombre'])}</b><span>{euros(p2)}</span></div>
          <div class="sb-flecha"><span>+ {euros(p3 - p2)}</span></div>
          <div class="sb n3"><img src="../assets/3d/medalla-3.png" alt=""><b>{e(PACKS[NIVELES[2]]['nombre'])}</b><span>{euros(p3)}</span></div>
        </div>'''
    preguntas = [
        ('¿Cuánto tiempo tengo para hacer el curso?', '12 meses desde que entras en el campus. Lo haces a tu ritmo: hay quien lo acaba en unas semanas y quien va poco a poco.'),
        ('¿Puedo hacerlo desde el móvil?', 'Sí. El campus funciona en el ordenador, la tableta y el móvil. Para los ejercicios con tus documentos te irá mejor el ordenador.'),
        ('¿Cómo reservo la mentoría?', 'Desde el campus tienes un enlace a la agenda: eliges día y hora. Puedes usar tus horas de golpe o en sesiones de 30 minutos o de 1 hora, durante los 12 meses.'),
        ('¿Cómo subo de nivel?', 'Escríbenos y te pasamos el enlace para pagar la diferencia. Mantienes todo lo que has hecho y se te abren los módulos nuevos.'),
        ('¿Qué pasa si me atasco?', 'En los niveles 2 y 3 tienes tu mentoría. En cualquier nivel nos puedes escribir a gerard@westlabs.es o por WhatsApp.'),
        ('¿En qué idioma es el campus?', 'En castellano.'),
    ]
    contenido = f'''
{hero(['Cómo funciona'], 'Particulares · Teleformación', 'Así se aprende en el campus', 'Vídeos, ejercicios con tus documentos y una formadora a tu lado',
      'Compras tu nivel, entras el mismo día y lo haces a tu ritmo durante 12 meses. Te contamos cómo es por dentro, cómo funciona la mentoría y qué pasa si quieres subir de nivel.',
      ['Empiezas hoy', '12 meses de acceso', 'Mentoría 1 a 1', 'Pago en 3 plazos'],
      '      <div class="hero-ilus">' + ilus('campus', 'ilus grande') + '</div>')}

<section class="pasos-sec" id="pasos">
  <div class="wrap">
    {cab('Paso a paso', 'De la compra', 'al certificado')}
    <ol class="camino">{pasos}</ol>
  </div>
</section>

<section class="como-est" id="campus">
  <div class="wrap dos-col">
    <div class="reveal">
      <div class="pre">El campus</div>
      <h2>Una lección <span class="acento">por dentro</span></h2>
      <p class="intro">Cada módulo tiene vídeos cortos, una guía descargable y un ejercicio que haces con tus propios documentos. Ves tu avance en todo momento y puedes repetir lo que quieras.</p>
      <ul class="lista-check">
        <li><span><b>Vídeos cortos</b>, de pocos minutos, para verlos cuando tengas un rato.</span></li>
        <li><span><b>Ejercicios con tu trabajo real</b>: tus correos, tus informes, tus presupuestos.</span></li>
        <li><span><b>Proyecto final</b>: en los niveles 2 y 3, te lo corrige una formadora.</span></li>
      </ul>
    </div>
    <div class="reveal">{campus_mock(2)}</div>
  </div>
</section>

<section class="mentoria-sec" id="mentoria">
  <div class="wrap dos-col">
    <div class="reveal">{ilus('mentoria', 'ilus grande')}</div>
    <div class="reveal">
      <div class="pre">Mentoría 1 a 1</div>
      <h2>Una formadora <span class="acento">a tu lado</span></h2>
      <p class="intro">En Claude Avanzado tienes 2 horas y en Claude Completo, 3. Son sesiones individuales por videollamada que reservas cuando quieras durante los 12 meses.</p>
      <div class="momentos">
        <div><span>1</span><b>Al empezar</b><small>Definimos tu caso y qué quieres conseguir.</small></div>
        <div><span>2</span><b>A mitad</b><small>Resolvemos dudas y desbloqueamos lo que no te sale.</small></div>
        <div><span>3</span><b>Al acabar</b><small>Revisamos tu proyecto y los siguientes pasos.</small></div>
      </div>
    </div>
  </div>
</section>

<section class="subir-sec" id="subir">
  <div class="wrap">
    {cab('Subir de nivel', 'Empieza por uno', 'y sube cuando quieras', 'Cada nivel incluye el anterior. Si empiezas por Claude Esencial y después quieres más, pagas solo la diferencia y sigues donde lo dejaste.')}
    {subir}
  </div>
</section>

<section class="pago-sec" id="pago-info">
  <div class="wrap">
    <div class="pago-grid">
      <div class="pg reveal">{ico('i-euro')}<b>De una vez o en 3 plazos</b><span>Sin intereses. En 3 plazos pagas una parte hoy y el resto en los dos meses siguientes.</span></div>
      <div class="pg reveal">{ico('i-shield')}<b>Pago seguro con Stripe</b><span>Tarjeta, Apple Pay, Google Pay o Klarna, sin salir de la página del curso.</span></div>
      <div class="pg reveal">{ico('i-receipt')}<b>Códigos de descuento</b><span>Si tienes uno, lo escribes antes de pagar y ves el precio rebajado.</span></div>
      <div class="pg reveal">{ico('i-laptop')}<b>Qué necesitas</b><span>Ordenador con internet y una cuenta de Claude: gratuita para el nivel 1, Pro para los niveles 2 y 3.</span></div>
    </div>
  </div>
</section>

{niveles_mini(None)}

{faq_sec(preguntas, 'Sobre el campus, la mentoría y el pago.')}

{cta_final('Elige tu nivel', 'y empieza hoy', 'Cada curso tiene su página con el temario completo. La compra se hace ahí.', f'<a href="#niveles" class="btn btn-claro">Ver los tres niveles {ARROW}</a>' + chr(10) + f'        <a href="certificado.html" class="btn btn-borde">Ver el certificado</a>')}
'''
    return pagina('Cómo funciona el campus · Cursos de Claude para particulares · Westlabs',
                  'Cómo son los cursos de Claude para particulares de Westlabs: campus a tu ritmo durante 12 meses, mentoría 1 a 1, subir de nivel pagando la diferencia y pago en 3 plazos.',
                  'Particulares · Cómo funciona', contenido)


# ---------------------------------------------------------------- certificado
def pagina_certificado():
    hitos = [('1 ago 2024', 'Entra en vigor', 'El Reglamento Europeo de IA se publica y empieza a contar el calendario.'),
             ('2 feb 2025', 'Artículo 4: alfabetización', 'Quien usa IA en su trabajo tiene que formarse para usarla bien. Es de las primeras normas que se aplican.', True),
             ('2 ago 2025', 'Modelos de uso general', 'Normas para quienes crean modelos como los que hay detrás de Claude o ChatGPT.'),
             ('2026', 'Supervisión y ajustes', 'Empiezan la supervisión y las sanciones, y la UE ajusta el reglamento. El artículo 4 sigue vigente.')]
    tl = ''.join(f'<li class="reveal{" dest" if len(h) > 3 else ""}"><span class="tl-f">{e(h[0])}</span><b>{e(h[1])}</b><small>{e(h[2])}</small></li>' for h in hitos)
    partes = [('1', 'Tu nombre', 'Certificado nominativo, a tu nombre.'), ('2', 'El curso y las horas', 'Qué curso has hecho y cuántas horas.'),
              ('3', 'Los contenidos', 'Incluida la alfabetización en IA del artículo 4.'), ('4', 'El QR', 'Abre una página de Westlabs que lo verifica.'),
              ('5', 'El sello AI Act', 'Deja claro que cubre el artículo 4.'), ('6', 'La entidad formadora', 'Westlabs, con el programa protocolizado ante notario.')]
    leyenda = ''.join(f'<li><span class="cn-num">{n}</span><div><b>{e(t)}</b><small>{e(d)}</small></div></li>' for n, t, d in partes)
    verif = [('i-phone', 'Escaneas el QR', 'Con la cámara del móvil, o abres el enlace.'), ('i-pin', 'Abre la web de Westlabs', 'Una página propia de tu certificado.'),
             ('i-doc', 'Ves los datos', 'Nombre, curso, horas y fecha.'), ('i-check', 'Queda verificado', 'Sin llamadas ni papeles.')]
    vf = ''.join(f'<li class="reveal">{ico(i)}<b>{e(t)}</b><small>{e(d)}</small></li>' for i, t, d in verif)
    pide = [('i-users', 'Formarte para usar la IA', 'Saber qué puede hacer, cómo funciona y dónde se equivoca.'),
            ('i-shield', 'Conocer los riesgos', 'Datos personales, confidencialidad y revisar lo que te devuelve.'),
            ('i-target', 'Según tu uso', 'La formación tiene que encajar con lo que haces con la IA en tu trabajo.'),
            ('i-doc', 'Poder demostrarlo', 'Tener constancia de la formación: horas, contenidos y fecha.')]
    pide_h = ''.join(f'<div class="pq reveal">{ico(i)}<div><b>{e(t)}</b><span>{e(d)}</span></div></div>' for i, t, d in pide)
    preguntas = [
        ('¿Es un título oficial?', 'No. Es un certificado de formación de Westlabs, nominativo y verificable, alineado con el artículo 4 del Reglamento Europeo de IA. No es un título oficial ni homologado: el reglamento no crea un título oficial para esto, pide que haya formación y que se pueda demostrar.'),
        ('¿Qué cursos dan este certificado?', 'Los tres niveles de Claude para particulares: Claude Esencial, Claude Avanzado y Claude Completo. Todos incluyen el módulo de IA segura y legal.'),
        ('¿Cuándo lo recibo?', 'Al acabar el curso: en Claude Esencial, al aprobar el test final; en Claude Avanzado y Claude Completo, al entregar tu proyecto.'),
        ('¿Me sirve si trabajo por cuenta propia?', 'Sí. Si usas IA con tus clientes o en tu trabajo, el certificado deja constancia de que te has formado, con horas y contenidos.'),
        ('¿Y si la norma cambia?', 'Revisamos los contenidos cuando cambia la normativa. En 2026 la UE ha ajustado el reglamento y el artículo 4 sigue vigente.'),
        ('¿Lo puedo poner en LinkedIn?', 'Sí. Puedes añadirlo en «Licencias y certificaciones» con el enlace de verificación.'),
    ]
    contenido = f'''
{hero(['Certificado'], 'Particulares · Certificado', 'Tu certificado de IA, alineado con el AI Act', 'Nominativo, verificable con QR y protocolizado ante notario',
      'El artículo 4 del Reglamento Europeo de IA pide a quien usa IA en su trabajo que se forme para usarla bien. Con cualquiera de los tres cursos de Claude te llevas un certificado que lo demuestra.',
      ['Artículo 4 del AI Act', 'Verificable con QR', 'Protocolizado ante notario', 'Para LinkedIn'],
      '      <div class="cert-caja hero-cert">' + cert_papel('Claude Esencial', 'Ejemplo de certificado de Westlabs AI School') + '</div>')}

<section class="ley" id="ai-act">
  <div class="wrap">
    {cab('La ley', 'El Reglamento Europeo de IA', 'en sencillo', 'Es la ley de la Unión Europea que regula la inteligencia artificial, también conocida como AI Act. Se aplica por fases y una de las primeras es la formación.')}
    <ol class="linea-t">{tl}</ol>
  </div>
</section>

<section class="art4" id="articulo-4">
  <div class="wrap dos-col">
    <div class="reveal">
      <div class="pre">Artículo 4</div>
      <h2>Qué pide <span class="acento">la alfabetización en IA</span></h2>
      <p class="intro">El artículo 4 habla de «alfabetización en IA»: que las personas que usan IA en su trabajo tengan los conocimientos necesarios para usarla con criterio. En la práctica, esto es lo que se espera:</p>
      <div class="pide">{pide_h}</div>
      <p class="nota-legal">Resumen orientativo. No sustituye el asesoramiento jurídico de cada caso.</p>
    </div>
    <div class="reveal">{ilus('escudo', 'ilus grande')}</div>
  </div>
</section>

<section class="anatomia" id="que-incluye">
  <div class="wrap">
    {cab('Tu certificado', 'Qué incluye', 'tu certificado')}
    <div class="anat reveal">
      <div class="anat-cert">
        {cert_papel('Claude Avanzado', 'Ejemplo de certificado con sus partes numeradas')}
        <span class="cn-num p1">1</span><span class="cn-num p2">2</span><span class="cn-num p3">3</span><span class="cn-num p4">4</span><span class="cn-num p5">5</span><span class="cn-num p6">6</span>
      </div>
      <ol class="anat-ley">{leyenda}</ol>
    </div>
  </div>
</section>

<section class="verifica" id="verifica">
  <div class="wrap">
    {cab('Verificación', 'Cualquiera puede', 'comprobarlo en segundos', 'Tu empresa, un cliente o quien vea tu perfil puede comprobar que el certificado es tuyo y es real.')}
    <ol class="flujo">{vf}</ol>
  </div>
</section>

{niveles_mini(None, ('Consíguelo con', 'cualquier nivel'))}

{faq_sec(preguntas, 'Sobre el certificado y el artículo 4 del AI Act.')}

{cta_final('Fórmate y', 'demuéstralo', 'Los tres niveles de Claude incluyen el certificado alineado con el artículo 4.', f'<a href="#niveles" class="btn btn-claro">Elige tu nivel {ARROW}</a>' + chr(10) + f'        <a href="como-funciona.html" class="btn btn-borde">Cómo funciona</a>')}
'''
    return pagina('Certificado de IA alineado con el AI Act (artículo 4) · Westlabs',
                  'El certificado de los cursos de Claude de Westlabs: nominativo, verificable con QR, protocolizado ante notario y alineado con el artículo 4 del Reglamento Europeo de IA.',
                  'Particulares · Certificado', contenido)


# ---------------------------------------------------------------- generar
def generar():
    d = os.path.join(RAIZ, 'particulares'); os.makedirs(d, exist_ok=True)
    paginas = {f'{s}.html': pagina_curso(s) for s in NIVELES}
    paginas['como-funciona.html'] = pagina_como()
    paginas['certificado.html'] = pagina_certificado()
    for nombre, txt in paginas.items():
        open(os.path.join(d, nombre), 'w', encoding='utf-8').write(txt)
    return list(paginas)

if __name__ == '__main__':
    print('Generadas:', ', '.join(generar()))
