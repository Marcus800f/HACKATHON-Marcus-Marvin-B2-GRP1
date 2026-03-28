# Script pour génerer un tableau avec python

# importation de l'outil matplotlib 
import matplotlib.pyplot as plt

#  Fond sombre  
plt.style.use('dark_background')

# Préparation des en-têtes de colonnes  
colonnes = [
    "Evaluation Methodology", 
    "Level of Contextual\nUnderstanding", 
    "Primary Source\nof Bias", 
    "Scientific\nReproducibility"
]

# Les 2 lignes de données 
donnees = [
    ["Manual Human Evaluation\n(Our Method)", "Very High\n(Detects subtle evasion strategies)", "Human Subjectivity\n(Depends on IT background)", "Moderate\n(Results may vary slightly)"],
    ["Automated LLM Judge\n(Standard Method)", "Low\n(Only looks for binary compliance)", "Algorithmic Bias\n(Flawed safety filters of judge AI)", "Very High\n(Produces exact same score)"]
]

# Création de l'espace de dessin  
fig, ax = plt.subplots(figsize=(20, 4))
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
plt.title('Table 5: Critical comparison of evaluation methodologies and their inherent biases', color='white', fontsize=20, weight='bold', pad=30)

# Affichage du résultat final
plt.show()