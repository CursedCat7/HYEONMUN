import requests

TOR_EXIT_NODES_URL = "https://check.torproject.org/torbulkexitlist"

def get_tor_exit_nodes():
    try:
        response = requests.get(TOR_EXIT_NODES_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return set(response.text.splitlines())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Tor exit nodes: {e}")
        return set()

TOR_EXIT_NODES = get_tor_exit_nodes()

def check_ip(ip: str) -> bool:
    """Check if IP is a Tor exit node"""
    return ip in TOR_EXIT_NODES


