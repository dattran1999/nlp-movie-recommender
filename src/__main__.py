import os.path
import sys
path = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

from .cosine_similarity import main as cosine_similarity
if __name__ == "__main__":
    cosine_similarity()
