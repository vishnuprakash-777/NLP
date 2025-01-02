import math
from collections import Counter

# Function to calculate entropy
def calculate_entropy(text):
    # Tokenize the text into words
    words = text.split()
    word_count = len(words)
    
    # Count the frequency of unigrams
    freq = Counter(words)
    
    # Calculate entropy
    entropy = 0
    for word, count in freq.items():
        prob = count / word_count  # Probability of the word
        entropy += prob * math.log2(prob)  # Contribution to entropy
    
    entropy = -entropy  # Convert entropy to positive
    return entropy

# Function to calculate perplexity
def calculate_perplexity(entropy):
    # Perplexity is 2^entropy
    perplexity = pow(2, entropy)
    return perplexity

# Example Usage
text = "this is a sample text this is a test"

# Calculate entropy
entropy = calculate_entropy(text)
print("Entropy:", entropy)

# Calculate perplexity
perplexity = calculate_perplexity(entropy)
print("Perplexity:", perplexity)
