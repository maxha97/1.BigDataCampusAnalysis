
class Subject:
    def __init__(self, kor=0, eng=0, math=0):
        self.__kor = kor
        self.__eng = eng
        self.__math = math

    def setKor(self, kor):
        self.__kor = kor

    def getKor(self):
        return self.__kor

    def setMath(self, math):
        self.__math = math

    def getMath(self):
        return self.__math

    def setEng(self, eng):
        self.__eng = eng

    def getEng(self):
        return self.__eng