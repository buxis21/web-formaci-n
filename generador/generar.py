# -*- coding: utf-8 -*-
"""
GENERADOR DE FICHAS DE CURSO
    python3 generador/generar.py
Crea cursos/<slug>.html para cada curso de datos.py y el MAPA-WEB.md.
Las partes comunes (iconos, cabecera, pie) están en generador/parciales/.
No edites a mano los HTML de cursos/: se sobrescriben al generar.
"""
import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from datos import CURSOS, POR_SLUG, HERR, CAMPUS, CAMPUS_TEMARIO, CONVOCATORIA, siguientes

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARC = os.path.join(os.path.dirname(__file__), 'parciales')
leer = lambda f: open(os.path.join(PARC, f), encoding='utf-8').read()
ICONOS, CABECERA, PIE = leer('iconos.html'), leer('cabecera.html'), leer('pie.html')
WEB3FORMS = 'ab432877-6901-4527-b6b2-86e117e9f28f'
CONV_ANUNCIADAS = {'alfabetizacion-en-ia', 'claude-esencial', 'chatgpt-esencial', 'microsoft-365-copilot-esencial', 'copilot-studio-i-crea-tu-primer-agente'}
e = lambda t: html.escape(str(t), quote=True)
ARROW = '<svg class="i fl"><use href="#i-arrow"/></svg>'

def horas(h):
    return (f'{h:g}'.replace('.', ',')) + ' h'

def tile(logo, alt=''):
    return f'<span class="logo-tile"><img src="../assets/herramientas/{logo}" alt="{e(alt)}"></span>'

def tiles(c, alts=False):
    if len(c['tools']) == 1:
        return tile(c['tools'][0], c.get('tools_txt', '') if alts else '')
    if not c['tools']:
        return f'<span class="logo-tile"><svg><use href="#{c["ico"]}"/></svg></span>'
    return '<span class="logos">' + ''.join(tile(t) for t in c['tools']) + '</span>'

def tools_txt(c):
    if c.get('tools_txt'): return c['tools_txt']
    return HERR[c['herr']]['nombre']

def campus_info(c):
    """Qué ofrece el campus en este curso: (horas_txt, texto_precio, opción particulares)"""
    if c.get('campus') == 'ready':
        return '10 h', '<b>119 €</b> con IVA · empresas: bonificable'
    if c.get('campus') == 'build':
        return 'Dentro de Build · 25 h', '<b>349 €</b> con IVA (230 € si ya tienes Ready)'
    if c.get('campus') == 'agents':
        return 'Dentro de Agents · 40 h', '<b>469 €</b> con IVA (120 € si ya tienes Build)'
    if c['hc']:
        return horas(c['hc']), 'Para empresas: bonificable por FUNDAE'
    return None, None

# ---------------------------------------------------------------- bloques
def hero(c):
    tiene_part = c['dir'] or c.get('campus')
    chips = [f'{horas(c["h"])}' + (f' · campus {horas(c["hc"])}' if isinstance(c['hc'], (int, float)) and c['hc'] else ''),
             'Sin requisitos' if c['req'] == 'Ninguno' else f'Requisito: {c["req"]}', 'Certificado verificable', 'Bonificable FUNDAE']
    if c.get('campus') in ('build', 'agents'):
        chips[0] = f'{horas(c["h"])} · en campus dentro de {c["campus"].capitalize()}'
    chips_html = ''.join(f'<span class="chip-h{" dest" if i == 0 else ""}"><svg class="i"><use href="#i-check"/></svg>{e(t)}</span>' for i, t in enumerate(chips))
    if len(c['tools']) > 1:
        logos = '<span class="logos">' + ''.join(tile(t, a) for t, a in zip(c['tools'], ['Claude', 'ChatGPT', 'Microsoft 365 Copilot', 'Gemini'])) + '</span>'
    else:
        logos = '<span class="logos">' + tile(c['tools'][0], tools_txt(c)) + '</span>'
    return f'''<section class="hero hero-curso oscuro" id="top">
  <canvas class="cielo" aria-hidden="true"></canvas>
  <div class="wrap">
    <nav class="migas" aria-label="Estás en"><a href="../index.html">Inicio</a><span>/</span><a href="../index.html#oferta">Cursos</a><span>/</span>{e(c['n'])}</nav>
    <div class="grid">
      <div>
        <div class="pre">{e(c['et'])}</div>
        <h1>{e(c['n'])}</h1>
        <span class="sub">{e(c['sub'])}</span>
        <p class="intro"><b>{e(c['lead'])}</b> {e(c['intro'])}</p>
        <div class="chips">{chips_html}</div>
        <div class="herr-hero"><small>{'Herramientas' if len(c['tools']) > 1 else 'Herramienta'}</small>{logos}</div>
      </div>
{inscripcion(c)}
    </div>
  </div>
  <svg class="ola" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 80V40C240 0 480 0 720 30s480 40 720 0v50z" fill="#fff"/></svg>
</section>'''

def ocultos(asunto):
    return f'''
            <input type="hidden" name="access_key" value="{WEB3FORMS}">
            <input type="hidden" name="subject" value="{e(asunto)}">
            <input type="hidden" name="from_name" value="Web Westlabs AI School">
            <input type="checkbox" name="botcheck" class="sr" tabindex="-1" autocomplete="off" aria-hidden="true">'''

def inscripcion(c):
    mods = []
    if c['dir']: mods.append('Online en directo')
    if c['ic']: mods += ['In company online', 'In company presencial']
    if c['hc']: mods.append('Campus')
    opts = ''.join(f'<option>{m}</option>' for m in mods + ['Aún no lo sé'])
    emp = f'''        <div class="ins-panel" role="tabpanel" id="panel-emp" aria-labelledby="tab-emp">
          <h2>Hablemos de la formación de tu equipo</h2>
          <p class="ayuda">Te preparamos una propuesta con fechas, modalidad y gestión de FUNDAE.</p>
          <form class="form" data-form="empresas" data-endpoint="https://api.web3forms.com/submit" novalidate>{ocultos('Propuesta para empresa · ' + c['n'])}
            <div class="campo"><label for="e-nombre">Nombre</label><input id="e-nombre" name="nombre" autocomplete="given-name" required></div>
            <div class="campo"><label for="e-apellidos">Apellidos</label><input id="e-apellidos" name="apellidos" autocomplete="family-name" required></div>
            <div class="campo full"><label for="e-email">Email</label><input id="e-email" name="email" type="email" autocomplete="email" required></div>
            <div class="campo"><label for="e-tel">Teléfono</label><input id="e-tel" name="telefono" type="tel" autocomplete="tel" required></div>
            <div class="campo"><label for="e-empresa">Empresa</label><input id="e-empresa" name="empresa" autocomplete="organization" required></div>
            <div class="campo"><label for="e-personas">Número de personas</label>
              <select id="e-personas" name="personas" required><option value="">Elige</option><option>1 a 5</option><option>6 a 10</option><option>11 a 25</option><option>26 a 50</option><option>Más de 50</option></select></div>
            <div class="campo"><label for="e-modalidad">Modalidad</label>
              <select id="e-modalidad" name="modalidad" required><option value="">Elige</option>{opts}</select></div>
            <div class="campo full"><span class="grupo-t" id="e-fundae-t">¿Queréis que gestionemos la FUNDAE?</span>
              <div class="opciones dos" role="radiogroup" aria-labelledby="e-fundae-t">
                <label class="op"><input type="radio" name="fundae" value="Sí" required><span>Sí, gestionadla</span></label>
                <label class="op"><input type="radio" name="fundae" value="No"><span>No hace falta</span></label>
              </div></div>
            <div class="campo full"><label for="e-com">Comentarios</label><textarea id="e-com" name="comentarios" placeholder="Fechas, idioma, áreas del equipo…"></textarea></div>
            <label class="legal full"><input type="checkbox" name="privacidad" value="Aceptada" required><span>He leído y acepto la <a href="../privacidad.html">política de privacidad</a>.</span></label>
            <p class="form-error full" role="alert" hidden></p>
            <button type="submit" class="btn btn-primario full">Solicita propuesta {ARROW}</button>
          </form>
          <div class="form-ok" role="status"><div class="ok">✓</div><h3>Gracias, lo tenemos</h3><p>Te escribimos para conocer a tu equipo y prepararte la propuesta.</p></div>
        </div>'''
    part_ops = []
    camp = c.get('campus')
    if camp:
        h_txt, _ = campus_info(c)
        P = CAMPUS[camp]
        nota = f'IVA incluido<br>{h_txt} en campus · 12 meses de acceso' if camp == 'ready' else f'IVA incluido<br>{P["et"]} · 12 meses de acceso'
        cuenta_txt = 'Cuenta gratuita de Claude, ChatGPT y Gemini' if camp == 'ready' else 'Necesitas Claude Pro (no incluida)'
        titulo = 'Campus, a tu ritmo' if camp == 'ready' else f'Campus, a tu ritmo · {P["et"].split(" · ")[0]}'
        part_ops.append((titulo, f'Empiezas cuando quieras · {cuenta_txt}', 'Campus', P['precio'], nota))
    if c['dir']:
        cuando = CONVOCATORIA.lower() if c['slug'] in CONV_ANUNCIADAS else 'fechas por confirmar'
        part_ops.append(('Online en directo', f'{int(c["h"] / 2)} sesiones de 2 h · {cuando}', 'Online en directo', 'Próximamente',
                         ('Primer trimestre de 2027<br>' if c['slug'] in CONV_ANUNCIADAS else 'Te avisamos cuando abramos grupo<br>') + 'fechas y precio por confirmar'))
    if not part_ops:
        return f'''      <div class="inscripcion solo-emp" id="inscripcion">
        <div class="ins-solo"><svg class="i"><use href="#i-building"/></svg>Curso para empresas · in company</div>
{emp}
      </div>'''
    radios = ''.join(
        f'<label class="op"><input type="radio" name="modalidad" value="{e(v)}"{" checked" if i == 0 else ""} data-precio-op="{e(p)}" data-precio-nota="{e(n)}"><span>{e(t)}<small>{e(s)}</small></span></label>'
        for i, (t, s, v, p, n) in enumerate(part_ops))
    p0 = part_ops[0]
    part = f'''        <div class="ins-panel" role="tabpanel" id="panel-part" aria-labelledby="tab-part" hidden>
          <h2>Apúntate al curso</h2>
          <p class="ayuda">{'Hazlo a tu ritmo en el campus o en directo con un grupo reducido.' if len(part_ops) > 1 else ('Hazlo a tu ritmo en el campus.' if camp else 'En directo, con un grupo reducido de varias empresas.')}</p>
          <div class="precio" id="precio-part"><b>{e(p0[3])}</b><span>{p0[4]}</span></div>
          <form class="form" data-form="particulares" data-endpoint="https://api.web3forms.com/submit" novalidate>{ocultos('Matrícula de particular · ' + c['n'])}
            <div class="campo full"><span class="grupo-t" id="p-mod-t">Modalidad</span>
              <div class="opciones" role="radiogroup" aria-labelledby="p-mod-t">
                {radios}
              </div></div>
            <div class="campo"><label for="p-nombre">Nombre</label><input id="p-nombre" name="nombre" autocomplete="given-name" required></div>
            <div class="campo"><label for="p-apellidos">Apellidos</label><input id="p-apellidos" name="apellidos" autocomplete="family-name" required></div>
            <div class="campo"><label for="p-email">Email</label><input id="p-email" name="email" type="email" autocomplete="email" required></div>
            <div class="campo"><label for="p-tel">Teléfono</label><input id="p-tel" name="telefono" type="tel" autocomplete="tel" required></div>
            <label class="legal full"><input type="checkbox" name="privacidad" value="Aceptada" required><span>He leído y acepto la <a href="../privacidad.html">política de privacidad</a>.</span></label>
            <p class="form-error full" role="alert" hidden></p>
            <button type="submit" class="btn btn-primario full">{'Matricúlate' if camp else 'Avísame de las fechas'} {ARROW}</button>
          </form>
          <div class="form-ok" role="status"><div class="ok">✓</div><h3>¡Ya casi está!</h3><p>{'Te escribimos para completar la matrícula y darte acceso.' if camp else 'Te avisamos en cuanto abramos fechas.'}</p></div>
        </div>'''
    return f'''      <div class="inscripcion" id="inscripcion">
        <div class="ins-tabs" role="tablist" aria-label="¿Para quién es la formación?">
          <button role="tab" id="tab-emp" aria-controls="panel-emp" aria-selected="true"><svg class="i"><use href="#i-building"/></svg>Empresas</button>
          <button role="tab" id="tab-part" aria-controls="panel-part" aria-selected="false" tabindex="-1"><svg class="i"><use href="#i-users"/></svg>Particulares</button>
        </div>
{emp}
{part}
      </div>'''

def anclas(c):
    items = [('por-que', 'Por qué este curso'), ('modalidades', 'Fechas y modalidades'), ('temario', 'Temario'), ('certificado', 'Certificado')]
    if c.get('campus'): items.append(('precio', 'Particulares'))
    items += [('fundae', 'FUNDAE'), ('faqs', 'Preguntas')]
    return '<nav class="anclas" aria-label="Secciones del curso">\n  <div class="wrap">\n' + ''.join(f'    <a href="#{a}">{t}</a>\n' for a, t in items) + '    <a href="#inscripcion" class="apunta">¡Apúntate!</a>\n  </div>\n</nav>'

def info(c):
    mods = [m for m, ok in [('Directo', c['dir']), ('in company', c['ic']), ('campus', c['hc'])] if ok]
    mods_txt = mods[0] if len(mods) == 1 else ', '.join(mods[:-1]) + ' y ' + mods[-1]
    mods_txt = mods_txt[0].upper() + mods_txt[1:]
    h_campus, _ = campus_info(c)
    dur_small = f'<small>{"Campus: " + h_campus if h_campus and not h_campus.endswith(" h") or (h_campus and "Dentro" in h_campus) else (h_campus + " en campus" if h_campus else (str(int(c["h"] / 2)) + " sesiones de 2 h"))}</small>'
    if c['dir']:
        conv = (CONVOCATORIA, 'Campus: empieza cuando quieras' if c['hc'] else 'Grupo abierto en directo') if c['slug'] in CONV_ANUNCIADAS else ('Fechas por confirmar', 'In company: cuando os vaya bien')
    else:
        conv = ('A medida', 'En las fechas que elija tu empresa')
    return f'''<section class="info-curso" aria-label="Información del curso">
  <div class="wrap">
    <div class="datos reveal">
      <div class="dato"><span class="logo-tile"><svg><use href="#i-video"/></svg></span><h3>Duración</h3><p>{horas(c['h']).replace(' h', ' horas')}{dur_small}</p></div>
      <div class="dato"><span class="logo-tile"><svg><use href="#i-laptop"/></svg></span><h3>Modalidades</h3><p>{e(mods_txt)}</p></div>
      <div class="dato"><span class="logo-tile"><svg><use href="#i-grid"/></svg></span><h3>{'Herramientas' if len(c['tools']) > 1 else 'Herramienta'}</h3><p>{e(tools_txt(c))}</p></div>
      <div class="dato"><span class="logo-tile"><svg><use href="#i-compass"/></svg></span><h3>Requisitos</h3><p>{e(c['req'])}<small>{e(c['req_det'])}</small></p></div>
      <div class="dato"><span class="logo-tile"><svg><use href="#i-target"/></svg></span><h3>{'Próxima convocatoria' if c['dir'] else 'Fechas'}</h3><p>{e(conv[0])}<small>{e(conv[1])}</small></p></div>
    </div>
  </div>
</section>'''

def porque(c):
    foto = c.get('foto') or (HERR[c['herr']]['foto'] if c['herr'] in HERR else 'aula-practica.jpg')
    alt = c.get('foto_alt') or (HERR[c['herr']]['foto_alt'] if c['herr'] in HERR else '')
    ch = c['chip_foto']
    lista = ''.join(f'\n          <li><span>{l}</span></li>' for l in c['lista'])
    pq = ''.join(f'\n      <div class="pq"><span class="logo-tile"><svg><use href="#{i}"/></svg></span><div><b>{e(t)}</b><span>{e(d)}</span></div></div>' for i, t, d in c['pq'])
    return f'''<section class="porque-curso" id="por-que">
  <div class="wrap">
    <div class="dos-col">
      <div class="reveal">
        <div class="pre">Por qué este curso</div>
        <h2>{e(c['h2_porque'][0])} <span class="acento">{e(c['h2_porque'][1])}</span></h2>
        <p class="intro">{e(c['porque'])}</p>
        <ul class="lista-check">{lista}
        </ul>
        <div class="sales-con"><b>Sales con</b><p>{e(c['sale'])}</p></div>
      </div>
      <div class="foto-porque reveal">
        <figure><img src="../assets/fotos/{foto}" alt="{e(alt)}" loading="lazy"></figure>
        <div class="flotante-dato"><span class="logo-tile"><svg><use href="#{ch[0][0]}"/></svg></span><div>{e(ch[0][1])}<small>{e(ch[0][2])}</small></div></div>
        <div class="flotante-dato b"><span class="logo-tile"><svg><use href="#{ch[1][0]}"/></svg></span><div>{e(ch[1][1])}<small>{e(ch[1][2])}</small></div></div>
      </div>
    </div>
    <div class="para-quien reveal">{pq}
    </div>
  </div>
</section>'''

def modalidades(c):
    tarjetas = []
    ses = int(c['h'] / 2); jor = c['h'] / 4
    jor_txt = f'{int(jor)} jornadas de 4 h presenciales' if jor == int(jor) and jor > 1 else ('1 jornada de 4 h presencial' if jor == 1 else f'jornadas de 4 h presenciales')
    anunciada = c['slug'] in CONV_ANUNCIADAS
    if c['dir']:
        tarjetas.append(f'''      <article class="mf reveal">
        <div class="mf-media"><img class="mf-3d" src="../assets/3d/video.png" alt=""><img src="../assets/fotos/online.jpg" alt="Alumna conectada a una clase en directo por videollamada" loading="lazy"><span class="mf-badge">Particulares y empresas</span></div>
        <div class="mf-txt">
          <span class="mf-et">Online en directo</span>
          <h3>Grupo abierto</h3>
          <p class="mf-desc">Clases por videollamada con alumnos de varias empresas. Ideal si eres una persona o sois pocas.</p>
          <dl class="ficha">
            <div><dt>Duración</dt><dd>{horas(c['h'])} · {ses} sesiones de 2 h</dd></div>
            <div><dt>Fechas</dt><dd>{'Fijas · ' + CONVOCATORIA.lower() if anunciada else 'Fijas · por confirmar'}</dd></div>
            <div><dt>Grupo</dt><dd>Reducido, de varias empresas</dd></div>
            <div><dt>Casos</dt><dd>Los tuyos, corregidos en clase</dd></div>
            <div><dt>Precio</dt><dd>Por persona · por confirmar</dd></div>
          </dl>
          <a href="#inscripcion" class="btn btn-claro btn-sm" data-abre="tab-part">Avísame de las fechas {ARROW}</a>
        </div>
      </article>''')
    if c['ic']:
        tarjetas.append(f'''      <article class="mf mf-dest reveal">
        <div class="mf-media"><img class="mf-3d" src="../assets/3d/edificio.png" alt=""><img src="../assets/fotos/incompany-chatgpt.jpg" alt="Formación in company en las instalaciones de una empresa" loading="lazy"><span class="mf-badge">Empresas</span></div>
        <div class="mf-txt">
          <span class="mf-et">Online o presencial</span>
          <h3>Solo tu equipo</h3>
          <p class="mf-desc">Un grupo cerrado para tu empresa, por videollamada o en vuestras oficinas, con vuestros casos.</p>
          <dl class="ficha">
            <div><dt>Duración</dt><dd>{horas(c['h'])} · sesiones de 2 h online o {jor_txt}</dd></div>
            <div><dt>Fechas</dt><dd>Las que os vayan bien</dd></div>
            <div><dt>Grupo</dt><dd>Solo personas de tu empresa</dd></div>
            <div><dt>Casos</dt><dd>Preparados en una consultoría previa</dd></div>
            <div><dt>Precio</dt><dd>Por grupo, en la propuesta</dd></div>
          </dl>
          <a href="#inscripcion" class="btn btn-claro btn-sm"{' data-abre="tab-emp"' if (c['dir'] or c.get('campus')) else ''}>Solicita propuesta {ARROW}</a>
        </div>
      </article>''')
    h_campus, precio_campus = campus_info(c)
    if h_campus:
        camp = c.get('campus')
        if camp == 'ready':
            fil = [('Duración', '10 h, con más práctica'), ('Fechas', 'Empiezas cuando quieras · 12 meses de acceso'), ('Cuenta', 'Gratuita de Claude, ChatGPT y Gemini'), ('Casos', 'Miniproyecto autoevaluado'), ('Precio', precio_campus)]
            desc = 'Vídeos cortos, ejercicios con tus documentos, guías descargables y un test final.'
            badge = 'Particulares y empresas'
        elif camp in ('build', 'agents'):
            P = CAMPUS[camp]
            fil = [('Curso', f'{P["et"].split(" · ")[0]} · {P["nombre"]}'), ('Duración', P['et'].split(' · ')[1] + ' acumuladas'), ('Cuenta', 'Claude Pro (no incluida)'),
                   ('Casos', 'Proyecto corregido por una formadora' if camp == 'build' else 'Dos proyectos corregidos'), ('Precio', precio_campus)]
            desc = 'Este curso está incluido en uno de nuestros cursos del campus, con vídeos, ejercicios con tus documentos y proyectos corregidos.'
            badge = 'Particulares y empresas'
        else:
            fil = [('Duración', f'{h_campus}, con más práctica'), ('Fechas', 'Empiezas cuando quieras · 12 meses de acceso'), ('Casos', 'Proyectos con tu propio caso'), ('Precio', precio_campus)]
            desc = 'Teleformación a tu ritmo, con la teoría en vídeo y ejercicios con tu caso.'
            badge = 'Empresas'
        filas = ''.join(f'\n            <div><dt>{e(a)}</dt><dd>{b}</dd></div>' for a, b in fil)
        tarjetas.append(f'''      <article class="mf reveal">
        <div class="mf-media"><img class="mf-3d" src="../assets/3d/portatil.png" alt=""><img src="../assets/fotos/campus.jpg" alt="Pantalla de acceso a WestLabs Campus" loading="lazy"><span class="mf-badge">{badge}</span></div>
        <div class="mf-txt">
          <span class="mf-et">A tu ritmo</span>
          <h3>Campus</h3>
          <p class="mf-desc">{desc}</p>
          <dl class="ficha">{filas}
          </dl>
          <a href="#inscripcion" class="btn btn-claro btn-sm" data-abre="{'tab-part' if camp else 'tab-emp'}">{'Matricúlate' if camp else 'Solicita propuesta'} {ARROW}</a>
        </div>
      </article>''')
    n = len(tarjetas)
    intro = {3: 'El mismo temario y el mismo certificado en tres formatos. Para particulares y para empresas, según cuántas personas sois y cómo preferís aprender.',
             2: 'El mismo temario y el mismo certificado en dos formatos, según cuántas personas sois y cómo preferís aprender.',
             1: 'Un curso para hacer con tu equipo, online o en vuestras oficinas, con los casos de vuestra empresa.'}[n]
    return f'''<section class="modalidades oscuro" id="modalidades">
  <div class="wrap">
    <div class="cab-sec reveal">
      <div class="pre">Fechas y modalidades</div>
      <h2>{'Elige cómo' if n > 1 else 'Cómo es'} <span class="acento">{'quieres hacerlo' if n > 1 else 'la formación'}</span></h2>
      <p class="intro">{intro}</p>
    </div>
    <div class="modfotos mods-curso n{n}">
{chr(10).join(tarjetas)}
    </div>
    <p class="mods-nota reveal"><svg class="i"><use href="#i-check"/></svg>{'Todas las modalidades son bonificables por FUNDAE para empresas y dan el mismo certificado.' if n > 1 else 'Bonificable por FUNDAE: nos encargamos de toda la gestión.'}</p>
  </div>
</section>'''

def acordeon(id_, mods):
    out = []
    for i, m in enumerate(mods):
        num = '✓' if m['t'].startswith('Test final') else str(i + 1)
        comun = ' <span class="comun">común</span>' if m['comun'] else ''
        puntos = ''.join(f'\n            <li>{e(p)}</li>' for p in m['puntos'])
        llevas = f'\n            <p class="entregable"><b>Te llevas:</b> {e(m["llevas"])}</p>' if m.get('llevas') else ''
        out.append(f'''          <details{' open' if i == 0 else ''}><summary><span class="num">{num}</span><span class="t">{e(m['t'])}{comun}<small>{e(m['sub'])}</small></span><span class="hrs">{horas(m['h'])}</span></summary><div class="cuerpo"><ul>{puntos}</ul>{llevas}</div></details>''')
    return f'        <div class="acordeon" id="{id_}">\n' + '\n'.join(out) + '\n        </div>'

def temario(c):
    mods = c['temario']; total = sum(m['h'] for m in mods)
    assert abs(total - c['h']) < .01, (c['n'], total, c['h'])
    camp = c.get('campus'); tc = CAMPUS_TEMARIO.get(camp) if camp else None
    tiene_comun = any(m['comun'] for m in mods) or (tc and any(m['comun'] for m in tc))
    intro = ('Los módulos marcados como <span class="comun">común</span> son los mismos en todos nuestros cursos: si ya los has hecho con nosotros, te los saltas.'
             if tiene_comun else 'Cada módulo combina explicación y práctica con tus casos. Las horas son las de la modalidad en directo o in company.')
    etiqueta = 'Directo o in company' if c['dir'] else 'In company'
    if tc:
        tot_c = sum(m['h'] for m in tc)
        ncamp = {'ready': 'Campus', 'build': 'Campus · Build', 'agents': 'Campus · Agents'}[camp]
        tabs = f'''      <div class="tabs-c" role="tablist" aria-label="Versión del temario">
        <button role="tab" id="tt-dir" aria-controls="pt-dir" aria-selected="true">{etiqueta} <em>{horas(c['h'])}</em></button>
        <button role="tab" id="tt-cam" aria-controls="pt-cam" aria-selected="false" tabindex="-1">{ncamp} <em>{horas(tot_c) if camp == 'ready' else '+' + horas(tot_c)}</em></button>
      </div>'''
    else:
        tabs = ''
    sale = e(c['sale']) + (' ' + e(c['sale_campus']) if c.get('sale_campus') else '')
    nmods = len(mods)
    panel_dir = f'''      <div role="tabpanel" id="pt-dir" aria-labelledby="tt-dir">
        <div class="tem-cab">
          <p class="tem-total"><b>{nmods} módulos · {horas(c['h']).replace(' h', ' horas')}</b> · {'sin requisitos' if c['req'] == 'Ninguno' else 'requisito: ' + e(c['req'])}</p>
          <div class="faq-acciones"><button type="button" data-acordeon="tem-dir" data-accion="abrir">Expandir todo</button><button type="button" data-acordeon="tem-dir" data-accion="cerrar">Contraer todo</button></div>
        </div>
{acordeon('tem-dir', mods)}{(chr(10) + '        <p class="nota">' + e(c['nota_temario']) + '</p>') if c.get('nota_temario') else ''}
      </div>'''
    panel_cam = ''
    if tc:
        P = CAMPUS[camp]
        cab = {'ready': f'<b>5 módulos y test · 10 horas</b> · cuenta gratuita',
               'build': f'<b>Build: {len(tc)} módulos · +15 horas sobre Ready</b> · Claude Pro',
               'agents': f'<b>Agents: {len(tc)} módulos · +15 horas sobre Build</b> · Claude Pro'}[camp]
        nota = ('Las horas cuentan la dedicación total: unas 2 o 3 horas de trabajo por cada hora de vídeo. El campus está en castellano.' if camp == 'ready'
                else f'En el campus, {"los niveles 1 y 2 van juntos en Build" if camp == "build" else "el nivel 3 va en Agents"}, con los mismos módulos y más práctica. Las horas cuentan la dedicación total. El campus está en castellano.')
        panel_cam = f'''
      <div role="tabpanel" id="pt-cam" aria-labelledby="tt-cam" hidden>
        <div class="tem-cab">
          <p class="tem-total">{cab}</p>
          <div class="faq-acciones"><button type="button" data-acordeon="tem-cam" data-accion="abrir">Expandir todo</button><button type="button" data-acordeon="tem-cam" data-accion="cerrar">Contraer todo</button></div>
        </div>
{acordeon('tem-cam', tc)}
        <p class="nota">{nota}</p>
      </div>'''
    return f'''<section class="temario" id="temario">
  <div class="wrap tem-grid">
    <div class="tem-lado reveal">
      <div class="pre">Temario</div>
      <h2>Qué vas a ver <span class="acento">módulo a módulo</span></h2>
      <p class="intro">{intro}</p>
{tabs}
      <div class="tem-sale"><span class="logo-tile"><svg><use href="#i-shield"/></svg></span><div><b>Te llevas</b><p>{sale}</p></div></div>
    </div>

    <div>
{panel_dir}{panel_cam}
    </div>
  </div>
</section>'''

def certificado(c):
    if c['art4']:
        cd = f'ha completado el curso <b>{e(c["n"])} ({horas(c["h"])})</b>, con los contenidos de alfabetización en IA del <b>art. 4 del Reglamento Europeo de IA</b>.'
        intro = 'El artículo 4 del Reglamento Europeo de IA pide a las empresas que usan IA que formen a su equipo. Este certificado sirve como prueba de esa formación, con horas y contenidos.'
        b2 = '<li><span><b>Alineado con el artículo 4</b> del Reglamento Europeo de IA: el curso incluye el bloque de IA segura y legal.</span></li>'
        seal = '\n          <div class="seal"><div><span>AI ACT</span><b>ART. 4</b></div></div>'
    elif c.get('aldia'):
        cd = f'ha completado el curso <b>{e(c["n"])} ({horas(c["h"])})</b>, que renueva la formación anual en IA.'
        intro = 'Sirve como prueba de la formación anual de tu equipo en IA, con horas y contenidos.'
        b2 = '<li><span><b>Renueva la formación anual en IA</b>, alineada con el artículo 4 del Reglamento Europeo de IA.</span></li>'
        seal = '\n          <div class="seal"><div><span>AI ACT</span><b>ART. 4</b></div></div>'
    else:
        cd = f'ha completado el curso <b>{e(c["n"])} ({horas(c["h"])})</b>.'
        intro = 'Un certificado con tu nombre, el curso, las horas y los contenidos, que puedes enseñar a tu empresa o a tus clientes.'
        b2 = '<li><span>El <b>bloque de IA segura y legal</b> del artículo 4 va en los cursos de entrada; si ya lo has hecho con nosotros, no se repite.</span></li>'
        seal = ''
    return f'''<section class="aiact" id="certificado">
  <div class="wrap dos-col">
    <div class="cert-caja reveal">
      <div class="cert-wrap" role="img" aria-label="Ejemplo de certificado del curso {e(c['n'])}">
        <div class="paper back"></div>
        <div class="paper mid"></div>
        <div class="paper front"><div class="frame">
          <img class="cl" src="../assets/logo/westlabs-ai-school.png" alt="">
          <div class="ct">FORMACIÓN EN IA</div>
          <div class="ch">Certificado de formación</div>
          <div class="cs">Se certifica que</div>
          <div class="cn">Nombre del participante</div>
          <div class="cd">{cd}</div>
          <div class="cfoot">
            <div class="csig"><i>Verificable</i>Código QR</div>
            <div class="csig r"><i>Westlabs</i>Entidad formadora</div>
          </div>{seal}
        </div></div>
      </div>
    </div>
    <div class="reveal">
      <div class="pre">Certificado</div>
      <h2>Un certificado que <span class="acento">puedes demostrar</span></h2>
      <p class="intro">{intro}</p>
      <ul class="lista-check">
        <li><span><b>Nominativo y verificable:</b> lleva un QR que abre una página de Westlabs con tu nombre, el curso, las horas y la fecha.</span></li>
        {b2}
        <li><span>El modelo de certificado y el programa están <b>protocolizados ante notario</b>.</span></li>
        <li><span>Es el mismo programa que damos a equipos de empresa.</span></li>
      </ul>
      <a href="#inscripcion" class="btn btn-primario">Consigue tu certificado {ARROW}</a>
    </div>
  </div>
</section>'''

def escalera(c):
    camp = c.get('campus')
    if not camp: return ''
    cards = []
    for i, k in enumerate(['ready', 'build', 'agents']):
        P = CAMPUS[k]; actual = (k == camp)
        clase = 'esc actual' if actual else f'esc e{i + 1}' if i else 'esc e2'
        if not actual and i == 0: clase = 'esc e3'
        lis = ''.join(f'<li>{e(x)}</li>' for x in P['lista'])
        boton = f'\n        <a href="#inscripcion" class="btn btn-claro" data-abre="tab-part">Matricúlate {ARROW}</a>' if actual else ''
        aqui = '\n        <span class="aqui">Este curso</span>' if actual else ''
        cards.append(f'''      <article class="{clase} reveal">{aqui}
        <img class="medalla-e" src="../assets/3d/medalla-{P['medalla']}.png" alt="">
        <span class="et">{e(P['et'])}</span>
        <h3>{e(P['nombre'])}</h3>
        <div class="px">{e(P['precio'])}<small>con IVA</small></div>
        <p>{e(P['txt'])}</p>
        <ul>{lis}</ul>{boton}
      </article>''')
    nombre_c = {'ready': 'Alfabetización en IA es Ready', 'build': 'este curso va dentro de Build', 'agents': 'este curso va dentro de Agents'}[camp]
    return f'''<section class="escalera" id="precio">
  <div class="wrap">
    <div class="cab-sec reveal">
      <div class="pre">Para particulares</div>
      <h2>{'Empieza por aquí y' if camp == 'ready' else 'Tres cursos,'} <span class="acento">{'sube cuando quieras' if camp == 'ready' else 'paso a paso'}</span></h2>
      <p class="intro">En el campus, {nombre_c}. Cada curso incluye el anterior y, si ya tienes uno, pagas solo la diferencia.</p>
    </div>
    <div class="escalones">
{chr(10).join(cards)}
    </div>
    <p class="empresa-linea reveal">¿Lo paga tu empresa? Tenemos estos cursos en versión bonificable por FUNDAE. <a href="#inscripcion" data-abre="tab-emp">Pide propuesta</a></p>
  </div>
</section>'''

def fundae(c):
    return f'''<section class="fundae-sec" id="fundae">
  <div class="wrap">
    <div class="fbanda reveal">
      <img class="flogo" src="../assets/logos/fundae.png" alt="Fundación Estatal para la Formación en el Empleo">
      <div>
        <h3>Curso bonificable a través de FUNDAE</h3>
        <p>Somos entidad organizadora: si tu empresa tiene crédito de formación, nos encargamos de toda la gestión, sin intermediarios.</p>
      </div>
      <a href="#inscripcion" class="btn btn-primario"{' data-abre="tab-emp"' if (c['dir'] or c.get('campus')) else ''}>Consulta cómo bonificar {ARROW}</a>
    </div>
  </div>
</section>'''

def faqs(c):
    N = c['n']; q = []
    practica = ('Práctica', 'Proyecto', 'Cierre', 'Presentación', 'Test', 'Taller')
    temas = [m['t'] for m in c['temario'] if not m['t'].startswith(practica)]
    temas = [t[0].lower() + t[1:] if not t.startswith(('IA ', 'Claude', 'ChatGPT', 'Microsoft', 'Gemini', 'Copilot')) else t for t in temas]
    temas_txt = temas[0] if len(temas) == 1 else ', '.join(temas[:-1]) + ' y ' + temas[-1]
    sale = c['sale'][0].lower() + c['sale'][1:] if not c['sale'].startswith(('Claude', 'ChatGPT', 'Microsoft', 'Gemini', 'Copilot')) else c['sale']
    q.append(('¿Qué habré aprendido al acabar el curso?', f'Trabajas estos temas: {temas_txt}, siempre con práctica sobre tus casos. Al acabar te llevas {sale.rstrip(".")}.'))
    if c['req'] == 'Ninguno':
        req = 'No. El curso no tiene requisitos. Solo necesitas un ordenador con conexión a internet.'
    else:
        previo = c['req']
        if c['req'].startswith('Nivel') and c['herr'] in HERR:
            previo = f'{HERR[c["herr"]]["nombre"]} {["Esencial", "Avanzado", "Experto"][int(c["req"][-1]) - 1]}'
        req = f'No hace falta saber programar. Sí te pedimos haber hecho antes {previo} o tener una experiencia equivalente, porque partimos de lo que se ve ahí.'
    q.append(('¿Necesito conocimientos técnicos?', req))
    q.append(('¿Qué herramienta o licencia necesito?', c['cuenta']))
    if c['art4'] or c.get('aldia'):
        q.append(('¿Sirve para el artículo 4 del AI Act?', 'El artículo 4 del Reglamento Europeo de IA pide a las empresas que usan IA que tomen medidas para formar a su equipo. ' +
                  ('El certificado de este curso está alineado con ese artículo y sirve como prueba de la formación, con horas y contenidos.' if c['art4'] else 'Este curso renueva cada año esa formación y deja constancia con horas y contenidos.') + ' No es un título oficial ni homologado.'))
    q.append(('¿Cómo se verifica el certificado?', 'Cada certificado lleva un código QR que abre una página de Westlabs con el nombre, el curso, las horas y la fecha. El modelo de certificado y el programa están protocolizados ante notario.'))
    if c['dir'] or c.get('campus'):
        q.append(('¿Cómo me apunto?', '<ul><li><b>Particulares:</b> en el formulario de arriba, pestaña Particulares.' + (' Eliges el campus o el próximo grupo abierto en directo.' if c['dir'] and c.get('campus') else (' Te matriculas en el campus.' if c.get('campus') else ' Te avisamos cuando abramos el próximo grupo en directo.')) +
                  '</li><li><b>Empresas:</b> en la pestaña Empresas. Te preparamos una propuesta con fechas, modalidad y la gestión de FUNDAE.</li></ul>'))
    else:
        q.append(('¿Cómo lo contratamos?', 'Rellena el formulario de arriba. Hablamos con vosotros, preparamos los casos de vuestra empresa en una consultoría previa y os enviamos la propuesta con fechas, modalidad y la gestión de FUNDAE.'))
    ses = int(c['h'] / 2); jor = c['h'] / 4
    t = f'Son {int(c["h"])} horas: '
    t += f'{ses} sesiones de 2 h online' + (f' o {int(jor)} jornadas de 4 h presenciales' if jor == int(jor) and jor > 1 else '') + '.'
    if c.get('campus') == 'ready': t += ' En el campus son 10 horas a tu ritmo, con 12 meses para hacerlo.'
    elif c.get('campus'): t += f' En el campus va dentro de {c["campus"].capitalize()}, a tu ritmo y con 12 meses de acceso.'
    elif c['hc']: t += f' En el campus son {int(c["hc"])} horas a tu ritmo.'
    q.append(('¿Cuánto tiempo tengo que dedicarle?', t))
    if c['dir']:
        q.append(('¿Qué diferencia hay entre el grupo abierto y la formación para mi empresa?', 'En el grupo abierto te apuntas a unas fechas fijas con alumnos de otras empresas: va bien si eres una persona o sois pocas. La formación para tu empresa es un grupo solo vuestro, online o presencial, en las fechas que elijáis y con casos de vuestro trabajo preparados antes.'))
    sig = [POR_SLUG[s]['n'] for s in siguientes(c)[:2] if s in POR_SLUG]
    if sig:
        q.append(('¿Qué hago después?', f'Puedes seguir con {sig[0]}' + (f' o con {sig[1]}' if len(sig) > 1 else '') + '. Los tienes al final de esta página.'))
    q.append(('¿Puedo bonificar el curso por FUNDAE?', 'Sí, si lo paga tu empresa y tiene crédito de formación. Somos entidad organizadora y hacemos toda la gestión. Los autónomos sin trabajadores no pueden bonificar.'))
    q.append(('¿En qué idiomas se imparte?', 'En castellano, catalán o inglés.' + (' El campus, de momento, en castellano.' if c['hc'] else '')))
    det = ''.join(f'\n      <details><summary>{e(p)}</summary><div class="cuerpo">{r}</div></details>' for p, r in q)
    return f'''<section class="faq" id="faqs">
  <div class="wrap">
    <div class="faq-cab reveal">
      <div class="pre">Dudas</div>
      <h2>Preguntas <span class="acento">frecuentes</span></h2>
      <p class="intro">Lo que más nos preguntan sobre {e(N)}.</p>
      <div class="faq-acciones"><button type="button" data-acordeon="faq-lista" data-accion="abrir">Expandir todo</button><button type="button" data-acordeon="faq-lista" data-accion="cerrar">Contraer todo</button></div>
      <div class="faq-contacto"><b>¿No encuentras tu respuesta?</b><span>Escríbenos a <a href="mailto:gerard@westlabs.es">gerard@westlabs.es</a> o llámanos al <a href="tel:+34711790775">711 790 775</a>.</span></div>
    </div>
    <div class="acordeon reveal" id="faq-lista">{det}
    </div>
  </div>
</section>'''

def tarjeta(x):
    tags = [m for m, ok in [('En directo', x['dir']), ('In company', x['ic']), ('Campus', x['hc'])] if ok]
    med = f'<img class="medalla" src="../assets/3d/medalla-{x["nivel"]}.png" alt="">' if x.get('nivel') else ''
    return (f'<a href="{x["slug"]}.html" class="curso reveal" style="background:var(--{x["bg"]})"><div class="cab">{tiles(x)}<div class="tit"><span class="et">{e(x["ficha_et"])}{med}</span><h4>{e(x["n"])}</h4></div></div>'
            f'<p class="que">{e(x["d"])}</p><div class="tags"><span class="tag h">{horas(x["h"])}</span>' + ''.join(f'<span class="tag">{t}</span>' for t in tags) +
            '</div><span class="ver"><svg class="i"><use href="#i-arrow"/></svg></span></a>')

def siguiente(c):
    sig = [POR_SLUG[s] for s in siguientes(c) if s in POR_SLUG][:4]
    if not sig: return ''
    txt = c.get('sig_txt') or 'Cursos que encajan después de este, con la misma herramienta o en tu área.'
    return f'''<section class="oferta siguiente" aria-labelledby="sig-t">
  <div class="wrap">
    <div class="cab-sec reveal">
      <div class="pre">Siguiente paso</div>
      <h2 id="sig-t">Sigue <span class="acento">aprendiendo</span></h2>
      <p class="intro">{e(txt)}</p>
    </div>
    <div class="cursos n{len(sig)}">
      {chr(10).join('      ' + tarjeta(x) if i else tarjeta(x) for i, x in enumerate(sig))}
    </div>
  </div>
</section>'''

def cta(c):
    a, b = c['cta']
    dual = c['dir'] or c.get('campus')
    botones = (f'<a href="#inscripcion" class="btn btn-claro" data-abre="tab-emp">Solicita propuesta {ARROW}</a>\n        <a href="#inscripcion" class="btn btn-borde" data-abre="tab-part">{"Matricúlate" if c.get("campus") else "Apúntate"}</a>'
               if dual else f'<a href="#inscripcion" class="btn btn-claro">Solicita propuesta {ARROW}</a>\n        <a href="../index.html#oferta" class="btn btn-borde">Ver más cursos</a>')
    return f'''<section class="cta-final">
  <div class="wrap">
    <div class="caja oscuro reveal">
      <div>
        <h2>{e(a)} <span class="acento">{e(b)}</span></h2>
        <p class="intro">{e(c['sale'])}</p>
      </div>
      <div class="botones">
        {botones}
      </div>
    </div>
  </div>
</section>'''

def pagina(c):
    desc = f'Curso de {c["n"]} ({horas(c["h"])}): {c["d"][0].lower() + c["d"][1:]}. Online en directo, in company o en campus. Certificado verificable. Bonificable por FUNDAE.'
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Curso {e(c['n'])} ({horas(c['h'])}) · Westlabs</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="../assets/logo/icono-westlabs.png">
<link rel="stylesheet" href="../assets/css/base.css">
<link rel="stylesheet" href="../assets/css/curso.css">
</head>
<!-- Página generada con generador/generar.py a partir de generador/datos.py. No la edites a mano. -->
<body data-curso="{e(c['n'])}">
{ICONOS}<div class="progreso" aria-hidden="true"></div>
<a class="skip" href="#contenido">Ir al contenido</a>

{CABECERA}<main id="contenido">

<!-- ============ HERO + INSCRIPCIÓN ============ -->
{hero(c)}

<!-- ============ NAVEGACIÓN DEL CURSO ============ -->
{anclas(c)}

<!-- ============ INFORMACIÓN DEL CURSO ============ -->
{info(c)}

<!-- ============ POR QUÉ ============ -->
{porque(c)}

<!-- ============ MODALIDADES ============ -->
{modalidades(c)}

<!-- ============ TEMARIO ============ -->
{temario(c)}

<!-- ============ CERTIFICADO ============ -->
{certificado(c)}
{('<!-- ============ PRECIO PARTICULARES ============ -->' + chr(10) + escalera(c) + chr(10)) if c.get('campus') else ''}
<!-- ============ FUNDAE ============ -->
{fundae(c)}

<!-- ============ FAQ ============ -->
{faqs(c)}

<!-- ============ SIGUIENTE PASO ============ -->
{siguiente(c)}

<!-- ============ CTA FINAL ============ -->
{cta(c)}

</main>

{PIE}<script src="../assets/js/curso.js"></script>
</body>
</html>
'''

# ---------------------------------------------------------------- mapa
def mapa():
    L = ['# Mapa de la web', '', 'Generado con `python3 generador/generar.py`. Lista todas las páginas, qué hay en cada una y a dónde enlaza.', '',
         '## Páginas generales', '', '| Página | Archivo | Qué es |', '|---|---|---|',
         '| Portada | `index.html` | Catálogo con las pestañas Cursos y Especializados y el selector de herramienta. Cada tarjeta enlaza a su ficha en `cursos/`. |',
         '| Aviso legal | `aviso-legal.html` | Datos de Westlabs SCP y condiciones de uso |',
         '| Política de privacidad | `privacidad.html` | Datos de los formularios, finalidades y derechos |',
         '| Política de cookies | `cookies.html` | Sin cookies de análisis ni publicidad |',
         '| Contacto | `contacto.html` | **Pendiente de crear** |',
         '| Formación para empresas | `empresas.html` | **Pendiente de crear** |', '',
         '## Fichas de curso', '',
         f'{len(CURSOS)} fichas en `cursos/`. Todas tienen el formulario de empresas (Web3Forms). Las que tienen directo o campus tienen también el de particulares.', '']
    for tipo, tit in [('curso', 'Pestaña Cursos'), ('esp', 'Pestaña Especializados')]:
        L += [f'### {tit}', '', '| Curso | Archivo | Horas | Directo | In company | Campus | Particulares | Siguiente paso |', '|---|---|---|---|---|---|---|---|']
        for c in [x for x in CURSOS if x['t'] == tipo]:
            hc, pc = campus_info(c)
            part = ('Campus ' + CAMPUS[c['campus']]['precio'] + ' (Stripe pendiente)' if c.get('campus') else '') + (' + aviso directo' if c['dir'] else '')
            part = part.strip(' +') or '—'
            sig = ', '.join(f'[{POR_SLUG[s]["n"]}](cursos/{s}.html)' for s in siguientes(c) if s in POR_SLUG)
            L.append(f'| {c["n"]} | [`cursos/{c["slug"]}.html`](cursos/{c["slug"]}.html) | {horas(c["h"])} | {"✓" if c["dir"] else "—"} | {"✓" if c["ic"] else "—"} | {hc or "—"} | {part} | {sig} |')
        L.append('')
    L += ['## Conexiones', '',
          '| Qué | Dónde | Estado |', '|---|---|---|',
          '| Formularios → correo | Web3Forms, clave en cada formulario. Asunto: «Propuesta para empresa · [curso]» o «Matrícula de particular · [curso]» | Configurado. Falta probar un envío real en la web publicada |',
          '| Pago campus Ready, Build y Agents | Enlaces de pago de Stripe en `generador/datos.py` (`CAMPUS[...]["stripe"]`) | Pendiente |',
          '| Campus | https://campus.westlabs.es | Por confirmar |',
          '| Consultoría e implementación | https://westlabs.es | Por confirmar |',
          '| LinkedIn | https://www.linkedin.com/company/westlabss | Por confirmar |',
          '| Publicación | Netlify conectado a la rama `main` | Pendiente |', '',
          '## Cómo se cambia una ficha', '',
          '1. Edita `generador/datos.py` (textos, horas, temario, precios) o `generador/generar.py` (estructura de la ficha).',
          '2. Ejecuta `python3 generador/generar.py`.',
          '3. Se regeneran todas las fichas de `cursos/` y este mapa.',
          '4. El diseño está en `assets/css/base.css` y `assets/css/curso.css`; el comportamiento, en `assets/js/curso.js`.', '']
    return '\n'.join(L)

if __name__ == '__main__':
    os.makedirs(os.path.join(RAIZ, 'cursos'), exist_ok=True)
    for c in CURSOS:
        open(os.path.join(RAIZ, 'cursos', c['slug'] + '.html'), 'w', encoding='utf-8').write(pagina(c))
    open(os.path.join(RAIZ, 'MAPA-WEB.md'), 'w', encoding='utf-8').write(mapa())
    print(f'{len(CURSOS)} fichas generadas en cursos/ y MAPA-WEB.md actualizado')
