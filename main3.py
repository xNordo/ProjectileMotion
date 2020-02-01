import numpy as np
from math import cos, sin, pi, radians
import matplotlib.pyplot as plt


N = 1000000 #Ilość iteracji
t = np.linspace(0, 10, N+1)

krok = t[1] - t[0]

a = np.zeros((N+1, 2))
v = np.zeros((N+1, 2))
r = np.zeros((N+1, 2))


rho = 1.2
cx = 0.47
x = float(input("Wprowadź prędkość początkową rzutu (m/s): "))
h = float(input("Wprowadź wysokość początkową rzutu (m): "))
alpha = float(input("Wprowadź kąt rzutu (stopnie): "))
alpha = radians(alpha) # konwertuje kąt wyrażony w stopniach do radianów
m = float(input("Wprowadź masę obiektu (kg): "))
g = float(input("Wprowadź stałą grawitacyjną (m/s^2): "))
d = float(input("Wprowadź średnicę kuli (m): "))
A = pi*d**2     # powierzchnia przekroju w m^2


v[0] = (x*cos(alpha), x*sin(alpha))     # prędkośc początkowa m/s
r[0] = (0, h)   # pozycja początkowa <x;y>

def F(r, v, t):
    return (0, -m*g) - 0.5*rho*cx*A*abs(v)*v


# Wyliczenie przyśpieszenia, prędkości i pozycji
for i in range(N):
    a[i] = F(r[i], v[i], t[i])/m
    v[i+1] = v[i] + a[i]*krok
    r[i+1] = r[i] + v[i]*krok

# wyciągnięcie współrzędnych
x = r[:, 0]
y = r[:, 1]

# Rysowanie wykresu
plt.plot(x,y)
plt.xlabel("dystans poziomy w metrach")
plt.ylabel("dystans pionowy w metrach")
plt.title("Rzut ukośny")
plt.grid()
plt.axis([0, max(x)+20, 0, max(y)+20])
plt.show()



