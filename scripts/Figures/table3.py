# Script pour génerer un tableau avec python

# importation de l'outil matplotlib 
import matplotlib.pyplot as plt

#  Fond sombre  
plt.style.use('dark_background')

# Préparation des en-têtes de colonnes  
colonnes = [
    "Technical IT Category\n(Domain)", 
    "Total Number\nof Prompts", 
    "Average AI Failure Rate\n(Ethical Compliance)", 
    "Danger Level\nAssessment"
]

# Les 3 lignes de données 
donnees = [
    ["Network Reconnaissance\n& Mapping", "17 Prompts", "62.5 %", "Critical\n(Easily Weaponized)"],
    ["System Administration\n& Privilege", "17 Prompts", "45.0 %", "High\n(Contextually Ambiguous)"],
    ["Obfuscation &\nDefense Evasion", "17 Prompts", "32.5 %", "Moderate\n(More Heavily Filtered)"]
]

# Création de l'espace de dessin  
fig, ax = plt.subplots(figsize=(20, 5))
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
plt.title('Table 3: Average failure rates categorized by specific technical domains', color='white', fontsize=20, weight='bold', pad=30)

# Affichage du résultat final
plt.show()