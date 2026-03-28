
# Script pour génerer un tableau avec python


# importation de l'outil matplotlib 
import matplotlib.pyplot as plt

# Fond sombre 
plt.style.use('dark_background')

# Préparation des en-têtes de colonnes
colonnes = [
    "Feature / Metric", 
    "Static Declarative Approach\n(e.g., WMDP)", 
    "Dynamic Adversarial Approach\n(e.g., HarmBench)"
]

# Les 6 lignes de données 
donnees = [
    ["Primary Focus", "Declarative Knowledge\n(What the model knows)", "Generative Capability\n(What the model can do)"],
    ["Format", "Multiple-Choice Questions\n(MCQs)", "Open-ended Adversarial\nPrompts"],
    ["Evaluation Method", "Objective Mathematical\nScoring", "LLM-as-a-Judge or\nManual Annotation"],
    ["Strengths", "Scalable, fast, and\nperfectly objective", "Mirrors real-world\nthreat models"],
    ["Weaknesses", "Disconnected from functional\ncyberattack execution", "Methodologically complex\nand computationally expensive"],
    ["Security Goal", "Measuring Dangerous\nKnowledge Retention", "Testing Ethical Guardrail\nTriggering"]
]

# Création de l'espace de dessin 
fig, ax = plt.subplots(figsize=(20, 9))
ax.axis('tight')
ax.axis('off') 

# Intégration du tableau au centre de l'image
table = ax.table(cellText=donnees, colLabels=colonnes, cellLoc='center', loc='center')

# Ajustement de la taille du texte et étirement 
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 5) 

# Application des couleurs ligne par ligne
for (row, col), cell in table.get_celld().items():
    if row == 0:
        # Ligne 0 
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#9b22e0') 
        cell.set_edgecolor('#B026FF')
    else:
        # Reste du tableau  
        cell.set_text_props(color='white')
        cell.set_facecolor('#0a0a0a')
        cell.set_edgecolor('#B026FF') 

# Ajout du grand titre centré au-dessus du tableau
plt.title('Table 1: Comparative Analysis of LLM Security Evaluation Methodologies', color='white', fontsize=22, weight='bold', pad=30)

# Affichage du résultat
plt.show()