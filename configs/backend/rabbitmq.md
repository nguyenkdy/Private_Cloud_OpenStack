# RabbitMQ (Message Queue) Setup - Ubuntu

Source: https://docs.openstack.org/install-guide/environment-messaging-ubuntu.html
(OpenStack 2026.1 Installation Guide)

RabbitMQ has no single application config file shown in the install guide for
this step - the guide only shows package installation and `rabbitmqctl`
commands to create the OpenStack service account and grant it permissions.
Replace `RABBIT_PASS` with your own secret before real use.

Runs on the controller node.

## Install package

```
# apt install rabbitmq-server
```

## Create the OpenStack user

```
# rabbitmqctl add_user openstack RABBIT_PASS
```

Replace `RABBIT_PASS` with an appropriate password.

## Grant the user configuration, write, and read permissions

```
# rabbitmqctl set_permissions openstack ".*" ".*" ".*"
```

## Note from the guide

> Sometimes it's necessary to increase the file descriptor limit for RabbitMQ
> to handle a large number of connections properly.
