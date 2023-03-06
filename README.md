# Cloudflare Status API

A custom plugin 'Special Agent' for CheckMK to query the publicly available www.cloudflarestatus.com API and retrieve services and report on their state.

For usage, create a dummy host and set the host configuration as:
* IP address family - No IP
* Checkmk agent / API integrations - Configured API Integrations, no Checkmk agent
* SNMP - No SNMP
