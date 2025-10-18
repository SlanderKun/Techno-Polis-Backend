import config
import faststream.rabbit

broker = faststream.rabbit.RabbitBroker(config.settings.rabbitmq.rabbitmq_url)
