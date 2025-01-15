import os

# Diretórios a serem criados
directories = [
    "src/kafka",
    "src/spark",
    "src/elasticsearch",
    "src/grafana",
    "configs/kafka",
    "configs/spark",
    "configs/grafana",
    "logs"
]

# Criar as pastas com arquivos .gitkeep para evitar que fiquem vazias no repositório Git
for directory in directories:
    os.makedirs(directory, exist_ok=True)  # Cria a pasta, se ela não existir
    with open(os.path.join(directory, ".gitkeep"), "w") as f:  # Cria o arquivo .gitkeep
        f.write("")

print("Estrutura de pastas criada com sucesso!")
