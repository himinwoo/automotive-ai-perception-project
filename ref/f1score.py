import tensorflow as tf

def f1_score_tensorflow(y_true, y_pred):
    y_pred = tf.cast(y_pred > 0.5, tf.float32)
    y_true = tf.cast(y_true, tf.float32)

    y_pred_flat = tf.reshape(y_pred, [-1])
    y_true_flat = tf.reshape(y_true, [-1])

    TP = tf.reduce_sum(y_pred_flat * y_true_flat)
    FP = tf.reduce_sum(y_pred_flat * (1 - y_true_flat))
    FN = tf.reduce_sum((1 - y_pred_flat) * y_true_flat)

    precision = TP / (TP + FP + 1e-8)
    recall = TP / (TP + FN + 1e-8)

    return 2 * (precision * recall) / (precision + recall + 1e-8)
