"""Python Plugin Reloader for QGIS.

    begin                : 2010-01-24
    copyright            : (C) 2010 by Borys Jurgiel
    email                : qgis at borysjurgiel dot pl
    The "Reload" icon copyright by Matt Ball http://www.mattballdesign.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""

import os


def resolve(name, basepath=None):
    if not basepath:
        basepath = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(basepath, name)


def classFactory(iface):
    """Load plugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geolines_qc_plugin import GeolinesQCPlugin

    return GeolinesQCPlugin(iface)
