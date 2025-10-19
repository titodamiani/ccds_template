#!/usr/bin/env python3
"""
Prediction pipeline script.

This script runs model inference on new data.
"""

import sys
from pathlib import Path

# Add src to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from {{ cookiecutter.module_name }}.modeling.predict import main as predict

def main():
    """Run the prediction pipeline."""
    print("Starting prediction pipeline...")
    
    # Make predictions
    print("Generating predictions...")
    predict()
    
    print("Prediction pipeline complete!")

if __name__ == "__main__":
    main()