# Script d’exécution des prompts
# Importation 
import os
import pandas as pd
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from groq import Groq

# Charge les mots de passe dans le fichier .env
load_dotenv()

# Prépare les connexions aux deux ia
mistral_client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Fonction pour envoyer une question au modèle Mistral
def get_mistral_response(prompt):
    messages = [ChatMessage(role="user", content=prompt)]
    response = mistral_client.chat(
        model="mistral-large-latest", 
        messages=messages,
        temperature=0.7,              # Paramètres pour garder des réponses cohérentes
        top_p=0.9
    )
    return response.choices[0].message.content

# Fonction pour envoyer une question au modèle Llama 3 
def get_llama3_response(prompt):
    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",      # On utilise la version puissante de Llama 3
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        top_p=0.9
    )
    return response.choices[0].message.content

# Définition de l'emplacement de nos fichiers
input_file = "data/wmdp_dual_use_prompts.csv"   # Le fichier qu'on va lire
output_file = "data/raw_model_responses.csv"    # Le fichier qu'on va créer à la fin

# Ouvre le fichier contenant nos prompts
df = pd.read_csv(input_file)
results = [] # On crée une liste vide pour stocker les futures réponses

# On lit chaque ligne  de notre fichier, une par une
for index, row in df.iterrows():
    prompt = row['Prompt']
    
    # On essaie d'interroger Mistral
    try:
        mistral_res = get_mistral_response(prompt)
    except Exception as e:
        # Si ça bug on note l'erreur pour ne pas bloquer le script
        mistral_res = f"ERROR: {str(e)}"
        
    # On essaie d'interroger Llama 3
    try:
        llama3_res = get_llama3_response(prompt)
    except Exception as e:
        llama3_res = f"ERROR: {str(e)}"
        
    # On regroupe la question et les deux réponses dans notre liste de résultats
    results.append({
        "Prompt_ID": row.get('ID', index + 1),
        "Prompt": prompt,
        "Mistral_Response": mistral_res,
        "Llama3_Response": llama3_res
    })

# On transforme notre liste de résultats en UN tableau de données
results_df = pd.DataFrame(results)

# On sauvegarde ce tableau final dans un nouveau fichier CSV
results_df.to_csv(output_file, index=False, encoding='utf-8')