# -*- coding: utf-8 -*-
import web
import logging
import threading
import logging.handlers
import os
import time

#import logging
#logging.basicConfig()

lock = threading.Lock()
logger = 0
handler = 0
log_name = 0
is_debug = False

def show(log):
	if True:
		lock.acquire()
		print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),log)
		lock.release()

def init(name): 
	global logger
	global handler
	global log_name
	try: 
		dirpath = "log/"
		if os.path.exists(dirpath) == False:
			os.makedirs(dirpath)
		log_name = dirpath + name
		logger = logging.getLogger('[%s]'%name)
		handler = logging.handlers.RotatingFileHandler(log_name,maxBytes=20*1024*1024,backupCount=10)
		# handler = logging.handlers.TimedRotatingFileHandler(log_name,'D',1,30)
		# handler.suffix = "%Y-%m-%d.log"
		# handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
		#formatter = logging.Formatter('%(asctime)s %(name)s[%(levelname)-7s]:%(message)s')
		formatter = logging.Formatter('%(asctime)s [%(levelname)-7s]:%(message)s')
		handler.setFormatter(formatter)    
		logger.addHandler(handler)
		# logger.setLevel(logging.INFO)
		logger.setLevel(logging.DEBUG)
	except Exception,ex:
		print 'log init error %s:%s'%(Exception,ex)

def log(level, log):
	#lock.acquire()
	try:
		show(log)
		logger.log(level,log)
	except Exception,ex:
		print 'log log %s:%s'%(Exception,ex)
	#lock.release()

def info(log):
	#lock.acquire()
	try:
		show(log)
		logger.info(log)
	except Exception,ex:
		print 'log info %s:%s'%(Exception,ex)
	#lock.release()

def warning(log):
	#lock.acquire()
	try:
		show(log)
		logger.warning(log)
	except Exception,ex:
		print 'log warning %s:%s'%(Exception,ex)
	#lock.release()

def error(log):
	#lock.acquire()
	try:
		show(log)
		logger.error(log)
	except Exception,ex:
		print 'log error %s:%s'%(Exception,ex)
	#lock.release()

def debug(log):
	global is_debug
	if False == is_debug:
		return
	#lock.acquire()
	try:
		show(log)
		logger.debug(log)
	except Exception,ex:
		print 'log error %s:%s'%(Exception,ex)
	#lock.release()

class logDS:
	def POST(self):
		data = web.input()
		global is_debug
		response = 'no debug...'
		if data['debug'] == "1":
			is_debug = True
			response = 'debug...'
		else:
			is_debug = False
		return response

	def GET(self):
		response = 'no debug...'
		global is_debug
		if is_debug:
			response = 'debug...'
		return response

if __name__ == "__main__":
	print '__main__ begin....'
	init('logDS.log')
	log(logging.DEBUG, 'test log')
	log(logging.INFO, 'test log')
	log(logging.WARNING, 'test log')
	log(logging.ERROR, 'test log')
	info('test info')
	warning('test warning')
	error('test error')
	debug('test debug 00')
	#global is_debug
	is_debug = True
	debug('test debug 11')
	is_debug = False
	debug('test debug 22')
	print '__main__ end....'