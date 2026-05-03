import random

def monte_carlo_integration(num_points):
    under_curve = 0

    for _ in range (num_points):
        x, y = random.random(), random.random()

        if y < x**2: #f(x) = x^2
            under_curve +=1
    
    return under_curve / num_points

print("Aproximacion de la Integral: ", monte_carlo_integration(10000))
