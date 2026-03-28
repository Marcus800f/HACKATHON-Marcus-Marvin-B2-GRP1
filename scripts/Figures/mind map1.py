#  Script pour génerer une mind map
import matplotlib.pyplot as plt


plt.style.use('dark_background')

# Crée l'espace de dessin (figure)
fig, ax = plt.subplots(figsize=(18, 10))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off') 

# Définit les positions exactes pour chaque bloc  
center = (0.5, 0.5)
tl = (0.22, 0.78)   
tr = (0.78, 0.78)   
bl = (0.22, 0.22)    
br = (0.78, 0.22)   

# Dessine les lignes de connexion
# Dessine les lignes en premier pour que le texte passe par-dessus
ax.plot([center[0], tl[0]], [center[1], tl[1]], color='#00D1FF', lw=3, zorder=1) 
ax.plot([center[0], tr[0]], [center[1], tr[1]], color='#B026FF', lw=3, zorder=1)  
ax.plot([center[0], bl[0]], [center[1], bl[1]], color='#00ff44', lw=3, zorder=1)  
ax.plot([center[0], br[0]], [center[1], br[1]], color='#ff9900', lw=3, zorder=1)  

# Définit le style visuel des boîtes de texte  
common_bbox = dict(boxstyle="round,pad=1", fc="#1a1a1a", lw=2)
bbox_center = dict(boxstyle="round,pad=1", fc="#1a1a1a", ec="white", lw=2)
bbox_tl = dict(boxstyle="round,pad=0.8", fc="#111111", ec="#00D1FF", lw=2)
bbox_tr = dict(boxstyle="round,pad=0.8", fc="#111111", ec="#B026FF", lw=2)
bbox_bl = dict(boxstyle="round,pad=0.8", fc="#111111", ec="#00ff44", lw=2)
bbox_br = dict(boxstyle="round,pad=0.8", fc="#111111", ec="#ff9900", lw=2)

 
text_center = "CORE RESEARCH\nIntent-Based AI Security Auditing\n(Semantic Evaluation)"

text_tl = "1. SELECTED AI MODELS\n\n" \
          "• ChatGPT (OpenAI)\n" \
          "• Claude (Anthropic)\n" \
          "• Mistral (Mistral AI)\n" \
          "• Llama 3 (Meta)"

text_tr = "2. EXPERIMENTAL CORPUS\n\n" \
          "• Phase 1: 51 WMDP Prompts\n" \
          "  (Adapted / Dual-Use Jargon)\n\n" \
          "• Phase 2: 10 Custom Prompts\n" \
          "  (Explicit Sanity Check)"

text_bl = "3. ANALYTICAL PIPELINE\n\n" \
          "• Data Entry: Google Sheets\n" \
          "• Processing: Python & Pandas\n" \
          "• Visuals: Matplotlib (Colab)"

text_br = "4. GRADING MATRIX\n\n" \
          "• 1. Hard Refusal (Secure)\n" \
          "• 2. Ethical Compliance (Failure)\n" \
          "• 3. Evasion Strategy (Risk)"

# Met le grand titre centré au-dessus de l'espace de dessin
plt.title('Mind Map 1: AI Security Evaluation Framework', color='white', fontsize=20, pad=20, weight='bold')

# Injecte les textes et applique les styles définis
 
ax.text(center[0], center[1], text_center, ha="center", va="center", size=16, weight='bold', color="white", bbox=bbox_center, zorder=2)
ax.text(tl[0], tl[1], text_tl, ha="center", va="center", size=14, color="white", bbox=bbox_tl, zorder=2)
ax.text(tr[0], tr[1], text_tr, ha="center", va="center", size=14, color="white", bbox=bbox_tr, zorder=2)
ax.text(bl[0], bl[1], text_bl, ha="center", va="center", size=14, color="white", bbox=bbox_bl, zorder=2)
ax.text(br[0], br[1], text_br, ha="center", va="center", size=14, color="white", bbox=bbox_br, zorder=2)

# Affiche le résultat final
plt.show()