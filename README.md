# Ansible Get-Interfaces
This module will make a mapping between Interface name and a related topic used by the consumer using the ipaddress.
**Example:** the interface with ipaddress 46.0.X.X (based on regex) will be management.
Then, this module will create a fact called 'gi_management_interface' and will map against the interface name that contains this regex.

## How this module works
This module have 2 variables:
- topic
- regex

**Topic**, will make sense to the module's consumer, for example, 'pxe' or maybe 'service' and the interface with this addressing will take this role as a fact, creating 'gi_service_interface'.

**Regex**, will be the addressing that must fit with an ipaddress of an existant interface.

## Execution
- Playbook:
```
- name: get private ip
  get_interface:
    topic: 'management'
    regex: '192.168'
```

- Input:
```
$ ansible-playbook -i inventory test.yml --ask-pass
```

- Output:
```
PLAY [Test filter plugin] ******************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Set Management interface based on a regex] *******************************
changed: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => {
    "msg": "management interface virbr0"
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0   
```
