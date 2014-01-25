Ansible
=======


Directory Structure
===================
<pre>
.
├── ansible.cfg                 ==> Ansible Configuration File
├── files                       ==> Directory to store generic/adhoc files
├── handlers                    ==> Directory to be define generic/adhoc handler
│   └── services.yml            ==> Example of a generic handler
├── inventory                   ==> The inventory directory as defined in `ansible.cfg`
│   └── hosts                   ==> The hosts directory containing the hosts definition
│       ├── group_vars          ==> The groups level variable directory
│       ├── host_vars           ==> The hosts level variable directory
│       └── localhost           ==> A typical host definition 
├── playbooks                   ==> Adhoc/one-time playbooks 
│   ├── add-ssh-key.yml         ==> A typical example of a one-time/adhoc playbook
├── plugins                     ==> Plugin directory as defined in `ansible.cfg`
│   ├── action                  ==> `Action` Plugin Directory
│   ├── callback                ==> `CallBack` Plugin Directory
│   ├── connection              ==> `Connection` Plugin Directory
│   ├── filter                  ==> `Filter` Plugin Directory
│   ├── inventory               ==> `Inventory` Plugin Directory [not supported by core Ansible]
│   ├── library                 ==> `Library` for extending Ansible Module Capability
│   ├── lookup                  ==> `Lookup` Plugin Directory
│   └── vars                    ==> `Vars` Plugin Directory
├── README.md                   ==> This file
├── roles                       ==> Organised reusable Playbooks
├── scripts                     ==> Adhoc scripts for bootstrapping, etc. May not be connected to Ansible
├── secrets                     ==> Some secrets variable like pems
└── templates                   ==> Generic Templates
</pre>
