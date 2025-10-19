#!/usr/bin/env python3
"""
Generate plots and visualizations script.

This script creates visualizations from processed data.
"""

import sys
from pathlib import Path

# Add src to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from {{ cookiecutter.module_name }}.plots import main as generate_plots

def main():
    """Generate plots and visualizations."""
    print("Starting plot generation...")
    
    # Generate plots
    print("Creating visualizations...")
    generate_plots()
    
    print("Plot generation complete!")

if __name__ == "__main__":
    main()