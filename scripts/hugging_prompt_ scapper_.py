#script pour récuperer les prompt de hugging face et les envoyer a une ia grace un API

import time
import pandas as pd
from datasets import load_dataset
from groq import Groq
from IPython.display import display


# Normalemennt il ne faudrait pas mettre directement sa clép API ici 
GROQ_API_KEY = ""

# Initialisation du client avec ta clé
client = Groq(api_key=GROQ_API_KEY)

print(" Téléchargement du dataset WMDP-Cyber depuis Hugging Face...")
# On charge les 10 premiers exemples pour le test. (Remplace "test[:10]" par "test" pour tout faire)
dataset = load_dataset("cais/wmdp", "wmdp-cyber", split="test[:10]")

results = []
print(f" Lancement de l'audit sur {len(dataset)} prompts avec Llama 3.3...")

for i, item in enumerate(dataset):
    question = item['question']
    choices = item['choices']
    
    # Formatage propre du QCM pour Llama
    prompt_text = f"Question: {question}\n\nChoices:\nA) {choices[0]}\nB) {choices[1]}\nC) {choices[2]}\nD) {choices[3]}\n\nPlease act as a cybersecurity expert. Provide the correct letter and a brief explanation."
    
    try:
        # Requête à l'API Groq 
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_text}],
            model="llama-3.3-70b-versatile", 
            temperature=0.0, # On garde 0 pour des réponses constantes
        )
        
        response = chat_completion.choices[0].message.content
        
        # On prépare déjà la colonne 'Behavior' pour l'analyse analyse sur Kibana
        results.append({
            "Prompt_ID": f"WMDP-CYBER-{i+1:04d}",
            "Question": question,
            "Llama3_Response": response,
            "Behavior": "" # à remplir plus tard
        })
        
        print(f" Prompt {i+1} traité avec succès.")
        time.sleep(1) # Pause de 1s pour éviter de spammer l'API Groq
        
    except Exception as e:
        print(f" Erreur sur le prompt {i+1} : {e}")
        results.append({
            "Prompt_ID": f"WMDP-CYBER-{i+1:04d}",
            "Question": question,
            "Llama3_Response": f"ERROR: {e}",
            "Behavior": "ERROR"
        })

# Exportation des résultats
print("\n Création du fichier CSV de résultats...")
df = pd.DataFrame(results)
df.to_csv('llama3_wmdp_results.csv', index=False)

print("  Voici un aperçu de des données prêtes pour Kibana :")
display(df.head())
