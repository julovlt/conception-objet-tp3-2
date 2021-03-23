def list_from_yaml(data):
    ans = []
    for d in data:
        if d['type'] == "Box":
            ans.append(Box.from_yaml(d))
        elif d["type"] == "Thing":
            ans.append(Thing.from_yaml(d))
    return ans

class Box:
    @staticmethod
    def from_yaml(data):
        return Box(is_open=data['is_open'], capacity=data['capacity'])

    def __init__(self, is_open=True, capacity=None, key=None):
        self._contents = []
        self._status = is_open
        self._capacity = capacity
        self._key = key

    def add(self,truc):
        self._contents.append(truc)

    def __contains__(self, truc):
        return truc in self._contents

    def remove(self, truc):
        self._contents.remove(truc)

    def is_open(self):
        return self._status

    def open(self):
        if self._key == None:
            self._status = True

    def close(self):
        self._status = False

    def action_look(self):
        if(self.is_open()):
            return "la boite contient : " + ", ".join(self._contents)
        else:
            return "la boite est fermee"

    def set_capacity(self, c):
        self._capacity = c

    def capacity(self):
        return self._capacity

    def has_room_for(self, t):
        return self.capacity() is None or t.volume() <= self.capacity()

    def action_add(self, t):
        if self.is_open() and self.has_room_for(t):
            self.add(t)
            if self.capacity() is not None:
                self.set_capacity(self.capacity() - t.volume())
            return True
        else:
            return False

    def find(self, t_name):
        if self.is_open():
            for t in self._contents:
                if t.has_name(t_name):
                    return t
            return None
        else:
            return None

    def open_with(self,t):
        if self._key == t:
            self._status = True

    def set_key(self,t):
        self._key = t

class Thing:
    def from_yaml(data):
        return Thing(v=data['volume'], name=data['name'])

    def __init__(self, v, name=None):
        self._volume = v
        self._name = name

    def __repr__(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def has_name(self, name):
        return self._name == name

    def volume(self):
        return self._volume
