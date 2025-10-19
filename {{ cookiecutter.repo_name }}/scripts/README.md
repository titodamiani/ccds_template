# Scripts Directory

This directory contains standalone executable scripts for running various pipelines and tasks.

## Available Scripts

- `process_data.py` - Complete data processing pipeline from raw to processed data
- `train_model.py` - Model training pipeline 
- `predict.py` - Model inference/prediction pipeline
- `generate_plots.py` - Visualization and plotting pipeline

## Usage

Scripts can be run directly from the project root:

```bash
python scripts/process_data.py
python scripts/train_model.py  
python scripts/predict.py
python scripts/generate_plots.py
```

Or using the Makefile shortcuts:

```bash
make data      # Run data processing
make train     # Run model training
make predict   # Run predictions
make plots     # Generate visualizations
```

## Design Philosophy

Scripts in this directory are meant to be:
- **Executable**: Can be run directly from command line
- **Pipeline-oriented**: Orchestrate multiple steps or modules
- **Self-contained**: Handle their own argument parsing and error handling
- **Import from src/**: Use reusable code from the `src/` package

The `src/` directory contains the reusable library code that these scripts import and orchestrate.