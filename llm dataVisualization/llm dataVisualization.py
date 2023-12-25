import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data
models = ["Bloom", "EleutherAI GPT-Neo", "Cohere Tiny", "OpenAI Whisper", "Meta AI LLaMA-Small"]
parameters = [1.5e9, 2.7e9, 350e6, 1.2e9, 7e9]
open_source = [True, True, False, True, True]
nlp_tasks = [
    "Text generation",
    "Question answering",
    "Translation",
    "Text summarization",
    "Summarization",
    "Sentiment analysis",
    "Speech recognition",
    "Transcription"
]

# Pie Chart - Open Source vs Closed Source
plt.figure(figsize=(8, 8))
plt.pie(
    [open_source.count(True), open_source.count(False)],
    labels=["Open Source", "Closed Source"],
    autopct='%1.1f%%',
)
plt.title('Open Source vs Closed Source Models')
plt.show()

# Bar Graph - Model Parameters
plt.figure(figsize=(10, 8))
plt.bar(models, parameters)
plt.xticks(rotation=30)
plt.xlabel('Model Name')
plt.ylabel('Number of Parameters')
plt.title('Model Parameters Comparison')
plt.show()

# Radar Chart - NLP Tasks
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for i, model in enumerate(models):
    tasks = np.array([1 if task in db['models'][i]['nlp_tasks'] else 0 for task in nlp_tasks])
    plt.plot(tasks, label=model)
    plt.fill(tasks, alpha=0.25)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.title('NLP Tasks Supported by Models')
plt.show()