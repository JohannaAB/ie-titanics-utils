"""
IE Titanic utils.
"""

__version__ = "0.1.0"  # semver.org

import pandas as pd
import sys 

from ie_utils import tokenize

def main():
    print(tokenize(sys.argv[1]))
    
if __name__ == "__main__":
    main()
