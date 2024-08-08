import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Subject': [1, 2, 3, 4, 5, 6],
    'Age': [43, 21, 25, 42, 57, 59],
    'Glucose': [99, 65, 79, 75, 87, 81]
}

df=pd.DataFrame(data)

x = df['Age']
y = df['Glucose']

sum_x=np.sum(x)
print(sum_x)

sum_y=np.sum(y)
print(sum_y)

x_squ=np.sum(x*x)
print(x_squ)

xy=np.sum(x*y)
print(xy)

n=len(x)
print(n)
#slope
m = (n*xy-sum_x*sum_y)/(n*x_squ - sum_x*sum_x)
print(m)
#intercept
b = (sum_y - m*sum_x)/n
print(b)

print(f"y = {m}x + {b}")

new_x = 55
predicted_y = m * new_x + b
print(f"Predicted value for x = {new_x}: {predicted_y}")

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y, color='red', label='Regression Line')
plt.xlabel('Age')
plt.ylabel('Glucose')
plt.title('Linear Regression')
plt.legend()
plt.show()
