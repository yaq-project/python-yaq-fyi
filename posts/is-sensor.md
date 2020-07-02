---
id: is-sensor
title: Implementing the `is-sensor` trait
---

The [`is-sensor`](https://yaq.fyi/traits/is-sensor) trait is formally defined by [YEP-302](https://yeps.yaq.fyi/302).

The `is-sensor` trait defines the `Sensor` class. A lot of the machinery
for making sensors work, including handling of looping and exposed
methods, is implemented as part of the `Sensor` class. That said, each
sensor will have its own configuration and you necessarily have to
implement the function to actually perform a measurement.

As the implementor, you are responsible for filling out three
attributes: `_channel_names`, `_channel_units`, and `_channel_shapes`.
`_channel_names` is a simple list of strings with names of each recorded
value. `_channel_units` is a dictionary mapping the names to strings
representing the units. `_channel_shapes` may be omitted if all channels
are scalar values, otherwise it is a dictionary mapping names to tuples
of integers representing the shapes.

A typical `is-sensor` daemon will look something like:

```
from yaqd_core import Sensor

class ExampleSensor(Sensor):
    _kind = "example-sensor"

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
	self._channel_names = ["channel0", "channel1"]
	self._channel_units = {"channel0": "V", "channel1": "A"}
	# If shaped, you would also include self._channel_shapes

    async def _measure(self):
        # Do whatever needs to be done to fill a dictionary mapping names to values
	    # (or arrays for shaped data)
	    return {"channel0": 1.234, "channel1": 3.14}
```
