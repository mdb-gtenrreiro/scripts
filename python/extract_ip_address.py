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


def main():
    """
    Main function to demonstrate the IP extraction functionality.
    """
    # Test cases
    test_strings = [
        "The server is running on 192.168.1.100 port 8080",
        "Connect to https://10.0.0.1:3000 for the dashboard",
        "Invalid IP: 999.999.999.999 and valid IP: 172.16.0.1",
        "IPv6 example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334",
        "No IP address in this string",
        "Multiple IPs: 192.168.1.1, 10.0.0.1, and 172.16.0.1",
        "Edge case: 192.168.1.256 is invalid but 192.168.1.255 is valid"
    ]
    
    print("=== IP Address Extraction Demo ===\n")
    
    for i, test_string in enumerate(test_strings, 1):
        print(f"Test {i}: {test_string}")
        
        # Extract first IP
        first_ip = extract_ip_address(test_string)
        print(f"  First IP found: {first_ip}")
        
        # Extract all IPs
        all_ips = extract_all_ip_addresses(test_string)
        print(f"  All IPs found: {all_ips}")
        print()


if __name__ == "__main__":
    main()
