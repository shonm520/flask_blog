#-*- coding:utf-8 -*-

from flask_script import Manager, Server
#from app import app

from app import views

#import views

manager = Manager(views.app)
manager.add_command("runserver", Server(host='192.168.0.136', port=5052, use_debugger=True))
if __name__ == '__main__':
    manager.run()
