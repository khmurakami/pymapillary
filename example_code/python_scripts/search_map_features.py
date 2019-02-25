#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This sample code

from pymapillary import Mapillary

map = Mappilary("insert client id here")
print(map.search_map_features("trafficsigns",1))
