// Crea una sesión de Stripe Checkout incrustada (ui_mode: embedded) para un curso de particulares.
// Variables de entorno en Netlify:
//   STRIPE_SECRET_KEY                      clave secreta (sk_live_... o sk_test_...)
//   STRIPE_PRICE_CLAUDE_ESENCIAL           ID del precio en Stripe (price_...)
//   STRIPE_PRICE_CLAUDE_AVANZADO
//   STRIPE_PRICE_CLAUDE_COMPLETO
import { stripe, json } from '../lib/stripe.mjs';

const PRECIOS = {
  'claude-esencial': 'STRIPE_PRICE_CLAUDE_ESENCIAL',
  'claude-avanzado': 'STRIPE_PRICE_CLAUDE_AVANZADO',
  'claude-completo': 'STRIPE_PRICE_CLAUDE_COMPLETO',
};

export default async (req) => {
  if (req.method !== 'POST') return json({ error: 'Método no permitido' }, 405);
  const { curso, codigo } = await req.json().catch(() => ({}));
  const precio = PRECIOS[curso] && process.env[PRECIOS[curso]];
  if (!precio) return json({ error: 'Este curso todavía no se puede pagar online. Escríbenos y te ayudamos.' }, 400);

  const base = process.env.URL || new URL(req.url).origin;
  const p = {
    mode: 'payment',
    ui_mode: 'embedded',
    locale: 'es',
    'line_items[0][price]': precio,
    'line_items[0][quantity]': '1',
    return_url: `${base}/gracias.html?session_id={CHECKOUT_SESSION_ID}`,
    'phone_number_collection[enabled]': 'true',
    'metadata[curso]': curso,
  };

  const cod = String(codigo || '').trim();
  try {
    if (cod) {
      // Código escrito en la web: lo buscamos y lo aplicamos ya, así el formulario sale con el precio rebajado.
      const l = await stripe('promotion_codes', { code: cod, active: 'true', limit: '1' }, 'GET');
      if (!l.data?.length) return json({ error: 'Este código no existe o ya no es válido.', codigo: true }, 400);
      p['discounts[0][promotion_code]'] = l.data[0].id;
    } else {
      // Sin código: el cliente puede añadirlo dentro del formulario de pago.
      p.allow_promotion_codes = 'true';
    }
    const s = await stripe('checkout/sessions', p);
    return json({ clientSecret: s.client_secret });
  } catch (e) {
    const msg = e.stripe?.code === 'coupon_expired' || /promotion|coupon/i.test(e.message)
      ? 'Este código no se puede aplicar a este curso.' : 'No hemos podido abrir el pago. Prueba de nuevo en un momento.';
    console.error('crear-pago', e.message);
    return json({ error: msg, codigo: /promotion|coupon/i.test(e.message) }, 400);
  }
};
