class Model:
    pass


class Classes:
    """
    Class to store the prediction classes for the model.
    Class would be store in a key val dict
    """
    pass


class Classifier(object):

    def __init__(self, model: Model, classes: list):
        """
        Init classifier with object detection model and classes to predict
        :param model: Model to use
        :param classes: Classes to predict
        """
        self._model = model
        self._classes = classes

    def classify(self, image):
        """
        Image passed in would be a
        :param image:
        :return:
        """
        print('classifying')
        return self.classifier(image)
