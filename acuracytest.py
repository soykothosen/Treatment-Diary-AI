def calculate_accuracy(actual, predicted):
    """
    Calculate accuracy given actual and predicted labels.
    
    :param actual: List of actual labels (ground truth).
    :param predicted: List of predicted labels.
    :return: Accuracy as a float.
    """
    if len(actual) != len(predicted):
        raise ValueError("The lengths of actual and predicted lists must be the same.")
    
    correct_predictions = sum([1 for a, p in zip(actual, predicted) if a == p])
    total_predictions = len(actual)
    accuracy = correct_predictions / total_predictions
    
    return accuracy

# Example Data
actual_medicines = ["Paracetamol", "Ibuprofen", "Amlodipine", "Metformin"]
predicted_medicines = ["Paracetamol", "Aspirin", "Amlodipine", "Metformin"]

# Calculate Accuracy
accuracy = calculate_accuracy(actual_medicines, predicted_medicines)
print(f"Accuracy: {accuracy * 100:.2f}%")
