# Numerical Integration Calculator

A graphical user interface (GUI) application for computing numerical integration using the **Trapezoidal Rule**, **Simpson's Rule**, and **Scipy's Quad Integration**. This application allows users to input a function, define integration limits, specify the number of intervals, and visualize the function's graph interactively.

## Features
- **Supports numerical integration** using:
  - Trapezoidal Rule
  - Simpson’s Rule
  - Standard Integration (using SciPy's `quad` function)
- **Graphical Representation** of the function with an interactive hover effect displaying (x, y) values.
- **Tkinter-based GUI** with a modern `ttkbootstrap` theme.
- **Reset/Compute Again Button** to allow multiple calculations.

## Installation & Setup
### Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Required Libraries
Install the dependencies using:

```sh
pip install numpy matplotlib scipy ttkbootstrap
```

### Running the Application
To start the application, run:

```sh
python main.py
```

## Usage
1. **Enter a function** in terms of `x`, e.g., `np.sin(x) + x**2`.
2. **Specify integration limits** (Lower Limit `a` and Upper Limit `b`).
3. **Enter the number of intervals** for numerical methods.
4. **Click "Integrate"** to compute results.
5. **View results** for Trapezoidal, Simpson’s, and Standard integration.
6. **Hover over the graph** to see dynamic `(x, y)` values.
7. **Click "Compute Again"** to reset inputs and perform a new calculation.

## Code Overview
### 1. Safe Expression Evaluation
The `safe_eval` function ensures user-defined functions are evaluated securely, allowing only `x` and `numpy` operations.

### 2. Numerical Integration Methods
- **Trapezoidal Rule**: Approximates the integral using trapezoids.
- **Simpson’s Rule**: Uses parabolic interpolation for better accuracy.
- **SciPy's Quad Function**: Provides a standard reference for integration.

### 3. Interactive Graphing
- **Matplotlib plots** the function over the given range.
- **Hover effect** dynamically updates `(x, y)` values without redrawing.

### 4. GUI Elements
- **Tkinter-based layout** using `ttkbootstrap`.
- **Form fields for function input, limits, and intervals**.
- **Buttons for calculation and reset actions**.


## Future Improvements
- Add support for more numerical methods.
- Enable exporting results to a file.
- Improve UI responsiveness for better user experience.

## License
This project is open-source under the MIT License.

Feel free to modify or extend this project as needed! 🚀
