import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx

db = {
  "models": [
    {
      "name": "Bloom",
      "parameters": 1.5e9,
      "open_source": 'true',
      "nlp_tasks": [
        "Text generation",
        "Question answering",
        "Translation",
        "Text summarization"
      ],
      "developed_by": "Google AI",
      "resources": {
        "Github": "https://github.com/google-research/bloom"
      }
    },
    {
      "name": "EleutherAI GPT-Neo",
      "parameters": 2.7e9,
      "open_source": 'true',
      "nlp_tasks": [
        "Text generation",
        "Summarization",
        "Question answering",
        "Translation"
      ],
      "developed_by": "EleutherAI",
      "resources": {
        "Github": "https://github.com/EleutherAI/gpt-neo"
      }
    },
    {
      "name": "Cohere Tiny",
      "parameters": 350e6,
      "open_source": 'false',
      "nlp_tasks": [
        "Text generation",
        "Summarization",
        "Question answering",
        "Sentiment analysis"
      ],
      "developed_by": "Cohere",
      "resources": {
        "Website": "https://cohere.ai/"
      }
    },
    {
      "name": "OpenAI Whisper",
      "parameters": 1.2e9,
      "open_source": 'true',
      "nlp_tasks": [
        "Speech recognition",
        "Transcription",
        "Translation"
      ],
      "developed_by": "OpenAI",
      "resources": {
        "Github": "https://github.com/openai/whisper"
      }
    },
    {
      "name": "Meta AI LLaMA-Small",
      "parameters": 7e9,
      "open_source": 'true',
      "nlp_tasks": [
        "Text generation",
        "Question answering",
        "Translation",
        "Summarization"
      ],
      "developed_by": "Meta AI",
      "resources": {
        "Github": "https://github.com/facebookresearch/llama"
      }
    }
  ]
}

# Create a dataframe from the dictionary
df = pd.DataFrame(db['models'])

# Pie chart of NLP tasks
tasks = df['nlp_tasks'].apply(lambda x: ', '.join(x))
plt.figure(figsize=(10, 10))
plt.pie(tasks.value_counts(), labels=tasks.value_counts().index, autopct='%1.1f%%')
plt.title('Distribution of NLP Tasks')
plt.show()

# Bar chart of parameters
plt.figure(figsize=(10, 10))
plt.bar(df['name'], df['parameters'])
plt.title('Parameters of Language Models')
plt.xlabel('Model Name')
plt.ylabel('Parameters (billions)')
plt.show()

# Scatter plot of parameters vs. NLP tasks
plt.figure(figsize=(10, 10))
plt.scatter(df['parameters'], df['nlp_tasks'].apply(lambda x: len(x)))
plt.title('Relationship between Parameters and NLP Tasks')
plt.xlabel('Parameters (billions)')
plt.ylabel('Number of NLP Tasks')
plt.show()

# Bad diagram of model relationships
G = nx.Graph()
edges = []
for i in range(len(df)):
    for j in range(i+1, len(df)):
        if df['nlp_tasks'][i] == df['nlp_tasks'][j]:
            edges.append((df['name'][i], df['name'][j]))
G.add_edges_from(edges)
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=500)

# edges
nx.draw_networkx_edges(G, pos, alpha=0.5)

# labels
nx.draw_networkx_labels(G, pos, font_size=10)

plt.axis('off')
plt.show()