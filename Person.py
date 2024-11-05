class Person:
    def __init__(self, yoloId, features, kalman):
        assert(type(yoloId) == int)

        self.__id = yoloId
        self.__features = features
        self.__kalman = kalman
    
    def set_id(self, newYoloId):
        assert(type(newYoloId) == int)

        self.__id = newYoloId

    def get_id(self):
        return self.__id

    def set_features(self, newFeatures):
        self.__features = newFeatures

    def get_features(self):
        return self.__features

    def set_kalman(self, newKalman):
        self.__kalman = newKalman

    def get_features(self):
        return self.__kalman