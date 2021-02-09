class Box:
    def __init__(self):
        self._contents = []

    def add(self,truc):
        self._contents.append(truc)


    def __contains__(self, truc):
        return truc in self._contents
