# -*- coding: utf-8 -*-
"""
DATOS DE LOS CURSOS (catálogo de la portada: Formación general y Por herramienta)
Para cambiar un texto, unas horas o un precio: cámbialo aquí y ejecuta
    python3 generador/generar.py
Se vuelven a crear todas las fichas de cursos/ y el MAPA-WEB.md.
Los nombres tienen que coincidir con la lista CURSOS del <script> de index.html.
"""
import unicodedata, re

def slug(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')

# Próximas convocatorias en directo (la portada las lee de la hoja de Google)
CONVOCATORIA = 'Desde el 11 de enero de 2027'

# ---------------------------------------------------------------- herramientas
HERR = {
    'claude': dict(
        m_apps='Skills y Claude en tus apps', m_autom='Automatizaciones y Claude en Chrome', m_mini='Artefactos y mini aplicaciones',
        nombre='Claude', logo='claude.svg', foto='incompany-claude.jpg', foto_alt='Formación de Claude con el equipo de una empresa',
        reutil='skills', reutil_larga='skills: instrucciones que Claude reutiliza siempre que las necesita',
        apps='Claude en Excel, Word y correo', autom='tareas programadas y automatizaciones en el navegador',
        mini='artefactos y miniaplicaciones', agentes='agentes con Claude',
        ecosistema='Claude en la web, en el escritorio y en el móvil',
        cuenta1='una cuenta de Claude: gratuita para empezar; Pro o Team para sacarle todo el partido',
        cuenta2='Claude Pro, Team o Enterprise',
        nombres=['Claude Esencial', 'Claude Avanzado', 'Claude Completo']),
    'chatgpt': dict(
        m_apps='GPTs y ChatGPT en tus apps', m_autom='Tareas programadas y ChatGPT en el navegador', m_mini='Canvas y mini aplicaciones',
        nombre='ChatGPT', logo='chatgpt.png', foto='incompany-chatgpt.jpg', foto_alt='Formación de ChatGPT con el equipo de una empresa',
        reutil='GPTs a medida', reutil_larga='GPTs a medida: asistentes con tus instrucciones y tus documentos',
        apps='ChatGPT con tus documentos y tu correo', autom='tareas programadas',
        mini='Canvas y miniaplicaciones', agentes='el modo agente de ChatGPT',
        ecosistema='ChatGPT en la web, en el escritorio y en el móvil',
        cuenta1='una cuenta de ChatGPT: gratuita para empezar; Plus, Team o Enterprise para sacarle todo el partido',
        cuenta2='ChatGPT Plus, Team o Enterprise',
        nombres=['Fundamentos de ChatGPT', 'ChatGPT en profundidad', 'ChatGPT de cero a experto']),
    'microsoft': dict(
        m_apps='Prompts guardados y Copilot en tus apps', m_autom='Automatizaciones con Microsoft 365', m_mini='Documentos y páginas con Copilot',
        nombre='Microsoft 365 Copilot', logo='copilot.png', foto='aula-practica.jpg', foto_alt='Alumnos practicando con ordenadores durante una formación',
        reutil='prompts guardados', reutil_larga='prompts guardados para no repetir instrucciones',
        apps='Copilot en Word, Excel, PowerPoint, Outlook y Teams', autom='automatizaciones con Microsoft 365',
        mini='documentos y páginas generados con Copilot', agentes='agentes en Microsoft 365 Copilot',
        ecosistema='Copilot Chat, Notebooks y las apps de Microsoft 365',
        cuenta1='una cuenta de Microsoft 365 de empresa. El nivel 1 funciona con Copilot Chat, sin licencia de Copilot',
        cuenta2='la licencia de Microsoft 365 Copilot. Desde el 15 de abril de 2026, sin ella no hay Copilot dentro de Word, Excel, PowerPoint ni OneNote',
        nombres=['Microsoft 365 Copilot desde cero', 'Copilot en tus apps de Microsoft 365', 'Microsoft 365 Copilot completo']),
    'gemini': dict(
        m_apps='Gems y Gemini en tus apps', m_autom='Automatizaciones con Google Workspace', m_mini='Canvas y mini aplicaciones',
        nombre='Gemini', logo='gemini.png', foto='grupo-abierto.jpg', foto_alt='Alumnos practicando con sus portátiles durante una formación',
        reutil='Gems', reutil_larga='Gems: asistentes con tus instrucciones para las tareas que repites',
        apps='Gemini en Gmail, Docs y Sheets', autom='automatizaciones con Google Workspace',
        mini='miniaplicaciones', agentes='agentes con Gemini',
        ecosistema='Gemini en la web y dentro de Google Workspace',
        cuenta1='una cuenta de Google: gratuita para empezar; Google Workspace con Gemini para la empresa',
        cuenta2='Google Workspace con Gemini',
        nombres=['Introducción a Gemini', 'Gemini práctico', 'Gemini completo']),
}
ORDEN_HERR = ['claude', 'chatgpt', 'microsoft', 'gemini']

# Campus para particulares (escalera Ready / Build / Agents). Enlace de Stripe: pendiente.
CAMPUS = {   # packs para particulares: teleformación en el campus + mentoría (página particulares.html)
    'ready':  dict(nombre='Pack Esencial', et='Ready · 10 h', precio='79 €', antes='119 €', plazo='26,33 €', stripe='',
                   txt='El campus de Alfabetización en IA a tu ritmo, para empezar con la IA o acreditar tu formación.',
                   lista=['Campus Ready · 10 h', 'Certificado verificable', '12 meses de acceso'], medalla=1),
    'build':  dict(nombre='Pack Profesional', et='Build · 25 h', precio='299 €', antes='449 €', plazo='99,67 €', stripe='',
                   txt='Conectas Claude a tu correo y tus documentos, creas tus skills y dejas una tarea tuya automatizada.',
                   lista=['Incluye Ready', '2 h de mentoría 1 a 1', 'Proyecto corregido'], medalla=2),
    'agents': dict(nombre='Pack Completo', et='Agents · 40 h', precio='449 €', antes='649 €', plazo='149,67 €', stripe='',
                   txt='Creas miniaplicaciones a partir de un Excel y un agente que hace un proceso tuyo de principio a fin.',
                   lista=['Incluye Ready y Build', '3 h de mentoría 1 a 1', 'Dos proyectos corregidos'], medalla=3),
}
# Aula síncrona para empresas: online en directo, alumnos de varias empresas, precio por alumno (sin IVA)
AULA = {'alfabetizacion-en-ia': 190}
AULA_NIVEL = {1: 190, 2: 390, 3: 490}
# Oferta de lanzamiento de los packs: 'precio' es el de lanzamiento y 'antes' el normal.
# Al acabar la oferta, pon en 'precio' el valor de 'antes' y deja LANZAMIENTO = ''.
LANZAMIENTO = 'Precio de lanzamiento hasta el 31 de enero'

# ---------------------------------------------------------------- módulos
def M(t, sub, h, puntos, comun=False, llevas=None, grupo=None):
    return dict(t=t, sub=sub, h=h, puntos=puntos, comun=comun, llevas=llevas, grupo=grupo)

def mod_intro(prompting=True):
    return M('Introducción a la IA' + (' y prompting' if prompting else ''), 'Qué es y cómo pedirle las cosas', 2,
             ['Qué es la IA generativa y qué puede hacer por tu trabajo, y qué no',
              'Cómo funciona, sin tecnicismos: por qué a veces se equivoca o se inventa datos',
              'Prompting: cómo pedirle las cosas para que responda bien',
              'Trabajar con tus propios documentos'], comun=True)

def mod_legal():
    return M('IA segura y legal', 'AI Act (artículo 4) y RGPD', 2,
             ['Qué pide el artículo 4 del Reglamento Europeo de IA a las empresas que usan IA',
              'RGPD: qué datos puedes compartir con una IA y cuáles no',
              'Cuentas personales y de empresa: dónde acaban tus datos',
              'Cómo revisar lo que te devuelve la IA antes de usarlo'], comun=True)

cap = lambda t: t[0].upper() + t[1:]

# Estructura de los tres niveles (documento «Formación in-company», apartado 1.2):
# Nivel 1 = Ready (8 h) · Nivel 2 = Build (incluye Ready, 17 h por persona) · Nivel 3 = Agents (incluye Build, 22,5 h por persona).
# Los talleres son de 1,5 h por persona (en empresa, 3 grupos por área de 1,5 h). La sesión de cierre va al final del nivel contratado.
def temario_n1(k):
    H = HERR[k]
    return [M('Introducción a la IA', 'AI first y prompting', 2,
              ['Qué es la IA generativa, cómo funciona y dónde se equivoca', 'Mentalidad AI first: qué tareas puedes pasarle',
               'Prompting: cómo pedirle las cosas para que responda bien'], comun=True, llevas='Una forma de pedir que funciona.'),
            M(f'Conocemos {H["nombre"]}', 'Ecosistema y configuración', 2,
              [f'El ecosistema completo: {H["ecosistema"]}', 'Configuración, preferencias, estilos y memoria',
               'De menos a más: chat, investigación y trabajo con tus archivos'], llevas='La herramienta configurada.'),
            M('IA segura y legal', 'AI Act (art. 4) y RGPD', 2,
              ['El AI Act en sencillo y el artículo 4', 'RGPD y semáforo de datos: qué puedes compartir y qué no',
               'Configuración segura y cómo revisar lo que sale'], comun=True, llevas='La alfabetización del art. 4 cumplida.'),
            M('Cómo la usamos', 'Proyectos y conectores', 2,
              ['Un proyecto con tus archivos e instrucciones', 'Conectores con tu correo, tu calendario y tus documentos',
               'Dos o tres casos reales de tu trabajo dentro'], llevas='Un proyecto con tus casos funcionando.')]

def temario_n2(k, cierre=True):
    H = HERR[k]
    mods = [M(H['m_apps'], 'Instrucciones reutilizables y la IA en tus aplicaciones', 2,
              [f'Las tareas que repites pasan a ser {H["reutil"]}', H['apps']], llevas=f'Tus {H["reutil"]} creadas.'),
            M(H['m_autom'], 'Que las tareas se hagan solas', 2,
              [cap(H['autom']), 'Por ejemplo, un informe que se prepara solo cada lunes', 'La IA trabajando en webs por ti'], llevas='Una tarea programada funcionando.'),
            M('Taller práctico 1', 'Tus tareas repetidas, con tu caso', 1.5,
              ['En grupo por área (administración, comercial, técnicos…)', f'Cada persona convierte sus tareas repetidas en {H["reutil"]}'], llevas='Las instrucciones de tu puesto.'),
            M('Taller práctico 2', 'Una tarea automatizada', 1.5,
              ['Cada área deja una tarea automatizada funcionando', 'Con un proceso real de su trabajo'], llevas='Una automatización en tu área.')]
    if cierre:
        mods.append(M('Sesión de cierre', 'Todo el grupo junto', 2,
              ['Cada área enseña lo que ha montado', 'Repasamos las horas ahorradas y fijamos el plan de los próximos meses', 'Entrega de certificados'], llevas='Un plan para los próximos meses.'))
    return mods

def temario_n3(k):
    H = HERR[k]
    return [M(H['m_mini'], 'Pequeñas herramientas para el equipo', 2,
              ['Documentos y visuales al momento', 'Pequeñas herramientas: una calculadora de ofertas, un formulario de incidencias o un panel a partir de un Excel',
               'Cómo compartirlas con el equipo'], llevas='Una mini app para tu equipo.'),
            M('Agentes avanzados', 'Todas las piezas juntas', 2,
              ['El proyecto del nivel 1 evoluciona a agente', f'Instrucciones completas, {H["reutil"]}, conectores y tareas programadas trabajando juntos',
               'Un agente que hace un trabajo de principio a fin'], llevas='Tu agente diseñado.'),
            M('Taller práctico 3', 'Tu agente en marcha', 1.5,
              ['Cada área convierte su proyecto en un agente', 'Lo pone a trabajar con nosotros al lado'], llevas='El agente en uso en tu área.'),
            M('Sesión de cierre', 'Todo el grupo junto', 2,
              ['Cada área enseña lo que ha montado', 'Repasamos las horas ahorradas y fijamos el plan de los próximos meses', 'Entrega de certificados'], llevas='Un plan para los próximos meses.')]

def con_grupo(mods, grupo):
    out = [dict(m) for m in mods]; out[0]['grupo'] = grupo; return out

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
}

# ---------------------------------------------------------------- cursos
CURSOS = []

def add(**c):
    c.setdefault('slug', slug(c['n']))
    c.setdefault('dir', True); c.setdefault('ic', True); c.setdefault('hc', 0)
    c.setdefault('art4', False); c.setdefault('req', 'Ninguno'); c.setdefault('req_det', 'Ni conocimientos técnicos')
    c.setdefault('campus', None)
    c.setdefault('tools', [HERR[c['herr']]['logo']] if c.get('herr') in HERR else [])
    CURSOS.append(c)

TODAS = ['claude.svg', 'chatgpt.png', 'copilot.png', 'gemini.png']

# ======================= FORMACIÓN GENERAL =======================
add(n='Alfabetización en IA', t='general', herr='general', et='Formación general · Para toda la plantilla', ficha_et='Para toda la plantilla',
    sub='Usa la IA con criterio, con seguridad y dentro de la ley', img3d='alfabetizacion',
    lead='El curso para empezar con la inteligencia artificial o para acreditar tu formación.',
    intro='Entiendes qué es la IA generativa y cómo pedirle las cosas, sabes qué datos puedes compartir y cuáles no, y pruebas Claude, ChatGPT, Copilot y Gemini para elegir la que te encaja.',
    tools=TODAS, tools_txt='Claude, ChatGPT, Copilot y Gemini', h=8, hc=10, art4=True, campus='ready', ico='i-shield', bg='p1',
    p=['Qué es la IA y cómo usarla con criterio', 'AI Act y RGPD en sencillo', 'Certificado del art. 4'],
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
    cuenta='Ninguna de pago. En el campus trabajas con las cuentas gratuitas de Claude, ChatGPT y Gemini. En directo o in company usamos las cuentas que tengas; si tu empresa ya paga alguna herramienta, trabajamos con esa.',
    temario=[mod_intro(prompting=False),
             mod_legal(),
             M('Las herramientas', 'Claude, ChatGPT, Copilot y Gemini', 2,
               ['Qué hace bien cada una y para qué tipo de tarea', 'La misma tarea en las cuatro, una al lado de la otra',
                'Configurarla para tu trabajo: instrucciones y memoria', 'Cómo elegir según lo que ya usa tu empresa']),
             M('Práctica y test final', 'Con tus documentos', 2, ['Casos de uso de tu puesto, resueltos en clase', 'Test final para obtener el certificado'])],
    cta=('Empieza con la IA', 'con buen pie'),
    sig=['claude-esencial', 'fundamentos-de-chatgpt', 'microsoft-365-copilot-desde-cero', 'prompting-eficaz'],
    sig_txt='Al acabar, sigue con la herramienta que usas. Te saltas el bloque común que ya has hecho aquí.')

add(n='Prompting eficaz', t='general', herr='general', et='Formación general · Para toda la plantilla', ficha_et='Para toda la plantilla',
    sub='Pídele las cosas a la IA para que responda bien a la primera', img3d='prompting',
    lead='Un taller corto para pedirle las cosas a la IA y obtener respuestas fiables.',
    intro='Aprendes cómo se construye una buena instrucción, cómo comprobar lo que te devuelve y cómo convertir lo que funciona en plantillas para tu trabajo. Sirve para cualquier herramienta.',
    tools=TODAS, tools_txt='Cualquiera: Claude, ChatGPT, Copilot o Gemini', h=4, hc=4, ico='i-pen', bg='p3',
    p=['Cómo pedirle las cosas a la IA', 'Respuestas fiables y reutilizables', 'Plantillas para tu trabajo'],
    h2_porque=('La diferencia está', 'en cómo se lo pides'),
    porque='La mayoría de respuestas flojas de la IA vienen de instrucciones flojas. En cuatro horas cambias tu forma de pedirle las cosas y te llevas plantillas listas para usar.',
    lista=['<b>La estructura de un buen prompt:</b> rol, contexto, tarea y formato.',
           '<b>Respuestas fiables:</b> ejemplos, comprobación y cómo iterar.',
           '<b>Trabajar con tus documentos</b> sin perder el control de lo que compartes.',
           '<b>Tus plantillas:</b> las instrucciones que funcionan, guardadas para reutilizarlas.'],
    sale='Tu plantilla de prompts para las tareas de tu trabajo.',
    pq=[('i-chat', 'Si usas la IA pero no te convence', 'Las respuestas son genéricas o tienes que corregirlas mucho.'),
        ('i-users', 'Si quieres que todo el equipo pida igual', 'Con un mismo método y plantillas compartidas.'),
        ('i-compass', 'Si quieres una base rápida', 'Cuatro horas, sin requisitos y con cualquier herramienta.')],
    chip_foto=[('i-pen', 'Tus plantillas', 'Listas para reutilizar'), ('i-check', 'Respuestas fiables', 'Cómo comprobarlas')],
    foto='grupo-abierto.jpg', foto_alt='Alumnos practicando con sus portátiles durante una formación',
    cuenta='Ninguna de pago. Practicamos con la herramienta que ya uses, también con cuentas gratuitas.',
    temario=[M('Cómo responde la IA', 'Por qué importa cómo se lo pides', 1, ['Qué hace la IA con tu instrucción', 'Por qué a veces se inventa datos', 'Errores típicos al pedirle las cosas']),
             M('La estructura de un buen prompt', 'Rol, contexto, tarea y formato', 1, ['Las cuatro piezas de una buena instrucción', 'Darle contexto con tus documentos', 'Pedir el formato exacto que necesitas']),
             M('Respuestas fiables', 'Ejemplos, comprobación e iteración', 1, ['Darle ejemplos de lo que quieres', 'Cómo comprobar lo que te devuelve', 'Mejorar la respuesta paso a paso']),
             M('Plantillas para tu trabajo', 'Práctica con tus tareas', 1, ['Eliges tres tareas de tu trabajo', 'Creas y pruebas sus plantillas'], llevas='tu plantilla de prompts.')],
    cta=('Pídele las cosas a la IA', 'como un experto'),
    sig=['investigacion-y-analisis-con-ia', 'documentos-y-presentaciones-con-ia', 'alfabetizacion-en-ia', 'claude-esencial'])

add(n='Investigación y análisis con IA', t='general', herr='general', et='Formación general · Taller práctico', ficha_et='Taller práctico',
    sub='Busca, contrasta y resume información con IA', img3d='investigacion',
    lead='Un taller práctico para investigar y analizar información con IA sin perder rigor.',
    intro='Buscas y contrastas fuentes, resumes y comparas documentos largos, y conviertes lo que encuentras en informes claros. Con tus temas de trabajo y comprobando siempre de dónde sale cada dato.',
    tools=TODAS, tools_txt='Claude, ChatGPT, Copilot o Gemini', h=4, ico='i-chart', bg='p2',
    p=['Buscar y contrastar fuentes', 'Resumir y comparar información', 'Informes claros'],
    h2_porque=('Investigar más rápido', 'sin perder rigor'),
    porque='La IA puede leer, buscar y resumir en minutos lo que antes llevaba horas. La clave es saber cuándo fiarse y cómo comprobarlo.',
    lista=['<b>Búsqueda con IA:</b> encontrar información actual y citar las fuentes.',
           '<b>Contrastar:</b> cómo detectar datos inventados o desactualizados.',
           '<b>Resumir y comparar</b> documentos largos, contratos o informes.',
           '<b>Informes claros</b> a partir de lo que has encontrado.'],
    sale='Un informe hecho con tu tema de trabajo y un método para investigar con IA y comprobar las fuentes.',
    pq=[('i-chart', 'Si analizas información a menudo', 'Mercado, competencia, normativa o clientes.'),
        ('i-doc', 'Si lees documentos largos', 'Y necesitas resumirlos o compararlos.'),
        ('i-check', 'Si te preocupa la fiabilidad', 'Y quieres saber cuándo fiarte de la IA.')],
    chip_foto=[('i-chart', 'Informes claros', 'Con tus temas'), ('i-check', 'Fuentes comprobadas', 'Sin datos inventados')],
    foto='despacho.jpg', foto_alt='Reunión de trabajo en un despacho',
    cuenta='Te recomendamos una cuenta de pago de la herramienta que uses, porque la búsqueda y la lectura de documentos largos funcionan mejor. Si solo tienes la gratuita, también puedes seguir el taller.',
    temario=[M('Buscar con IA', 'Información actual y con fuentes', 1, ['Búsqueda e investigación con IA', 'Pedir siempre las fuentes']),
             M('Contrastar', 'Cuándo fiarse y cuándo no', 1, ['Detectar datos inventados o desactualizados', 'Comprobar con la fuente original']),
             M('Resumir y comparar', 'Documentos largos', 1, ['Resúmenes que no se dejan nada importante', 'Comparar varios documentos o propuestas']),
             M('Informes claros', 'Práctica con tu tema', 1, ['Del análisis al informe', 'Tablas, conclusiones y próximos pasos'])],
    cta=('Investiga con IA', 'y con rigor'),
    sig=['documentos-y-presentaciones-con-ia', 'prompting-eficaz', 'claude-avanzado', 'chatgpt-en-profundidad'])

add(n='Documentos y presentaciones con IA', t='general', herr='general', et='Formación general · Taller práctico', ficha_et='Taller práctico',
    sub='Informes, propuestas y presentaciones en menos tiempo', img3d='documentos',
    lead='Un taller práctico para preparar documentos y presentaciones con IA, con el estilo de tu empresa.',
    intro='Preparas informes y propuestas a partir de tus notas, creas presentaciones en menos tiempo y haces que todo salga con el tono y el formato de tu empresa.',
    tools=TODAS, tools_txt='Claude, ChatGPT, Copilot o Gemini', h=4, ico='i-doc', bg='p5',
    p=['Informes y propuestas', 'Presentaciones en menos tiempo', 'Con el estilo de tu empresa'],
    h2_porque=('Del borrador al documento', 'en la mitad de tiempo'),
    porque='Informes, propuestas y presentaciones se llevan buena parte de la semana. Con IA llegas antes a un buen borrador y dedicas el tiempo a lo que importa.',
    lista=['<b>Informes y propuestas</b> a partir de tus notas y documentos.',
           '<b>Presentaciones:</b> estructura, textos y diapositivas en menos tiempo.',
           '<b>El estilo de tu empresa:</b> tono, plantillas y formato.',
           '<b>Revisar antes de enviar:</b> qué comprobar siempre.'],
    sale='Un documento y una presentación de tu trabajo, hechos con IA y con el estilo de tu empresa.',
    pq=[('i-doc', 'Si preparas informes o propuestas', 'Y te llevan horas cada semana.'),
        ('i-mega', 'Si haces presentaciones', 'Para clientes, dirección o el equipo.'),
        ('i-building', 'Si quieres un estilo común', 'Que todo el equipo entregue con el mismo formato.')],
    chip_foto=[('i-doc', 'Informes y propuestas', 'A partir de tus notas'), ('i-mega', 'Presentaciones', 'En menos tiempo')],
    foto='incompany-claude.jpg', foto_alt='Formación con el equipo de una empresa',
    cuenta='Te recomendamos una cuenta de pago de la herramienta que uses. Para Copilot dentro de Word y PowerPoint hace falta la licencia de Microsoft 365 Copilot.',
    temario=[M('Informes y propuestas', 'A partir de tus notas', 1, ['Del correo o las notas al primer borrador', 'Estructura y argumentos']),
             M('Presentaciones', 'Estructura, textos y diapositivas', 1, ['Guion de la presentación', 'Diapositivas en menos tiempo']),
             M('El estilo de tu empresa', 'Tono, plantillas y formato', 1, ['Instrucciones con vuestro tono', 'Plantillas que se reutilizan']),
             M('Práctica con tus documentos', 'Y revisión antes de enviar', 1, ['Preparas un documento y una presentación tuyos', 'Qué revisar siempre antes de enviar'])],
    cta=('Documentos y presentaciones', 'en menos tiempo'),
    sig=['investigacion-y-analisis-con-ia', 'prompting-eficaz', 'copilot-en-tus-apps-de-microsoft-365', 'claude-avanzado'])

add(n='IA para dirección', t='general', herr='general', et='Formación general · Para dirección', ficha_et='Para dirección', img3d='direccion',
    sub='Plan de IA y política de uso para tu empresa', h=8, dir=False, art4=True,
    lead='Decide por dónde empezar con la IA en tu empresa y con qué reglas.',
    intro='Para dirección y gerencia: qué es la IA, qué le toca a dirección en el AI Act, dónde aplicarla, cómo priorizar y medir el retorno, y el plan de adopción con su política de uso.',
    tools=TODAS, tools_txt='Sin herramienta concreta', ico='i-boss', bg='p4',
    p=['Dónde aplicar la IA', 'Priorizar y medir el retorno', 'Plan de adopción'],
    h2_porque=('La IA vista', 'desde dirección'),
    porque='Antes de formar a todo el equipo, dirección tiene que decidir para qué, con qué herramientas y con qué reglas.',
    lista=['<b>Introducción a la IA</b> para tomar decisiones con criterio.', '<b>IA segura y legal:</b> qué le toca a dirección.',
           '<b>Dónde aplicarla:</b> casos, prioridades y retorno.', '<b>Plan de adopción</b> y política interna de uso.'],
    sale='Un plan de IA para la empresa y su política de uso.',
    pq=[('i-boss', 'Si diriges una empresa o un área', 'Y tienes que decidir qué hacer con la IA.'), ('i-euro', 'Si quieres saber coste y retorno', 'Antes de invertir.'),
        ('i-shield', 'Si necesitas una política de uso', 'Clara y adaptada a tu empresa.')],
    chip_foto=[('i-boss', 'Para dirección', 'Decisiones con criterio'), ('i-shield', 'Política de uso', 'Lista para aplicar')],
    foto='despacho.jpg', foto_alt='Reunión de trabajo en un despacho',
    cuenta='No hace falta ninguna herramienta concreta. Vemos ejemplos con las que ya usa tu empresa.',
    temario=[M('Introducción a la IA', 'Lo que dirección tiene que saber', 2, ['Qué es la IA generativa y qué puede hacer por la empresa', 'Qué herramientas hay y en qué se diferencian'], comun=True),
             M('IA segura y legal', 'Qué le toca a dirección', 2, ['El artículo 4 del Reglamento Europeo de IA', 'RGPD y riesgos'], comun=True),
             M('Dónde aplicar la IA', 'Casos, coste y retorno', 2, ['Detectar los casos con más retorno', 'Priorizar y medir el ahorro']),
             M('Plan de adopción', 'Y política interna de uso', 2, ['Plan de implantación por fases', 'Política de uso de la IA en la empresa'])],
    cta=('La IA en tu empresa,', 'con un plan'),
    sig=['ia-y-cumplimiento-normativo', 'alfabetizacion-en-ia', 'prompting-eficaz', 'claude-esencial'])

add(n='IA y cumplimiento normativo', t='general', herr='general', et='Formación general · Para legal y compliance', ficha_et='Para legal y compliance', img3d='cumplimiento',
    sub='AI Act, datos y propiedad intelectual en la práctica', h=8, art4=True,
    lead='Lo que el AI Act, el RGPD y la propiedad intelectual piden cuando tu empresa usa IA.',
    intro='Para legal, compliance y protección de datos: las obligaciones del Reglamento Europeo de IA según cómo la uséis, los datos personales y la confidencialidad, la propiedad intelectual de lo que genera la IA y una política de uso interna.',
    tools=TODAS, tools_txt='Sin herramienta concreta', ico='i-scale', bg='p6',
    p=['Obligaciones del AI Act', 'Datos y propiedad intelectual', 'Política de uso interna'],
    h2_porque=('Usar IA en la empresa', 'con las reglas claras'),
    porque='El Reglamento Europeo de IA ya se aplica por fases. Legal y compliance necesitan saber qué toca hacer, qué documentar y qué reglas poner al equipo.',
    lista=['<b>Obligaciones del AI Act</b> según el uso que hacéis de la IA.',
           '<b>Datos personales y confidencialidad:</b> RGPD y secretos de empresa.',
           '<b>Propiedad intelectual:</b> de quién es lo que genera la IA y qué riesgos hay.',
           '<b>Política de uso interna</b> lista para adaptar.'],
    sale='Un mapa de las obligaciones que os tocan y una política de uso de la IA adaptada a vuestra empresa.',
    pq=[('i-scale', 'Si trabajas en legal o compliance', 'Y te toca poner las reglas del uso de la IA.'),
        ('i-shield', 'Si eres responsable de protección de datos', 'Y quieres saber qué datos pueden ir a una IA.'),
        ('i-boss', 'Si diriges la empresa', 'Y quieres tener claras las obligaciones.')],
    chip_foto=[('i-scale', 'AI Act en la práctica', 'Qué os toca hacer'), ('i-shield', 'Política de uso', 'Lista para adaptar')],
    foto='despacho.jpg', foto_alt='Reunión de trabajo en un despacho',
    cuenta='No hace falta ninguna herramienta concreta.',
    temario=[M('El Reglamento Europeo de IA', 'Obligaciones según el uso', 2, ['Calendario de aplicación', 'Niveles de riesgo y qué implican', 'El artículo 4: formación del equipo'], comun=True),
             M('Datos personales y confidencialidad', 'RGPD y secretos de empresa', 2, ['Qué datos pueden ir a una IA y cuáles no', 'Cuentas de empresa, contratos y encargados de tratamiento']),
             M('Propiedad intelectual', 'Lo que genera la IA', 2, ['De quién es lo que genera la IA', 'Riesgos al usar contenido de terceros']),
             M('Política de uso interna', 'Reglas claras para el equipo', 2, ['Qué debe incluir una política de uso de la IA', 'Adaptarla a vuestra empresa'], llevas='una política de uso para adaptar.')],
    nota_temario='Este curso es formativo y no sustituye el asesoramiento jurídico de cada caso.',
    cta=('La IA en tu empresa,', 'con las reglas claras'),
    sig=['ia-para-direccion', 'alfabetizacion-en-ia', 'prompting-eficaz', 'claude-esencial'])

# ======================= POR HERRAMIENTA =======================
HORAS_NIVEL = [8, 17, 22.5]   # horas por persona: Ready, Build (incluye Ready) y Agents (incluye Build)
for k in ORDEN_HERR:
    H = HERR[k]; N = H['nombre']; NOM = H['nombres']; es_c = (k == 'claude')
    t1, t2, t2sc, t3 = temario_n1(k), temario_n2(k), temario_n2(k, cierre=False), temario_n3(k)
    camp = 'build' if es_c else None
    # Nivel 1
    add(n=NOM[0], t='herr', herr=k, nivel=1, et=f'{N} · Nivel 1 · Para empezar', ficha_et='Nivel 1 · Ready · Para empezar',
        dur_dir='8 h · 4 sesiones de 2 h', dur_ic='2 días de 4 h presenciales o 4 sesiones de 2 h online',
        sub=f'Empieza a usar {N} en tu trabajo', h=8, hc=(25 if es_c else 'pronto'), campus=camp, art4=True, ico='i-chat', bg='p3',
        p={'claude': ['Prompting y configuración', 'Proyectos y memoria', 'Conectores con tus herramientas'],
           'chatgpt': ['Prompting y configuración', 'Proyectos y memoria', 'Conectores con tus herramientas'],
           'microsoft': ['Copilot Chat, también sin licencia', 'Prompting y Notebooks', 'Documentos de tu empresa'],
           'gemini': ['Prompting y configuración', 'Gemini en Google Workspace', 'Conexión con Drive']}[k],
        lead=f'Empieza a usar {N} en tu trabajo, bien configurado y con tus casos.',
        intro='Cuatro módulos de 2 h: introducción a la IA y prompting, la herramienta configurada, IA segura y legal, y proyectos con conectores. Acabas con un proyecto con tus casos funcionando y el certificado del artículo 4.',
        h2_porque=(f'{N} configurado', 'para tu trabajo'),
        porque=f'Un curso práctico para pasar de hacerle preguntas sueltas a {N} a tenerlo configurado y trabajando con tus documentos.',
        lista=['<b>Prompting:</b> cómo pedirle las cosas para que responda bien a la primera.',
               f'<b>Configuración y memoria:</b> {N} adaptado a tu forma de trabajar.',
               '<b>Proyectos y conectores:</b> tu contexto, tus archivos, tu correo y tu calendario.',
               '<b>IA segura y legal:</b> el artículo 4 del Reglamento Europeo de IA y el RGPD.'],
        sale='La herramienta configurada, un proyecto con tus casos funcionando y la alfabetización del art. 4 cumplida.',
        pq=[('i-compass', f'Si empiezas con {N}', 'O lo usas de vez en cuando y quieres sacarle partido.'),
            ('i-building', f'Si tu empresa trabaja con {N}', 'Y el equipo tiene que usarlo bien y con seguridad.'),
            ('i-shield', 'Si necesitas acreditarlo', 'Incluye el bloque de IA segura y legal del artículo 4.')],
        chip_foto=[('i-doc', 'Con tus documentos', 'Proyectos y conectores'), ('i-shield', 'AI Act · artículo 4', 'Incluido en el certificado')],
        cuenta=f'Necesitas {H["cuenta1"]}.', temario=t1, cta=(f'Empieza a trabajar con {N}', 'desde el primer día'),
        sig=[slug(NOM[1]), slug(NOM[2])] + (['copilot-studio'] if k == 'microsoft' else []) + ['prompting-eficaz', 'documentos-y-presentaciones-con-ia'])
    # Nivel 2 (incluye el 1)
    add(n=NOM[1], t='herr', herr=k, nivel=2, et=f'{N} · Nivel 2 · Incluye nivel 1', ficha_et='Nivel 2 · Build · Incluye nivel 1',
        dur_dir='17 h por persona · teoría en sesiones de 2 h y talleres de 1,5 h',
        faq_dur='Son 17 horas por persona, con el nivel 1 incluido: 12 h de teoría en sesiones de 2 h, dos talleres prácticos de 1,5 h y la sesión de cierre de 2 h. En empresa son 6 días.', dur_ic='6 días: 17 h por persona (23 h de formador, talleres en 3 grupos por área)',
        sub=f'Que {N} te haga tareas enteras', h=17, hc=(25 if es_c else 'pronto'), campus=camp, art4=True, ico='i-chat', bg='p2',
        p={'claude': ['Todo lo del nivel 1', 'Skills y Claude en Excel, Word y correo', 'Automatizaciones en el navegador'],
           'chatgpt': ['Todo lo del nivel 1', 'GPTs a medida y tareas programadas', 'ChatGPT en documentos y correo'],
           'microsoft': ['Todo lo del nivel 1', 'Copilot en Word, Excel y PowerPoint', 'Outlook y Teams'],
           'gemini': ['Todo lo del nivel 1', 'Gems para tareas repetidas', 'Gmail, Docs, Sheets y automatizaciones']}[k],
        lead=f'Todo lo del nivel 1 y, además, que {N} te haga tareas enteras.',
        intro=f'Todo el nivel 1 y, además, {H["m_apps"].lower()}, {H["m_autom"].lower()}, dos talleres prácticos por área con vuestros casos y una sesión de cierre. Acabas con tus {H["reutil"]} y una tarea automatizada funcionando.',
        h2_porque=('De pedirle cosas', 'a que trabaje por ti'),
        porque=f'Si ya sabes que vas a usar {N} cada día, este curso junta los niveles 1 y 2: la base bien hecha y, encima, las funciones que te ahorran horas.',
        lista=['<b>Todo lo del nivel 1:</b> prompting, configuración, proyectos, conectores e IA segura y legal.',
               f'<b>Instrucciones reutilizables:</b> {H["reutil_larga"]}.',
               f'<b>La IA dentro de tus apps:</b> {H["apps"]}.',
               f'<b>Automatizaciones:</b> {H["autom"]}.',
               '<b>Dos talleres prácticos</b> por área con vuestros casos y una sesión de cierre.'],
        sale='Tus instrucciones reutilizables, una tarea automatizada funcionando y un plan para los próximos meses.',
        pq=[('i-refresh', 'Si repites las mismas tareas', 'Correos, informes o documentos que haces cada semana.'),
            ('i-bolt', 'Si quieres automatizar', 'Sin programar y con las herramientas que ya tienes.'),
            ('i-building', 'Si tu equipo va a usarlo a diario', 'Y quiere la base y el siguiente paso de una vez.')],
        chip_foto=[('i-bolt', 'Tareas que se hacen solas', 'Automatizaciones'), ('i-doc', cap(H['reutil']), 'Instrucciones reutilizables')],
        cuenta=f'Para el nivel 1 te vale {H["cuenta1"].split(":")[0] if ":" in H["cuenta1"] else H["cuenta1"]}; para la parte del nivel 2 necesitas {H["cuenta2"]}.',
        temario=con_grupo(t1, f'Nivel 1 · Ready · {NOM[0]} · 8 h') + con_grupo(t2, 'Nivel 2 · Build · 9 h'),
        cta=(f'Que {N} haga', 'tareas enteras'),
        sig=[slug(NOM[2])] + (['copilot-studio'] if k == 'microsoft' else []) + ['documentos-y-presentaciones-con-ia', 'investigacion-y-analisis-con-ia', 'prompting-eficaz'])
    # Nivel 3 (curso completo)
    add(n=NOM[2], t='herr', herr=k, nivel=3, completo=True, et=f'{N} · Nivel 3 · Curso completo', ficha_et='Nivel 3 · Agents · Curso completo',
        dur_dir='22,5 h por persona · teoría en sesiones de 2 h y talleres de 1,5 h',
        faq_dur='Son 22,5 horas por persona, con los niveles 1 y 2 incluidos: 16 h de teoría en sesiones de 2 h, tres talleres prácticos de 1,5 h y la sesión de cierre de 2 h. En empresa son 8 días y, además, 1 h con dirección.', dur_ic='8 días + 1 h con dirección: 22,5 h por persona (31,5 h de formador)',
        sub='De cero a tu propio agente funcionando', h=22.5, art4=True, ico='i-robot', bg='p5',
        p={'claude': ['Todo lo de los niveles 1 y 2', 'Artefactos y mini aplicaciones', 'Agentes y tres talleres prácticos'],
           'chatgpt': ['Todo lo de los niveles 1 y 2', 'Canvas y mini aplicaciones', 'Agentes y tres talleres prácticos'],
           'microsoft': ['Todo lo de los niveles 1 y 2', 'Documentos y páginas con Copilot', 'Agentes y tres talleres prácticos'],
           'gemini': ['Todo lo de los niveles 1 y 2', 'Canvas y mini aplicaciones', 'Agentes y tres talleres prácticos']}[k],
        lead=f'El curso completo de {N}: de la base a tu propio agente funcionando.',
        intro=f'Incluye los niveles 1 y 2 y, además, {H["m_mini"].lower()}, agentes avanzados y un tercer taller en el que cada área pone su agente a trabajar. En empresa, se añade una sesión de 1 h con dirección para fijar los siguientes pasos.',
        h2_porque=('Todo el recorrido', 'en un solo curso'),
        porque='El nivel más completo: la base bien hecha, las automatizaciones y, encima, un agente que hace un trabajo de principio a fin en cada área.',
        lista=['<b>Niveles 1 y 2:</b> configuración, proyectos, conectores, instrucciones reutilizables y automatizaciones.',
               f'<b>{cap(H["mini"])} y agentes:</b> todas las piezas juntas, con {H["agentes"]}.',
               '<b>Tres talleres prácticos</b> por área y una sesión de cierre. En empresa, también una sesión con dirección.'],
        sale='Un agente propio funcionando en un proceso real de tu trabajo.',
        pq=[('i-robot', 'Si quieres montar un agente', 'Que haga un proceso de tu trabajo de principio a fin.'),
            ('i-tools', 'Si quieres tus propias herramientas', 'Miniaplicaciones hechas a tu medida.'),
            ('i-rocket', f'Si quieres dominar {N}', 'De cero a experto en un solo curso.')],
        chip_foto=[('i-robot', 'Agente propio', 'En un proceso real'), ('i-target', '3 talleres', 'Con vuestros casos')],
        cuenta=f'Necesitas {H["cuenta2"]}.',
        temario=con_grupo(t1, f'Nivel 1 · Ready · {NOM[0]} · 8 h') + con_grupo(t2sc, f'Nivel 2 · Build · {NOM[1]} · 7 h') + con_grupo(t3, 'Nivel 3 · Agents · 7,5 h'),
        cta=('Monta tu propio agente', f'con {N}'),
        sig=(['copilot-studio'] if k == 'microsoft' else []) + ['ia-para-direccion', 'ia-y-cumplimiento-normativo', 'investigacion-y-analisis-con-ia', 'documentos-y-presentaciones-con-ia'])

add(n='Copilot Studio', t='herr', herr='microsoft', extra=True, tools=['copilot-studio.png'], tools_txt='Copilot Studio',
    et='Microsoft · Complemento', ficha_et='Complemento', sub='Crea tu primer agente sin programar', h=12, art4=True, ico='i-robot', bg='p6',
    p=['Crea tu primer agente sin programar', 'Con SharePoint y tus archivos', 'Publicado en Teams'],
    lead='Crea tu primer agente con Copilot Studio y publícalo en Teams.',
    intro='Creas un agente describiéndolo, le das conocimiento con SharePoint, archivos y webs, lo pruebas y lo publicas en Teams y Microsoft 365 Copilot. Con la licencia de Microsoft 365 Copilot, los agentes de uso interno no tienen coste extra.',
    h2_porque=('Tu primer agente', 'en Copilot Studio'),
    porque='Copilot Studio es la herramienta de Microsoft para crear agentes sin programar. Encaja en empresas que ya pagan Microsoft 365 Copilot.',
    lista=['<b>Qué es un agente</b> y cuándo tiene sentido.', '<b>Crearlo describiéndolo</b> y darle instrucciones.',
           '<b>Darle conocimiento:</b> SharePoint, archivos y webs.', '<b>IA segura en agentes:</b> permisos, datos y quién lo usa.'],
    sale='Un agente de preguntas internas publicado en Teams.',
    pq=[('i-robot', 'Si quieres un agente para el equipo', 'Que responda las preguntas internas de siempre.'),
        ('i-building', 'Si tu empresa usa Microsoft 365', 'Y ya paga Microsoft 365 Copilot.'), ('i-compass', 'Si no programas', 'Copilot Studio es low-code.')],
    chip_foto=[('i-robot', 'Publicado en Teams', 'Tu agente en marcha'), ('i-shield', 'IA segura', 'Permisos y datos')],
    foto='aula-practica.jpg', foto_alt='Alumnos practicando con ordenadores durante una formación',
    cuenta='Necesitas Microsoft 365 con acceso a Copilot Studio. Con la licencia de Microsoft 365 Copilot, los agentes de uso interno no tienen coste extra.',
    temario=[M('Qué es un agente y cuándo tiene sentido', 'Antes de crear nada', 2, ['Agentes, asistentes y automatizaciones', 'Casos que funcionan bien'], comun=True),
             M('Crear el agente describiéndolo', 'Y darle instrucciones', 2, ['Crear un agente desde una descripción', 'Instrucciones y tono']),
             M('Darle conocimiento', 'SharePoint, archivos y webs', 2, ['Fuentes de conocimiento', 'Cómo comprobar que responde bien']),
             M('IA segura en agentes', 'Permisos, datos y quién lo usa', 2, ['Quién puede usarlo y qué datos ve', 'El artículo 4 del Reglamento Europeo de IA aplicado a agentes'], comun=True),
             M('Probarlo y publicarlo', 'En Teams y Microsoft 365 Copilot', 2, ['Pruebas con preguntas reales', 'Publicación y seguimiento']),
             M('Proyecto: un agente de preguntas internas', 'Con tu caso', 2, ['Montas tu agente', 'Lo dejas publicado'])],
    nota_temario='Las funciones concretas de Copilot Studio se revisan al montar cada curso, porque Microsoft las cambia a menudo.',
    cta=('Crea tu primer agente', 'con Copilot Studio'),
    sig=['microsoft-365-copilot-completo', 'copilot-en-tus-apps-de-microsoft-365', 'ia-y-cumplimiento-normativo', 'ia-para-direccion'])

POR_SLUG = {c['slug']: c for c in CURSOS}

def siguientes(c):
    return [s for s in c.get('sig', []) if s in POR_SLUG and s != c['slug']][:4]
