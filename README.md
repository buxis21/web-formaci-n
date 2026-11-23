# Web de Westlabs AI School

Web de la escuela de formación en IA de Westlabs: portada con el catálogo, una ficha por curso y las páginas legales.

## Qué hay en el repositorio

| Archivo o carpeta | Qué es |
|---|---|
| `index.html` | Portada con el catálogo de cursos |
| `cursos/` | Una página por curso (por ahora, `alfabetizacion-en-ia.html`) |
| `aviso-legal.html`, `privacidad.html`, `cookies.html` | Páginas legales |
| `assets/css/base.css` | Estilos comunes de toda la web |
| `assets/css/curso.css` | Estilos de las fichas de curso |
| `assets/css/legal.css` | Estilos de las páginas legales |
| `assets/js/curso.js` | Menú, pestañas, formularios y animaciones de las fichas y las páginas legales |
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

## Pagos (Stripe)

- Para particulares se usa un **enlace de pago de Stripe** (`https://buy.stripe.com/...`) en el botón «Matricúlate». No hay plataforma de pago propia.
- Cada curso con precio tiene su producto y su enlace en Stripe.
- Antes de activar los enlaces reales, prueba el pago con el **modo de prueba** de Stripe.
- Pendiente: confirmar con Santi si los precios llevan el 21 % de IVA.

## Crear una ficha de curso nueva

1. Copia `cursos/alfabetizacion-en-ia.html` con el nombre del curso (el nombre del archivo sale del nombre del curso, en minúsculas y con guiones, por ejemplo `claude-esencial.html`).
2. Cambia los textos: título, datos del curso, temario, modalidades, precio y preguntas frecuentes.
3. Cambia el asunto de los dos formularios (`subject`) y `data-curso` en `<body>`.
4. Si el curso tiene precio para particulares, pon su enlace de Stripe.

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
- [ ] Enlace de pago de Stripe para Ready (119 €) en el botón «Matricúlate»
- [ ] Revisión de las páginas legales por el abogado
- [ ] Tipografía AllRoundGothic en `assets/fonts/` (ahora los títulos salen en Poppins)
- [ ] Páginas `contacto.html` y `empresas.html`
- [ ] Confirmar enlaces: campus.westlabs.es, westlabs.es, LinkedIn y el email y teléfono de contacto
- [ ] Fichas del resto de cursos
