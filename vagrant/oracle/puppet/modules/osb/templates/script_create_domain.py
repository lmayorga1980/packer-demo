#!/usr/bin/python
import os, sys
#  http://docs.oracle.com/cd/E28280_01/install.1111/b32474/silent_install.htm#CHDGECID
#
# Parameters:
# osb_domain	Define the Oracle Service Bus Domain
#

def createDomain(domain_name, weblogic_password, admin_server_name, listen_port, listen_address, mdw_home, domains_home):
	wls_home = mdw_home + "/wlserver_10.3",
	readTemplate(wls_home + '/common/templates/domains/wls.jar')
	#readTemplate(mdw_home + "/OracleOSB1/common/templates/applications/wlsb_single_server.jar")
	cd('/Security/base_domain/User/weblogic')
	cmo.setPassword(weblogic_password)
	cd('/Server/AdminServer')
	cmo.setName(admin_server_name)
	cmo.setListenPort(listen_port)
	cmo.setListenAddress(listen_address)
	writeDomain(domains_home + "/" + domain_name)
	closeTemplate()
	exit()
	return

createDomain("osb_domain", "welcome1", "AdminServer", 7001, "localhost", "<%=@mdw%>", "<%=@domain_directory%>")

