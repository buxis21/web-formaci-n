# Mapa de la web

Se genera solo con `python3 generador/generar.py`. Lista todas las páginas, qué hay en cada una y a dónde enlazan.

## Páginas generales

| Página | Archivo | Qué es |
|---|---|---|
| Portada | [`index.html`](index.html) | Catálogo en dos pestañas (Formación general y Por herramienta). Cada tarjeta enlaza a su ficha en `cursos/` |
| Contacto | [`contacto.html`](contacto.html) | Formulario de contacto. Recibe `?curso=` desde la portada |
| Aviso legal | [`aviso-legal.html`](aviso-legal.html) | Datos de Westlabs SCP y condiciones de uso |
| Política de privacidad | [`privacidad.html`](privacidad.html) | Datos de los formularios, finalidades y derechos |
| Política de cookies | [`cookies.html`](cookies.html) | Sin cookies de análisis ni publicidad |

## Fichas de curso

19 fichas en `cursos/`, una por cada tarjeta de la portada. Todas tienen el formulario de empresas (Web3Forms); las que tienen directo o campus, también el de particulares.

### Formación general

| Curso | Archivo | Horas | Directo | Presencial | Campus | Particulares | Siguiente paso |
|---|---|---|---|---|---|---|---|
| Alfabetización en IA | [`cursos/alfabetizacion-en-ia.html`](cursos/alfabetizacion-en-ia.html) | 8 h | ✓ | ✓ | 10 h | Pack Esencial 79 € (Stripe pendiente) | [Claude Esencial](cursos/claude-esencial.html), [Fundamentos de ChatGPT](cursos/fundamentos-de-chatgpt.html), [Microsoft 365 Copilot desde cero](cursos/microsoft-365-copilot-desde-cero.html), [Prompting eficaz](cursos/prompting-eficaz.html) |
| Prompting eficaz | [`cursos/prompting-eficaz.html`](cursos/prompting-eficaz.html) | 4 h | ✓ | ✓ | 4 h | Aviso de fechas o de campus | [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html), [Alfabetización en IA](cursos/alfabetizacion-en-ia.html), [Claude Esencial](cursos/claude-esencial.html) |
| Investigación y análisis con IA | [`cursos/investigacion-y-analisis-con-ia.html`](cursos/investigacion-y-analisis-con-ia.html) | 4 h | ✓ | ✓ | — | Aviso de fechas o de campus | [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html), [Prompting eficaz](cursos/prompting-eficaz.html), [Claude Avanzado](cursos/claude-avanzado.html), [ChatGPT en profundidad](cursos/chatgpt-en-profundidad.html) |
| Documentos y presentaciones con IA | [`cursos/documentos-y-presentaciones-con-ia.html`](cursos/documentos-y-presentaciones-con-ia.html) | 4 h | ✓ | ✓ | — | Aviso de fechas o de campus | [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html), [Prompting eficaz](cursos/prompting-eficaz.html), [Copilot en tus apps de Microsoft 365](cursos/copilot-en-tus-apps-de-microsoft-365.html), [Claude Avanzado](cursos/claude-avanzado.html) |
| IA para dirección | [`cursos/ia-para-direccion.html`](cursos/ia-para-direccion.html) | 8 h | — | ✓ | — | — | [IA y cumplimiento normativo](cursos/ia-y-cumplimiento-normativo.html), [Alfabetización en IA](cursos/alfabetizacion-en-ia.html), [Prompting eficaz](cursos/prompting-eficaz.html), [Claude Esencial](cursos/claude-esencial.html) |
| IA y cumplimiento normativo | [`cursos/ia-y-cumplimiento-normativo.html`](cursos/ia-y-cumplimiento-normativo.html) | 8 h | ✓ | ✓ | — | Aviso de fechas o de campus | [IA para dirección](cursos/ia-para-direccion.html), [Alfabetización en IA](cursos/alfabetizacion-en-ia.html), [Prompting eficaz](cursos/prompting-eficaz.html), [Claude Esencial](cursos/claude-esencial.html) |

### Por herramienta

| Curso | Archivo | Horas | Directo | Presencial | Campus | Particulares | Siguiente paso |
|---|---|---|---|---|---|---|---|
| Claude Esencial (Claude, nivel 1) | [`cursos/claude-esencial.html`](cursos/claude-esencial.html) | 8 h | ✓ | ✓ | Dentro de Build · 25 h | Pack Profesional 299 € (Stripe pendiente) | [Claude Avanzado](cursos/claude-avanzado.html), [Claude Completo](cursos/claude-completo.html), [Prompting eficaz](cursos/prompting-eficaz.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html) |
| Claude Avanzado (Claude, nivel 2) | [`cursos/claude-avanzado.html`](cursos/claude-avanzado.html) | 17 h | ✓ | ✓ | Dentro de Build · 25 h | Pack Profesional 299 € (Stripe pendiente) | [Claude Completo](cursos/claude-completo.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html), [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html), [Prompting eficaz](cursos/prompting-eficaz.html) |
| Claude Completo (Claude, nivel 3) | [`cursos/claude-completo.html`](cursos/claude-completo.html) | 22,5 h | ✓ | ✓ | — | Aviso de fechas o de campus | [IA para dirección](cursos/ia-para-direccion.html), [IA y cumplimiento normativo](cursos/ia-y-cumplimiento-normativo.html), [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html) |
| Fundamentos de ChatGPT (ChatGPT, nivel 1) | [`cursos/fundamentos-de-chatgpt.html`](cursos/fundamentos-de-chatgpt.html) | 8 h | ✓ | ✓ | Próximamente | Aviso de fechas o de campus | [ChatGPT en profundidad](cursos/chatgpt-en-profundidad.html), [ChatGPT de cero a experto](cursos/chatgpt-de-cero-a-experto.html), [Prompting eficaz](cursos/prompting-eficaz.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html) |
| ChatGPT en profundidad (ChatGPT, nivel 2) | [`cursos/chatgpt-en-profundidad.html`](cursos/chatgpt-en-profundidad.html) | 17 h | ✓ | ✓ | Próximamente | Aviso de fechas o de campus | [ChatGPT de cero a experto](cursos/chatgpt-de-cero-a-experto.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html), [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html), [Prompting eficaz](cursos/prompting-eficaz.html) |
| ChatGPT de cero a experto (ChatGPT, nivel 3) | [`cursos/chatgpt-de-cero-a-experto.html`](cursos/chatgpt-de-cero-a-experto.html) | 22,5 h | ✓ | ✓ | — | Aviso de fechas o de campus | [IA para dirección](cursos/ia-para-direccion.html), [IA y cumplimiento normativo](cursos/ia-y-cumplimiento-normativo.html), [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html) |
| Microsoft 365 Copilot desde cero (Microsoft 365 Copilot, nivel 1) | [`cursos/microsoft-365-copilot-desde-cero.html`](cursos/microsoft-365-copilot-desde-cero.html) | 8 h | ✓ | ✓ | Próximamente | Aviso de fechas o de campus | [Copilot en tus apps de Microsoft 365](cursos/copilot-en-tus-apps-de-microsoft-365.html), [Microsoft 365 Copilot completo](cursos/microsoft-365-copilot-completo.html), [Copilot Studio](cursos/copilot-studio.html), [Prompting eficaz](cursos/prompting-eficaz.html) |
| Copilot en tus apps de Microsoft 365 (Microsoft 365 Copilot, nivel 2) | [`cursos/copilot-en-tus-apps-de-microsoft-365.html`](cursos/copilot-en-tus-apps-de-microsoft-365.html) | 17 h | ✓ | ✓ | Próximamente | Aviso de fechas o de campus | [Microsoft 365 Copilot completo](cursos/microsoft-365-copilot-completo.html), [Copilot Studio](cursos/copilot-studio.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html), [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html) |
| Microsoft 365 Copilot completo (Microsoft 365 Copilot, nivel 3) | [`cursos/microsoft-365-copilot-completo.html`](cursos/microsoft-365-copilot-completo.html) | 22,5 h | ✓ | ✓ | — | Aviso de fechas o de campus | [Copilot Studio](cursos/copilot-studio.html), [IA para dirección](cursos/ia-para-direccion.html), [IA y cumplimiento normativo](cursos/ia-y-cumplimiento-normativo.html), [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html) |
| Introducción a Gemini (Gemini, nivel 1) | [`cursos/introduccion-a-gemini.html`](cursos/introduccion-a-gemini.html) | 8 h | ✓ | ✓ | Próximamente | Aviso de fechas o de campus | [Gemini práctico](cursos/gemini-practico.html), [Gemini completo](cursos/gemini-completo.html), [Prompting eficaz](cursos/prompting-eficaz.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html) |
| Gemini práctico (Gemini, nivel 2) | [`cursos/gemini-practico.html`](cursos/gemini-practico.html) | 17 h | ✓ | ✓ | Próximamente | Aviso de fechas o de campus | [Gemini completo](cursos/gemini-completo.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html), [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html), [Prompting eficaz](cursos/prompting-eficaz.html) |
| Gemini completo (Gemini, nivel 3) | [`cursos/gemini-completo.html`](cursos/gemini-completo.html) | 22,5 h | ✓ | ✓ | — | Aviso de fechas o de campus | [IA para dirección](cursos/ia-para-direccion.html), [IA y cumplimiento normativo](cursos/ia-y-cumplimiento-normativo.html), [Investigación y análisis con IA](cursos/investigacion-y-analisis-con-ia.html), [Documentos y presentaciones con IA](cursos/documentos-y-presentaciones-con-ia.html) |
| Copilot Studio | [`cursos/copilot-studio.html`](cursos/copilot-studio.html) | 12 h | ✓ | ✓ | — | Aviso de fechas o de campus | [Microsoft 365 Copilot completo](cursos/microsoft-365-copilot-completo.html), [Copilot en tus apps de Microsoft 365](cursos/copilot-en-tus-apps-de-microsoft-365.html), [IA y cumplimiento normativo](cursos/ia-y-cumplimiento-normativo.html), [IA para dirección](cursos/ia-para-direccion.html) |

## Conexiones

| Qué | Dónde | Estado |
|---|---|---|
| Formularios de las fichas → correo | Web3Forms, clave en cada formulario. Asunto: «Propuesta para empresa · [curso]» o «Matrícula de particular · [curso]» | Configurado. Falta probar un envío real en la web publicada |
| Convocatorias de la portada | Hoja de Google «Convocatorias» (copia en `datos/convocatorias-westlabs.xlsx`) | Conectado |
| Pago de los packs (Esencial, Profesional y Completo, con códigos de descuento) | Enlaces de pago de Stripe en `generador/datos.py` (`CAMPUS[...]["stripe"]`) | Pendiente |
| Campus | https://westlabscampus.es/login | Conectado |
| WhatsApp de Gerard | https://wa.me/34636875779 | Conectado |
| Publicación | Netlify conectado a la rama `main` | Pendiente |

## Cómo se cambia una ficha

1. Edita `generador/datos.py` (textos, horas, temario, precios) o `generador/generar.py` (estructura de la ficha).
2. Ejecuta `python3 generador/generar.py`: se regeneran todas las fichas de `cursos/` y este mapa.
3. Si cambias el nombre de un curso, cámbialo también en la lista `CURSOS` de `index.html`.
4. El diseño está en `assets/css/base.css` y `assets/css/curso.css`; el comportamiento, en `assets/js/curso.js`.
