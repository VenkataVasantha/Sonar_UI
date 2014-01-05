#!/usr/bin/python
# vim:set ft=python:ts=4:sts=4:

import sys
import pprint

sys.path.insert( 0, 'modules' )
import Sonar.DB as sdb

db = sdb.SonarDB()
if not db:
    print "Connection Fail !!!";
    sys.exit(1)

pp = pprint.PrettyPrinter( indent = 4 )

hosts = db.getHosts()
if hosts is not None:
    pp.pprint( hosts )


