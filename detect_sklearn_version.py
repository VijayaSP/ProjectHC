import pickle
import sklearn
import warnings
from sklearn.exceptions import InconsistentVersionWarning

#catch the InconsistentVersionWarning and print the version of sklearn
warnings.simplefilter("error", InconsistentVersionWarning)

try:
    model=pickle.load(open('saved_model.sav','rb'))
except InconsistentVersionWarning as w:
    print(w.original_sklearn_version)    