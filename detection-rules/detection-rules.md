# Elastic Detection Rules - Geo Anomaly Authentication Detection

This document contains example detection rules used during the lab to identify suspicious authentication activity, VPN/TOR usage, and possible impossible travel scenarios.

---

# Rule 1 - TOR Authentication Activity

## Description

Detects authentication events originating from TOR exit nodes.

## Severity

Medium

## Rule Type

KQL

## Query

```kql
tor_exit_node:true and event_type:"login_success"
```

## Possible Indicators

* Anonymous connections
* Credential abuse
* Evasion techniques
* Threat actor infrastructure

---

# Rule 2 - VPN Authentication Activity

## Description

Detects successful authentication events performed through VPN infrastructure.

## Severity

Medium

## Rule Type

KQL

## Query

```kql
vpn:true and event_type:"login_success"
```

## Possible Indicators

* Suspicious remote access
* Geolocation evasion
* Account misuse

---

# Rule 3 - Suspicious Countries Authentication

## Description

Detects authentication activity originating from high-risk countries.

## Severity

High

## Rule Type

KQL

## Query

```kql
country:"Russia" or country:"China" or country:"Iran" or country:"North Korea"
```

## Possible Indicators

* Threat actor activity
* Compromised credentials
* Suspicious geolocation behavior

---

# Rule 4 - Failed Authentication Attempts

## Description

Detects failed login attempts that may indicate brute force activity or credential stuffing.

## Severity

Medium

## Rule Type

KQL

## Query

```kql
event_type:"login_failed"
```

## Possible Indicators

* Password spraying
* Credential stuffing
* Unauthorized access attempts

---

# Rule 5 - TOR + VPN Combined Activity

## Description

Detects authentication activity using both VPN and TOR infrastructure.

## Severity

High

## Rule Type

KQL

## Query

```kql
vpn:true and tor_exit_node:true
```

## Possible Indicators

* Anonymous infrastructure usage
* Advanced evasion techniques
* Potential malicious activity

---

# Rule 6 - Suspicious Successful Authentication

## Description

Detects successful authentications from suspicious countries using TOR or VPN.

## Severity

High

## Rule Type

KQL

## Query

```kql
(country:"Russia" or country:"China" or country:"Iran") and (vpn:true or tor_exit_node:true) and event_type:"login_success"
```

## Possible Indicators

* Potential account compromise
* Suspicious remote access
* Threat actor activity

---

# Rule 7 - Possible Impossible Travel Investigation

## Description

Used during manual threat hunting to investigate possible impossible travel scenarios for specific users.

## Severity

Critical

## Rule Type

KQL

## Query

```kql
user:"finance.user"
```

## Investigation Steps

1. Review timestamps.
2. Compare countries and cities.
3. Analyze elapsed time between events.
4. Validate VPN/TOR activity.
5. Determine if the travel speed is physically impossible.

---

# Rule 8 - Administrative Account Monitoring

## Description

Monitors authentication activity involving privileged or administrative accounts.

## Severity

High

## Rule Type

KQL

## Query

```kql
user:"admin01"
```

## Possible Indicators

* Privileged account misuse
* Credential compromise
* Unauthorized administrative access

---


