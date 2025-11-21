#!/usr/bin/env python
"""
Generate sample data files for testing the notebook without real data.
This creates dummy data files with the correct shapes.

WARNING: These are not real training data! 
They are only for testing the notebook execution.
For actual training, you need the real dataset.
"""
import os
import numpy as np

def create_sample_data():
    """Create sample data files with correct shapes."""
    
    print("Creating sample data files...")
    print("⚠ WARNING: These are dummy files for testing only!")
    print("")
    
    # Create ref directory if it doesn't exist
    os.makedirs('ref', exist_ok=True)
    
    # Based on the notebook, we know:
    # - X_train and X_test are RGB images: (N, 128, 256, 3)
    # - y_train is binary mask: (N, 128, 256)
    # - X_test has 1248 samples
    
    # Create training data (smaller set for quick testing)
    n_train = 100
    print(f"Creating X_train.npz: ({n_train}, 128, 256, 3)")
    X_train = np.random.randint(0, 256, size=(n_train, 128, 256, 3), dtype=np.uint8)
    np.savez_compressed('ref/X_train.npz', X_train)
    
    print(f"Creating y_train.npz: ({n_train}, 128, 256)")
    # Create some random lane-like patterns
    y_train = np.zeros((n_train, 128, 256), dtype=np.uint8)
    for i in range(n_train):
        # Add some random lines to simulate lanes
        x_positions = [80, 100, 150, 170]
        for x in x_positions:
            if np.random.random() > 0.3:  # 70% chance of line
                y_train[i, 50:120, max(0, x-2):min(256, x+2)] = 1
    np.savez_compressed('ref/y_train.npz', y_train)
    
    # Create test data
    n_test = 1248
    print(f"Creating X_test.npz: ({n_test}, 128, 256, 3)")
    X_test = np.random.randint(0, 256, size=(n_test, 128, 256, 3), dtype=np.uint8)
    np.savez_compressed('ref/X_test.npz', X_test)
    
    print("")
    print("✓ Sample data files created successfully!")
    print("")
    print("Files created:")
    print("  - ref/X_train.npz")
    print("  - ref/y_train.npz")
    print("  - ref/X_test.npz")
    print("")
    print("You can now run the notebook, but remember:")
    print("  ⚠ These are NOT real training data")
    print("  ⚠ The model will not produce meaningful results")
    print("  ⚠ Replace with real data for actual training")
    print("")

if __name__ == '__main__':
    create_sample_data()
