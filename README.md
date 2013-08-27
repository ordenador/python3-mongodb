python3-mongodb
===============

Python3 with Mongodb - hello world



easy_install pymongo


#Installar mongodb
export MONGODB_HOME=/path/mongodb
echo "logpath=$MONGODB_HOME/log/mongo.log" > $MONGODB_HOME/mongod.cfg
echo "dbpath=$MONGODB_HOME/data" >> $MONGODB_HOME/mongod.cfg

## start server
$MONGODB_HOME/bin/mongod

## start cliente y crear db: scraping
	MongoDB shell version: 2.4.6
	connecting to: test
	> show dbs
	local   0.078125GB
	test    0.203125GB
	> use strapingdb
	switched to db strapingdb
	> db.users.save({username:"straping"})
	> db.users.find()
	{ "_id" : ObjectId("521c1a93d8a7d65e29fa999e"), "username" : "straping" }
	> show dbs
	local   0.078125GB
	strapingdb      0.203125GB
	test    0.203125GB
	>
