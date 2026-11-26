# -*- coding: utf-8 -*-
"""
TEXTOS DE LAS PÁGINAS DE PARTICULARES (carpeta particulares/)
Cada nivel de Claude tiene su propia página, y es ahí donde se compra.
Precios, nombres y lista corta están en datos.py (PACKS). Aquí va el resto:
temario en teleformación, qué consigues, ejemplo y preguntas.
Después de cambiar algo, ejecuta:  python3 generador/generar.py
"""

def MOD(t, sub, puntos, llevas, nivel, ilus):
    return dict(t=t, sub=sub, puntos=puntos, llevas=llevas, nivel=nivel, ilus=ilus)

# Recorrido completo de los tres niveles. Cada nivel incluye los módulos de los anteriores.
RECORRIDO = [
    MOD('Introducción a la IA', 'AI first y prompting',
        ['Qué es la IA generativa, cómo funciona y dónde se equivoca', 'Mentalidad AI first: qué tareas le puedes pasar',
         'Prompting: cómo pedirle las cosas para que responda bien a la primera'],
        'una forma de pedir que funciona.', 1, 'chat'),
    MOD('Conoce Claude', 'Ecosistema y configuración',
        ['Claude en la web, en el escritorio y en el móvil', 'Preferencias, estilos y memoria',
         'De menos a más: chat, investigación y trabajo con tus archivos'],
        'Claude configurado para tu forma de trabajar.', 1, 'ajustes'),
    MOD('IA segura y legal', 'AI Act (artículo 4) y RGPD',
        ['El Reglamento Europeo de IA en sencillo y qué pide el artículo 4', 'Semáforo de datos: qué puedes compartir con una IA y qué no',
         'Configuración segura y cómo revisar lo que te devuelve'],
        'la formación del artículo 4 hecha y un checklist de protección de datos.', 1, 'escudo'),
    MOD('Proyectos y conectores', 'Tu trabajo siempre a mano',
        ['Un proyecto con tus archivos y tus instrucciones', 'Conectores con tu correo, tu calendario y tus documentos',
         'Dos o tres casos reales de tu trabajo dentro'],
        'un proyecto con tus casos funcionando.', 1, 'proyecto'),
    MOD('Skills y Claude en tus apps', 'Instrucciones que se reutilizan',
        ['Las tareas que repites pasan a ser skills: instrucciones que Claude usa siempre que las necesita',
         'Claude dentro de Excel, Word y tu correo'],
        'tus skills creadas.', 2, 'skills'),
    MOD('Automatizaciones y Claude en Chrome', 'Que las tareas se hagan solas',
        ['Tareas programadas: por ejemplo, un resumen que se prepara solo cada lunes', 'Claude trabajando en webs por ti, desde el navegador',
         'Qué merece la pena automatizar y qué no'],
        'una tarea programada funcionando.', 2, 'auto'),
    MOD('Proyecto práctico corregido', 'Con tu caso',
        ['Conviertes tus tareas repetidas en skills y dejas una automatizada', 'Lo entregas en el campus y una formadora te lo corrige'],
        'tu primer proyecto corregido.', 2, 'revision'),
    MOD('Artefactos y miniaplicaciones', 'Tus propias herramientas',
        ['Documentos y visuales al momento', 'Pequeñas herramientas: una calculadora de presupuestos, un formulario o un panel a partir de un Excel',
         'Cómo compartirlas con quien trabaja contigo'],
        'una miniaplicación hecha a tu medida.', 3, 'miniapp'),
    MOD('Agentes', 'Todas las piezas juntas',
        ['Tu proyecto del nivel 1 evoluciona a agente', 'Instrucciones, skills, conectores y tareas programadas trabajando juntos',
         'Un agente que hace un trabajo de principio a fin'],
        'tu agente diseñado.', 3, 'agente'),
    MOD('Proyecto final corregido', 'Tu agente en marcha',
        ['Pones tu agente a trabajar en un proceso real tuyo', 'Lo entregas y una formadora te lo corrige'],
        'tu segundo proyecto corregido y tu agente en uso.', 3, 'cohete'),
]

PART = {
    'claude-esencial': dict(
        nivel=1, h1='Claude Esencial', sub='Empieza a usar Claude en tu trabajo desde el primer día',
        lead='Pasa de hacerle preguntas sueltas a Claude a tenerlo configurado y trabajando con tus documentos.',
        intro='Cuatro módulos en vídeo con ejercicios sobre tus propios archivos. Acabas con un proyecto con tus casos funcionando y un certificado alineado con el artículo 4 del Reglamento Europeo de IA.',
        chips=['A tu ritmo', '12 meses de acceso', 'Cuenta gratuita de Claude', 'Certificado AI Act art. 4'],
        para=[('i-compass', 'Si empiezas con Claude', 'O lo usas de vez en cuando y quieres sacarle partido de verdad.'),
              ('i-doc', 'Si trabajas con documentos', 'Correos, informes, presupuestos o propuestas que escribes cada semana.'),
              ('i-shield', 'Si necesitas acreditarlo', 'Incluye el bloque de IA segura y legal del artículo 4 del AI Act.')],
        logros=[('chat', 'Pedir las cosas bien', 'Escribes instrucciones claras y Claude responde bien a la primera, sin dar vueltas.'),
                ('proyecto', 'Un proyecto con tu contexto', 'Tus archivos, tus instrucciones y tus casos en un solo sitio, siempre a mano.'),
                ('escudo', 'Usarlo con seguridad', 'Sabes qué datos puedes compartir y cómo revisar lo que te devuelve.')],
        ejemplo=dict(titulo='Un proyecto «Presupuestos» que conoce tus precios',
                     pide='Prepárame el presupuesto para la reforma de la cocina de la señora Puig, con la tarifa de este año.',
                     responde='Hecho. He usado tu tarifa 2026 y tu plantilla. Total: 4.380 € + IVA. He marcado en amarillo dos partidas que no estaban en la tarifa para que las revises.',
                     nota='Lo montas en el módulo 4 con tus propios archivos.'),
        sale='Claude configurado, un proyecto con tus casos funcionando y la formación del artículo 4 hecha.',
        faq_extra=[('¿Qué cuenta de Claude necesito?', 'Te vale la cuenta gratuita de Claude para hacer el curso. Si después quieres pasar al nivel 2, ahí sí necesitarás Claude Pro.')],
        desc='Curso de Claude para particulares: aprende a usar Claude en tu trabajo a tu ritmo, con certificado verificable alineado con el artículo 4 del AI Act. 119 € o 3 plazos sin intereses.'),
    'claude-avanzado': dict(
        nivel=2, h1='Claude Avanzado', sub='Que Claude te haga tareas enteras',
        lead='Todo el nivel 1 y, además, las funciones que te ahorran horas cada semana.',
        intro='Skills, Claude dentro de Excel, Word y tu correo, y tareas que se hacen solas. Con 2 horas de mentoría 1 a 1 y un proyecto que te corrige una formadora.',
        chips=['Incluye el nivel 1', '2 h de mentoría 1 a 1', 'Proyecto corregido', 'Certificado AI Act art. 4'],
        para=[('i-refresh', 'Si repites las mismas tareas', 'Correos, informes o documentos que haces igual cada semana.'),
              ('i-bolt', 'Si quieres automatizar', 'Sin programar y con las herramientas que ya usas.'),
              ('i-users', 'Si quieres a alguien al lado', 'Una formadora que revisa tu caso y te desbloquea.')],
        logros=[('skills', 'Tus tareas, en skills', 'Lo que repites se convierte en instrucciones que Claude reutiliza siempre.'),
                ('auto', 'Tareas que se hacen solas', 'Un resumen, un informe o un seguimiento que se prepara sin que lo pidas.'),
                ('mentoria', 'Una formadora a tu lado', '2 horas de mentoría para revisar tu caso y tu proyecto.')],
        ejemplo=dict(titulo='El resumen del lunes, preparado solo',
                     pide='Cada lunes a las 8:00, revisa mi correo y mi calendario de la semana y prepárame un resumen con lo urgente.',
                     responde='Tarea programada. Lunes 8:00: 3 correos esperan tu respuesta, 2 reuniones nuevas y una entrega el jueves. Te dejo los borradores de respuesta listos.',
                     nota='Lo montas en el módulo 6 y lo revisas con tu formadora.'),
        sale='Tus skills, una tarea automatizada funcionando y tu proyecto corregido.',
        faq_extra=[('¿Qué cuenta de Claude necesito?', 'Claude Pro, que no está incluida en el precio. Trabajamos con proyectos, conectores, skills y tareas programadas, que necesitan la versión de pago.'),
                   ('¿Cómo funciona la mentoría?', 'Tienes 2 horas de mentoría individual por videollamada. Las reservas desde el campus cuando quieras durante los 12 meses: todas juntas o en sesiones de 30 minutos o de 1 hora.')],
        desc='Curso Claude Avanzado para particulares: skills, Claude en Excel, Word y correo y automatizaciones, con 2 h de mentoría 1 a 1 y certificado alineado con el AI Act. 449 € o 3 plazos.'),
    'claude-completo': dict(
        nivel=3, h1='Claude Completo', sub='De cero a tu propio agente funcionando',
        lead='El curso completo: la base bien hecha, las automatizaciones y tus propias herramientas y agentes.',
        intro='Incluye los niveles 1 y 2 y, además, artefactos, miniaplicaciones y agentes. Con 3 horas de mentoría 1 a 1 y dos proyectos corregidos.',
        chips=['Incluye los niveles 1 y 2', '3 h de mentoría 1 a 1', 'Dos proyectos corregidos', 'Certificado AI Act art. 4'],
        para=[('i-robot', 'Si quieres montar un agente', 'Que haga un proceso de tu trabajo de principio a fin.'),
              ('i-tools', 'Si quieres tus propias herramientas', 'Miniaplicaciones hechas a tu medida, sin programar.'),
              ('i-rocket', 'Si quieres dominar Claude', 'Todo el recorrido en un solo curso y con acompañamiento.')],
        logros=[('miniapp', 'Tus propias herramientas', 'Una calculadora, un formulario o un panel hechos con Claude a tu medida.'),
                ('agente', 'Tu agente trabajando', 'Instrucciones, skills, conectores y tareas juntos en un proceso real.'),
                ('mentoria', 'Acompañamiento de principio a fin', '3 horas de mentoría y dos proyectos corregidos.')],
        ejemplo=dict(titulo='Un agente que prepara tus propuestas',
                     pide='Ha entrado una petición nueva en el formulario. Prepara la propuesta.',
                     responde='He leído la petición, he calculado el precio con tu calculadora, he redactado la propuesta con tu plantilla y te la he dejado en borradores para que la revises y la envíes.',
                     nota='Lo montas en los módulos 8 a 10 y te lo corrige tu formadora.'),
        sale='Una miniaplicación propia, un agente funcionando en un proceso real y dos proyectos corregidos.',
        faq_extra=[('¿Qué cuenta de Claude necesito?', 'Claude Pro, que no está incluida en el precio. Para los niveles 2 y 3 trabajamos con funciones que necesitan la versión de pago.'),
                   ('¿Cómo funciona la mentoría?', 'Tienes 3 horas de mentoría individual por videollamada. Las reservas desde el campus cuando quieras durante los 12 meses: todas juntas o en sesiones de 30 minutos o de 1 hora.'),
                   ('¿Tengo que saber programar?', 'No. Las miniaplicaciones y los agentes se montan con Claude, describiendo lo que quieres. Te enseñamos a pedirlo y a revisarlo.')],
        desc='Curso Claude Completo para particulares: de cero a tu propio agente, con miniaplicaciones, 3 h de mentoría 1 a 1, dos proyectos corregidos y certificado alineado con el AI Act. 649 €.'),
}

# Preguntas comunes a las tres páginas de curso
FAQ_COMUN = [
    ('¿Cuándo empiezo?', 'El mismo día. Al pagar te llega el acceso al campus y empiezas cuando quieras. Tienes 12 meses para hacerlo a tu ritmo.'),
    ('¿Cómo funciona el pago en 3 plazos?', 'Al pagar eliges la opción de 3 plazos. Pagas una parte en el momento y el resto en los dos meses siguientes, sin intereses. Tienes el curso completo desde el primer día.'),
    ('¿Tengo un código de descuento, dónde lo pongo?', 'En el campo «¿Tienes un código de descuento?» de esta página, antes de pulsar «Comprar», o dentro del formulario de pago, en «Añadir código promocional». Ves el precio rebajado antes de pagar.'),
    ('¿Puedo empezar por un nivel y subir después?', 'Sí. Cada nivel incluye el anterior y, si subes, pagas solo la diferencia. No repites lo que ya has hecho.'),
    ('¿El certificado es oficial?', 'Es un certificado de formación de Westlabs, nominativo y verificable con QR, alineado con el artículo 4 del Reglamento Europeo de IA. No es un título oficial ni homologado.'),
]

# Pasos del cómo funciona (página particulares/como-funciona.html)
PASOS = [
    ('i-target', 'Eliges tu nivel', 'Entras en la página del curso y lo pagas online, de una vez o en 3 plazos.'),
    ('i-laptop', 'Entras en el campus', 'Te llega el acceso y empiezas el mismo día, desde el ordenador o el móvil.'),
    ('i-video', 'Vídeos y ejercicios', 'Vídeos cortos y ejercicios con tus propios documentos, módulo a módulo.'),
    ('i-users', 'Mentoría 1 a 1', 'En los niveles 2 y 3 reservas tu mentoría cuando la necesitas.'),
    ('i-shield', 'Te certificas', 'Entregas tu proyecto o haces el test final y descargas tu certificado.'),
]

# Clave publicable de Stripe (pk_live_... o pk_test_...). Es pública por diseño.
# Mientras esté vacía, «Comprar» lleva al formulario de reserva de la propia página del curso.
STRIPE_PK = ''
