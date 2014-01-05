# vim:set ft=python:ts=4:sts=4:
import yaml
import MySQLdb
import sys

class SonarDB:

    def __init__(self, confpath=None):

        self.__confpath = confpath or "conf/settings.conf"

	    # Open the conf file for database connection settings
		# to connect to database

	    try:
            stream = open( self.__confpath, "r" )
		    conf   = yaml.safe_load( stream )
            dbconf = conf['dbconf']
			con    = MySQLdb.connect( dbconf['host'], dbconf['user'], dbconf['pswd'], dbconf['db'] )

		except IOError:
		    print "ERROR: Cant find or open the file"
            sys.exit(1)

		except MySQLdb.Error, e:
		    print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

		except:
		    print "ERROR: Cant load the settings file"
            sys.exit(1)

		else:
		    self.__con = con

		finally:
		    if stream:
                stream.close()

    def __del__(self):

        if self.__con:
            self.__con.close()


    def getHosts(self):

        try:
            cursor = self.__con.cursor()
            cursor.execute( "SELECT * from Host" )
            rows  = cursor.fetchall()
        
        except MySQLdb.Error, e:
		    print "Error %d: %s" % (e.args[0],e.args[1])
            return None

        except:
            print "ERROR: Unable to run query"
            return None

        else:
            return rows

