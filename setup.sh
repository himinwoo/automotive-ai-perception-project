#!/bin/bash

echo "======================================"
echo "Automotive AI Perception Project Setup"
echo "======================================"
echo ""

# Check Python version
echo "Checking Python version..."
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
echo "Current Python version: $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python -m venv venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo ""

# Check if data files exist
echo "Checking for data files..."
MISSING_FILES=0
if [ ! -f "ref/X_train.npz" ]; then
    echo "⚠ Missing: ref/X_train.npz"
    MISSING_FILES=1
fi
if [ ! -f "ref/y_train.npz" ]; then
    echo "⚠ Missing: ref/y_train.npz"
    MISSING_FILES=1
fi
if [ ! -f "ref/X_test.npz" ]; then
    echo "⚠ Missing: ref/X_test.npz"
    MISSING_FILES=1
fi

if [ $MISSING_FILES -eq 0 ]; then
    echo "✓ All data files found!"
else
    echo ""
    echo "⚠ Please add the missing .npz data files to the ref/ directory"
    echo "  before running the notebook."
fi
echo ""

# Create submission directory if it doesn't exist
if [ ! -d "submission" ]; then
    mkdir submission
    echo "Created submission directory."
fi
echo ""

echo "======================================"
echo "Setup complete!"
echo "======================================"
echo ""
echo "To start Jupyter Notebook, run:"
echo "  source venv/bin/activate"
echo "  jupyter notebook"
echo ""
