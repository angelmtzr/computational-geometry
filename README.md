# computational-geometry

This repository contains my own computational geometry Python package: [`geometric`](./geometric). It covers fundamental algorithms and data structures, with a focus on practical applications. Topics covered include:
- 2D Points
- Convex Hull
- Line Segment Intersection
- Polygon/Layer Overlap

The [matplotlib](https://matplotlib.org/) package is used to easily see the outputs of the program in a graphical way.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

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

The [`geometric`](./geometric) package contains several subpackages and modules, including:
- [`convex`](./geometric/convex): contains modules with different algorithms for computing the convex hull of a set of points, as well as a class that facilitates handling and displaying the convex hull.


To use any of these modules, simply import them in your Python code:
```python
from geometric import Point
from geometric.convex import ConvexHull
```

## Contributing

Contributions are welcome! If you find any bugs or want to suggest new features, please open an issue or submit a pull request.
