import yaqc
from pprint import pprint

sysmon = yaqc.Client(38202)
pprint(sysmon.list_methods())
sysmon.get_channel_names()
sysmon.get_channel_units()
sysmon.busy()
sysmon.measure(loop=True)
sysmon.get_measured()
sysmon.get_measured()
sysmon.get_measured()
sysmon.get_measured()
sysmon.busy()
