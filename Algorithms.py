#Pandas locate based on index
import pandas as pd
df = pd.read_csv('[name].csv')
print(df.iloc[[12]]) #Locates everything in index 12

#Make mglearn wave(Not Machine Learning, just useful for future reference)
import mglearn
from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.make_wave(n_samples=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

#KNeighborsClassifier:

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)

#Linear Regression:

from sklearn.linear_model import LinearRegression

lr = LinearRegression().fit(X_train, y_train)

#Ridge Regression(uses regularization: each feature should have as little affect on the outcome as possible while
#being able to predict correctly to avoid overfitting) - increase alpha means increase in generalization, decrease in training accuracy

from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0).fit(X_train, y_train)

#Lasso(Alternate to Ridge, but some feautures become completely ignored to make the model easier to intepret; L1 Regularization)
#An increase in alpha would be an increase in amount of feautures used

from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)

#Logistic Regression(One type of linear model used for classification; L2 Regularization by default)
#The higher C is, the increased complexity of the model(which makes the predictory better in most cases)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1,max_iter=10000,penalty="l2").fit(X_train, y_train)

#Decision Tree(greater the depth, the more overfitting)

from sklearn.tree import DecisionTreeClassifier

tr = DecisionTreeClassifier(max_depth=4,random_state=0).fit(X_train, y_train)

#Random Forest/RandomForestClassifier(the more n_estimators, the more trees in the voting process, You should have as much trees as possible to make the voting more accurate)

from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=10,random_state=0).fit(X_train, y_train)

#Gradiatent Boosted Regression Trees(USED VERY OFTEN IN MACHINE LEARNING COMPETITIONS) Builds trees where each tree tries to correct the mistakes of the previous one
#Does not work well with high dimensional sparse data(data with a lot of elements and a lot of 0's)
#Learning rate: Higher means trees try stronger to correct other mistakes
#Max depth: Lower means lower compexity of the tree, low max_depth for gradient boosted models

from sklearn.ensemble import GradientBoostingClassifier

gbrt = GradientBoostingClassifier(random_state=0,max_depth=3,learning_rate=0.1).fit(X_train, y_train)

#SVMs: A type of linear model which uses the kernel trick to transform your data and find the best boundary between all the possible feautures of outputs(POWERFUL!!!)
#Kernel trick: 'poly'/Polynomial Kernel: Computes all possible polynomials up to a certain degree of the original feautures(e.g. feauture1 ** 2 * feauture2 ** 5)
#Kernel trick: 'rbf'/Gaussian Kernel: It consideres all possible polynomials for all degrees, but the importance of each feauture decreases with a higher degree
#gamma: low gamma means lower complexity of model, high gamma means higher complexity of model
#C: low C means each data point has a limited influence on model, high C means each datapoint has higher influence on model(use higher C when model underfitting)

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

#scale data to 0 and 1
min_on_training = X_train.min(axis=0)
range_on_training = (X_train - min_on_training).max(axis=0)
X_train_scaled = (X_train - min_on_training) / range_on_training
X_test_scaled = (X_test - min_on_training) / range_on_training
#calculate svm
svm = SVC(kernel='rbf',C=10,gamma=0.1).fit(X_train_scaled, y_train)

#Neural networks: Reduces the number of nodes([12,12] has 12 nodes) reduces complexity, increasing it increases the complexity
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(solver='lbfgs', random_state=0, hidden_layer_sizes=[10,10]).fit(X_train, y_train)

#Grid Search CV(Perfect for finding what parameters to put for your specific model!)
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
param_grid = {'n_neighbors':[1,2,3,4,5,6,7,8,9]}
grid = GridSearchCV(KNeighborsClassifier(),param_grid,verbose=3)
print(grid.best_params_)
model = grid.fit(X_train, y_train)

#K Means Cluserting 
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = make_blobs(n_samples=150,n_features=2,centers=4,cluster_std=1.8,random_state=0) 
kmeans = KMeans(n_clusters=4)
model = kmeans.fit(data[0])

fig, axes = plt.subplots(1,2)
axes[0].scatter(data[0][:,0],data[0][:,1],c=data[1])
axes[0].set_title('Original')
axes[1].scatter(data[0][:,0],data[0][:,1],c=model.labels_)
axes[1].set_title('K Means')
plt.show()

#MinMaxScaler(scales data, very common for neural networks
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#---------------TENSORFLOW NEURAL NETWORK--------
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import pandas as pd

model = keras.Sequential()
model.add(keras.layers.Dense(11, activation='relu'))
model.add(keras.layers.Dense(11, activation='relu'))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(1))
model.compile(optimizer='adam',loss='mse')
stopping = keras.callbacks.EarlyStopping(monitor='val_loss',mode='min', verbose=1, patience=10)
model.fit(X_train, y_train, epochs=5, batch_size=50, validation_loss=(X_test, y_test), callbacks=[stopping])

losses = pd.DataFrame(model.history.history)
losses.plot()
plt.show()
