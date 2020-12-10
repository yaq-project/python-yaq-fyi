---
id: has-turret 
title: Implementing the `has-turret` trait
---

The [`has-turret`](https://yaq.fyi/traits/has-turret) trait is formally defined by [YEP-304](https://yeps.yaq.fyi/304).


Implementing `has-turret` involves writing getter and setter methods, and
storing one state variable:


```
from yaqd_core import HasTurret, IsDaemon

class ExampleHasTurret(HasTurret, IsDaemon):
    _kind = "example-has-turret

    def set_turret(self, index):
        self._busy = True
        # Perform the actual setting of the turret for your device
	self.device.set_turret(index)
	self._state["turret"] = index

    def get_turret(self):
        return self._state["turret"]
```
