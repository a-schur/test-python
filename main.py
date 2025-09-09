#!/usr/bin/env python3
"""
A simple Python script that uses outdated dependencies.
This is for testing dependabot-core locally.
"""

import requests
import numpy as np


def fetch_data():
    """Fetch some sample data from a public API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()


def process_data(data):
    """Process the data with numpy."""
    # Create a simple array
    arr = np.array([1, 2, 3, 4, 5])
    return {
        "original_data": data,
        "array_sum": np.sum(arr),
        "array_mean": np.mean(arr)
    }


def main():
    """Main function."""
    print("Fetching data...")
    data = fetch_data()
    print(f"Fetched: {data['title']}")
    
    print("Processing with numpy...")
    result = process_data(data)
    print(f"Array sum: {result['array_sum']}")
    print(f"Array mean: {result['array_mean']}")


if __name__ == "__main__":
    main()
