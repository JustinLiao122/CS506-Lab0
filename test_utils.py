## Please fill in all the parts labeled as ### YOUR CODE HERE

import numpy as np
import pytest
from utils import *

def test_dot_product():
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])
    
    result = dot_product(vector1, vector2)
    
    assert result == 32, f"Expected 32, but got {result}"
    
def test_cosine_similarity():
    ### YOUR CODE HERE
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])

    result = cosine_similarity(vector1, vector2)
    
    expected_result = 0.9746318461970762
    
    assert np.isclose(result, expected_result), f"Expected {expected_result}, but got {result}"

def test_nearest_neighbor():
    ### YOUR CODE HERE
    vector1 = np.array([1, 2, 3])
    
    vectors = np.array([[3, 1, 1], [7, 3, 5], [8, 7, 6]])
    result = nearest_neighbor(vector1, vectors)
    
    expected_index = 2
    
    assert result == expected_index, f"Expected index {expected_index}, but got {result}"
