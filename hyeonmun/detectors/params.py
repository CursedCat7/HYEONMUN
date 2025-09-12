from urllib.parse import urlparse, parse_qs
import re

# SQL Injection, XSS, LFI check patterns
SUSPICIOUS_PATTERNS = [
    # SQL Injection
    r"\b(union\s+select|select\s+.+from|insert\s+into|delete\s+from|drop\s+table|alter\s+table|truncate\s+table|exec\s+|xp_cmdshell|benchmark|sleep)\b",
    r"(\'|\")\s*(or|and)\s*(\'|\")?1\s*=\s*1",
    r"\b(cast|convert)\b\s*\(\s*.*\s*as\s*.*\s*\)",
    r"\b(information_schema|pg_catalog)\b",
    r"\b(load_file|outfile|dumpfile)\b",
    r"\b(into\s+outfile|into\s+dumpfile)\b",

    # XSS
    r"<script>|<svg/onload=|javascript:|onmouseover=|onerror=|onload=|alert\(|confirm\(|prompt\(",
    r"<img\s+src\s*=\s*['\"]?javascript:",
    r"<body\s+onload=",
    r"eval\(|document\.write\(|window\.location=",

    # Local File Inclusion (LFI) / Path Traversal
    r"\.\./|\.\.\\|%2e%2e%2f|%2e%2e%5c",
    r"/etc/passwd|/windows/win.ini|/proc/self/environ",
    r"file:///",

    # Command Injection
    r"\|\||&|;|\\n|`|\$\(|\$\{",


    r"\'", r"\"", r"--", r";", r"/\*", r"\*/", r"<", r">", r"=", r"\(", r"\)", r"\{", r"\}", r"\`"
]

async def check_params(request) -> bool:
    """Return True if suspicious query or body parameters are found"""
    # Check query parameters
    query_params = parse_qs(urlparse(str(request.url)).query)
    for values in query_params.values():
        for v in values:
            if isinstance(v, str):
                for pattern in SUSPICIOUS_PATTERNS:
                    if re.search(pattern, v, re.IGNORECASE):
                        return True
                # Check for unusually long parameter values
                if len(v) > 2048: 
                    return True

    # Check JSON body parameters
    try:
        json_data = await request.json()
        if isinstance(json_data, dict):
            for v in json_data.values():
                if isinstance(v, str):
                    for pattern in SUSPICIOUS_PATTERNS:
                        if re.search(pattern, v, re.IGNORECASE):
                            return True
                    if len(v) > 2048:
                        return True
                elif isinstance(v, (list, dict)): 
                    pass
    except Exception:
        pass

    # Check form data (if applicable)
    try:
        form_data = await request.form()
        for v in form_data.values():
            if isinstance(v, str):
                for pattern in SUSPICIOUS_PATTERNS:
                    if re.search(pattern, v, re.IGNORECASE):
                        return True
                if len(v) > 2048:
                    return True
    except Exception: 
        pass

    return False



