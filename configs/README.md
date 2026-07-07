# OpenStack 2026.1 Ubuntu Reference Configs

These are reference configuration files transcribed verbatim from the
official OpenStack 2026.1 Installation Guide (Ubuntu flavor), matching the
components described in the top-level README.md. **All passwords, secrets,
and placeholder values (e.g. `KEYSTONE_DBPASS`, `RABBIT_PASS`,
`METADATA_SECRET`, `NEUTRON_PASS`, IP addresses like `10.0.0.11`) must be
replaced with real values before any of this is used in an actual
deployment.**

Every file has a header comment citing its exact source URL and noting
related install steps (SQL/CLI commands, package installs, service restarts)
that the guide shows alongside the config but which aren't config-file
content themselves.

## backend/ - Shared backend services

| File | Contents | Source |
|---|---|---|
| `mariadb.cnf` | `/etc/mysql/mariadb.conf.d/99-openstack.cnf` | https://docs.openstack.org/install-guide/environment-sql-database-ubuntu.html |
| `rabbitmq.md` | RabbitMQ has no dedicated config file in the guide - install + `rabbitmqctl` user/permission commands | https://docs.openstack.org/install-guide/environment-messaging-ubuntu.html |
| `memcached.conf` | `/etc/memcached.conf` bind-address edit | https://docs.openstack.org/install-guide/environment-memcached-ubuntu.html |
| `etcd.conf` | `/etc/default/etcd` | https://docs.openstack.org/install-guide/environment-etcd-ubuntu.html |

## keystone/ - Identity service

| File | Contents | Source |
|---|---|---|
| `keystone.conf` | `/etc/keystone/keystone.conf` ([database], [token]) | https://docs.openstack.org/keystone/2026.1/install/keystone-install-ubuntu.html |

## glance/ - Image service

| File | Contents | Source |
|---|---|---|
| `glance-api.conf` | `/etc/glance/glance-api.conf` | https://docs.openstack.org/glance/2026.1/install/install-ubuntu.html |

(No `glance-api-paste.ini` edits are shown in the guide, so none is included.)

## nova/ - Compute service

| File | Contents | Source |
|---|---|---|
| `nova-controller.conf` | `/etc/nova/nova.conf` on the controller node, including the `[neutron]` and `[cinder]` sections added later by the Networking and Block Storage guide steps | https://docs.openstack.org/nova/2026.1/install/controller-install-ubuntu.html |
| `nova-compute.conf` | `/etc/nova/nova.conf` on the compute node, including the `[neutron]` section | https://docs.openstack.org/nova/2026.1/install/compute-install-ubuntu.html |

## neutron/ - Networking service (self-service networks, Open vSwitch)

The 2026.1 guide's "self-service networks" (option 2) example uses the Open
vSwitch mechanism driver, not Linux Bridge.

| File | Contents | Source |
|---|---|---|
| `neutron-controller.conf` | `/etc/neutron/neutron.conf` on the controller node | https://docs.openstack.org/neutron/2026.1/install/controller-install-option2-ubuntu.html |
| `neutron-compute.conf` | `/etc/neutron/neutron.conf` on the compute node | https://docs.openstack.org/neutron/2026.1/install/compute-install-ubuntu.html, https://docs.openstack.org/neutron/2026.1/install/compute-install-option2-ubuntu.html |
| `ml2_conf.ini` | `/etc/neutron/plugins/ml2/ml2_conf.ini` | https://docs.openstack.org/neutron/2026.1/install/controller-install-option2-ubuntu.html |
| `openvswitch_agent.ini` | `/etc/neutron/plugins/ml2/openvswitch_agent.ini` (identical content on controller and compute nodes) | https://docs.openstack.org/neutron/2026.1/install/controller-install-option2-ubuntu.html, https://docs.openstack.org/neutron/2026.1/install/compute-install-option2-ubuntu.html |
| `dhcp_agent.ini` | `/etc/neutron/dhcp_agent.ini` | https://docs.openstack.org/neutron/2026.1/install/controller-install-option2-ubuntu.html |
| `metadata_agent.ini` | `/etc/neutron/metadata_agent.ini` | https://docs.openstack.org/neutron/2026.1/install/controller-install-ubuntu.html |
| `l3_agent.md` | The guide shows no specific `l3_agent.ini` key/value edits for this release - documented as a note instead of a fabricated config | https://docs.openstack.org/neutron/2026.1/install/controller-install-option2-ubuntu.html |

## cinder/ - Block Storage service

| File | Contents | Source |
|---|---|---|
| `cinder-controller.conf` | `/etc/cinder/cinder.conf` on the controller node | https://docs.openstack.org/cinder/2026.1/install/cinder-controller-install-ubuntu.html |
| `cinder-storage.conf` | `/etc/cinder/cinder.conf` on the storage (LVM) node | https://docs.openstack.org/cinder/2026.1/install/cinder-storage-install-ubuntu.html |

## swift/ - Object Storage service

| File | Contents | Source |
|---|---|---|
| `proxy-server.conf` | `/etc/swift/proxy-server.conf` | https://docs.openstack.org/swift/2026.1/install/controller-install-ubuntu.html |
| `account-server.conf` | `/etc/swift/account-server.conf` | https://docs.openstack.org/swift/2026.1/install/storage-install-ubuntu-debian.html |
| `container-server.conf` | `/etc/swift/container-server.conf` | https://docs.openstack.org/swift/2026.1/install/storage-install-ubuntu-debian.html |
| `object-server.conf` | `/etc/swift/object-server.conf` | https://docs.openstack.org/swift/2026.1/install/storage-install-ubuntu-debian.html |
| `swift.conf` | `/etc/swift/swift.conf` ([swift-hash], [storage-policy:0]) | https://docs.openstack.org/swift/2026.1/install/finalize-installation-ubuntu-debian.html |
| `rings-setup.md` | `swift-ring-builder` commands for account/container/object rings (not a config file) | https://docs.openstack.org/swift/2026.1/install/initial-rings.html |

## heat/ - Orchestration service

| File | Contents | Source |
|---|---|---|
| `heat.conf` | `/etc/heat/heat.conf` | https://docs.openstack.org/heat/2026.1/install/install-ubuntu.html |

## octavia/ - Load-balancer service

| File | Contents | Source |
|---|---|---|
| `octavia.conf` | `/etc/octavia/octavia.conf` | https://docs.openstack.org/octavia/2026.1/install/install-ubuntu.html |

## horizon/ - Dashboard

| File | Contents | Source |
|---|---|---|
| `local_settings.py` | `/etc/openstack-dashboard/local_settings.py` edits/additions | https://docs.openstack.org/horizon/2026.1/install/install-ubuntu.html |

---

These are OpenStack **2026.1 Ubuntu** reference configs transcribed from the
official install guide at docs.openstack.org, and every placeholder
password/secret must be changed before any real use.
