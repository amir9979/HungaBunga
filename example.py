

import random

from hunga_bunga import HungaBungaClassifier, HungaBungaRegressor, HungaBungaZeroKnowledge
from hunga_bunga.regression import gen_reg_data
from sklearn import datasets



# ---------- Getting The Data ----------

iris = datasets.load_iris()
X_c, y_c = iris.data, iris.target
X_r, y_r = gen_reg_data(10, 3, 100, 3, sum, 0.3)



# ---------- Classification ----------

clf = HungaBungaClassifier()
clf.fit(X_c, y_r)
print(clf.predict(X_c))



# ---------- Regression ----------

mdl = HungaBungaRegressor()
mdl.fit(X_c, y_r)
print(mdl.predict(X_c))



# ---------- Zero Knowledge ----------

X, y = random.choice(((X_c, y_c), (X_r, y_r)))
mdl = HungaBungaZeroKnowledge()
mdl.fit(X, y)
print(mdl.predict(X), mdl.problem_type)

#        <3 Dean, this is 4 U <3