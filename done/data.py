
# # example of a ordinal encoding
# from sklearn.preprocessing import OneHotEncoder
# from numpy import asarray
# from sklearn.preprocessing import OrdinalEncoder
# # define data
# data = asarray([['red'], ['green'], ['blue']])
# print(data)
# # define ordinal encoding
# encoder = OrdinalEncoder()
# # transform data
# result = encoder.fit_transform(data)
# print(result)


# # example of a one hot encoding
# # define data
# data = asarray([['red'], ['green'], ['blue']])
# print(data)
# # define one hot encoding
# encoder = OneHotEncoder(sparse=False)
# # transform data
# onehot = encoder.fit_transform(data)
# print(onehot)

# # example of a dummy variable encoding
# # define data
# data = asarray([['red'], ['green'], ['blue']])
# print(data)
# # define one hot encoding
# encoder = OneHotEncoder(drop='first', sparse=False)
# # transform data
# onehot = encoder.fit_transform(data)
# print(onehot)
# # load and summarize the dataset
# from pandas import read_csv
# # define the location of the dataset
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/breast-cancer.csv"
# # load the dataset
# dataset = read_csv(url, header=None)
# # retrieve the array of data
# data = dataset.values
# # separate into input and output columns
# x = data[:, :-1].astype(str)
# y = data[:, -1].astype(str)
# # summarize
# print('Input', X.shape)
# print('Output', y.shape)

# # ordinal encode the breast cancer dataset
# from pandas import read_csv
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OrdinalEncoder
# # define the location of the dataset
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/breast-cancer.csv"
# # load the dataset
# dataset = read_csv(url, header=None)
# # retrieve the array of data
# data = dataset.values
# # separate into input and output columns
# X = data[:, :-1].astype(str)
# y = data[:, -1].astype(str)
# # ordinal encode input variables
# ordinal_encoder = OrdinalEncoder()
# X = ordinal_encoder.fit_transform(X)
# # ordinal encode target variable
# label_encoder = LabelEncoder()
# y = label_encoder.fit_transform(y)
# # summarize the transformed data
# print('Input', X.shape)
# print(X[:5, :])
# print('Output', y.shape)
# print(y[:5])

# evaluate logistic regression on the breast cancer dataset with an ordinal encoding
from numpy import mean
from numpy import std
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score
# define the location of the dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/breast-cancer.csv"
# load the dataset
dataset = read_csv(url, header=None)
# retrieve the array of data
data = dataset.values
# separate into input and output columns
X = data[:, :-1].astype(str)
y = data[:, -1].astype(str)
# split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=1)
# ordinal encode input variables
ordinal_encoder = OrdinalEncoder()
ordinal_encoder.fit(X_train)
X_train = ordinal_encoder.transform(X_train)
X_test = ordinal_encoder.transform(X_test)
# ordinal encode target variable
label_encoder = LabelEncoder()
label_encoder.fit(y_train)
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)
# define the model
model = LogisticRegression()
# fit on the training set
model.fit(X_train, y_train)
# predict on test set
yhat = model.predict(X_test)
# evaluate predictions
accuracy = accuracy_score(y_test, yhat)
print('Accuracy: %.2f' % (accuracy*100))
