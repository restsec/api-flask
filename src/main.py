# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:15:29 2017

"""

from flask import Flask
import argparse
import logging

import controllers.pessoal as con

app = Flask(__name__)
app.register_blueprint(con.pessoal_controllers)

if __name__ == '__main__':
    # configuring the parameters parser and storing parameters in global vars
    parser = argparse.ArgumentParser(description='"API Servidor" to provide/handle employee\'s data.')

    parser.add_argument("-s", "--servername", metavar='server_name', 
                        help='Name of the database host server')
    parser.add_argument("-d", "--database", 
                        help="Name of the database", metavar="database_name")
    parser.add_argument("-u", "--username", 
                        help="Username to access the database", metavar="username")
    parser.add_argument("-w", "--password", 
                        help="User's password to acess the database", metavar="user_password")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("-p", "--port", type=int, default=8000,
                        help="Port the program will try to use to serve de API", metavar="api_port")
    args = parser.parse_args()

    con.configure_params(args.servername, args.database, args.username, args.password)

    if args.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    logging.basicConfig(filename='python-api.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=log_level)
    logging.info("API Employee started")

    # starting the web server
    app.run(debug=args.debug, host='0.0.0.0', port=args.port)
