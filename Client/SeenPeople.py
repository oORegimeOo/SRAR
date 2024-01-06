class Person:
    def __init__(self):
        self.idx = None
        self.givenName = None
        self.surname = None
        self.age = None
        self.job = None
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.upperText = ""
        self.lowerText = ""

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getW(self):
        return self.w

    def setW(self, w):
        self.w = w

    def getH(self):
        return self.h

    def setH(self, h):
        self.h = h

    def getIdx(self):
        return self.idx

    def setIdx(self, idx):
        self.idx = idx

    def getGivenName(self):
        return self.givenName

    def setGivenName(self, givenName):
        self.givenName = givenName

    def getSurname(self):
        return self.surname

    def setSurname(self, surname):
        self.surname = surname

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job

    def getUpperText(self):
        return self.upperText

    def setUpperText(self):
        self.upperText = self.getGivenName() + " " + self.getSurname() + ", " + str(self.getAge())

    def getLowerText(self):
        return self.lowerText

    def setLowerText(self):
        self.lowerText = self.getJob()

    def proofNewId(self, idx):
        if idx == self.getIdx():
            return False
        else:
            return True

    def proofNewPerson(self, data):
        if self.proofNewId(data[0]):
            self.setIdx(data[0])
            self.setGivenName(data[1])
            self.setSurname(data[2])
            self.setAge(data[3])
            self.setJob(data[4])
            self.setUpperText()
            self.setLowerText()