#Creates decision tree from a training set using features in a csv file, prints 
#the decision tree, and returns accuracy after applying to a test set

#Import required modules
import csv
import xlwt
import pandas as pd
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn.externals.six import StringIO
from sklearn.externals.six import StringIO 
import pydot 
import os
#-----------------------------------------------------------------------------

#Import training set features from csv to a list
os.chdir('Directory Name Here')
database1 = pd.read_csv("File Here.csv")
data_as_dict = pd.DataFrame({'Variable 1': database1['Variable 1'],
        'Variable 2': database1['Variable 2'],
        'Variable 3': database1['Variable 3'],
        'Variable 4': database1['Variable 4']})
#-----------------------------------------------------------------------------

#Create separate list for training set target variable
target = data_as_dict[['Variable 4']]
LabelEncoder = preprocessing.LabelEncoder()
target = LabelEncoder.fit_transform(target)
del data_as_dict['Variable 4']
#-----------------------------------------------------------------------------

#Iterates through training set dictionary and turns into list
data = [dict(r.iteritems()) for _, r in data_as_dict.iterrows()]
data = DictVectorizer(sparse=False).fit_transform(data)
#-----------------------------------------------------------------------------

#Runs decision tree
DecisionTree = tree.DecisionTreeClassifier()
DecisionTree.fit(data, target)
#-----------------------------------------------------------------------------

#Prints decision tree
with open("All.dot", 'w') as f:
    f = tree.export_graphviz(dt, out_file=f)   
os.unlink("All.dot")
dot_data = StringIO()
tree.export_graphviz(dt, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("Decision Tree File Name Here.pdf")
#-----------------------------------------------------------------------------

#Import test set features from csv to a list
database2 = pd.read_csv("File Here.csv")
data_as_dict2 = pd.DataFrame({'Variable 5': database1['Variable 5'],
        'Variable 6': database1['Variable 6'],
        'Variable 7': database1['Variable 7'],
        'Variable 8': database1['Variable 8']})
#-----------------------------------------------------------------------------

#Create separate list for test set target variable
target2 = data_as_dict2[['Variable 8']]
LabelEncoder2 = preprocessing.LabelEncoder()
target2 = le.fit_transform(target2)
del data_as_dict2['Variable 8']
#-----------------------------------------------------------------------------

#Iterates through test set dictionary and turns into list
data2 = [dict(r.iteritems()) for _, r in data_as_dict2.iterrows()]
data2 = DictVectorizer(sparse=False).fit_transform(data2)
#-----------------------------------------------------------------------------

#Predicts which category each entity will be in based in decision tree and returns accuracy
predicted_cat = DecisionTree.predict(data2)
dt.score(data_fea2, labels_fea2)
#-----------------------------------------------------------------------------

#Creates a dictionary containing predicted and actual categories and creates a csv from that
final_dict = {'Actual': database2['Variable 8'], 'Predicted': predicted_cat}
pd.DataFrame(final_dict).to_csv(r"Location and Name of New csv Here.csv",encoding="utf-8")

