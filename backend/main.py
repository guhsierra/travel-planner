from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from crewai import Agent, Task, Crew
import uvicorn
import os


# Certifique-se de que sua chave da OpenAI está no ambiente
os.environ["OPENAI_API_KEY"] = "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"  # OU configure no sistema


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:5173"] para mais segurança
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Modelo para os dados de entrada
class TravelRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str
    interests: List[str]


# Função que cria e executa a Crew
async def plan_trip_with_crew(data: TravelRequest) -> dict:
    # Criação do agente
    planner = Agent(
        role="Agente de Viagem",
        goal="Planejar uma viagem personalizada com base nos interesses do usuário.",
        backstory="Especialista em turismo, cultura local e organização de roteiros.",
        verbose=True
    )


    # Criação da tarefa
    task = Task(
        description=(
            f"Crie um roteiro de viagem para {data.destination}, "
            f"de {data.start_date} até {data.end_date}, "
            f"com foco nos interesses: {', '.join(data.interests)}."
        ),
        expected_output="Um roteiro diário com sugestões de atividades e locais para visitar.",
        agent=planner
    )


    # Criação e execução da Crew
    crew = Crew(agents=[planner], tasks=[task])
    result = crew.kickoff()
    return {"trip_plan": result}


# Rota da API
@app.post("/plan-trip")
async def plan_trip(request: TravelRequest):
    try:
        return await plan_trip_with_crew(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Execução local
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)