# Cloudflare Status API

A custom plugin 'Special Agent' for CheckMK to query the publicly available www.cloudflarestatus.com API and retrieve services and report on their state.

For usage
1. Create a dummy host
    A. Set the host configuration as:
      * IP address family - No IP
      * Checkmk agent / API integrations - Configured API Integrations, no Checkmk agent
      * SNMP - No SNMP
2. Setup a rule under "Cloudflare API Component Checks" associated to the dummy host.
    1. Check the URL box
    2. Add your dummy host to the explicit hosts list.
3. Perform a Service Discovery on your dummy host.
4. Choose what to ignore or monitor.
5. Commit your changes.

TO DO:  
Consolidate yield statements
More meaningful webui options?
Is a URL necessary since it defaults and isn't part of the check, only the script to pull data.
