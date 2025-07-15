#!/usr/bin/env python3
"""
Python script that extracts IP addresses from strings.
"""

import re
import ipaddress
from typing import Optional, List


def extract_ip_address(text: str) -> Optional[str]:
    """
    Extracts the first valid IP address from a given string.

    Args:
        text (str): The input string that might contain an IP address

    Returns:
        Optional[str]: The first valid IP address found, or None if no valid IP is found
    """
    if not text:
        return None

    # Regular expression pattern for IPv4 addresses
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

    # Regular expression pattern for IPv6 addresses (simplified)
    ipv6_pattern = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b|\b(?:[0-9a-fA-F]{1,4}:){1,7}:|\b::(?:[0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}\b|\b::1\b|\b::\b'

    # Find all potential IP addresses
    potential_ips = []

    # Find IPv4 addresses
    ipv4_matches = re.findall(ipv4_pattern, text)
    potential_ips.extend(ipv4_matches)

    # Find IPv6 addresses
    ipv6_matches = re.findall(ipv6_pattern, text)
    potential_ips.extend(ipv6_matches)

    # Validate each potential IP address
    for ip in potential_ips:
        try:
            # Use ipaddress module to validate
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            continue

    return None


def extract_all_ip_addresses(text: str) -> List[str]:
    """
    Extracts all valid IP addresses from a given string.

    Args:
        text (str): The input string that might contain IP addresses

    Returns:
        List[str]: A list of all valid IP addresses found
    """
    if not text:
        return []

    # Regular expression pattern for IPv4 addresses
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

    # Regular expression pattern for IPv6 addresses (simplified)
    ipv6_pattern = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b|\b(?:[0-9a-fA-F]{1,4}:){1,7}:|\b::(?:[0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}\b|\b::1\b|\b::\b'

    # Find all potential IP addresses
    potential_ips = []

    # Find IPv4 addresses
    ipv4_matches = re.findall(ipv4_pattern, text)
    potential_ips.extend(ipv4_matches)

    # Find IPv6 addresses
    ipv6_matches = re.findall(ipv6_pattern, text)
    potential_ips.extend(ipv6_matches)

    # Validate each potential IP address
    valid_ips = []
    for ip in potential_ips:
        try:
            # Use ipaddress module to validate
            ipaddress.ip_address(ip)
            valid_ips.append(ip)
        except ValueError:
            continue

    return valid_ips


def main(input_string: str):
    """
    Main function that extracts IP address from the provided string.

    Args:
        input_string (str): The string to search for IP addresses
    """
    ip_address = extract_ip_address(input_string)
    print(ip_address)
    return ip_address


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python extract_ip_address.py <string_to_search>")
        sys.exit(1)

    main(sys.argv[1])
