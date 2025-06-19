# AC-3 Algorithm Implementation

This repository contains an implementation of the AC-3 (Arc Consistency Algorithm #3) algorithm, which is a fundamental algorithm in artificial intelligence for solving Constraint Satisfaction Problems (CSPs).

## Overview

The AC-3 algorithm is used to achieve arc consistency in a constraint satisfaction problem. It works by ensuring that for any two variables with a constraint between them, all values in one variable's domain are consistent with at least one value in the other variable's domain.

## Features

- Pure Python implementation of AC-3 algorithm
- Support for various constraint satisfaction problems
- Easy-to-understand code structure
- Efficient implementation with queue-based approach

## How It Works

The algorithm works through these main steps:

1. Initialize a queue with all arcs in the CSP
2. While the queue is not empty:
   - Remove an arc (X,Y) from the queue
   - If the domain of X is reduced when making it arc consistent with Y:
     - Add all arcs (Z,X) to the queue where Z is a neighbor of X

## Usage

```python
# Example usage of the AC-3 algorithm
# Initialize your CSP with domains and constraints
csp = {
    'x': {'domain': {1, 2, 3}},
    'y': {'domain': {1, 2, 3}},
    # ... more variables
}

# Run the AC-3 algorithm
result = ac3(csp, arcs)
```

## Requirements

- Python 3.x
- No additional dependencies required

## Installation

Clone this repository:
```bash
git clone https://github.com/myselfaryan/AC-3-algorithm.git
cd AC-3-algorithm
```

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating your feature branch (`git checkout -b feature/amazing-feature`)
3. Committing your changes (`git commit -m 'Add some amazing feature'`)
4. Pushing to the branch (`git push origin feature/amazing-feature`)
5. Opening a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Aryan
- Roll No: S20220010021

## Acknowledgments

- Thanks to all contributors and the AI community
- Special thanks to the original AC-3 algorithm developers
