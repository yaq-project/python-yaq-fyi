---
id: has-limits
title: Implementing the `has-limits` trait
---

The [`has-limits`](https://yaq.fyi/traits/has-limits) trait is formally defined by [YEP-303](https://yeps.yaq.fyi/303).

The `has-limits` trait defines the `ContinuousHardware` class. The class
implements all that is needed to be compliant with the trait, and
introduces an attribute `hw_limits`. `hw_limits` is a 2-tuple which can
represent programatically defined limits (e.g. firmware limits from the
device itself). Handling of taking the intersection with user defined
configuration limits is handled by the `ContinuousHardware` class. While
implementing [`has-position`](../has-position) is required as well, here is an
example demonstrating new behavior:

```
from yaqd_core import ContinuousHardware

class ExampleHasLimits(ContinuousHardware):
    _kind = "example-has-limits"

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
        self.hw_limits = (0., 50.)
```
