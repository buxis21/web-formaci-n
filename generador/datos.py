# -*- coding: utf-8 -*-
"""
DATOS DE LOS CURSOS
Sale del documento «Westlabs · Cursos de teleformación» (noviembre 2026).
Para cambiar un texto, unas horas o un precio: cámbialo aquí y ejecuta
    python3 generador/generar.py
y se vuelven a crear todas las fichas de cursos/ y el MAPA-WEB.md.
"""
import unicodedata, re

def slug(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')

# ---------------------------------------------------------------- herramientas
HERR = {
    'claude': dict(
        nombre='Claude', logo='claude.svg', foto='incompany-claude.jpg',
        foto_alt='Formación de Claude con el equipo de una empresa',
        reutil='skills', reutil_larga='skills: instrucciones que Claude reutiliza siempre que las necesita',
        apps='Claude en Excel, Word y Chrome', autom='tareas programadas y conectores',
        mini='artefactos y mini aplicaciones', agentes='Cowork',
        ecosistema='Claude en la web, en el escritorio y en el móvil',
        cuenta1='una cuenta de Claude (gratuita para empezar; Pro o Team para sacarle todo el partido)',
        cuenta2='Claude Pro, Team o Enterprise',
        que=['Prompting, configuración y memoria, proyectos y conectores',
             'Skills, Claude en Excel, Word y Chrome, y automatizaciones',
             'Contexto avanzado, artefactos y mini aplicaciones, agentes y un proyecto propio'],
        nombres_cat=['Claude para el trabajo', 'Claude: skills y automatizaciones', 'Agentes con Claude'],
        bg=['p3', 'p2', 'p5']),
    'chatgpt': dict(
        nombre='ChatGPT', logo='chatgpt.png', foto='incompany-chatgpt.jpg',
        foto_alt='Formación de ChatGPT con el equipo de una empresa',
        reutil='GPTs', reutil_larga='GPTs propios: asistentes con tus instrucciones y tus documentos',
        apps='ChatGPT con tus documentos, tu Excel y tu correo', autom='tareas programadas y conectores',
        mini='Canvas y mini aplicaciones', agentes='el modo agente de ChatGPT',
        ecosistema='ChatGPT en la web, en el escritorio y en el móvil',
        cuenta1='una cuenta de ChatGPT (gratuita para empezar; Plus, Team o Enterprise para sacarle todo el partido)',
        cuenta2='ChatGPT Plus, Team o Enterprise',
        que=['Prompting, configuración y memoria, proyectos y conectores',
             'GPTs propios, tareas programadas y la IA en tus documentos y correo',
             'Contexto avanzado, Canvas y mini aplicaciones, agentes y un proyecto propio'],
        nombres_cat=['ChatGPT para el trabajo', 'ChatGPT: GPTs y tareas programadas', 'Agentes con ChatGPT'],
        bg=['p2', 'p4', 'p5']),
    'microsoft': dict(
        nombre='Microsoft 365 Copilot', logo='copilot.png', foto='aula-practica.jpg',
        foto_alt='Alumnos practicando con ordenadores durante una formación',
        reutil='prompts guardados y agentes sencillos', reutil_larga='prompts guardados y agentes sencillos para no repetir instrucciones',
        apps='Copilot dentro de Word, Excel, PowerPoint y Outlook', autom='automatizaciones con Microsoft 365',
        mini='páginas y documentos generados con Copilot', agentes='agentes en Microsoft 365 Copilot',
        ecosistema='Copilot Chat, Teams y las apps de Microsoft 365',
        cuenta1='una cuenta de Microsoft 365 de empresa (el nivel 1 funciona con Copilot Chat, sin licencia de Copilot)',
        cuenta2='la licencia de Microsoft 365 Copilot',
        que=['Copilot Chat, prompting, Notebooks y conectores (funciona sin licencia)',
             'Copilot dentro de Word, Excel, PowerPoint y Outlook, y automatizaciones',
             'Contexto avanzado, agentes en Microsoft 365 Copilot y un proyecto propio'],
        nombres_cat=['Microsoft 365 Copilot para el trabajo', 'Microsoft 365 Copilot en Word, Excel, PowerPoint y Outlook', 'Agentes en Microsoft 365 Copilot'],
        bg=['p5', 'p3', 'p4']),
    'gemini': dict(
        nombre='Gemini', logo='gemini.png', foto='grupo-abierto.jpg',
        foto_alt='Alumnos practicando con sus portátiles durante una formación',
        reutil='Gems', reutil_larga='Gems: asistentes con tus instrucciones para tareas que repites',
        apps='Gemini en Gmail, Docs y Sheets', autom='automatizaciones con Google Workspace',
        mini='Canvas y mini aplicaciones', agentes='agentes con Gemini',
        ecosistema='Gemini en la web y dentro de Google Workspace',
        cuenta1='una cuenta de Google (gratuita para empezar; Google Workspace con Gemini para la empresa)',
        cuenta2='Google Workspace con Gemini',
        que=['Prompting, Gemini en Google Workspace, proyectos y conectores',
             'Gems, Gemini en Gmail, Docs y Sheets, y automatizaciones',
             'Contexto avanzado, mini aplicaciones, agentes y un proyecto propio'],
        nombres_cat=['Gemini en Google Workspace', 'Gemini: Gems y automatizaciones', 'Agentes con Gemini'],
        bg=['p4', 'p2', 'p3']),
}
ORDEN_HERR = ['claude', 'chatgpt', 'microsoft', 'gemini']
NIVEL = ['Esencial', 'Avanzado', 'Experto']

# Convocatorias en directo ya anunciadas en la portada (primer trimestre de 2027)
CONVOCATORIA = 'Primer trimestre de 2027'

# Campus para particulares (escalera Ready / Build / Agents). Enlace de Stripe: pendiente.
CAMPUS = {
    'ready':  dict(nombre='Alfabetización en IA', et='Ready · 10 h', precio='119 €', horas=10, stripe='',
                   txt='Para quien empieza con la IA o necesita acreditar su formación. En empresa, este programa sale a 229 € por persona en un grupo de 10.',
                   lista=['Cuenta gratuita', 'Certificado verificable', '12 meses de acceso'], medalla=1),
    'build':  dict(nombre='IA aplicada a tu trabajo', et='Build · 25 h', precio='349 €', horas=25, stripe='',
                   txt='Conectas Claude a tu correo y tus documentos, creas tus skills y dejas una tarea tuya automatizada.',
                   lista=['Incluye Ready', 'Necesitas Claude Pro', 'Proyecto corregido por una formadora'], medalla=2),
    'agents': dict(nombre='Herramientas y agentes propios', et='Agents · 40 h', precio='469 €', horas=40, stripe='',
                   txt='Creas mini aplicaciones a partir de un Excel y un agente que hace un proceso tuyo de principio a fin.',
                   lista=['Incluye Ready y Build', 'Necesitas Claude Pro', 'Dos proyectos corregidos'], medalla=3),
}

# ---------------------------------------------------------------- módulos
def M(t, sub, h, puntos, comun=False, llevas=None):
    return dict(t=t, sub=sub, h=h, puntos=puntos, comun=comun, llevas=llevas)

def mod_intro(prompting=True):
    return M('Introducción a la IA' + (' y prompting' if prompting else ''), 'Qué es y cómo pedirle las cosas', 2,
             ['Qué es la IA generativa y qué puede hacer por tu trabajo, y qué no',
              'Cómo funciona, sin tecnicismos: por qué a veces se equivoca o se inventa datos',
              'Prompting: cómo pedirle las cosas para que responda bien',
              'Trabajar con tus propios documentos'], comun=True)

def mod_legal(sub='AI Act (artículo 4) y RGPD'):
    return M('IA segura y legal', sub, 2,
             ['Qué pide el artículo 4 del Reglamento Europeo de IA a las empresas que usan IA',
              'RGPD: qué datos puedes compartir con una IA y cuáles no',
              'Cuentas personales y de empresa: dónde acaban tus datos',
              'Cómo revisar lo que te devuelve la IA antes de usarlo'], comun=True)

def temario_n1(k):
    H = HERR[k]
    return [mod_intro(),
            M(f'Conocemos {H["nombre"]}', 'Ecosistema, configuración y memoria', 2,
              [f'{H["ecosistema"][0].upper()}{H["ecosistema"][1:]}', 'Configurarla para tu trabajo: instrucciones personalizadas y memoria',
               'Qué versión y qué cuenta necesitas']),
            mod_legal(),
            M('Cómo la usamos', 'Proyectos y conectores', 2,
              ['Proyectos: tu contexto y tus documentos siempre a mano', 'Conectores con tu correo, tus archivos y tu calendario',
               'El caso de ejemplo: preparar una oferta a partir del correo de un cliente']),
            M('Práctica con tu caso', 'Dos sesiones con tus tareas', 4,
              ['Eliges tareas reales de tu trabajo', 'Las resolvemos con la herramienta, paso a paso',
               'Dejas un proyecto con tu caso funcionando'])]

def temario_n2(k):
    H = HERR[k]
    return [M('Instrucciones reutilizables', H['reutil'][0].upper() + H['reutil'][1:], 2,
              [f'{H["reutil_larga"][0].upper()}{H["reutil_larga"][1:]}', 'Cuándo merece la pena crear una', 'Crear la primera con tu caso']),
            M('La IA dentro de tus apps', H['apps'], 2,
              [f'{H["apps"]}', 'Trabajar sobre tus propios archivos sin copiar y pegar']),
            M('Automatizaciones y la IA en el navegador', 'Que las tareas se hagan solas', 2,
              [f'{H["autom"][0].upper()}{H["autom"][1:]}', 'La IA en el navegador: buscar, comparar y rellenar', 'Qué automatizar y qué no']),
            M('Práctica 1: tus tareas repetidas', 'Con tus instrucciones reutilizables', 4,
              ['Detectas las tareas que repites cada semana', 'Creas tus instrucciones reutilizables para ellas']),
            M('Práctica 2: una tarea automatizada', 'De principio a fin', 4,
              ['Eliges una tarea de tu trabajo', 'La dejas automatizada y la pruebas con casos reales']),
            M('Cierre y certificado', 'Repaso y próximos pasos', 2,
              ['Presentas lo que has montado', 'Plan para seguir usándolo en tu día a día'])]

def temario_n3(k):
    H = HERR[k]
    return [M('La IA por dentro', 'Modelos, contexto y fiabilidad', 2,
              ['Qué modelo usar para cada tarea', 'Cómo gestiona el contexto y dónde se equivoca', 'Cómo comprobar que un resultado es fiable']),
            M('Instrucciones y contexto avanzados', 'Para resultados que no dependen de la suerte', 2,
              ['Instrucciones largas y bien estructuradas', 'Documentos de referencia y ejemplos']),
            M('Artefactos y mini aplicaciones', H['mini'][0].upper() + H['mini'][1:], 2,
              ['Pequeñas herramientas a partir de un Excel o una plantilla', 'Compartirlas con quien las necesita']),
            M('Agentes: todas las piezas juntas', H['agentes'][0].upper() + H['agentes'][1:], 2,
              ['Qué es un agente y cuándo tiene sentido', 'Instrucciones, conectores y automatizaciones trabajando juntos']),
            M('Compartir con el equipo', 'Que no dependa de una sola persona', 2,
              ['Documentar lo que has montado', 'Permisos, revisiones y mantenimiento']),
            M('Proyecto propio con 4 seguimientos', 'Un proceso real de tu trabajo', 8,
              ['Eliges un proceso de tu trabajo', 'Cuatro sesiones de seguimiento de 2 h', 'Lo dejas funcionando en el día a día']),
            M('Presentación final y certificado', 'Enseñas tu agente', 2,
              ['Presentas tu agente al grupo', 'Mejoras y próximos pasos'])]

def temario_aldia(k):
    return [M('Novedades del año', 'Lo que ha cambiado en la herramienta', 2,
              ['Las funciones nuevas que sí te sirven', 'Lo que ha cambiado en la forma de trabajar']),
            M('Lo que no se ha asentado', 'Según el formulario previo', 2,
              ['Antes del curso nos cuentas qué usas y qué no', 'Repasamos lo que más cuesta al grupo']),
            M('Taller con tu caso', 'Ponerlo en práctica', 4,
              ['Aplicas las novedades a tus tareas', 'Sales con lo aprendido funcionando'])]

AREAS = {
    'comercial y marketing': dict(
        casos='reuniones, propuestas, seguimiento de leads, contenido y campañas',
        t1='Propuestas, correos a clientes y preparación de reuniones', t2='Contenido y campañas, o el seguimiento de leads',
        d='Reuniones, propuestas, leads, contenido y campañas', bg='p1'),
    'administración y finanzas': dict(
        casos='facturas, conciliaciones, informes y previsiones',
        t1='Facturas, conciliaciones y documentación', t2='Un informe o una previsión que se prepara sola',
        d='Facturas, conciliaciones, informes y previsiones', bg='p3'),
    'RRHH': dict(
        casos='selección sin sesgos, acogida, formación y comunicación interna',
        t1='Ofertas de empleo, cribado de candidaturas sin sesgos y comunicación interna', t2='El proceso de acogida de una persona nueva',
        d='Selección sin sesgos, acogida, formación y comunicación interna', bg='p4'),
}

def temario_area(k, area):
    H, A = HERR[k], AREAS[area]
    return [mod_intro(),
            M(f'Conocemos {H["nombre"]}', 'Lo que necesitas de la herramienta', 2,
              [f'{H["ecosistema"][0].upper()}{H["ecosistema"][1:]}', 'Configurarla para tu puesto']),
            mod_legal(),
            M('Cómo la usamos, con casos del área', f'Casos de {area}', 2,
              [f'Casos reales de {area}: {A["casos"]}', 'Proyectos y conectores para tu puesto']),
            M('Taller del área 1: las tareas del puesto', A['t1'], 4,
              ['Resolvemos las tareas de tu puesto con la herramienta', 'Con tus documentos y tus casos']),
            M('Taller del área 2: un proceso automatizado', A['t2'], 4,
              ['Eliges un proceso del área', 'Lo dejas automatizado y probado'])]

# ---------------------------------------------------------------- campus (temarios para particulares)
CAMPUS_TEMARIO = {
    'ready': [
        M('Qué es la IA generativa', 'Lo que hace bien y lo que no', 1, ['Qué es la IA generativa y cómo responde', 'Por qué a veces se equivoca y cómo detectarlo'], comun=True),
        M('Prompting con tus documentos', 'Cómo pedirle las cosas', 2.5, ['Cómo escribir una buena instrucción', 'Trabajar con tus propios documentos'], llevas='tu plantilla de prompts.'),
        M('Claude, ChatGPT y Gemini', 'Elegir y configurar', 2, ['Qué hace bien cada una', 'Configurarla para tu trabajo'], llevas='tu herramienta configurada.'),
        M('IA segura y legal', 'AI Act y RGPD', 2, ['El artículo 4 del Reglamento Europeo de IA', 'Qué datos puedes compartir y cuáles no'], comun=True, llevas='una política de uso personal y un checklist de protección de datos.'),
        M('Casos de uso y miniproyecto', 'Con tus documentos', 2, ['Casos de uso para tu trabajo', 'Miniproyecto que autoevalúas tú']),
        M('Test final', 'Para obtener el certificado', 0.5, ['Un test corto sobre los cinco módulos', 'Al aprobarlo descargas tu certificado'])],
    'build': [
        M('Proyectos, contexto y memoria', 'Tu trabajo siempre a mano', 2, ['Proyectos con tus documentos', 'Memoria e instrucciones personalizadas']),
        M('Conectores', 'Correo, Drive y calendario', 2.5, ['Conectar Claude a tu correo, tus archivos y tu calendario', 'Qué datos ve y cómo controlarlo']),
        M('Skills', 'Instrucciones que se reutilizan', 2.5, ['Crear tus propias skills', 'Cuándo merece la pena'], llevas='dos skills propias.'),
        M('Claude en Excel, Word y Chrome', 'La IA dentro de tus apps', 3, ['Claude dentro de tus archivos', 'Claude en el navegador'], llevas='una tarea hecha en tu Excel.'),
        M('Automatizaciones', 'Tareas que se hacen solas', 2.5, ['Tareas programadas', 'Qué automatizar y qué no'], llevas='tu automatización.'),
        M('Proyecto práctico y test', 'Corregido por una formadora', 2.5, ['Un proyecto de tu trabajo', 'Test final'])],
    'agents': [
        M('La IA por dentro', 'Modelos, contexto y fiabilidad', 2, ['Qué modelo usar para cada tarea', 'Cómo comprobar que un resultado es fiable']),
        M('Instrucciones y contexto avanzados', 'Resultados que no dependen de la suerte', 2, ['Instrucciones largas y bien estructuradas', 'Documentos de referencia y ejemplos']),
        M('Artefactos y mini aplicaciones', 'A partir de un Excel', 3, ['Pequeñas herramientas para tu trabajo', 'Compartirlas'], llevas='una mini app para tu trabajo.'),
        M('Agentes con Cowork', 'Un proceso de principio a fin', 4, ['Qué es un agente y cuándo tiene sentido', 'Montar tu agente paso a paso']),
        M('Proyecto final', 'Corregido por una formadora', 4, ['Tu agente en uso en un proceso real', 'Corrección y mejoras'], llevas='tu agente en uso, corregido.')],
}

# ---------------------------------------------------------------- cursos
CURSOS = []

def add(**c):
    c.setdefault('slug', slug(c['n']))
    c.setdefault('dir', True); c.setdefault('ic', True); c.setdefault('hc', 0)
    c.setdefault('art4', False); c.setdefault('req', 'Ninguno'); c.setdefault('req_det', 'Ni conocimientos técnicos')
    c.setdefault('campus', None); c.setdefault('campus_txt', '')
    c.setdefault('tools', [HERR[c['herr']]['logo']] if c.get('herr') in HERR else [])
    CURSOS.append(c)

# 1 · Alfabetización en IA
add(n='Alfabetización en IA', t='curso', herr='todas', et='Curso · Para empezar', ficha_et='Para empezar',
    sub='Usa la IA con criterio, con seguridad y dentro de la ley',
    lead='El curso para empezar con la inteligencia artificial o para acreditar tu formación.',
    intro='Entiendes qué es la IA generativa y cómo pedirle las cosas, sabes qué datos puedes compartir y cuáles no, y pruebas Claude, ChatGPT, Copilot y Gemini para elegir la que te encaja.',
    tools=['claude.svg', 'chatgpt.png', 'copilot.png', 'gemini.png'], tools_txt='Claude, ChatGPT, Copilot y Gemini',
    h=8, hc=10, art4=True, campus='ready', ico='i-shield', bg='p1',
    d='Qué es la IA, AI Act y RGPD, y las cuatro herramientas para elegir con criterio',
    h2_porque=('La base para usar la IA', 'en tu trabajo'),
    porque='Un curso práctico para pasar de probar la IA de vez en cuando a usarla bien: con tus documentos, con buenas instrucciones y sabiendo qué datos puedes compartir.',
    lista=['<b>Qué es la IA generativa</b> y cómo pedirle las cosas para que responda bien.',
           '<b>IA segura y legal:</b> el artículo 4 del Reglamento Europeo de IA y el RGPD aplicados a tu día a día.',
           '<b>Claude, ChatGPT, Copilot y Gemini:</b> qué hace bien cada una, para elegir con criterio.',
           '<b>Práctica con tus documentos</b> y un test final para obtener el certificado.'],
    sale='El certificado de alfabetización en IA, alineado con el artículo 4 del Reglamento Europeo de IA, y criterio para elegir la herramienta que te encaja.',
    sale_campus='En el campus, además: tu plantilla de prompts, tu herramienta configurada, una política de uso personal y un checklist de protección de datos.',
    pq=[('i-compass', 'Si empiezas con la IA', 'No la has usado o la usas sin saber si lo haces bien.'),
        ('i-shield', 'Si tienes que acreditarlo', 'Tu empresa o un cliente te pide una prueba de tu formación en IA.'),
        ('i-building', 'Si formas a tu equipo', 'Quieres que todo el equipo parta de la misma base antes de ir a una herramienta.')],
    chip_foto=[('i-shield', 'AI Act · artículo 4', 'Incluido en el certificado'), ('i-doc', 'Con tus documentos', 'Ejercicios con tu caso')],
    foto='aula-practica.jpg', foto_alt='Alumnos practicando con ordenadores durante una formación de IA',
    cuenta='No. En el campus trabajas con las cuentas gratuitas de Claude, ChatGPT y Gemini. En directo o in company usamos las cuentas que tengas; si tu empresa ya paga alguna herramienta, trabajamos con esa.',
    temario=[mod_intro(prompting=False) | dict(sub='Qué es y cómo pedirle las cosas'),
             mod_legal(),
             M('Las herramientas', 'Claude, ChatGPT, Copilot y Gemini', 2,
               ['Qué hace bien cada una y para qué tipo de tarea', 'La misma tarea en las cuatro, una al lado de la otra',
                'Configurarla para tu trabajo: instrucciones y memoria', 'Cómo elegir según lo que ya usa tu empresa']),
             M('Práctica y test final', 'Con tus documentos', 2, ['Casos de uso de tu puesto, resueltos en clase', 'Test final para obtener el certificado'])],
    cta=('Empieza con la IA', 'con buen pie'), dest=True, sig_txt='Al acabar, pasa al nivel 1 de la herramienta que usas. Te saltas el bloque común que ya has hecho aquí.')

for k in ORDEN_HERR:
    H = HERR[k]; N = H['nombre']; es_c = (k == 'claude')
    sig_nivel = lambda i: f'{N} {NIVEL[i]}'
    # Nivel 1
    add(n=f'{N} {NIVEL[0]}', t='curso', herr=k, nivel=1, et=f'Curso · Nivel 1 de 3', ficha_et='Nivel 1 de 3',
        sub=H['nombres_cat'][0], h=12, hc=('Build' if es_c else 0), campus=('build' if es_c else None),
        lead=f'Empieza a usar {N} en tu trabajo, bien configurado y con tus casos.',
        intro=f'Aprendes a pedirle las cosas, lo configuras con tu forma de trabajar, organizas tus proyectos y lo conectas a tu correo y tus documentos. Acabas con un proyecto tuyo funcionando.',
        d=H['que'][0], art4=True, bg=H['bg'][0], ico='i-chat',
        h2_porque=(f'{N} configurado', 'para tu trabajo'),
        porque=f'Un curso práctico para pasar de hacerle preguntas sueltas a {N} a tenerlo configurado y trabajando con tus documentos.',
        lista=['<b>Prompting:</b> cómo pedirle las cosas para que responda bien a la primera.',
               f'<b>Configuración y memoria:</b> {N} adaptado a tu forma de trabajar.',
               '<b>Proyectos y conectores:</b> tu contexto, tus archivos, tu correo y tu calendario.',
               '<b>IA segura y legal:</b> el artículo 4 del Reglamento Europeo de IA y el RGPD.'],
        sale='La herramienta configurada y un proyecto con tu caso funcionando.',
        pq=[('i-compass', f'Si ya usas {N} de vez en cuando', 'Y quieres sacarle partido de verdad.'),
            ('i-building', f'Si tu empresa trabaja con {N}', 'Y el equipo tiene que usarlo bien y con seguridad.'),
            ('i-shield', 'Si necesitas acreditarlo', 'Incluye el bloque de IA segura y legal del artículo 4.')],
        chip_foto=[('i-doc', 'Con tus documentos', 'Proyectos y conectores'), ('i-shield', 'AI Act · artículo 4', 'Incluido en el certificado')],
        cuenta=f'Necesitas {H["cuenta1"]}.',
        temario=temario_n1(k), dest=(k != 'gemini'),
        cta=(f'Empieza a trabajar con {N}', 'desde el primer día'))
    # Nivel 2
    add(n=f'{N} {NIVEL[1]}', t='curso', herr=k, nivel=2, et='Curso · Nivel 2 de 3', ficha_et='Nivel 2 de 3',
        sub=H['nombres_cat'][1], h=16, hc=('Build' if es_c else 0), campus=('build' if es_c else None),
        req='Nivel 1', req_det=f'{N} {NIVEL[0]} o experiencia equivalente',
        lead=f'Que {N} te haga tareas enteras.',
        intro=f'Creas tus {H["reutil"]}, trabajas con la IA dentro de tus apps y dejas tareas que se hacen solas. Acabas con tus instrucciones reutilizables y una tarea automatizada.',
        d=H['que'][1], bg=H['bg'][1], ico='i-chat',
        h2_porque=('De pedirle cosas', 'a que trabaje por ti'),
        porque=f'El paso siguiente después del nivel 1: dejar de repetir instrucciones y que {N} haga tareas completas dentro de las herramientas que ya usas.',
        lista=[f'<b>Instrucciones reutilizables:</b> {H["reutil_larga"]}.',
               f'<b>La IA dentro de tus apps:</b> {H["apps"]}.',
               f'<b>Automatizaciones:</b> {H["autom"]}, y la IA en el navegador.',
               '<b>Dos prácticas con tus tareas:</b> las que repites cada semana y una que se hace sola.'],
        sale='Tus instrucciones reutilizables y una tarea que se hace sola.',
        pq=[('i-refresh', 'Si repites las mismas tareas', 'Correos, informes o documentos que haces cada semana.'),
            ('i-bolt', 'Si quieres automatizar', 'Sin programar y con las herramientas que ya tienes.'),
            ('i-building', 'Si tu equipo ya ha hecho el nivel 1', 'Y quiere dar el siguiente paso juntos.')],
        chip_foto=[('i-bolt', 'Tareas que se hacen solas', 'Automatizaciones'), ('i-doc', H['reutil'][0].upper() + H['reutil'][1:], 'Instrucciones reutilizables')],
        cuenta=f'Necesitas {H["cuenta2"]}.' + (' Desde el 15 de abril de 2026, sin licencia de Microsoft 365 Copilot no hay Copilot dentro de Word, Excel, PowerPoint ni OneNote.' if k == 'microsoft' else ''),
        temario=temario_n2(k), cta=(f'Que {N} haga', 'tareas enteras'))
    # Nivel 3
    add(n=f'{N} {NIVEL[2]}', t='curso', herr=k, nivel=3, et='Curso · Nivel 3 de 3', ficha_et='Nivel 3 de 3',
        sub=H['nombres_cat'][2], h=20, hc=('Agents' if es_c else 0), campus=('agents' if es_c else None),
        req='Nivel 2', req_det=f'{N} {NIVEL[1]} o experiencia equivalente',
        lead='Monta tus propias herramientas y un agente que hace un proceso de principio a fin.',
        intro=f'Entiendes la IA por dentro, trabajas con contexto avanzado, creas mini aplicaciones y juntas todas las piezas en un agente. Acabas con un agente propio funcionando en un proceso real, con cuatro sesiones de seguimiento.',
        d=H['que'][2], bg=H['bg'][2], ico='i-robot',
        h2_porque=('Tu propio agente', 'en un proceso real'),
        porque='El último nivel: lo que en Westlabs montamos como proyecto para empresas, aquí aprendes a montarlo tú, con seguimiento hasta que funciona.',
        lista=['<b>La IA por dentro:</b> modelos, contexto y fiabilidad.',
               f'<b>{H["mini"][0].upper() + H["mini"][1:]}:</b> pequeñas herramientas para tu trabajo.',
               f'<b>Agentes:</b> instrucciones, conectores y automatizaciones juntos, con {H["agentes"]}.',
               '<b>Proyecto propio con 4 seguimientos</b> y presentación final.'],
        sale='Un agente propio funcionando en un proceso real.',
        pq=[('i-robot', 'Si quieres montar un agente', 'Que haga un proceso de tu trabajo de principio a fin.'),
            ('i-tools', 'Si quieres tus propias herramientas', 'Mini aplicaciones hechas a tu medida.'),
            ('i-users', 'Si vas a compartirlo con el equipo', 'Y tiene que funcionar sin depender de ti.')],
        chip_foto=[('i-robot', 'Agente propio', 'En un proceso real'), ('i-target', '4 seguimientos', 'Hasta que funciona')],
        cuenta=f'Necesitas {H["cuenta2"]}.',
        temario=temario_n3(k), cta=('Monta tu propio agente', f'con {N}'))
    # Al día
    add(n=f'{N} al día', t='curso', herr=k, et='Curso · Cada año', ficha_et='Cada año', sub='Reciclaje anual',
        h=8, hc=10, lead=f'Ponte al día con {N} una vez al año.',
        intro='Repasamos las novedades del año, reforzamos lo que no se ha asentado según lo que nos cuentas antes del curso y lo aplicamos en un taller con tu caso.',
        d='Novedades del año, lo que no se ha asentado y un taller con tu caso', bg='p6', ico='i-refresh',
        h2_porque=('Lo nuevo de cada año', 'aplicado a tu trabajo'),
        porque=f'{N} cambia cada pocos meses. Este curso corto te pone al día y renueva la formación anual en IA de tu equipo.',
        lista=['<b>Novedades del año</b> que sí te sirven en el trabajo.',
               '<b>Lo que no se ha asentado:</b> lo vemos según un formulario que rellenas antes.',
               '<b>Taller con tu caso:</b> aplicas lo nuevo a tus tareas.',
               '<b>Certificado</b> que renueva la formación anual en IA.'],
        sale='Lo aprendido al día y la formación anual del artículo 4 renovada.',
        pq=[('i-refresh', 'Si ya hiciste un curso con nosotros', 'Y quieres ponerte al día.'),
            ('i-building', 'Si tu equipo ya usa la herramienta', 'Y quiere reforzar lo que más cuesta.'),
            ('i-shield', 'Si renováis la formación cada año', 'Con horas y contenidos documentados.')],
        chip_foto=[('i-refresh', 'Novedades del año', 'Lo que sí te sirve'), ('i-target', 'Taller con tu caso', '4 horas de práctica')],
        cuenta=f'Trabajamos con la cuenta que uses: {H["cuenta2"]} o la versión que tenga tu empresa.',
        temario=temario_aldia(k), aldia=True, cta=(f'Ponte al día', f'con {N}'))

for k in ORDEN_HERR:
    H = HERR[k]; N = H['nombre']
    for area, A in AREAS.items():
        add(n=f'{N} para {area}', t='esp', herr=k, et='Especializado · Por área', ficha_et='Por área',
            sub=f'{N} con los casos de {area}', h=16, hc=25, art4=True,
            lead=f'{N} aplicado a las tareas de {area}.',
            intro=f'Aprendes la herramienta con casos de tu área: {A["casos"]}. Dos talleres con las tareas de tu puesto y un proceso del área automatizado.',
            d=A['d'], bg=A['bg'], ico='i-users',
            h2_porque=(f'IA para {area}', 'con tus casos'),
            porque=f'El mismo método que los niveles generales, pero con los casos de {area} desde el primer módulo.',
            lista=['<b>Prompting y la herramienta</b> desde cero, sin requisitos.',
                   f'<b>Casos de {area}:</b> {A["casos"]}.',
                   '<b>IA segura y legal:</b> el artículo 4 del Reglamento Europeo de IA y el RGPD.',
                   '<b>Dos talleres:</b> las tareas del puesto y un proceso del área automatizado.'],
            sale='Los casos de tu puesto resueltos con la herramienta.',
            pq=[('i-users', f'Si trabajas en {area}', 'Y quieres casos de tu día a día, no ejemplos genéricos.'),
                ('i-building', 'Si formas a un departamento', 'Con un temario hecho para su trabajo.'),
                ('i-compass', 'Si empiezas desde cero', 'No hace falta haber hecho otros cursos.')],
            chip_foto=[('i-users', 'Casos del área', area[0].upper() + area[1:]), ('i-shield', 'AI Act · artículo 4', 'Incluido en el certificado')],
            cuenta=f'Necesitas {H["cuenta1"]}.', temario=temario_area(k, area),
            area=area, cta=(f'{N} para', area))

for k in ['claude', 'chatgpt', 'microsoft']:
    H = HERR[k]; N = H['nombre']
    add(n=f'Administración de {N} para empresas', t='esp', herr=k, et='Especializado · Para IT', ficha_et='Para IT',
        sub='Cuenta de empresa configurada y bajo control', h=8, dir=False,
        lead=f'Configura y controla la cuenta de empresa de {N}.',
        intro='Para quien administra la herramienta: usuarios y permisos, seguridad y privacidad, lo que se comparte en la organización y el seguimiento del uso y los costes.',
        d='Usuarios y permisos, seguridad, lo que se comparte, uso y costes', bg='p2', ico='i-gear',
        h2_porque=('La cuenta de empresa', 'bajo control'),
        porque=f'Cuando {N} se usa en toda la empresa, alguien tiene que decidir quién accede a qué, qué datos se conectan y cuánto cuesta.',
        lista=['<b>Cuentas, usuarios y permisos.</b>', '<b>Seguridad y privacidad:</b> datos y conectores permitidos.',
               '<b>Lo que se comparte</b> en la organización.', '<b>Uso, costes y seguimiento.</b>'],
        sale='La cuenta de empresa configurada y bajo control.',
        pq=[('i-gear', 'Si administras la herramienta', 'IT, sistemas o quien lleve las cuentas.'),
            ('i-shield', 'Si te preocupa la seguridad', 'Qué datos salen y qué conectores se permiten.'),
            ('i-euro', 'Si controlas los costes', 'Licencias, uso y seguimiento.')],
        chip_foto=[('i-shield', 'Seguridad y privacidad', 'Datos y conectores'), ('i-gear', 'Usuarios y permisos', 'Cuenta de empresa')],
        cuenta=f'Necesitas acceso de administración a la cuenta de empresa de {N}.',
        temario=[M('Cuentas, usuarios y permisos', 'Quién accede a qué', 2, ['Altas, bajas y grupos', 'Roles y permisos']),
                 M('Seguridad y privacidad', 'Datos y conectores permitidos', 2, ['Qué conectores activar y cuáles no', 'Políticas de datos de la cuenta de empresa']),
                 M('Lo que se comparte en la organización', 'Proyectos, instrucciones y agentes', 2, ['Qué se comparte y con quién', 'Orden y mantenimiento']),
                 M('Uso, costes y seguimiento', 'Saber qué pasa en la cuenta', 2, ['Paneles de uso', 'Licencias y costes'])],
        cta=(f'{N} en tu empresa,', 'bajo control'))

add(n='Claude Code para no programadores', t='esp', herr='claude', et='Especializado · Avanzado', ficha_et='Avanzado',
    sub='Tus propias herramientas sin programar', h=16, dir=False, req='Nivel 2', req_det='Claude Avanzado o experiencia equivalente',
    lead='Usa Claude Code para crear tus propias herramientas, sin saber programar.',
    intro='Trabajas con carpetas, archivos y datos desde Claude Code, con instrucciones y contexto avanzados, y creas pequeñas herramientas para tu trabajo. Acabas con una herramienta propia, con cuatro sesiones de seguimiento.',
    d='Carpetas, archivos y datos, y tus propias herramientas sin programar', bg='p5', ico='i-studio',
    h2_porque=('Claude Code', 'sin ser programador'),
    porque='Claude Code no es solo para programadores: sirve para ordenar archivos, tratar datos y crear pequeñas herramientas describiéndolas.',
    lista=['<b>La IA por dentro:</b> modelos, contexto y fiabilidad.', '<b>Claude Code:</b> carpetas, archivos y datos.',
           '<b>Instrucciones y contexto avanzados.</b>', '<b>Pequeñas herramientas sin programar</b> y un proyecto propio con 4 seguimientos.'],
    sale='Una herramienta propia hecha con Claude Code.',
    pq=[('i-studio', 'Si ya dominas Claude', 'Y quieres ir un paso más allá.'), ('i-db', 'Si trabajas con muchos archivos o datos', 'Y quieres ordenarlos y tratarlos.'),
        ('i-tools', 'Si necesitas una herramienta a medida', 'Sin depender de un programador.')],
    chip_foto=[('i-studio', 'Sin programar', 'Describes lo que quieres'), ('i-target', '4 seguimientos', 'Hasta que funciona')],
    cuenta='Necesitas Claude Pro, Max, Team o Enterprise, que incluyen Claude Code.',
    temario=[M('La IA por dentro', 'Modelos, contexto y fiabilidad', 2, ['Qué modelo usar', 'Cómo comprobar que un resultado es fiable']),
             M('Claude Code: carpetas, archivos y datos', 'Tu ordenador como espacio de trabajo', 2, ['Qué es Claude Code y cómo se instala', 'Trabajar con carpetas, archivos y datos']),
             M('Instrucciones y contexto avanzados', 'Resultados fiables', 2, ['Instrucciones bien estructuradas', 'Documentos de referencia']),
             M('Pequeñas herramientas sin programar', 'Describes lo que necesitas', 2, ['De la idea a una herramienta que funciona', 'Probarla y mejorarla']),
             M('Proyecto propio con 4 seguimientos', 'Tu herramienta, funcionando', 8, ['Eliges una herramienta para tu trabajo', 'Cuatro seguimientos de 2 h'])],
    cta=('Crea tus herramientas', 'con Claude Code'), dest=True)

add(n='Copilot Studio I · Crea tu primer agente', t='esp', herr='microsoft', tools=['copilot-studio.png'], tools_txt='Copilot Studio',
    et='Especializado · Agentes', ficha_et='Agentes', sub='Un agente de preguntas internas, publicado en Teams', h=12, art4=True,
    lead='Crea tu primer agente con Copilot Studio y publícalo en Teams.',
    intro='Creas un agente describiéndolo, le das conocimiento con SharePoint, archivos y webs, lo pruebas y lo publicas en Teams y Microsoft 365 Copilot. Si tu empresa ya tiene la licencia de Microsoft 365 Copilot, los agentes de uso interno no tienen coste extra.',
    d='Un agente con SharePoint y archivos, publicado en Teams', bg='p5', ico='i-robot',
    h2_porque=('Tu primer agente', 'en Copilot Studio'),
    porque='Copilot Studio es la herramienta de Microsoft para crear agentes sin programar. Encaja en empresas que ya pagan Microsoft 365 Copilot.',
    lista=['<b>Qué es un agente</b> y cuándo tiene sentido.', '<b>Crearlo describiéndolo</b> y darle instrucciones.',
           '<b>Darle conocimiento:</b> SharePoint, archivos y webs.', '<b>IA segura en agentes:</b> permisos, datos y quién lo usa.'],
    sale='Un agente de preguntas internas publicado en Teams.',
    pq=[('i-robot', 'Si quieres un agente para el equipo', 'Que responda las preguntas internas de siempre.'),
        ('i-building', 'Si tu empresa usa Microsoft 365', 'Y ya paga Microsoft 365 Copilot.'), ('i-compass', 'Si no programas', 'Copilot Studio es low-code.')],
    chip_foto=[('i-robot', 'Publicado en Teams', 'Tu agente en marcha'), ('i-shield', 'IA segura', 'Permisos y datos')],
    cuenta='Necesitas Microsoft 365 con acceso a Copilot Studio. Con la licencia de Microsoft 365 Copilot, los agentes de uso interno no tienen coste extra.',
    temario=[M('Qué es un agente y cuándo tiene sentido', 'Antes de crear nada', 2, ['Agentes, asistentes y automatizaciones', 'Casos que funcionan bien'], comun=True),
             M('Crear el agente describiéndolo', 'Y darle instrucciones', 2, ['Crear un agente desde una descripción', 'Instrucciones y tono']),
             M('Darle conocimiento', 'SharePoint, archivos y webs', 2, ['Fuentes de conocimiento', 'Cómo comprobar que responde bien']),
             M('IA segura en agentes', 'Permisos, datos y quién lo usa', 2, ['Quién puede usarlo y qué datos ve', 'El artículo 4 del Reglamento Europeo de IA aplicado a agentes'], comun=True),
             M('Probarlo y publicarlo', 'En Teams y Microsoft 365 Copilot', 2, ['Pruebas con preguntas reales', 'Publicación y seguimiento']),
             M('Proyecto: un agente de preguntas internas', 'Con tu caso', 2, ['Montas tu agente', 'Lo dejas publicado'])],
    nota_temario='Las funciones concretas de Copilot Studio se revisan al montar cada curso, porque Microsoft las cambia a menudo.',
    cta=('Crea tu primer agente', 'con Copilot Studio'), dest=True)

add(n='Copilot Studio II · Agentes conectados a tu empresa', t='esp', herr='microsoft', tools=['copilot-studio.png'], tools_txt='Copilot Studio',
    et='Especializado · Agentes', ficha_et='Agentes', sub='Agentes que trabajan con los datos de tus sistemas', h=16,
    req='Copilot Studio I', req_det='O experiencia equivalente',
    lead='Agentes de Copilot Studio conectados a los sistemas de tu empresa.',
    intro='Añades acciones y conectores, creas flujos de agente y haces que trabajen con los datos de tus sistemas. Repasamos el gobierno y los costes, y acabas con un agente conectado, con cuatro sesiones de seguimiento.',
    d='Acciones, conectores, flujos y los datos de tus sistemas', bg='p6', ico='i-robot',
    h2_porque=('Agentes que hacen cosas', 'en tus sistemas'),
    porque='El paso siguiente a Copilot Studio I: que el agente no solo responda, sino que actúe con los datos de tu empresa.',
    lista=['<b>Acciones y conectores.</b>', '<b>Flujos de agente.</b>', '<b>Agentes con los datos de tus sistemas.</b>',
           '<b>Gobierno y costes:</b> licencias, consumo y quién crea agentes.'],
    sale='Un agente conectado a tus sistemas. Por ejemplo, uno de acogida para RRHH.',
    pq=[('i-flow', 'Si ya has creado agentes', 'Y quieres que hagan más que responder.'), ('i-db', 'Si tienes datos en otros sistemas', 'Y quieres que el agente trabaje con ellos.'),
        ('i-gear', 'Si gobiernas los agentes de la empresa', 'Licencias, consumo y permisos.')],
    chip_foto=[('i-flow', 'Conectado a tus sistemas', 'Acciones y flujos'), ('i-target', '4 seguimientos', 'Hasta que funciona')],
    cuenta='Necesitas Microsoft 365 con acceso a Copilot Studio y permisos para conectar los sistemas de la empresa.',
    temario=[M('Acciones y conectores', 'Que el agente haga cosas', 2, ['Acciones del agente', 'Conectores con otros sistemas']),
             M('Flujos de agente', 'Procesos de varios pasos', 2, ['Diseñar un flujo', 'Probarlo']),
             M('Agentes con los datos de tus sistemas', 'Información de la empresa', 2, ['Fuentes de datos', 'Permisos y seguridad']),
             M('Gobierno y costes', 'Licencias, consumo y quién crea agentes', 2, ['Licencias y consumo', 'Normas para crear agentes en la empresa']),
             M('Proyecto propio con 4 seguimientos', 'Tu agente conectado', 8, ['Eliges un proceso', 'Cuatro seguimientos de 2 h'])],
    nota_temario='Las funciones concretas de Copilot Studio se revisan al montar cada curso, porque Microsoft las cambia a menudo.',
    cta=('Agentes conectados', 'a tu empresa'))

add(n='IA para dirección', t='esp', herr='todas', tools=['claude.svg', 'chatgpt.png', 'copilot.png', 'gemini.png'], tools_txt='Sin herramienta concreta',
    et='Especializado · Dirección', ficha_et='Dirección', sub='Plan de IA y política de uso para tu empresa', h=8, dir=False, art4=True,
    lead='Decide por dónde empezar con la IA en tu empresa y con qué reglas.',
    intro='Para dirección y gerencia: qué es la IA, qué le toca a dirección en el AI Act, por dónde empezar con casos, coste y retorno, y el plan y la política interna de uso.',
    d='Por dónde empezar, coste y retorno, y la política de uso interna', bg='p2', ico='i-boss',
    h2_porque=('La IA vista', 'desde dirección'),
    porque='Antes de formar a todo el equipo, dirección tiene que decidir para qué, con qué herramientas y con qué reglas.',
    lista=['<b>Introducción a la IA</b> para tomar decisiones con criterio.', '<b>IA segura y legal:</b> qué le toca a dirección.',
           '<b>Por dónde empezar:</b> casos, coste y retorno.', '<b>Plan y política interna de uso.</b>'],
    sale='Un plan de IA para la empresa y su política de uso.',
    pq=[('i-boss', 'Si diriges una empresa o un área', 'Y tienes que decidir qué hacer con la IA.'), ('i-euro', 'Si quieres saber coste y retorno', 'Antes de invertir.'),
        ('i-shield', 'Si necesitas una política de uso', 'Clara y adaptada a tu empresa.')],
    chip_foto=[('i-boss', 'Para dirección', 'Decisiones con criterio'), ('i-shield', 'Política de uso', 'Lista para aplicar')],
    cuenta='No hace falta ninguna herramienta concreta. Vemos ejemplos con las que ya usa tu empresa.',
    temario=[M('Introducción a la IA', 'Lo que dirección tiene que saber', 2, ['Qué es la IA generativa y qué puede hacer por la empresa', 'Qué herramientas hay y en qué se diferencian'], comun=True),
             M('IA segura y legal', 'Qué le toca a dirección', 2, ['El artículo 4 del Reglamento Europeo de IA', 'RGPD y riesgos'], comun=True),
             M('Por dónde empezar', 'Casos, coste y retorno', 2, ['Detectar los casos con más retorno', 'Calcular coste y ahorro']),
             M('Plan y política interna de uso', 'Reglas claras para el equipo', 2, ['Plan de implantación', 'Política de uso de la IA en la empresa'])],
    foto='despacho.jpg', foto_alt='Reunión de trabajo en un despacho', cta=('La IA en tu empresa,', 'con un plan'))

POR_SLUG = {c['slug']: c for c in CURSOS}

# ---------------------------------------------------------------- siguiente paso de cada curso
def siguientes(c):
    k, s = c.get('herr'), c['slug']
    if s == 'alfabetizacion-en-ia':
        return [slug(f'{HERR[h]["nombre"]} Esencial') for h in ORDEN_HERR]
    if c.get('nivel'):
        N = HERR[k]['nombre']; i = c['nivel']
        out = [slug(f'{N} {NIVEL[i]}')] if i < 3 else []
        if i == 2 and k == 'claude': out.append('claude-code-para-no-programadores')
        if i == 3 and k == 'microsoft': out.append(slug('Copilot Studio I · Crea tu primer agente'))
        out += [slug(f'{N} para {a}') for a in AREAS][:3 - len(out) + 1]
        out.append(slug(f'{N} al día'))
        return out[:4]
    if c.get('aldia'):
        N = HERR[k]['nombre']; return [slug(f'{N} {n}') for n in NIVEL] + [slug(f'{N} para comercial y marketing')]
    if c.get('area'):
        N = HERR[k]['nombre']; return [slug(f'{N} {NIVEL[1]}')] + [slug(f'{N} para {a}') for a in AREAS if a != c['area']] + [slug(f'{N} al día')]
    if s.startswith('administracion-de'):
        N = HERR[k]['nombre']; return [slug(f'{N} {n}') for n in NIVEL] + ['ia-para-direccion']
    if s == 'claude-code-para-no-programadores':
        return ['claude-experto', 'claude-avanzado', 'claude-al-dia', 'administracion-de-claude-para-empresas']
    if s.startswith('copilot-studio-i-'):
        return [slug('Copilot Studio II · Agentes conectados a tu empresa'), 'microsoft-365-copilot-experto', 'microsoft-365-copilot-avanzado', 'administracion-de-microsoft-365-copilot-para-empresas']
    if s.startswith('copilot-studio-ii'):
        return ['microsoft-365-copilot-experto', 'administracion-de-microsoft-365-copilot-para-empresas', 'microsoft-365-copilot-al-dia', 'ia-para-direccion']
    if s == 'ia-para-direccion':
        return ['alfabetizacion-en-ia', 'claude-esencial', 'chatgpt-esencial', 'microsoft-365-copilot-esencial']
    return []
