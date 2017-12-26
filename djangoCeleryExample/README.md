1. Adding user in rabbitmq
rabbitmqctl add_user djangouser djangoPassword
rabbitmqctl add_vhost djangohost
rabbitmqctl set_user_tags djangouser administrator
rabbitmqctl set_permissions -p djangohost djangouser ".*" ".*" ".*"
2. Broker Url
broker_url = 'amqp://djangouser:djangoPassword@127.0.0.1:5672/djangohost'
