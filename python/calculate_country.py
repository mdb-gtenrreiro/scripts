#!/usr/bin/env python3
"""
Python script that determines the country or body of water for given coordinates.
"""

import sys
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError


def calculate_country(latitude: float, longitude: float) -> str:
    """
    Determines the country or body of water for given latitude and longitude.

    Args:
        latitude (float): The latitude coordinate
        longitude (float): The longitude coordinate

    Returns:
        str: The name of the country or body of water
    """
    try:
        # Initialize the geocoder
        geolocator = Nominatim(user_agent="calculate_country_script")

        # Perform reverse geocoding
        location = geolocator.reverse(f"{latitude}, {longitude}", timeout=10)

        if location is None:
            return "Unknown location"

        # Extract address components
        address = location.raw.get('address', {})

        # Try to get country first
        country = address.get('country')
        if country:
            return country

        # If no country, check for body of water or other geographic features
        body_of_water = (
            address.get('body_of_water') or
            address.get('water') or
            address.get('sea') or
            address.get('ocean') or
            address.get('bay') or
            address.get('lake') or
            address.get('river')
        )

        if body_of_water:
            return body_of_water

        # Check display name for water bodies if not in address components
        display_name = location.raw.get('display_name', '')
        if any(water_word in display_name.lower() for water_word in
               ['ocean', 'sea', 'bay', 'lake', 'river', 'strait', 'gulf']):
            # Extract the first part which is usually the water body name
            parts = display_name.split(',')
            if parts:
                return parts[0].strip()

        # If we have a location but no specific country or water body
        if location.address:
            return f"International waters or unspecified location: {location.address}"

        return "Unknown location"

    except GeocoderTimedOut:
        return "Error: Geocoding service timed out"
    except GeocoderServiceError as e:
        return f"Error: Geocoding service error - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"


def main(latitude_str: str, longitude_str: str):
    """
    Main function that processes the latitude and longitude parameters.

    Args:
        latitude_str (str): The latitude as a string
        longitude_str (str): The longitude as a string
    """
    try:
        # Convert string parameters to float
        latitude = float(latitude_str)
        longitude = float(longitude_str)

        # Validate coordinate ranges
        if not (-90 <= latitude <= 90):
            print("Error: Latitude must be between -90 and 90 degrees")
            return

        if not (-180 <= longitude <= 180):
            print("Error: Longitude must be between -180 and 180 degrees")
            return

        # Calculate and print the result
        result = calculate_country(latitude, longitude)
        print(result)
        return result

    except ValueError:
        print("Error: Latitude and longitude must be valid numbers")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python calculate_country.py <latitude> <longitude>")
        print("Example: python calculate_country.py 40.7128 -74.0060")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
