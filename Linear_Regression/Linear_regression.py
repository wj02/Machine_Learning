import numpy as np
from matplotlib import pyplot as plt

X = np.arange(0, 10, 0.02)
Z = [21 + 5 * x for x in X]
Y = np.array([np.random.normal(z, 0.5) for z in Z])

# data pre-processing
# X变成500*1
X = X.reshape(X.shape[0], 1)
Y = np.array(Y).reshape(Y.shape[0], 1)


# 初始参数，随机
w = 1
b = 1
# 超参数 学习率
alpha = 0.01
# 迭代次数
epochs = 9000

# training
num_of_training = X.shape[0]
loss_set = []
for epoch in range(epochs):
    dw = np.sum(-(2 / num_of_training) * X * (Y - w * X - b))
    db = np.sum(-(2 / num_of_training) * (Y - w * X - b))
    # 均方误差算损失
    loss = np.sum((Y - w * X - b) ** 2) / num_of_training
    loss_set.append(loss)
    # alpha 越小，迭代越慢
    w = w - alpha * dw
    b = b - alpha * db
    print('Train Epoch: {}\tLoss: {:.6f}'.format(epoch, loss))
print(f"w={w:.2f}  b={b:.2f}")
print(f"loss={loss:.6f}")

plt.title("Training loss")
X_a = [_ for _ in range(epochs)]
plt.plot(X_a, loss_set)
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.show()


x_set = [0, 10]
y_set = [w * x + b for x in x_set]
plt.title("Linear regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(X, Y, 'bo', markersize='2')
plt.plot(x_set, y_set, 'r', linewidth=4)
plt.show()