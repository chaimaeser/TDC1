import matplotlib.pyplot as plt

# Entrée
n = int(input("Enter number of elements : "))
lambdas = []
epaisseur = []
temp = []
for i in range(n):
    lambdas.append(float(input("Enter lambda " + str(i) + " : ")))
    epaisseur.append(float(input("Enter epaisseur " + str(i) + " : ")))
    t1 = float(input("Temperature 1 : "))
    t2 = float(input("Temperature 2 : "))
    temp.append([t1, t2])

# Les axes
x_axis = []
y_axis = []
for i in range(n):
    if len(x_axis) == 0:
        a = 0
    else:
        a = x_axis[len(x_axis)-1]
    x_axis.append(a)
    y_axis.append(temp[i][0])
    x_axis.append(a + epaisseur[i])
    y_axis.append(temp[i][1])

# Plot
plt.plot(x_axis, y_axis)
plt.plot(x_axis, y_axis, "o")
for i in x_axis:
    plt.axvline(x = i, color = 'g')
plt.axis([0, int(sum(epaisseur)) + 1, 0, max(max(temp)) + 5])
plt.ylabel('Temperature')
plt.show()