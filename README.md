# Web de Westlabs AI School

Web de la escuela de formación en IA de Westlabs: portada con el catálogo, una ficha por curso y las páginas legales.

## Qué hay en el repositorio

| Archivo o carpeta | Qué es |
|---|---|
| `index.html` | Portada con el catálogo de cursos (estilos y código dentro del propio archivo) |
| `contacto.html` | Formulario para empresas (propuesta) con el curso preelegido |
| `particulares.html` | Packs de teleformación para particulares (precio de lanzamiento hasta el 31 de enero: Esencial 79 €, Profesional 299 €, Completo 449 €; precio normal 119, 449 y 649 €) con mentoría y pago en 3 plazos |
| `cursos/` | Una ficha por cada curso de la portada (19). **Se generan solas**: no se editan a mano |
| `generador/` | Datos de los cursos (`datos.py`), plantilla de la ficha (`generar.py`) y partes comunes de las fichas (`parciales/`) |
| `MAPA-WEB.md` | Mapa de todas las páginas y sus conexiones (se genera solo) |
| `aviso-legal.html`, `privacidad.html`, `cookies.html` | Páginas legales |
| `assets/css/base.css` | Estilos comunes de toda la web |
| `assets/css/curso.css` | Estilos de las fichas de curso |
| `assets/css/legal.css` | Estilos de las páginas legales |
| `assets/js/curso.js` | Menú, pestañas, formularios y animaciones de las fichas, el contacto y las páginas legales |
| `datos/convocatorias-westlabs.xlsx` | Plantilla de la hoja de convocatorias (la que se usa de verdad está en Google Sheets) |
| `assets/` (resto) | Logos, fotos, fondos, iconos 3D y tipografías |

## Cómo se publica

- **Rama `main` = la web de verdad.** Lo que está en `main` es lo que ve todo el mundo.
- **Ramas de trabajo = pruebas.** Los cambios se hacen siempre en una rama aparte, nunca directamente en `main`.
- **Netlify** está conectado al repositorio: publica `main` en el dominio y crea un enlace de prueba para cada pull request.

### Para hacer un cambio

1. Pide el cambio a Claude (o hazlo tú) en una **rama de trabajo**.
2. Se abre una **pull request** en GitHub hacia `main`.
3. Netlify comenta en la pull request un **enlace de prueba** con el cambio. Revísalo ahí, en ordenador y en móvil.
4. Si está bien, pulsa **Merge** en GitHub. En uno o dos minutos la web publicada se actualiza sola.
5. Si algo sale mal después de publicar, en Netlify (Deploys) puedes volver a la versión anterior con un clic.

### Configuración de Netlify (se hace una vez)

1. Entra en netlify.com con tu cuenta de GitHub.
2. **Add new site → Import an existing project → GitHub** y elige este repositorio.
3. Rama a publicar: `main`. Sin comando de build. Carpeta a publicar: la raíz.
4. En **Domain settings**, conecta el dominio de la escuela.
5. Comprueba que **Deploy Previews** está activado para las pull requests.

## Formularios (Web3Forms)

- Las fichas de curso tienen dos formularios, **Empresas** y **Particulares**. Al enviarlos, Web3Forms manda un correo con todos los datos.
- La clave de Web3Forms está en cada formulario (`access_key`). Es pública por diseño, no es un secreto.
- Asunto del correo: «Propuesta para empresa · [curso]» o «Matrícula de particular · [curso]».
- Las pruebas de envío hay que hacerlas en la web publicada o en el enlace de prueba de Netlify. Desde una vista previa de claude.ai el envío puede no salir.
- Plan gratuito: revisa los límites de envíos al mes en web3forms.com/pricing.

## Convocatorias (Google Sheets)

- El panel «Próximas convocatorias» de la portada lee la hoja **Convocatorias Westlabs** de Google Drive (pestaña «Convocatorias»).
- El enlace está en `index.html`, en la constante `CONVOCATORIAS_CSV`.
- Para que la web pueda leerla, la hoja tiene que estar compartida como «Cualquier persona con el enlace: lector» o publicada en la web como CSV.
- Si la hoja no carga, se ve la lista escrita en la página.
- Estados: Abierta, Últimas plazas y Completa se muestran; Por confirmar sale como «Fechas por confirmar»; Oculta no sale.
- La columna «Notas internas» no se muestra en la web, pero cualquiera con el enlace puede ver la hoja.

## Menú, pie y enlaces

- El menú y el pie son iguales en todas las páginas. Si se cambia uno, hay que cambiarlo en `index.html`, `contacto.html`, las tres páginas legales y, para las fichas, en `generador/parciales/cabecera.html` y `pie.html` (y después generar).
- Los enlaces del menú a una herramienta usan `index.html?h=claude#oferta` (también `general`, `chatgpt`, `microsoft` y `gemini`): abren la portada con esa pestaña del catálogo.
- Todas las tarjetas de curso enlazan a su ficha en `cursos/` (lista `FICHAS` en `index.html`, que ahora incluye todos los cursos). `contacto.html?curso=Nombre del curso` sigue funcionando y deja el curso ya elegido en el formulario.
- «Empresas» lleva a la sección de empresas de la portada (`index.html#empresas`).
- Campus: https://westlabscampus.es/login · WhatsApp y teléfono de Gerard: 636 875 779.

## Oferta: empresas y particulares

- **Empresas:** solo en directo. «Solo tu equipo» (online o presencial, precio por grupo) o «Aula síncrona» (online, alumnos de varias empresas, precio por alumno sin IVA: 190 € nivel 1 y Alfabetización, 390 € nivel 2, 490 € nivel 3). Precios en `generador/datos.py` (`AULA` y `AULA_NIVEL`).
- **Particulares:** solo teleformación en el campus, con packs en `particulares.html`: Esencial 79 € (normal 119 €, Ready, sin mentoría), Profesional 299 € (normal 449 €, Build + 2 h de mentoría) y Completo 449 € (normal 649 €, Agents + 3 h de mentoría). Mentoría 1 a 1 reservable cuando quieran durante los 12 meses.

## Pagos (Stripe)

- **Pago en 3 plazos:** en Stripe, activa Klarna en Ajustes → Métodos de pago y márcalo en cada enlace de pago. El cliente elige pagar en 3 plazos sin intereses y Westlabs cobra el total de una vez (menos la comisión de Klarna).
- Para particulares se usa un **enlace de pago de Stripe** (`https://buy.stripe.com/...`) en el botón «Matricúlate». No hay plataforma de pago propia.
- Cada curso con precio tiene su producto y su enlace en Stripe.
- Antes de activar los enlaces reales, prueba el pago con el **modo de prueba** de Stripe.
- Pendiente: confirmar con Santi si los precios llevan el 21 % de IVA.

## Fichas de curso

Las 19 fichas de `cursos/` salen de una plantilla única y de un archivo de datos: todas tienen la misma estructura que la de Alfabetización en IA y se cambian a la vez.

- **Cambiar un texto, unas horas, un temario o un precio:** en `generador/datos.py`.
- **Cambiar la estructura de la ficha** (secciones y orden): en `generador/generar.py`.
- **Cambiar la cabecera, el pie o los iconos de las fichas:** en `generador/parciales/`.
- **Cambiar el diseño:** en `assets/css/curso.css`.

Después de cualquier cambio en `generador/`, vuelve a crear las fichas:

```
python3 generador/generar.py
```

Esto sobrescribe todas las fichas de `cursos/` y actualiza `MAPA-WEB.md`. No edites a mano los HTML de `cursos/`: el cambio se perdería la próxima vez que se generen.

**Curso nuevo:** añade un bloque `add(...)` en `generador/datos.py` (copia uno parecido), genera, y añade el curso a la lista `CURSOS` del `<script>` de `index.html` con el mismo nombre.

### Cursos del catálogo

- **Formación general:** Alfabetización en IA, Prompting eficaz, Investigación y análisis con IA, Documentos y presentaciones con IA, IA para dirección, IA y cumplimiento normativo.
- **Por herramienta**: los tres niveles siguen la estructura del documento «Formación in-company» (Ready, Build y Agents). Cada nivel incluye el anterior:
  - Nivel 1 · Ready · 8 h: Introducción a la IA, Conocemos la herramienta, IA segura y legal, Cómo la usamos.
  - Nivel 2 · Build · 17 h por persona: + instrucciones reutilizables y la IA en tus apps, automatizaciones, 2 talleres por área de 1,5 h y sesión de cierre.
  - Nivel 3 · Agents · 22,5 h por persona: + artefactos y mini aplicaciones, agentes avanzados, taller 3 y sesión de cierre (en empresa, también 1 h con dirección).
  - Claude: Claude Esencial, Claude Avanzado, Claude Completo.
  - ChatGPT: Fundamentos de ChatGPT, ChatGPT en profundidad, ChatGPT de cero a experto.
  - Microsoft: Microsoft 365 Copilot desde cero, Copilot en tus apps de Microsoft 365, Microsoft 365 Copilot completo, y Copilot Studio como complemento.
  - Gemini: Introducción a Gemini, Gemini práctico, Gemini completo.
- Los cursos especializados (por área, administración de la herramienta, Claude Code) están fuera por ahora.

El contenido de cada curso sale del documento «Westlabs: catálogo de cursos de IA y fichas para la web».

## Cómo hablamos de los cursos

Del catálogo, para que todas las páginas digan lo mismo:

| Decimos | No decimos |
|---|---|
| Certificado nominativo y verificable | Certificado oficial u homologado |
| Alineado con el artículo 4 del Reglamento Europeo de IA | Formación obligatoria o «evita multas» |
| Sirve como prueba de formación en IA | Con este curso cumples la ley |
| Modelo y programa protocolizados ante notario | Avalado por un notario o por la UE |
| El mismo programa que damos a empresas | Precio tachado o plazas limitadas |

## Pendiente

- [ ] Crear la rama `main` y conectar Netlify
- [ ] Probar un envío real de los formularios en la web publicada
- [ ] Enlaces de pago de Stripe para los tres packs, con «Permitir códigos promocionales» activado y Klarna para los 3 plazos
- [ ] Precio por persona de la modalidad online en directo (ahora sale «por confirmar»)
- [ ] Revisar los temarios de los cursos nuevos de formación general (Prompting eficaz, Investigación y análisis, Documentos y presentaciones, IA y cumplimiento normativo): no están en el catálogo en PDF
- [ ] Campus de ChatGPT, Microsoft y Gemini (niveles 1 y 2): la portada los marca con campus; las fichas dicen «próximamente»
- [ ] Revisión de las páginas legales por el abogado
- [ ] Tipografía AllRoundGothic en `assets/fonts/` (ahora los títulos salen en Poppins)
- [ ] Página propia de empresas (ahora el menú lleva a la sección de empresas de la portada)
- [ ] Compartir o publicar la hoja de convocatorias para que la web pueda leerla
- [ ] Enlace de la agenda de citas de Google Calendar para «Solicita propuesta»

## Códigos de descuento y fin de la oferta de lanzamiento

- **Códigos:** en Stripe, crea un cupón (Productos → Cupones) y uno o varios códigos promocionales asociados. En cada enlace de pago marca «Permitir códigos promocionales». El cliente escribe el código en la página de pago y ve el total antes de pagar; funciona también con Klarna en 3 plazos.
- **Fin de la oferta (31 de enero):** cambia el precio de los enlaces de pago en Stripe, y en la web: `generador/datos.py` (`precio` = valor de `antes`, `plazo` = nuevo tercio, `LANZAMIENTO = ''`), `particulares.html` (precios, plazos, banda y desplegable) e `index.html` («Desde 79 €»). Después ejecuta `python3 generador/generar.py`.
