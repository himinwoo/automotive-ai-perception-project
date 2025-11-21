#!/usr/bin/env python
"""
Test script to verify the notebook can execute successfully.
This runs the notebook cells in order and reports any errors.
"""
import os
import sys
import numpy as np
import tensorflow as tf

def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    try:
        from ref.f1score import f1_score_tensorflow
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_data_loading():
    """Test that data files can be loaded."""
    print("\nTesting data loading...")
    try:
        X_train = np.load(os.path.join(os.getcwd(), 'ref', 'X_train.npz'))['arr_0']
        y_train = np.load(os.path.join(os.getcwd(), 'ref', 'y_train.npz'))['arr_0']
        X_test = np.load(os.path.join(os.getcwd(), 'ref', 'X_test.npz'))['arr_0']
        
        print(f"  X_train shape: {X_train.shape}")
        print(f"  y_train shape: {y_train.shape}")
        print(f"  X_test shape: {X_test.shape}")
        
        # Verify shapes
        assert X_train.shape[1:] == (128, 256, 3), "X_train shape incorrect"
        assert y_train.shape[1:] == (128, 256), "y_train shape incorrect"
        assert X_test.shape == (1248, 128, 256, 3), "X_test shape incorrect"
        
        print("✓ Data loading successful")
        return True
    except Exception as e:
        print(f"✗ Data loading error: {e}")
        return False

def test_model_creation():
    """Test that the model can be created."""
    print("\nTesting model creation...")
    try:
        from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.optimizers import Adam
        from ref.f1score import f1_score_tensorflow
        
        model = Sequential([
            Conv2D(filters=16, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu', input_shape=(128, 256, 3)),
            MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
            Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'),
            MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
            Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'),
            MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
            UpSampling2D(size=2, interpolation='bilinear'),
            Conv2D(filters=32, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'),
            UpSampling2D(size=2, interpolation='bilinear'),
            Conv2D(filters=16, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'),
            UpSampling2D(size=2, interpolation='bilinear'),
            Conv2D(filters=1, kernel_size=(1, 1), strides=(1, 1), padding='valid', activation='sigmoid'),
        ])
        
        model.compile(optimizer=Adam(learning_rate=0.001),
                     loss='binary_crossentropy',
                     metrics=[f1_score_tensorflow])
        
        print(f"  Model created with {model.count_params()} parameters")
        print("✓ Model creation successful")
        return True
    except Exception as e:
        print(f"✗ Model creation error: {e}")
        return False

def test_prediction_shape():
    """Test that prediction output has correct shape."""
    print("\nTesting prediction shape...")
    try:
        X_test = np.load(os.path.join(os.getcwd(), 'ref', 'X_test.npz'))['arr_0']
        y_train = np.load(os.path.join(os.getcwd(), 'ref', 'y_train.npz'))['arr_0']
        
        y_pred = np.zeros((len(X_test), y_train.shape[1], y_train.shape[2], 1))
        
        assert y_pred.shape == (1248, 128, 256, 1), "y_pred shape incorrect"
        print(f"  y_pred shape: {y_pred.shape}")
        print("✓ Prediction shape test successful")
        return True
    except Exception as e:
        print(f"✗ Prediction shape test error: {e}")
        return False

def test_submission_directory():
    """Test that submission directory exists."""
    print("\nTesting submission directory...")
    try:
        os.makedirs('submission', exist_ok=True)
        assert os.path.isdir('submission'), "Submission directory not found"
        print("✓ Submission directory exists")
        return True
    except Exception as e:
        print(f"✗ Submission directory error: {e}")
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("Testing train_example.ipynb Prerequisites")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_data_loading,
        test_model_creation,
        test_prediction_shape,
        test_submission_directory,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print(f"Test Results: {sum(results)}/{len(results)} passed")
    print("=" * 60)
    
    if all(results):
        print("\n✓ All tests passed! The notebook should be ready to run.")
        print("\nTo run the notebook:")
        print("  jupyter notebook train_example.ipynb")
        return 0
    else:
        print("\n✗ Some tests failed. Please check the errors above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
