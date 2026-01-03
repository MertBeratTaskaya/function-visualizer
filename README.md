# Python Function Visualizer

An interactive Python tool for visualizing common mathematical functions with customizable parameters and intelligent graph rendering.

---

## ✨ Key Features

- Supports 10 mathematical function types
- Interactive graph inspection via mouse hover
- Automatic handling of:
  - Undefined points
  - Vertical asymptotes
- Degree-to-radian conversion for trigonometric functions
- Custom coefficient and range input

---

## 📐 Supported Functions

### Algebraic
- Linear: `f(x) = ax + b`
- Quadratic: `f(x) = ax² + bx + c`
- Exponential: `f(x) = a · e^(bx)`
- Logarithmic: `f(x) = a · ln(x)`

### Trigonometric
- `sin(x)`, `cos(x)`, `tan(x)`
- `cot(x)`, `sec(x)`, `csc(x)`

---

## 🚀 Getting Started

```bash
# 1 – Clone the repository
$ git clone https://github.com/MertBeratTaskaya/python-function-visualizer.git
$ cd python-function-visualizer

# 2 – Install dependencies
$ pip install numpy matplotlib mplcursors

# 3 – Run the application
$ python function_visualizer.py
```
📝 Notes
Trigonometric inputs are interpreted in degrees

Vertical asymptotes are displayed as red dashed lines

Undefined values are automatically excluded from plots

---

Made by [@MertBeratTaskaya](https://github.com/MertBeratTaskaya)
