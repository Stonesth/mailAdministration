#!/usr/bin/python
# -*- coding:utf-8 -*-
from Tools import tools_v000 as tools
import os
from os.path import dirname
from MyHours import myhours as m


# -18 for the name of this project cafeAdministration
save_path = os.path.dirname(os.path.abspath("__file__"))
propertiesFolder_path = save_path + "/"+ "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'cafeAdministration', 'user_text=')

# Open Browser
tools.openBrowserChrome()

m.connectToMyHours()
m.enterCredentials()
m.startTrackWithDescription(u'', u'Mail + administration', u'Business operations (non project / service related tasks) (P0710) - Business operations (non project / service related tasks)')

# Exit Chrome
tools.driver.quit()
