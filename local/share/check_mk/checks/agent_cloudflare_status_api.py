#!/usr/bin/env python3

def agent_cloudflare_status_api_arguments(params, hostname, ipaddress):
    args = []
    _url = params['url']
    if _url:
       args += ['-u',_url]
    return args

special_agent_info["cloudflare_status_api"] = agent_cloudflare_status_api_arguments
