# Swift Ring Builder Commands

Source: https://docs.openstack.org/swift/2026.1/install/initial-rings.html
(OpenStack 2026.1 Installation Guide - "Create and distribute initial rings")

Not a config file - these are `swift-ring-builder` commands run on the
controller node (run from within `/etc/swift`) to build the account,
container, and object rings. IP addresses, zones, and device names are
example placeholders from the guide and must be replaced with your own
storage node topology.

## Account ring

```
swift-ring-builder account.builder create 10 3 1
swift-ring-builder account.builder add --region 1 --zone 1 --ip 10.0.0.51 --port 6202 --device sdb --weight 100
swift-ring-builder account.builder add --region 1 --zone 1 --ip 10.0.0.51 --port 6202 --device sdc --weight 100
swift-ring-builder account.builder add --region 1 --zone 2 --ip 10.0.0.52 --port 6202 --device sdb --weight 100
swift-ring-builder account.builder add --region 1 --zone 2 --ip 10.0.0.52 --port 6202 --device sdc --weight 100
swift-ring-builder account.builder rebalance
```

## Container ring

```
swift-ring-builder container.builder create 10 3 1
swift-ring-builder container.builder add --region 1 --zone 1 --ip 10.0.0.51 --port 6201 --device sdb --weight 100
swift-ring-builder container.builder add --region 1 --zone 1 --ip 10.0.0.51 --port 6201 --device sdc --weight 100
swift-ring-builder container.builder add --region 1 --zone 2 --ip 10.0.0.52 --port 6201 --device sdb --weight 100
swift-ring-builder container.builder add --region 1 --zone 2 --ip 10.0.0.52 --port 6201 --device sdc --weight 100
swift-ring-builder container.builder rebalance
```

## Object ring

```
swift-ring-builder object.builder create 10 3 1
swift-ring-builder object.builder add --region 1 --zone 1 --ip 10.0.0.51 --port 6200 --device sdb --weight 100
swift-ring-builder object.builder add --region 1 --zone 1 --ip 10.0.0.51 --port 6200 --device sdc --weight 100
swift-ring-builder object.builder add --region 1 --zone 2 --ip 10.0.0.52 --port 6200 --device sdb --weight 100
swift-ring-builder object.builder add --region 1 --zone 2 --ip 10.0.0.52 --port 6200 --device sdc --weight 100
swift-ring-builder object.builder rebalance
```

Copy the resulting `account.ring.gz`, `container.ring.gz`, and
`object.ring.gz` files to `/etc/swift` on each storage node and proxy
service node.
