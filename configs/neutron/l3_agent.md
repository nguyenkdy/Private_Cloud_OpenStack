# Neutron L3 Agent - Ubuntu (self-service networking, option 2)

Source: https://docs.openstack.org/neutron/2026.1/install/controller-install-option2-ubuntu.html
(OpenStack 2026.1 Installation Guide)

The guide does not show any specific key=value edits for
`/etc/neutron/l3_agent.ini` in this release. It only states:

> Edit the `/etc/neutron/l3_agent.ini` file in case additional customization
> is needed.

No config snippet is provided, so no `l3_agent.ini` file has been
transcribed here - only this note, to avoid fabricating content that isn't
in the docs. The service itself is installed and restarted as part of the
controller node setup:

```
# apt install neutron-l3-agent
# service neutron-l3-agent restart
```
