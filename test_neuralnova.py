# test_neuralnova.py
"""
Tests for NeuralNova module.
"""

import unittest
from neuralnova import NeuralNova

class TestNeuralNova(unittest.TestCase):
    """Test cases for NeuralNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralNova()
        self.assertIsInstance(instance, NeuralNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
