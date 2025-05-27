const API_URL = 'http://localhost:8000/plan-trip'

export async function planTrip({ destination, start_date, end_date, interests }) {
  const response = await fetch(API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      destination,
      start_date,
      end_date,
      interests
    }),
  })

  if (!response.ok) {
    throw new Error('Erro ao buscar plano de viagem')
  }

  return await response.json()
}
