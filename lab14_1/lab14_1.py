import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200) # Діапазон

plt.plot(x, pow(x,np.cos(x)), label='x^cos(x)', color = "steelblue", linewidth = 3) # Графік функції
plt.title('My plot', fontsize=15, family="Times New Roman")   # назва графіка

plt.xlabel('x', fontsize=14, color='navy', family="Times New Roman") # позначення вісі абсцис
plt.ylabel('y', fontsize=14, color='navy', family="Times New Roman") # позначення вісі ординат
plt.legend() # Виведення легенди
plt.grid(True) # Виведення сітки

plt.show() # Виведення вікна