#!/usr/bin/env python3
"""
Python script that returns a BSON object with a message field.
"""

from bson import BSON
import json


def create_hello_bson():
    """
    Creates and returns a BSON object with a message field.
    
    Returns:
        bytes: BSON-encoded data
    """
    # Create the document
    document = {
        "message": "Hello World from Python"
    }
    
    # Encode to BSON
    bson_data = BSON.encode(document)
    
    return bson_data


def main():
    """
    Main function that creates the BSON object and displays information about it.
    """
    # Create the BSON object
    bson_data = create_hello_bson()
    
    # Display information
    print("BSON object created successfully!")
    print(f"BSON data (bytes): {bson_data}")
    print(f"BSON data length: {len(bson_data)} bytes")
    
    # Decode back to verify
    decoded = BSON(bson_data).decode()
    print(f"Decoded document: {json.dumps(decoded, indent=2)}")
    
    return bson_data


if __name__ == "__main__":
    main()
