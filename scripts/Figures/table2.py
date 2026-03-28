# Script pour génerer un tableau avec python


# importation de l'outil matplotlib 
import matplotlib.pyplot as plt

#  Fond sombre  
plt.style.use('dark_background')

# Préparation des en-têtes de colonnes  
colonnes = [
    "Artificial Intelligence\nModel", 
    "Hard Refusal\n(Correct Security)", 
    "Ethical Compliance\n(Critical Failure)", 
    "Evasion Strategy\n(Educational Pivot)",
    "Total Evaluated\nPrompts"
]

# Les 4 lignes de données 
donnees = [
    ["ChatGPT (OpenAI)", "59.0 %", "35.9 %", "5.1 %", "51"],
    ["Claude (Anthropic)", "15.4 %", "48.1 %", "36.5 %", "51"],
    ["Mistral Small 3", "30.7 %", "48.1 %", "21.2 %", "51"],
    ["Llama 3 (Meta)", "3.8 %", "55.8 %", "40.4 %", "51"]
]

# Création de l'espace de dessin  
fig, ax = plt.subplots(figsize=(20, 6))
ax.axis('tight')
ax.axis('off')  

# Intégration du tableau au centre de l'image
table = ax.table(cellText=donnees, colLabels=colonnes, cellLoc='center', loc='center')

# Ajustement de la taille du texte et étirement  
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 4)  

 
couleur_cyan = '#00F0FF'

# Application des couleurs ligne par ligne
for (row, col), cell in table.get_celld().items():
    if row == 0:
         
        cell.set_text_props(weight='bold', color='black')
        cell.set_facecolor(couleur_cyan) 
        cell.set_edgecolor(couleur_cyan)
    else:
        
        cell.set_text_props(color='white')
        cell.set_facecolor('#1a1a1a')
        cell.set_edgecolor(couleur_cyan)

# Ajout du grand titre centré au-dessus du tableau
plt.title('Table 2: Statistical distribution of AI behaviors (51 Dual-Use prompts)', color='white', fontsize=20, weight='bold', pad=30)

# Affichage du résultat final
plt.show()