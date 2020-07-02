---
id: has-position
title: Implementing the `has-position` trait
---

The [`has-position`](https://yaq.fyi/traits/has-position) trait is formally defined by [YEP-301](https://yeps.yaq.fyi/301).

The `has-position` trait defines the `Hardware` class.
Implementing this trait usually involves subclassing and writing two functions:

```
from yaqd_core import Hardware

class ExampleHasPosition(Hardware):
    _kind = "example-has-position"

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
        self._units = "mm"

    def _set_position(self, position):
        # The super class handles exposing set_position externally,
        # as well as setting `_busy`, and keeping track of the destination
        ...
        # Actually communicate with your device here
        self.device.set_position(position)

    async def update_state(self):
        # For a `Hardware`, the important things to update include the position 
        # and the busy state.
        # Each device will have a unique varient of this method, so a simple
        # example of a device that exposes these in single python calls is shown.
        while True:
            self._state["position"] = self.device.get_position()
            self._busy = not self.device.is_ready()
            if self._busy:
                await asyncio.sleep(0.01)
            else:
                await self._busy_sig.wait()
```

Note that `_set_position` does *not* wait for the position to be
attained. The `_units` attribute can be defined in a number of ways,
ranging from only allowing one value, to being user configurable, to
being read from the device itself. All other parts of this trait are
handled by the `Hardware` base class.
