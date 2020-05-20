---
id: uses-serial
title: Implementing the `uses-serial` trait
---

The [`uses-serial`](https://yaq.fyi/traits/uses-serial) trait is formally defined by [YEP-306](https://yeps.yaq.fyi/306).

The `uses-serial` trait is not typically going to be a terminal trait.
More specific configuration will be provided by traits which depend on
it. These must also implement the `direct_serial_write` method. See
[uses-uart](../uses-uart) and [uses-i2c](../uses-i2c) for more in depth implementation.
