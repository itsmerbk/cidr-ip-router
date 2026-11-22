import ipaddress

def route_packet(routes, dst_ip):
    ip = ipaddress.ip_address(dst_ip)
    matches = [(ipaddress.ip_network(cidr), gw) for cidr, gw in routes if ip in ipaddress.ip_network(cidr)]
    return max(matches, key=lambda x: x[0].prefixlen)[1]

if __name__ == "__main__":
    rt = [("0.0.0.0/0", "wan0"), ("10.0.0.0/8", "corp0"), ("10.24.1.0/24", "lab0")]
    assert route_packet(rt, "10.24.1.55") == "lab0"
    print("[PASS] 075_cidr_ip_router")
