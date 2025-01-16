from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'test_topic',  # Nome do tópico
    bootstrap_servers=['localhost:9092'],  # Endereço do broker Kafka
    auto_offset_reset='earliest',  # Ler mensagens desde o início
    enable_auto_commit=True,  # Confirmação automática das mensagens
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserializar JSON
)

print("Consumindo mensagens do Kafka:")
for message in consumer:
    print(f"Mensagem recebida: {message.value}")
