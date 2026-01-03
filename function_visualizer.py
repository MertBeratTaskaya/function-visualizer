import numpy as np
import matplotlib.pyplot as plt
import mplcursors

print("\n--- FUNCTION VISUALIZER ---")
print("1) Linear       f(x) = ax + b")
print("2) Quadratic    f(x) = ax² + bx + c")
print("3) Exponential  f(x) = a·e^(bx)")
print("4) Logarithmic  f(x) = a·ln(x)")
print("5) Sine         f(x) = a·sin(bx)")
print("6) Cosine       f(x) = a·cos(bx)")
print("7) Tangent      f(x) = a·tan(bx)")
print("8) Cotangent    f(x) = a·cot(bx)")
print("9) Secant       f(x) = a·sec(bx)")
print("10) Cosecant    f(x) = a·csc(bx)")

try:
    choice = int(input("\nChoose function type (1-10): "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if choice in [5, 6, 7, 8, 9, 10]:
    try:
        angle_min = float(input("Enter angle minimum (degrees): "))
        angle_max = float(input("Enter angle maximum (degrees): "))
    except ValueError:
        print("Invalid input.")
        exit()
    x_min = np.radians(angle_min)
    x_max = np.radians(angle_max)
else:
    try:
        x_min = float(input("Enter x minimum: "))
        x_max = float(input("Enter x maximum: "))
    except ValueError:
        print("Invalid input.")
        exit()

x = np.linspace(x_min, x_max, 1000)

b = 1 

if choice == 1:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        exit()
    y = a * x + b
    title = f"f(x) = {a}x + {b}"

elif choice == 2:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
    except ValueError:
        exit()
    y = a * x**2 + b * x + c
    title = f"f(x) = {a}x² + {b}x + {c}"

elif choice == 3:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        exit()
    y = a * np.exp(b * x)
    title = f"f(x) = {a}e^({b}x)"

elif choice == 4:
    try:
        a = float(input("a: "))
    except ValueError:
        exit()
    y = np.where(x > 0, a * np.log(x), np.nan)
    title = f"f(x) = {a} ln(x)"

elif choice == 5:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        exit()
    y = a * np.sin(b * x)
    title = f"f(x) = {a} sin({b}x)"

elif choice == 6:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        exit()
    y = a * np.cos(b * x)
    title = f"f(x) = {a} cos({b}x)"

elif choice == 7:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        exit()
    y = a * np.tan(b * x)
    y[:-1][np.diff(y) < 0] = np.nan
    title = f"f(x) = {a} tan({b}x)"

elif choice == 8:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        exit()
    y = a / np.tan(b * x)
    y[:-1][np.diff(y) > 0] = np.nan
    title = f"f(x) = {a} cot({b}x)"

elif choice == 9:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        exit()
    y = a / np.cos(b * x)
    y[np.abs(np.cos(b*x)) < 0.001] = np.nan
    title = f"f(x) = {a} sec({b}x)"

elif choice == 10:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        exit()
    y = a / np.sin(b * x)
    y[np.abs(np.sin(b*x)) < 0.001] = np.nan
    title = f"f(x) = {a} csc({b}x)"

else:
    print("Invalid choice.")
    exit()

color = "red"
plt.figure(figsize=(10, 6))

line, = plt.plot(x, y, color=color, linewidth=2)

plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

if choice == 4:
    plt.axvline(0, color="red", linestyle="--", linewidth=2, label="Asymptote x=0")

elif choice in [7, 9]: 
    if b != 0:
        period = np.pi / abs(b)
        start_val = (np.pi/2) / b
        k_min = np.floor((x_min - start_val) / period)
        k_max = np.ceil((x_max - start_val) / period)
        
        for k in range(int(k_min), int(k_max) + 1):
            asym_x = (np.pi/2 + k * np.pi) / b
            if x_min <= asym_x <= x_max:
                plt.axvline(asym_x, color="red", linestyle="--", linewidth=2)

elif choice in [8, 10]:
    if b != 0:
        period = np.pi / abs(b)
        k_min = np.floor(x_min / period)
        k_max = np.ceil(x_max / period)
        
        for k in range(int(k_min), int(k_max) + 1):
            asym_x = (k * np.pi) / b
            if x_min <= asym_x <= x_max:
                plt.axvline(asym_x, color="red", linestyle="--", linewidth=2)

plt.title(title, fontsize=14)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(alpha=0.3)

if choice in [7, 8, 9, 10]:
    plt.ylim(-10, 10)

if choice in [5, 6, 7, 8, 9, 10]:
    degrees = np.degrees(x)
    min_deg = np.degrees(x_min)
    max_deg = np.degrees(x_max)
    step = 90 if (max_deg - min_deg) > 360 else 45
    tick_degrees = np.arange(np.ceil(min_deg / step) * step, np.floor(max_deg / step) * step + step, step)
    tick_positions = np.radians(tick_degrees)
    tick_labels = [f"{d:.0f}°" for d in tick_degrees]
    plt.xticks(tick_positions, tick_labels, rotation=45)
    plt.xlabel("Angle (degrees)")

cursor = mplcursors.cursor(line, hover=True)
@cursor.connect("add")
def on_add(sel):
    x_val = sel.target[0]
    y_val = sel.target[1]
    if choice in [5, 6, 7, 8, 9, 10]:
        x_display = f"{np.degrees(x_val):.1f}°"
    else:
        x_display = f"{x_val:.3f}"
    sel.annotation.set_text(f"x = {x_display}\ny = {y_val:.3f}")
    sel.annotation.get_bbox_patch().set(alpha=0.9)

plt.tight_layout()
plt.show()