#!/usr/bin/env python3
"""
Training pipeline script.

This script runs the complete model training pipeline.
"""

import sys
from pathlib import Path

# Add src to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from {{ cookiecutter.module_name }}.modeling.train import main as train_model

def main():
    """Run the model training pipeline."""
    print("Starting model training pipeline...")
    
    # Train model
    print("Training model...")
    train_model()
    
    print("Model training complete!")

if __name__ == "__main__":
    main()