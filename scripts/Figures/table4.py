# Script pour génerer un tableau avec python

# importation de l'outil matplotlib 
import matplotlib.pyplot as plt

#  Fond sombre  
plt.style.use('dark_background')

# Préparation des en-têtes de colonnes  
colonnes = [
    "Artificial Intelligence\nModel", 
    "Rate of 'Educational Pivot'\n(Providing Dangerous Theory)", 
    "Security Assessment\nof this Behavior"
]

# Les 4 lignes de données 
donnees = [
    ["Llama 3 (Meta)", "40.4 %", "Critical Risk\n(Acts as a complete tutorial)"],
    ["Claude (Anthropic)", "36.5 %", "High Risk\n(Very detailed technical explanations)"],
    ["Mistral Small 3", "21.2 %", "Moderate Risk\n(Partial theoretical guidance)"],
    ["ChatGPT (OpenAI)", "5.1 %", "Low Risk\n(Usually triggers a hard refusal instead)"]
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
plt.title('Table 4: Frequency of the "Educational Pivot" evasion strategy', color='white', fontsize=20, weight='bold', pad=30)

# Affichage du résultat final
plt.show()