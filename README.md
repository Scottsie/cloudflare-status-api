# Cloudflare Status API

A custom plugin 'Special Agent' for CheckMK to query the publicly available www.cloudflarestatus.com API and retrieve services and report on their state.

For usage
1. Create a dummy host
2. Set the host configuration as:
  * IP address family - No IP
  * Checkmk agent / API integrations - Configured API Integrations, no Checkmk agent
  * SNMP - No SNMP
3. Setup a rule under "Cloudflare API Component Checks" associated to the dummy host.

TO DO:  
Consolidate yield statements  
More meaningful webui options?
