# Cloudflare Status API

A custom plugin 'Special Agent' for CheckMK to query the publicly available www.cloudflarestatus.com API and retrieve services and report on their state.

For usage
1. Create a dummy host
2. Set the host configuration as:
    * IP address family - No IP
    * Checkmk agent / API integrations - Configured API Integrations, no Checkmk agent
    * SNMP - No SNMP
3. Setup a rule under "Cloudflare API Component Checks" associated to the dummy host.
    * Check the URL box
    * Add your dummy host to the explicit hosts list.
4. Perform a Service Discovery on your dummy host.
5. Choose what services to ignore or monitor.
6. Commit your changes.

TO DO:  
Swap to using JSON output on data query (didn't know it support it originally)
Consolidate yield statements
More meaningful webui options?
Is a URL necessary since it defaults and isn't part of the check, only the script to pull data.
