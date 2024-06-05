#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.client import Client
from models.stylist import Stylist
import ipdb

Stylist.create_table()
Client.create_table()

ipdb.set_trace()
