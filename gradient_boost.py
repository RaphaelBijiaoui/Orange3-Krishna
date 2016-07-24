<<<<<<< HEAD
import sklearn.ensemble as skl_ensemble
from Orange.base import SklLearner
from Orange.classification.base_classification import (SklLearnerClassification,
                                                       SklModelClassification)
class SklGradientBoostingClassifier(SklModelClassification):
    pass

class SklGradientBoostingLearner(SklLearnerClassification):
    __wraps__ = skl_ensemble.GradientBoostingClassifier
    __returns__ = SklGradientBoostingClassifier
    name = 'skl GradientBoosting'
    
    def __init__(self, base_estimator=None, n_estimators=100, learning_rate=0.1,
                  random_state=None, preprocessors=None):
        if isinstance(base_estimator, SklLearner):
            base_estimator = base_estimator.__wraps__(**base_estimator.params)
        super().__init__(preprocessors=preprocessors)
        self.params = vars()
    
=======
import sklearn.ensemble as skl_ensemble
from Orange.base import SklLearner
from Orange.classification.base_classification import (SklLearnerClassification,
                                                       SklModelClassification)
class SklGradientBoostingClassifier(SklModelClassification):
    pass

class SklGradientBoostingLearner(SklLearnerClassification):
    __wraps__ = skl_ensemble.GradientBoostingClassifier
    __returns__ = SklGradientBoostingClassifier
    name = 'skl GradientBoosting'
    
    def __init__(self, base_estimator=None, n_estimators=100, learning_rate=0.1,
                  random_state=None, preprocessors=None):
        if isinstance(base_estimator, SklLearner):
            base_estimator = base_estimator.__wraps__(**base_estimator.params)
        super().__init__(preprocessors=preprocessors)
        self.params = vars()
    
>>>>>>> 34db075077e8d0328318b339a713a2fb6302cc82
