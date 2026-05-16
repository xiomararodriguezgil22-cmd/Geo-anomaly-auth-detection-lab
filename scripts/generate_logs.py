import json
import random
from datetime import datetime, timedelta

# ==========================================
# CONFIGURACIÓN GENERAL
# ==========================================

TOTAL_EVENTS = 300

# Fecha inicial del laboratorio
BASE_TIME = datetime(2026, 5, 13, 7, 0, 0)

# ==========================================
# USUARIOS SIMULADOS
# ==========================================

users = [
    "jrodriguez",
    "agarcia",
    "mlopez",
    "dtorres",
    "admin01",
    "finance.user",
    "hr.manager",
    "soc.analyst"
]

# ==========================================
# UBICACIONES NORMALES
# ==========================================

normal_locations = [
    {
        "country": "Colombia",
        "city": "Bogota",
        "latitude": 4.7110,
        "longitude": -74.0721,
        "isp": "Claro Colombia"
    },
    {
        "country": "Mexico",
        "city": "Mexico City",
        "latitude": 19.4326,
        "longitude": -99.1332,
        "isp": "Telmex"
    },
    {
        "country": "Peru",
        "city": "Lima",
        "latitude": -12.0464,
        "longitude": -77.0428,
        "isp": "Claro Peru"
    },
    {
        "country": "USA",
        "city": "Miami",
        "latitude": 25.7617,
        "longitude": -80.1918,
        "isp": "AT&T"
    }
]

# ==========================================
# UBICACIONES SOSPECHOSAS
# ==========================================

suspicious_locations = [
    {
        "country": "Russia",
        "city": "Moscow",
        "latitude": 55.7558,
        "longitude": 37.6173,
        "isp": "Moscow Telecom"
    },
    {
        "country": "China",
        "city": "Beijing",
        "latitude": 39.9042,
        "longitude": 116.4074,
        "isp": "China Telecom"
    },
    {
        "country": "Iran",
        "city": "Tehran",
        "latitude": 35.6892,
        "longitude": 51.3890,
        "isp": "IranNet"
    }
]

# ==========================================
# DISPOSITIVOS
# ==========================================

devices = [
    "Windows 10",
    "Windows 11",
    "Ubuntu 22.04",
    "macOS Ventura",
    "iPhone 15",
    "Android 14"
]

# ==========================================
# FUNCIÓN PARA GENERAR IPs ALEATORIAS
# ==========================================

def generate_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

# ==========================================
# LISTA FINAL DE EVENTOS
# ==========================================

events = []

# ==========================================
# GENERACIÓN DE EVENTOS NORMALES
# ==========================================

for i in range(260):

    location = random.choice(normal_locations)

    event = {
        "@timestamp": (
            BASE_TIME + timedelta(minutes=i * random.randint(1, 5))
        ).isoformat(),

        "user": random.choice(users),

        "src_ip": generate_ip(),

        "country": location["country"],
        "city": location["city"],

        "latitude": location["latitude"],
        "longitude": location["longitude"],

        "event_type": random.choice([
            "login_success",
            "login_success",
            "login_success",
            "login_failed"
        ]),

        "device": random.choice(devices),

        "isp": location["isp"],

        "vpn": random.choice([True, False]),

        "tor_exit_node": random.choice([
            False,
            False,
            False,
            True
        ]),

        "asn": f"AS{random.randint(1000,99999)} {location['isp']}"
    }

    events.append(event)

# ==========================================
# GENERACIÓN DE IMPOSSIBLE TRAVEL
# ==========================================

for i in range(20):

    user = random.choice(users)

    origin = random.choice(normal_locations)

    destination = random.choice(suspicious_locations)

    # Primer login
    first_time = BASE_TIME + timedelta(
        hours=random.randint(1, 8)
    )

    # Segundo login pocos minutos después
    second_time = first_time + timedelta(
        minutes=random.randint(2, 10)
    )

    login_1 = {
        "@timestamp": first_time.isoformat(),

        "user": user,

        "src_ip": generate_ip(),

        "country": origin["country"],
        "city": origin["city"],

        "latitude": origin["latitude"],
        "longitude": origin["longitude"],

        "event_type": "login_success",

        "device": random.choice(devices),

        "isp": origin["isp"],

        "vpn": False,

        "tor_exit_node": False,

        "asn": f"AS{random.randint(1000,99999)} {origin['isp']}"
    }

    login_2 = {
        "@timestamp": second_time.isoformat(),

        "user": user,

        "src_ip": generate_ip(),

        "country": destination["country"],
        "city": destination["city"],

        "latitude": destination["latitude"],
        "longitude": destination["longitude"],

        "event_type": "login_success",

        "device": random.choice(devices),

        "isp": destination["isp"],

        "vpn": True,

        "tor_exit_node": random.choice([True, False]),

        "asn": f"AS{random.randint(1000,99999)} {destination['isp']}"
    }

    events.append(login_1)
    events.append(login_2)

# ==========================================
# ORDENAR EVENTOS POR TIEMPO
# ==========================================

events.sort(key=lambda x: x["@timestamp"])

# ==========================================
# EXPORTAR A NDJSON
# ==========================================

with open("geo-anomaly-auth-detection.ndjson", "w") as file:

    for event in events:
        file.write(json.dumps(event) + "\n")

print("Successfully generated data set.")