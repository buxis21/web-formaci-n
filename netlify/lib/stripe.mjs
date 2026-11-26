// Llamadas a la API de Stripe sin dependencias (fetch de Node 18+).
// La clave secreta va en la variable de entorno STRIPE_SECRET_KEY de Netlify, nunca en el código.
export async function stripe(ruta, params, metodo = 'POST') {
  const clave = process.env.STRIPE_SECRET_KEY;
  if (!clave) throw new Error('Falta STRIPE_SECRET_KEY en Netlify');
  const qs = params ? new URLSearchParams(params).toString() : '';
  const url = 'https://api.stripe.com/v1/' + ruta + (metodo === 'GET' && qs ? '?' + qs : '');
  const r = await fetch(url, {
    method: metodo,
    headers: { Authorization: 'Bearer ' + clave, 'Content-Type': 'application/x-www-form-urlencoded' },
    body: metodo === 'POST' ? qs : undefined,
  });
  const j = await r.json();
  if (!r.ok) throw Object.assign(new Error(j.error?.message || 'Error de Stripe'), { stripe: j.error });
  return j;
}

export const json = (datos, estado = 200) =>
  new Response(JSON.stringify(datos), { status: estado, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });
