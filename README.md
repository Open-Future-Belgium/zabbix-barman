# zabbix-barman

zabbix-barman template

Barman monitoring template for Zabbix.


Requirements:

In order to work you need to configure following option for Zabbix 

* In your sudoers file add following option:
zabbix ALL=(barman) NOPASSWD: /usr/bin/barman


* Copy the userparameter_barman.con file to your zabbix agent on the barman server 

* Restart zabbix-agent

* Import Template Barman.xml in the Zabbix Server

* Link Template to your Barman Server

* Auto Discovery will do the rest
