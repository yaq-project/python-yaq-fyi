---
id: has-turret 
title: Implementing the `has-turret` trait
---

The [`has-turret`](https://yaq.fyi/traits/has-turret) trait is formally defined by [YEP-304](https://yeps.yaq.fyi/304).


Implementing `has-turret` involves writing getter and setter methods, and
storing one state variable:


```
from yaqd_core import Base

# Often daemons implementing has-turret will be some kind of Hardware, but it is not required
class ExampleTurret(Base):
    _kind = "example-turret"
    traits = ["has-turret"]

    def get_state(self):
        state = super().get_state()
        state["turret"] = self._turret
        return state

    def _load_state(self, state):
        super()._load_state(state)
        self._turret = state.get("turret", 0)

    def set_turret(self, index):
        self._busy = True
        # Perform the actual setting of the turret for your device

    def get_turret(self):
        return self._turret
```
