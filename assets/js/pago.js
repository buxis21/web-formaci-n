/* Pago con Stripe dentro de la web (Embedded Checkout).
   Configuración: pon la clave publicable de Stripe (pk_live_... o pk_test_...) en
   <body data-stripe-pk="..."> de particulares.html. Mientras esté vacía, «Comprar»
   lleva al formulario de reserva, como hasta ahora. */
(function () {
  const pk = document.body.dataset.stripePk || '';
  const dlg = document.getElementById('pago');
  const caja = document.getElementById('pago-form');
  const aviso = document.getElementById('pago-aviso');
  const titulo = document.getElementById('pago-titulo');
  const campoCod = document.getElementById('cod-desc');
  const FN = '/.netlify/functions/crear-pago';
  let stripe = null, checkout = null, ultimo = null;

  function cargarStripe() {
    if (window.Stripe) return Promise.resolve(window.Stripe(pk));
    return new Promise((ok, mal) => {
      const s = document.createElement('script');
      s.src = 'https://js.stripe.com/v3/';
      s.onload = () => ok(window.Stripe(pk));
      s.onerror = () => mal(new Error('No se ha podido cargar Stripe'));
      document.head.appendChild(s);
    });
  }

  function mostrarAviso(txt, conBotonSinCodigo) {
    aviso.hidden = false;
    aviso.innerHTML = '';
    const p = document.createElement('p'); p.textContent = txt; aviso.appendChild(p);
    if (conBotonSinCodigo) {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'btn btn-primario'; b.textContent = 'Seguir sin código';
      b.addEventListener('click', () => { campoCod.value = ''; abrir(ultimo.curso, ultimo.nombre, ''); });
      aviso.appendChild(b);
    }
  }

  async function cerrarCheckout() {
    if (checkout) { try { checkout.destroy(); } catch (e) {} checkout = null; }
    caja.innerHTML = '';
  }

  async function abrir(curso, nombre, codigo) {
    ultimo = { curso, nombre };
    await cerrarCheckout();
    titulo.textContent = nombre;
    aviso.hidden = true;
    caja.innerHTML = '<p class="pago-cargando">Cargando el pago seguro…</p>';
    if (!dlg.open) dlg.showModal();
    try {
      const [st, r] = await Promise.all([
        stripe || cargarStripe(),
        fetch(FN, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ curso, codigo }) }),
      ]);
      stripe = st;
      const d = await r.json().catch(() => ({}));
      if (!r.ok || !d.clientSecret) { caja.innerHTML = ''; mostrarAviso(d.error || 'No hemos podido abrir el pago. Prueba de nuevo en un momento.', d.codigo); return; }
      caja.innerHTML = '';
      checkout = await stripe.initEmbeddedCheckout({ fetchClientSecret: async () => d.clientSecret });
      checkout.mount('#pago-form');
    } catch (e) {
      caja.innerHTML = '';
      mostrarAviso('No hemos podido abrir el pago. Revisa tu conexión o escríbenos y te ayudamos.');
    }
  }

  document.querySelectorAll('[data-pack]').forEach(a => a.addEventListener('click', ev => {
    const cod = (campoCod.value || '').trim();
    if (pk && a.dataset.curso) {
      ev.preventDefault();
      abrir(a.dataset.curso, a.dataset.pack, cod);
      return;
    }
    // Sin Stripe configurado: deja el curso y el código en el formulario de reserva.
    const s = document.getElementById('r-pack');
    [...s.options].forEach(o => { if (o.text.startsWith(a.dataset.pack)) s.value = o.value; });
    if (cod) document.getElementById('r-codigo').value = cod;
  }));

  document.getElementById('pago-cerrar').addEventListener('click', () => dlg.close());
  dlg.addEventListener('close', cerrarCheckout);
  dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });

  // Desde las fichas: particulares.html?comprar=claude-avanzado abre directamente el pago.
  const q = new URLSearchParams(location.search).get('comprar');
  const btn = q && document.querySelector(`[data-curso="${CSS.escape(q)}"]`);
  if (btn && pk) btn.click();
})();
