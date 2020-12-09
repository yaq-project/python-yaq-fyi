---
id: is-homeable
title: Implementing the `is-homeable` trait
---

The [`is-homeable`](https://yaq.fyi/traits/is-homeable) trait is formally defined by [YEP-305](https://yeps.yaq.fyi/305).

Homeable hardware have a procedure which resets to a known position.
Homed devices are then returned to their destination.
This trait introduces only one additional method, `home`:


```
from yaqd_core import IsHomeable, HasPosition, IsDaemon

class ExampleHomeable(IsHomeable, HasPosition, IsDaemon):
    _kind = "example_homeable"

    def home(self):
        # Since homing is typically a long process, start a new asynchronous task
        # This may not be necessary, depending on how your device behaves,
        # but remember that home is defined as returning to the current destination
        # This method should return quickly, not wait for the homing to complete.
	self._homed_event = asyncio.Event()
        self._loop.create_task(self._home())

    async def _home(self):
        self._busy = True
        # Initiate the home
        ...
        await self._homed_event.wait()
        self.set_position(self._destination)

    ...
    # Somewhere in update_state or similar, `self._homed_event.set()` must be called
    # Usually in response to some indication from the device that it has completed motion
```
