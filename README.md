# Private_Cloud_OpenStack
## 🏗️ System Architecture

Below is the deployment model of the system, including the Controller, Compute/Storage nodes, Backend Services (MariaDB, RabbitMQ, Memcached, etcd), OpenStack Core Services (Nova, Neutron, Keystone, Glance, Cinder, Swift, Heat), and the monitoring/alerting system (Prometheus/Grafana):

<p align="center">
  <img width="70%" alt="OpenStack Architecture" src="https://github.com/user-attachments/assets/6ffcfc0d-e344-4330-909c-598db10a3316" />
</p>

---

## 🎥 Project Demo Video

To watch the detailed, real-world operation of the system, please access the Google Drive folder via the link below:

👉 **[Watch the System Demo Video here](https://drive.google.com/drive/folders/1zf7uFeplftviIn-IQP_doIUMNhrzWo9w?usp=drive_link)**

---

## 🛠️ Overview of Technologies & OpenStack Services

To provide a clearer understanding of the architecture shown above, here is a brief introduction to the backend services and core components used in this project:

### 1. Backend Services
These components form the operational backbone of the OpenStack Controller, ensuring communication, data consistency, and state management:
- **RabbitMQ:** The message broker responsible for inter-service communication. OpenStack services use it to send updates and coordinate tasks.
- **MariaDB:** The relational database management system (RDBMS) where all OpenStack services store their state, configuration, and metadata.
- **Memcached:** A distributed memory caching system used to store authentication tokens (from Keystone) to reduce database load and improve response times.
- **etcd:** A distributed key-value store used primarily by OpenStack components (like networking mechanisms or coordination helpers) for synchronization and distributed locking.

### 2. OpenStack Core Services
- **Keystone (Identity Service):** The central authentication and authorization service. It tracks users, roles, and provides a catalog of available endpoints for all other services.
- **Glance (Image Service):** Manages Virtual Machine (VM) disk images. It allows users to discover, register, and retrieve template images used to spin up instances.
- **Nova (Compute Service):** The heart of OpenStack cloud computing. It manages the lifecycle of instances (creation, scheduling, and decommissioning) across the Compute nodes.
- **Neutron (Networking Service):** Provides Network-Connectivity-as-a-Service between interface devices managed by other OpenStack services (like Nova). It handles IP allocation, routing, and switching.
- **Cinder (Block Storage):** Provides persistent block storage volumes to Nova virtual machines, allowing data to persist even if the VM instance is destroyed.
- **Swift (Object Storage):** A highly available, distributed, and scalable object storage system. Perfect for storing unstructured data like VM images or backups.
- **Heat (Orchestration Service):** Allows developers to automate the deployment of cloud infrastructure using human-readable templates (Infrastructure as Code - IaC).
- **Octavia (Load Balancer Service):** Delivers scalable, on-demand load balancing capabilities to manage traffic distribution across instances.
- **Horizon (Dashboard):** The web-based graphical user interface (GUI) that allows administrators and users to interact with OpenStack resources easily.

### 3. Monitoring & Observability Stack
- **Prometheus:** A powerful metrics aggregator that scrapes performance data from the Controller, Compute, and Storage nodes.
- **Grafana:** The visualization platform that connects to Prometheus to display real-time graphs, resource utilization dashboards, and system health status.

---

## 📚 References
- [OpenStack Component Services](https://www.openstack.org/software/project-navigator/openstack-components#openstack-services)
- [OpenStack Installation Guide (2026.1)](https://docs.openstack.org/2026.1/install/)
