import time
import requests
import json
import pandas as pd
import plotly.graph_objects as go

 
  
while True:
  data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
  json_data = json.loads(data.content)

  candidatos = []
  partido = []
  votos = []
  porcentagem = []
  for informacoes in json_data['cand']:
      candidatos.append(informacoes['nm'])
      votos.append(informacoes['vap'])
      porcentagem.append(informacoes['pvap'])

  df_eleicao = pd.DataFrame(list(zip(candidatos, votos, porcentagem)), columns =['Candidatos', 'Votos', 'Porcentagem'])

  gugabalatensa = go.Figure()


  gugabalatensa.add_traces(
      go.Pie(labels=df_eleicao['Candidatos'][::-1], values=df_eleicao['Votos'][::-1], )
    )
  gugabalatensa.show()  
  time.sleep(5)
    
print(df_eleicao)