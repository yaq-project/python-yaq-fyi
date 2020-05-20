---
id: is-homeable
title: Implementing the `is-homeable` trait
---

The [`is-homeable`](https://yaq.fyi/traits/is-homeable) trait is formally defined by [YEP-305](https://yeps.yaq.fyi/305).

Homeable hardware have a procedure which resets to a known position.
Homed devices are then returned to their destination. This trait is
required to be applied to a `Hardware` (or a subclass like `ContinuousHardware`)
daemon, and introduces only one additional method:


```
from yaqd_core import Hardware

class ExampleHomeable(Hardware):
    _kind = "example_homeable"
    traits = ["is-homeable"]

    def home(self):
        # Since homing is typically a long process, start a new asynchronous task
        # This may not be necessary, depending on how your device behaves,
        # but remember that home is defined as returning to the current destination
        # This method should return quickly, not wait for the homing to complete.
        loop = asyncio.get_event_loop()
        loop.create_task(self._home())

    async def _home(self):
        self._busy = True
        # Initiate the home
        ...
        await self._not_busy_sig.wait()
        self.set_position(self._destination)
```
