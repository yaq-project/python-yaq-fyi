---
id: transition-to-avro
title: Transition guide for the Avro implementation of `yaqd-core`
---

As of `yaqd-core` version 2020.06.2, yaq daemons use [Apache Avro](https://avro.apache.org/docs/1.9.2/spec.html).

This is a  major, breaking change to yaq daemons.

## Transitioning from old style TOML to New TOML files and AVPR files

### Using avro style identifiers
- name -> protocol
- description -> doc
- methods -> messages
- returns -> response
- parameters -> request (list, not table)

### config/state:
- check that types are valid definitions, include defaults
- state values _must_ have defaults


### messages:
- request: list of avro type definitions of parameters. May include default values.
  - May be omitted if there are no parameters
- response: single type definition
  - May be omitted if the return value is `null`

### Notes:
- anywhere where you wish to put an explict default null value, use the TOML string `"__null__"`
  - TOML has no explict null value, but a default of null is different than no default
- Most types are fairly simple to represent in toml format, however ndarrays can be complicated to integrate well. We plan to make this easier in the future.
- Once you have the TOML, use `yaq-traits compose <toml file>` to generate the `avpr` file
  - Both files must be placed in the same directory as the python file, named `<kind>.[toml|avpr]`

## Code changes to the daemons

- Convert variables saved into state into writes/reads from `_state` dict, remove get/load state methods, do anything from load which affect behavior in `__init__` after the super call
- remove defaults dict, traits list (included in toml)
- `self.config` -> `self._config` (most don't actually use this)
- `self.kind` -> `self._kind`
- ensure `get_traits`, `get_version`, `list_methods`, `get_state` not called, these methods are gone

### is-sensor daemons
- add `_` to `channel_[names|units|shapes]`, `measurment_id`, `looping`

### has-position daemons:
- `self._position` now `self._state["position"]`
- `self._destination now` `self._state["destination"]`

### has-limits daemons
- `self._hw_limits` now `self._state["hw_limits"]`

### is-discrete daemons
- `self._position_identifier` now `self._state["position_identifier"]`

### has-turret daemons
- turret tracking  now `self._state["turret"]`

### uses-i2c:
- `direct_serial_write` now explicitly will get bytes, not string

## Repository and packaging changes
- Use flit instead of setup tools
  - New `__version__.py` which does not report a branch when head is detached
  - `flit init` (copy contents from existing pyproject.toml, delete file and run `flit init`, past contents)
  - Add to [tool.flit.metadata] in pyproject.toml:
    - Check info already present
    - requires-python = ">=3.7"
    - requires = ["yaqd-core>=2020.06.3", \<other deps>]
    - classifiers (copy from setup.py, include license classifier
    - description-file="README.md"
  - Add [tool.flit.metadata.requires-extra]
    - dev=["black", "pre-commit"] 
    - any other extras-require from setup.py
  - Add [tool.flit.scripts]
    - equiv to `console_scripts` in setup.py
    - can be directly copied, quote moved to after `=` for toml
    - `yaqd-<kind> = "<module>:<Class>.main"
  - Use `pip install .` (without `-e`)
- Add `yaq-traits check` test unit
  - make sure to install `yaq-traits`
  - One call per avpr

