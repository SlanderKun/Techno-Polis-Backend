import config
import rabbit
import utils.acelery

app = utils.acelery.AsyncCelery(
    "worker",
    broker=config.settings.rabbitmq.rabbitmq_url,
    backend=config.settings.rabbitmq.rabbitmq_url,
    broker_instance=rabbit.broker,
)

import tasks  # noqa

app.conf.beat_schedule = {
    "periodic_task": {
        "task": "tasks.periodic_task",
        "schedule": 10.0,
    },
}
app.conf.timezone = "UTC"
