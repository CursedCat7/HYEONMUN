import requests

# proxycheck.io maby
PROXYCHECK_API_URL = "http://proxycheck.io/v2/{ip}?key=YOUR_API_KEY&vpn=1&asn=1"

#API key set .env or sh later
API_KEY = "YOUR_API_KEY" 

def check_ip(ip: str) -> bool:
    """Check if IP is VPN / Proxy / Datacenter using proxycheck.io API"""
    if API_KEY == "YOUR_API_KEY":
        print("Warning: Please replace 'YOUR_API_KEY' with your actual proxycheck.io API key.")
        return False 

    try:
        response = requests.get(PROXYCHECK_API_URL.format(ip=ip, key=API_KEY))
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        if ip in data:
            # VPN, Proxy, ASN (Datacenter) check
            is_vpn = data[ip].get('vpn') == 'yes'
            is_proxy = data[ip].get('proxy') == 'yes'
            is_asn_datacenter = data[ip].get('asn') and data[ip]['asn'].get('type') == 'datacenter'
            
            return is_vpn or is_proxy or is_asn_datacenter
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking IP with proxycheck.io: {e}")
        return False
    except ValueError:
        print(f"Error decoding JSON response from proxycheck.io for IP: {ip}")
        return False


