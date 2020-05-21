---
id: uses-uart
title: Implementing the `uses-uart` trait
---

The [`uses-uart`](https://yaq.fyi/traits/uses-uart) trait is formally defined by [YEP-307](https://yeps.yaq.fyi/307).

UART is the serial communication scheme used for RS-232 and similar
protocols. UART serial communication is characterized by a baudrate. In
python, the standard way of communicating with UART devices is the
[pyserial](https://pypi.org/project/pyserial/) library. We include in
the yaqd-core-python implementation a subclass of the pyserial
implementation that has some asynchronous functions avialable.
Using the provided serial class is not required, but can improve response times.
Implementing `uses-uart` also requires implementing `direct_serial_write` as defined by the `uses-serial` trait.

A typical `uses-uart` daemon will look something like:

```
__all__ = ["ExampleUsesUart"]

import asyncio

from yaqd_core import Base, aserial

class ExampleUsesUart(Base):
    _kind = "example-uses-uart"
    traits = ["uses-uart", "uses-serial"]
    defaults = {"baud_rate": 9600}  # Check your device for appropriate default

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
        self._serial_port = aserial.ASerial(config["serial_port"], config["baud_rate"])
        ...
        # perfom other setup, possibly including reads and writes

    def close(self):
        self._serial_port.close()

    def direct_serial_write(self, message):
        self._busy = True
        self._serial_port.write(message.encode())

    async def update_state(self):
        while True:
            self._serial_port.write(b"get_status")
            line = await self._serial_port.areadline()
            self._busy = line != b"ready"
            if self._busy:
                await asyncio.sleep(0.1)
            else:
                await self._busy_sig.wait()
```
