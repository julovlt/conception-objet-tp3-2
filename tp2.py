class Box:
    def __init__(self):
        self._contents = []
        self._status = True

    def add(self,truc):
        self._contents.append(truc)

    def __contains__(self, truc):
        return truc in self._contents

    def remove(self, truc):
        self._contents.remove(truc)

    def is_open(self):
        return self._status

    def open(self):
        self._status = True

    def close(self):
        self._status = False

    def action_look(self):
        if(self.is_open()):
            return "la boite contient : " + ", ".join(self._contents)
        else:
            return "la boite est fermee"
