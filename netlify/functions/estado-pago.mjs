// Devuelve el estado de una sesión de pago para la página gracias.html.
import { stripe, json } from '../lib/stripe.mjs';

const NOMBRES = { 'claude-esencial': 'Claude Esencial', 'claude-avanzado': 'Claude Avanzado', 'claude-completo': 'Claude Completo' };

export default async (req) => {
  const id = new URL(req.url).searchParams.get('session_id') || '';
  if (!/^cs_[A-Za-z0-9_]+$/.test(id)) return json({ error: 'Sesión no válida' }, 400);
  try {
    const s = await stripe('checkout/sessions/' + id, null, 'GET');
    return json({ estado: s.status, pago: s.payment_status, email: s.customer_details?.email || '', curso: NOMBRES[s.metadata?.curso] || '' });
  } catch (e) {
    console.error('estado-pago', e.message);
    return json({ error: 'No hemos podido comprobar el pago' }, 400);
  }
};
