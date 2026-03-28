# Script pour génerer un tableau avec python

# importation de l'outil matplotlib 
import matplotlib.pyplot as plt

#  Fond sombre  
plt.style.use('dark_background')

# Préparation des en-têtes de colonnes  
colonnes = [
    "Artificial Intelligence\nModel", 
    "Corporate Risk\nLevel", 
    "Primary Security\nThreat Vector", 
    "Enterprise Deployment\nRecommendation"
]

# Les 4 lignes de données exactes de l'image
donnees = [
    ["Llama 3 (Meta)", "Critical Risk", "Unrestricted generation of\nfunctional offensive code", "Do not deploy locally without\nstrict internal monitoring"],
    ["Mistral Small 3", "High Risk", "Easy access to system\nadministration exploits", "Requires secondary security\nfiltering layers"],
    ["Claude (Anthropic)", "High Risk", "Excessive theoretical explanations\n(Educational Pivot)", "Limit access to highly\ntechnical personnel only"],
    ["ChatGPT (OpenAI)", "Moderate Risk", "Still vulnerable to advanced\ndual-use IT jargon", "Safest current option, but\nrequires human oversight"]
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
table.scale(1.2, 4.5)  

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
plt.title('Table 6: Corporate risk assessment matrix based on dual-use vulnerability', color='white', fontsize=20, weight='bold', pad=30)

# Affichage du résultat final
plt.show()