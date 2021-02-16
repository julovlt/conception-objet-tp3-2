from tp2 import *

def test_box_create():
    b = Box()

def test_box_add():
    b = Box()
    b.add("truc1")
    b.add("truc2")

def test_box_in():
    b = Box()
    b.add("truc1")
    b.add("truc2")

    assert "truc1" in b
    assert "truc2" in b

def test_box_remove():
    b = Box()
    b.add("truc1")
    b.remove("truc1")

    assert "truc1" not in b

def test_box_is_open():
    b = Box()

    b.open()
    assert b.is_open()

    b.close()
    assert not b.is_open()

def test_action_look():
    b = Box()

    b.add("ceci")
    b.add("cela")

    b.open()
    assert b.action_look() == "la boite contient : ceci, cela"

    b.close()
    assert b.action_look() == "la boite est fermee"

def test_thing_create():
    t = Thing(3)
    assert t.volume() == 3
