import yaqc
from pprint import pprint

sysmon = yaqc.Client(38202)
sysmon.traits
pprint(dir(sysmon))
help(sysmon.measure)
help(sysmon.get_measured)
sysmon.get_channel_names()
sysmon.get_channel_units()
sysmon.busy()
sysmon.measure(loop=True)
sysmon.get_measured()
sysmon.get_measured()
sysmon.get_measured()
sysmon.get_measured()
sysmon.busy()
