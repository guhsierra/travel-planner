<template>
  <div class="container">
    <h1>Planejador de Viagem</h1>

    <div class="inputs">
      <input v-model="destination" placeholder="Destino (ex: Paris)" />
      <input v-model="startDate" type="date" />
      <input v-model="endDate" type="date" />
      <input v-model="interests" placeholder="Interesses (separados por vírgula)" />
    </div>

    <button @click="handleClick" :disabled="loading">
      {{ loading ? 'Carregando...' : 'Planejar viagem' }}
    </button>

    <div v-if="dias.length" class="carousel">
      <div class="navegacao">
        <button @click="anterior" :disabled="diaAtual === 0">◀️</button>
        <span>{{ dias[diaAtual].titulo }}</span>
        <button @click="proximo" :disabled="diaAtual === dias.length - 1">▶️</button>
      </div>

      <div class="dia-html" v-html="dias[diaAtual].html"></div>
    </div>

    <div v-if="error" class="erro">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { planTrip } from './services/travelPlannerService'
import { marked } from 'marked'

const destination = ref('')
const startDate = ref('')
const endDate = ref('')
const interests = ref('')
const error = ref('')
const loading = ref(false)
const dias = ref([])
const diaAtual = ref(0)

const handleClick = async () => {
  loading.value = true
  error.value = ''
  dias.value = []
  diaAtual.value = 0
  try {
    const data = await planTrip({
      destination: destination.value,
      start_date: startDate.value,
      end_date: endDate.value,
      interests: interests.value.split(',').map(i => i.trim()),
    })

    const texto = data.trip_plan.tasks_output?.[0]?.raw || ''
    dias.value = separarPorDias(texto).map(dia => ({
      ...dia,
      html: formatarMarkdown(dia.conteudo),
    }))
  } catch (e) {
    error.value = 'Erro ao buscar plano de viagem.'
    console.error(e)
  } finally {
    loading.value = false
  }
}

const separarPorDias = (texto) => {
  const partes = texto.split(/(\*\*Dia \d+:.*?\*\*)/g).filter(Boolean)
  const resultado = []
  for (let i = 0; i < partes.length; i++) {
    if (partes[i].startsWith('**Dia')) {
      resultado.push({
        titulo: partes[i].replace(/\*\*/g, ''),
        conteudo: partes[i + 1]?.trim() || '',
      })
      i++
    }
  }
  return resultado
}

const formatarMarkdown = (texto) => {
  return marked.parse(texto)
}

const proximo = () => {
  if (diaAtual.value < dias.value.length - 1) diaAtual.value++
}

const anterior = () => {
  if (diaAtual.value > 0) diaAtual.value--
}
</script>

<style scoped>
.container {
  max-width: 720px;
  margin: 40px auto;
  padding: 1.5rem;
  font-family: Arial, sans-serif;
  background-color: #1c1c1c;
  color: #eee;
  border-radius: 8px;
}

.inputs {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}

input {
  padding: 0.5rem;
  font-size: 1rem;
  border-radius: 4px;
  border: 1px solid #444;
  background-color: #2a2a2a;
  color: #fff;
}

button {
  padding: 0.6rem;
  font-size: 1rem;
  background-color: #00c853;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 1.2rem;
}

button:disabled {
  background-color: #888;
  cursor: not-allowed;
}

.carousel {
  background-color: #121212;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #333;
  margin-top: 1rem;
}

.navegacao {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: bold;
  margin-bottom: 1rem;
}

.navegacao button {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #00c853;
  cursor: pointer;
  padding: 0 0.5rem;
}

.navegacao button:disabled {
  color: #555;
  cursor: default;
}

.dia-html {
  font-size: 1rem;
  line-height: 1.4;
  color: #eee;
  white-space: pre-wrap;
}

.dia-html strong {
  color: #00e676;
}

.dia-html ul {
  margin-left: 1.2rem;
  list-style-type: "✅ ";
  padding-left: 1rem;
}

.dia-html li {
  margin-bottom: 0.3rem;
}

.dia-html h3, .dia-html h4 {
  margin-top: 0.8rem;
  color: #40c4ff;
}

.erro {
  color: #ff5252;
  margin-top: 1rem;
}
</style>


