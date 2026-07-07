# Source: https://docs.openstack.org/horizon/2026.1/install/install-ubuntu.html
# OpenStack 2026.1 Installation Guide - Horizon install and configure (Ubuntu)
#
# Destination on controller node: /etc/openstack-dashboard/local_settings.py
# (these are edits/additions to the existing file, not a full replacement)
#
# No secret placeholders requiring change in this file, but ALLOWED_HOSTS and
# TIME_ZONE are example values that must be adapted to your environment
# before real use.
#
# Related steps shown in the same guide page that are NOT part of this file:
#   - apt install openstack-dashboard
#   - Add to /etc/apache2/conf-available/openstack-dashboard.conf:
#       WSGIApplicationGroup %{GLOBAL}
#   - /usr/share/openstack-dashboard/manage.py collectstatic
#   - /usr/share/openstack-dashboard/manage.py compress
#   - systemctl reload apache2.service

OPENSTACK_HOST = "controller"

ALLOWED_HOSTS = ['one.example.com', 'two.example.com']

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

CACHES = {
    'default': {
         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
         'LOCATION': 'controller:11211',
    }
}

OPENSTACK_KEYSTONE_URL = "http://%s/identity/v3" % OPENSTACK_HOST

OPENSTACK_KEYSTONE_MULTIDOMAIN_SUPPORT = True

OPENSTACK_API_VERSIONS = {
    "identity": 3,
    "image": 2,
    "volume": 3,
}

OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = "Default"

# Networking (Option 1: provider networks)
OPENSTACK_NEUTRON_NETWORK = {
    ...
    'enable_router': False,
    'enable_quotas': False,
    'enable_ipv6': False,
    'enable_distributed_router': False,
    'enable_ha_router': False,
    'enable_fip_topology_check': False,
}

# Optional
TIME_ZONE = "TIME_ZONE"
