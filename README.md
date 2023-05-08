# computational-geometry

This repository contains my own computational geometry Python package: `geometric`.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

The `geometric` package covers fundamental algorithms and data structures used in computational geometry, with a focus on practical applications. Topics covered include:
- 2D Points
- Convex Hull
- Line Segment Intersection
- Polygon/Layer Overlap

## Getting Started

### Prerequisites

- Python 3.10
- pip (package installer for Python)

### Installation

1. Clone the repository:

```sh
git clone https://github.com/angelmtzr/computational-geometry.git
```

2. Install the required packages:

```sh
pip install -r requirements.txt
```

## Usage

The `geometric` package contains several subpackages and modules, including:
- `convex`: a package for computing the convex hull of a set of points.


To use any of these modules, simply import them in your Python code:
```python
from geometric import Point
from geometric.convex import ConvexHull
```

## Contributing

Contributions are welcome! If you find any bugs or want to suggest new features, please open an issue or submit a pull request.

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more information.
