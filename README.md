# Streaming Data Pipeline

Este repositório contém uma implementação de um pipeline de dados para processamento e monitoramento em tempo real. A estrutura do pipeline utiliza Kafka, Spark, Elasticsearch, Kibana e Grafana para o processamento e visualização dos dados.

## Estrutura do Repositório
```
├── docker-compose.yml
├── README.md
├── requirements.txt
├── src/
│   ├── kafka/
│   ├── spark/
│   ├── elasticsearch/
│   └── grafana/
├── configs/
│   ├── kafka/
│   ├── spark/
│   └── grafana/
└── logs/
```

## Pré-requisitos
- Docker e Docker Compose
- Python 3.8+
- Git
- Anaconda (opcional, mas recomendado)

## Configuração Inicial

### Criar Ambiente Virtual com Anaconda
1. **Crie o Ambiente**:
   ```bash
   conda create -n streaming_pipeline python=3.8
   ```

2. **Ative o Ambiente**:
   ```bash
   conda activate streaming_pipeline
   ```

3. **Atualize o `pip`**:
   ```bash
   pip install --upgrade pip
   ```

4. **Instale Dependências**:
   Caso esteja usando o ambiente virtual padrão:
   ```bash
   pip install -r requirements.txt
   ```
   Caso esteja usando Anaconda, instale os pacotes principais com Conda e complemente com Pip:
   ```bash
   conda install numpy pandas
   conda install -c conda-forge pyspark kafka-python
   pip install -r requirements.txt
   ```

5. **Suba os Serviços com Docker Compose**:
   ```bash
   docker-compose up -d
   ```

6. **Verifique os Serviços**:
- Kafka: `localhost:9092`
- Elasticsearch: `localhost:9200`
- Kibana: `localhost:5601`
- Grafana: `localhost:3000`

## Componentes

### Kafka
- Configurado para ingestão de dados de eventos.
- Código-fonte e scripts relacionados em `src/kafka/`.

### Spark
- Responsável pelo processamento dos dados em tempo real.
- Código-fonte em `src/spark/`.

### Elasticsearch e Kibana
- Elasticsearch: Armazena os dados processados.
- Kibana: Usado para visualização e análise dos dados.
- Configurações e dashboards em `configs/elasticsearch/` e `configs/kibana/`.

### Grafana
- Usado para monitoramento em tempo real dos dados do pipeline.
- Configurações em `configs/grafana/`.

## Próximos Passos
- Implementar a geração de eventos no Kafka usando Python.
- Desenvolver um job de streaming em Spark que consuma dados do Kafka.
- Configurar visualizações no Kibana e dashboards no Grafana.

## Contribuindo
- Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto é licenciado sob a [MIT License](LICENSE).
