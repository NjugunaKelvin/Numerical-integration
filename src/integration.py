import numpy as np
import matplotlib.pyplot as plt

# Function to evaluate user input safely
def safe_eval(expr, x):
    allowed_names = {"x": x, "np": np}
    try:
        return eval(expr, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        print(f"⚠️ Invalid function: {e}")
        return None

# Get user input for the function
while True:
    user_function = input("Enter the function in terms of x (e.g., x**2, np.sin(x), np.exp(x)): ")
    test_x = np.array([0, 1, 2])  # Test values
    if safe_eval(user_function, test_x) is not None:
        break
    print("Please enter a valid function using 'x'.")

# Get user input for integration limits
while True:
    try:
        a = float(input("Enter the lower limit of integration (a): "))
        b = float(input("Enter the upper limit of integration (b): "))
        if a < b:
            break
        else:
            print("⚠️ Lower limit must be less than upper limit.")
    except ValueError:
        print("⚠️ Please enter valid numerical values.")

# Get user input for number of intervals
while True:
    try:
        n = int(input("Enter the number of intervals (recommended: 1000): "))
        if n > 0:
            break
        else:
            print("⚠️ Number of intervals must be positive.")
    except ValueError:
        print("⚠️ Please enter a valid integer.")

# Function wrapper
def f(x):
    return safe_eval(user_function, x)

# Trapezoidal Rule
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

# Simpson’s Rule
def simpsons_rule(f, a, b, n):
    if n % 2 == 1:  # Simpson's rule requires even n
        n += 1
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return (h/3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

# Monte Carlo Integration
def monte_carlo_integration(f, a, b, num_samples=10000):
    x_rand = np.random.uniform(a, b, num_samples)
    y_rand = np.random.uniform(0, max(f(x_rand)), num_samples)
    below_curve = y_rand < f(x_rand)
    return (b - a) * max(f(x_rand)) * np.sum(below_curve) / num_samples

# Compute results
trapezoidal_area = trapezoidal_rule(f, a, b, n)
simpsons_area = simpsons_rule(f, a, b, n)
monte_carlo_area = monte_carlo_integration(f, a, b)

# Print results
print(f"\n🔹 Trapezoidal Rule Approximation: {trapezoidal_area:.4f}")
print(f"🔹 Simpson’s Rule Approximation: {simpsons_area:.4f}")
print(f"🔹 Monte Carlo Approximation: {monte_carlo_area:.4f}")

# Visualization
x_vals = np.linspace(a, b, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label=f"f(x) = {user_function}", color="blue")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan")
plt.legend()
plt.title(f"Numerical Integration for f(x) = {user_function}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
