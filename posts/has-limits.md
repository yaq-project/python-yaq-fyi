---
id: has-limits
title: Implementing the `has-limits` trait
---

The [`has-limits`](https://yaq.fyi/traits/has-limits) trait is formally defined by [YEP-303](https://yeps.yaq.fyi/303).

The `HasLimits` class implements all that is needed to be compliant with the trait.
The `hw_limits` entry in state is a 2-tuple which can represent programatically defined limits (e.g. firmware limits from the device itself, which may change at runtime).
Handling of taking the intersection with user defined configuration limits is handled by the `HasLimits` base class.
While implementing [`has-position`](../has-position) is required as well, here is an
example demonstrating new behavior:

```
from yaqd_core import HasLimits, HasPosition, IsDaemon

class ExamplHasLimits(HasLimits, HasPosition, IsDaemon):
    _kind = "example-has-limits"

    def __init__(
        self, name: str, config: Dict[str, Any], config_filepath: pathlib.Path
    ):
        super().__init__(name, config, config_filepath)
	self._state["hw_limits"] = (0., 50.)
```
