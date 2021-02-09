# zabbix-barman

zabbix-barman template

Barman monitoring template for Zabbix.


Requirements:

In order to work you need to configure following option for Zabbix 

* In your sudoers file add following option: 
* add it for example here on CentOS (/etc/sudoers.d/zabbix)
Defaults:zabbix !requiretty
zabbix ALL=(ALL) NOPASSWD: ALL

* Copy the userparameter_barman.conf file to your zabbix agent on the barman server. Usually this is /etc/zabbix/zabbix_agent2.d or /etc/zabbix/zabbix_agentd.d

* Alter the permissions
* chmod 660 userparameter_barman.conf
* chown zabbix:zabbix userparameter_barman.conf
* Restart zabbix-agent

* Copy barman_discovery.py to /usr/share/zabbix-agent/scripts/barman_discovery.py
* chmod 550 barman_discovery.py
* chown zabbix:zabbix barman_discovery.py

* Import Template Barman.xml in the Zabbix Server
* Link Template to your Barman Server in Zabbix (Configuration -> Hosts - Barman host - Tab templates)

* Auto Discovery will do the rest
