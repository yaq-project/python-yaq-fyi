---
id: uses-i2c
title: Implementing the `uses-i2c` trait
---

The [`uses-i2c`](https://yaq.fyi/traits/uses-i2c) trait is formally defined by [YEP-308](https://yeps.yaq.fyi/308).

Implementing `uses-i2c` requires one configuration parameter and implementing
`direct_serial_write` as defined by `uses-serial`.
There are many libraries in python that can manage low level i2c
communication. We have typically used
[smbus](https://pypi.org/project/smbus/).

A typical `uses-i2c` daemon will look something like:

```
__all__ = ["ExampleUsesI2c"]

import asyncio

from yaqd_core import Base

class ExampleUsesI2c(Base):
    _kind = "example-uses-i2c"

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
        self.address = config["i2c_addr"]
        self.bus = smbus.SMBus(1)
        ...
        # perfom other setup, possibly including reads and writes

    def direct_serial_write(self, message: bytes):
        self._busy = True
        for byte in message:
            self.bus.write_byte(self.address, byte)

    async def update_state(self):
        while True:
            self.bus.write_byte(self.address, 0x12)
            data = self.bus.read_i2c_block_data(self.address, 0x00, 3)
            self._busy = data == 0x01
            if self._busy:
                await asyncio.sleep(0.1)
            else:
                await self._busy_sig.wait()
```

Notes:
- It is common for a default device number to make sense, this is specified in the protocol.

