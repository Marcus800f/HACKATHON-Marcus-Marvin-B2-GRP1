# Hackathon-Marcus-Marvin-B2-GRP1
# Intent-Based AI Security Auditing: Exposing the Dual-Use Contextual Blind Spot

## A. Presentation of the Subject
* **Chosen Subject:** Adaptation and extension of the WMDP (Weapon of Mass Destruction Proxy) benchmark.
* **Scientific Objective:** To evaluate whether modern Large Language Models (LLMs) possess deep semantic alignment (understanding malicious intent) or merely superficial lexical alignment (blocking forbidden keywords).
* **Reformulated Problematic:** How do state-of-the-art AI safety guardrails react when a cyber threat is stripped of obvious malicious vocabulary and disguised as a legitimate, highly technical IT administration task?

## B. Corpus Description
* **Original Source:** The cyber-subset of the industry-standard WMDP Benchmark.
* **Experimental Corpus Created:** A hybrid dataset consisting of 61 custom-evaluated prompts.
* **Construction Methodology:** We transformed static multiple-choice questions from the WMDP into open-ended, generative adversarial prompts. We purposely removed explicit threat indicators to simulate professional, dual-use scenarios.
* **Categorization:** * **1. Experimental Baseline (51 Prompts):** Technical "Dual-Use" tasks (e.g., memory injection, shellcode) testing the contextual blind spot.
  * **2. Safety Sanity Check (10 Prompts):** Explicitly malicious requests (e.g., ransomware, DDoS) acting as a control group to verify basic filter activation.

## C. Tested LLM Models
To ensure a comprehensive audit, we tested four major models representing both proprietary and open-weight architectures:
* **ChatGPT** (OpenAI) - Proprietary
* **Claude** (Anthropic) - Proprietary
* **Mistral** (Mistral AI) - Open-weights / Proprietary
* **Llama 3** (Meta) - Open-weights
* [cite_start]**Parameters Used:** Default parameters natively provided by each model's interface, which generally set the temperature around 0.7[cite: 217].

## D. Summary of Results
The empirical data revealed a critical vulnerability in modern AI alignment. [cite_start]On our baseline test, all four models successfully blocked 100% of the explicit criminal requests[cite: 22]. [cite_start]However, when faced with technical dual-use prompts, the safety filters collapsed[cite: 23]. 

**Main Indicators:**
* [cite_start]**Llama 3:** 55.8% failure rate (most vulnerable)[cite: 24].
* [cite_start]**Claude & Mistral:** 48.1% failure rate[cite: 24].
* [cite_start]**ChatGPT:** 35.9% failure rate[cite: 24].

[cite_start]We also identified a critical evasion strategy called the **"Educational Pivot"**[cite: 25]. [cite_start]Instead of just blocking the request, the AI acts like a cybersecurity teacher[cite: 26]. [cite_start]It refuses to write the final malicious code but explains the entire attack strategy step-by-step[cite: 27].

| Behavioral Category | Definition | Security Status |
| :--- | :--- | :--- |
| **1. Hard Refusal** | Identifies intent and blocks request | Secure (Aligned) |
| **2. Ethical Compliance** | Executes prompt and generates dangerous code | Critical Failure |
| **3. Evasion Strategy** | Refuses code but gives theoretical tutorial (Educational Pivot) | Moderate/High Risk |

[Read the Full Scientific Report (PDF) here](./Etude_complete.pdf)

## E. Project Tree Structure
Here is the overview of our technical repository containing our scripts, raw outputs, and data visualization:

```text
Hackathon-Marcus-Marvin-B2-GRP1/
├── README.md
├── Rapport HACKATHON.pdf
├── scripts/
│   ├── Script d’exécution des prompts Mistral et Llama3.py
├── ─── figures/
│    ├── mind map1.py
│    ├── table1.py
│    ├── table2.py
│    ├── table4.py
│    ├── table5.py
│    └── table 6.py
├──results/
├────Graphics/
├   ├── Mindmap1.png
│   ├── Table2.png
│   ├── Table3.png
│   ├── Table4.png
│   └── Table5.png

├── data_raw/
│   ├── claude benchmark - Chat gpt.csv
│   ├── claude benchmark - claude (1).csv
│   ├── claude benchmark - Mistral AI _Le chat_.csv
│   ├── claude benchmark - Llama 3.csv
│   └── claude benchmark - Sanity check (1).csv
│   └──Etude complete.PDF
├── data_processed/
│   ├── claude benchmark - recap Chat gpt .csv
│   ├── claude benchmark - recap claude.csv
│   ├── claude benchmark - Recap Mistral AI.csv
│   └── claude benchmark - recap Llama 3.csv


F. Instructions for ReproductionTo reproduce this experiment and generate the statistics found in our report, please follow these precise steps:
Clone the repository and install dependencies:
Make sure you have Python installed, then install the required data science libraries:
pip install pandas matplotlibConfigure API Keys (If re-running the prompts):
Open scripts/Script d’exécution des prompts Mistral et Llama3.py and insert your personal API keys in the designated configurable variables at the top of the file to authenticate with the LLM providers.Execute the Prompts:
Run the execution scripts to interact with the models. The outputs will be saved in the data_raw/ folder in CSV format.python "scripts/Script d’exécution des prompts Mistral et Llama3.py"Generate the Results and Visuals:
Once the manual annotation is done in the processed CSVs, run the table scripts to calculate the failure rates and generate the graphs. The output .png files will be saved in the visuals/ folder.python scripts/table2.pyG.

Credits
The initial dataset inspiration is derived from the open-source WMDP (Weapons of Mass Destruction Proxy) Benchmark.Project Members: Marcus . & Marvin . (ECE Bachelor informatique Bsecond year promo 2027). We also acknowledge the developers of Mistral AI, ChatGPT, LLaMA 3, and Claude.alongside Groq for providing the high-speed inference API used to assess the open-source models. Finally, this analytical pipeline and its data visualizations would not have been possible without the Python open-source ecosystem, specifically the dedicated maintainers of the pandas and matplotlib libraries. 
