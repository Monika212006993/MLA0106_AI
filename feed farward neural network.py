import math

# ----- Activation Function -----
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# ----- Feed Forward -----
def feed_forward(inputs, weights1, weights2):
    # Hidden layer calculations
    hidden = []
    for neuron_weights in weights1:
        total = sum(i * w for i, w in zip(inputs, neuron_weights))
        hidden.append(sigmoid(total))
    
    # Output layer calculations
    output = []
    for neuron_weights in weights2:
        total = sum(h * w for h, w in zip(hidden, neuron_weights))
        output.append(sigmoid(total))
    
    return hidden, output


# ----- Example Input -----
inputs = [0.5, 0.8]

# Weights for hidden layer: 2 inputs → 2 hidden neurons
weights1 = [
    [0.2, -0.4],
    [0.7,  0.1]
]

# Weights for output layer: 2 hidden → 1 output neuron
weights2 = [
    [1.2, -0.8]
]

# ----- Run Network -----
hidden, output = feed_forward(inputs, weights1, weights2)

print("Hidden Layer Output:", hidden)
print("Final Output:", output)
