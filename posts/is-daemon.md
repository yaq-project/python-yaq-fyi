---
id: is-daemon
title: Implementing the `is-daemon` trait
---

The [`is-daemon`](https://yaq.fyi/traits/is-daemon) trait is formally defined by [YEP-300](https://yeps.yaq.fyi/300).

Everything in the `is-daemon` trait is implemented by the `Base` daemon
class. Simply subclassing any of the core daemon classes gives all methods
and configuration parsing.
All you need to do is add the functions/implement the traits unique to
your daemon.