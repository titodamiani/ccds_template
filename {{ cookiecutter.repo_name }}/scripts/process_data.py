#!/usr/bin/env python3
"""
Data processing pipeline script.

This script runs the complete data processing pipeline from raw data to processed features.
"""

import sys
from pathlib import Path

# Add src to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from {{ cookiecutter.module_name }}.dataset import main as process_dataset
from {{ cookiecutter.module_name }}.features import main as generate_features

def main():
    """Run the complete data processing pipeline."""
    print("Starting data processing pipeline...")
    
    # Process raw data
    print("Step 1: Processing raw dataset...")
    process_dataset()
    
    # Generate features
    print("Step 2: Generating features...")
    generate_features()
    
    print("Data processing pipeline complete!")

if __name__ == "__main__":
    main()