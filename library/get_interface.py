#!/usr/bin/python
import json
import re
import commands

def get_interface(topic, prefix):
    net_map = {}
    output = commands.getoutput("""/usr/sbin/ip l|grep "mtu" |awk '{print $2}' |grep -wv 'lo' | awk -F: '{print $1}'""")
    nics = output.split('\n')
    for nic in nics:
        ipaddr = commands.getoutput("""/usr/sbin/ip a show %s |grep -w inet |cut -d: -f2 | awk '{print $2}' | awk -F/ '{print $1}'""" % nic)
        if re.match(str(prefix), str(ipaddr)):
        #    module.fail_json(msg="MAPPING %s" % ipaddr)
            net_map['gi_' + topic + '_interface'] = nic
        else:
            pass
    return net_map

def main():
    global module
    module = AnsibleModule(
        argument_spec = dict(
            topic=dict(required=True),
            regex=dict(required=True),
        ),
        supports_check_mode = True,
    )
    ansible_facts_dict = {
        "changed" : False,
        "ansible_facts": {
            }
    }

    net_map = {}
    topic = module.params.get('topic')
    prefix = module.params.get('regex')
    net_map = get_interface(topic, prefix)

    if net_map:
        ansible_facts_dict['ansible_facts'][net_map.keys()[0]] = net_map.values()[0]
        ansible_facts_dict['changed'] = True
    else:
        module.fail_json(msg="Interface not Found for regex %s " % prefix)

    module.exit_json(**ansible_facts_dict)


from ansible.module_utils.basic import *
from ansible.module_utils.facts import *
main()
