---
id: is-discrete
title: Implementing the `is-discrete` trait
---

The [`is-discrete`](https://yaq.fyi/traits/is-discrete) trait is formally defined by [YEP-309](https://yeps.yaq.fyi/309).

Implementation usually involves subclassing and writing two methods.
It's also necessary to define `_position_identifiers`.

```
from yaqd_core import IsDiscrete, HasPosition, IsDaemon

class ExampleHasPosition(IsDiscrete, HasPosition, IsDaemon):
    _kind = "example-has-position"

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
	# Gets read from config, but you can define it programattically as well
	# Generally defining programmatically should be done only if reading
	# directly from a device (rather than a static mapping).
        self._position_identifiers = {
                "red": 667,
                "orange": 613,
                "yellow": 575,
                "green": 540,
                "blue": 470,
                "violet": 425,
        }

    def _set_position(self, position):
        # you will recieve position as a number
        # it's up to you to use that number to communicate appropriately
        # the following snippet is something that might appear here
        self.device.set_position(position)

    async def update_state(self):
        # you must update position and position_identifier
        # it's up to you exactly how that works for your hardware
        # remember that position_identifier can be None
        # typically, position remains numeric although it can be nan
        while True:
            self._state["position"] = self.device.get_position()
            self._state["position_identifier"] = convert(self._position)
            self._busy = not self.device.is_ready()
            if self._busy:
                await asyncio.sleep(0.01)
            else:
                await self._busy_sig.wait()
```

Check out the following implementations for good examples of typical `DiscreteHardware`:

- [fake-discrete-hardware](https://gitlab.com/yaq/yaqd-fakes/-/blob/master/yaqd_fakes/_fake_discrete_hardware.py)
- [gpio-digital-output](https://gitlab.com/yaq/yaqd-rpi-gpio/-/blob/master/yaqd_rpi_gpio/_gpio_digital_output.py)
