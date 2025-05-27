# 🧭 Planejador de Viagens com IA

Este é um projeto fullstack que utiliza **FastAPI**, **CrewAI** e **Vue 3 + Vite** para gerar roteiros de viagem personalizados com base no destino, datas e interesses do usuário.

## 🌍 Funcionalidades

- ✅ Usuário informa destino, período da viagem e interesses
- ✅ Backend usa **CrewAI** com agentes de IA para planejar o roteiro
- ✅ Frontend exibe os dias com **navegação entre páginas (setas)**
- ✅ Conteúdo formatado com **Markdown estilizado** (listas, negrito, cores)
- ✅ Estilo escuro moderno, responsivo e leve

---

## 🧠 Tecnologias utilizadas

| Camada      | Tecnologias                           |
|-------------|----------------------------------------|
| Backend     | Python, FastAPI, CrewAI, Uvicorn       |
| Frontend    | Vue 3, Vite, marked.js                 |
| Estilo      | CSS puro (com escuro estilizado)       |
| IA          | OpenAI via CrewAI                      |

---

## ▶️ Como rodar o projeto

### 🔹 Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
---

### 

###🔹 Frontend

``` bash
cd frontend
npm install
npm run dev
```

---
## Imagem da Interface

![preview](Imagens/travelplanner/travelplanne.png)
---

## Descrição

Projeto desenvolvido durante a Workintech na Unicesumar, como exercicío da palestra sobre Inteligencia Articficial da Agencia LiveSEO.
Código 100% escrito por IA, com objetivo de integração entre IA e automação Web. 

