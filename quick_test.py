#!/usr/bin/env python
"""
Quick test to execute the notebook with minimal training.
This creates a modified version of the notebook that runs faster for testing.
"""
import os
import sys
import numpy as np
import tensorflow as tf
from ref.f1score import f1_score_tensorflow

def quick_test():
    """Run a quick test with 2 epochs to verify everything works."""
    print("=" * 60)
    print("Quick Notebook Execution Test")
    print("=" * 60)
    
    # Suppress TF warnings
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    
    print("\n1. Loading data...")
    X_train = np.load(os.path.join('ref', 'X_train.npz'))['arr_0']
    y_train = np.load(os.path.join('ref', 'y_train.npz'))['arr_0']
    X_test = np.load(os.path.join('ref', 'X_test.npz'))['arr_0']
    print(f"   X_train: {X_train.shape}")
    print(f"   y_train: {y_train.shape}")
    print(f"   X_test: {X_test.shape}")
    
    print("\n2. Preprocessing data...")
    X_train = X_train / 255.0
    y_train = np.expand_dims(y_train, axis=-1)
    X_test = X_test / 255.0
    print("   Data normalized")
    
    print("\n3. Creating model...")
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.optimizers import Adam
    
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
    print(f"   Model created with {model.count_params():,} parameters")
    
    print("\n4. Training model (2 epochs for testing)...")
    history = model.fit(X_train, y_train, epochs=2, batch_size=16, 
                       validation_split=0.2, verbose=1)
    
    print("\n5. Making predictions...")
    y_pred = model.predict(X_test, verbose=0)
    print(f"   Predictions shape: {y_pred.shape}")
    
    print("\n6. Saving predictions...")
    os.makedirs('submission', exist_ok=True)
    output_file = os.path.join('submission', 'test_submission.npz')
    np.savez(output_file, y_pred)
    print(f"   Saved to: {output_file}")
    
    print("\n" + "=" * 60)
    print("✓ Quick test completed successfully!")
    print("=" * 60)
    print("\nThe notebook is ready to run with:")
    print("  jupyter notebook train_example.ipynb")
    print("\nNote: This was a quick test with sample data.")
    print("For actual training, use the real dataset and more epochs.")
    
    return 0

if __name__ == '__main__':
    try:
        sys.exit(quick_test())
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
