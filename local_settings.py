# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

""" There are 3 ways to override GeoNode settings:
   1. Using environment variables, if your changes to GeoNode are minimal.
   2. Creating a downstream project, if you are doing a lot of customization.
   3. Override settings in a local_settings.py file, legacy.
"""

import ast
import os
try:  # python2
    from urlparse import urlparse, urlunparse, urlsplit, urljoin
except ImportError:
    # Python 3 fallback
    from urllib.parse import urlparse, urlunparse, urlsplit, urljoin
from geonode.settings import *

#All configure add.
SITEURL = "http://localhost:8000/"
SITE_HOST_NAME = os.getenv('SITE_HOST_NAME', 'localhost')
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', "en")
#AUTH_USER_MODEL = os.getenv('AUTH_USER_MODEL', 'people.Profile')

GEONODE_CORE_APPS = (
    # GeoNode internal apps
    'geonode.api',
    'geonode.base',
    'geonode.br',
    'geonode.layers',
    'geonode.maps',
    'geonode.geoapps',
    'geonode.documents',
    'geonode.security',
    'geonode.catalogue',
    'geonode.catalogue.metadataxsl',
)

# GeoNode Apps
GEONODE_APPS_ENABLE = ast.literal_eval(os.getenv("GEONODE_APPS_ENABLE", "True"))
GEONODE_APPS_NAME = os.getenv("GEONODE_APPS_NAME", "Apps")
GEONODE_APPS_NAV_MENU_ENABLE = ast.literal_eval(os.getenv("GEONODE_APPS_NAV_MENU_ENABLE", "True"))

GEONODE_INTERNAL_APPS = (
    # GeoNode internal apps
    'geonode.people',
    'geonode.client',
    'geonode.themes',
    'geonode.proxy',
    'geonode.social',
    'geonode.groups',
    'geonode.services',
    'geonode.management_commands_http',

    # GeoServer Apps
    # Geoserver needs to come last because
    # it's signals may rely on other apps' signals.
    'geonode.geoserver',
    'geonode.upload',
    'geonode.tasks',
    'geonode.messaging',
    'geonode.favorite',
    'geonode.monitoring'
)

GEONODE_CONTRIB_APPS = (
    # GeoNode Contrib Apps
)

# Uncomment the following line to enable contrib apps
GEONODE_APPS = GEONODE_CORE_APPS + GEONODE_INTERNAL_APPS + GEONODE_CONTRIB_APPS

INSTALLED_APPS = (

    # Boostrap admin theme
    # 'django_admin_bootstrapped.bootstrap3',
    # 'django_admin_bootstrapped',

    # Apps bundled with Django
    'modeltranslation',
    'dal',
    'dal_select2',
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.gis',

    # Utility
    'dj_pagination',
    'taggit',
    'treebeard',
    'leaflet',
    'bootstrap3_datetime',
    'django_filters',
    'mptt',
    'storages',
    'floppyforms',
    'tinymce',
    'widget_tweaks',
    'django_celery_beat',
    'django_celery_results',
    'markdownify',
    'django_user_agents',

    # REST APIs
    'rest_framework',
    'rest_framework_gis',
    'dynamic_rest',
    'drf_spectacular',

    # Theme
    'django_forms_bootstrap',

    # Social
    'avatar',
    'dialogos',
    'pinax.ratings',
    'announcements',
    'actstream',
    'user_messages',
    'tastypie',
    'polymorphic',
    'guardian',
    'oauth2_provider',
    'corsheaders',
    'invitations',

    # login with external providers
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # GeoNode
    'geonode',

    #Forest app IA
    'forest',
)
INSTALLED_APPS += GEONODE_APPS

#end All add.


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(PROJECT_ROOT, "uploaded"))

STATIC_ROOT = os.getenv('STATIC_ROOT',
                        os.path.join(PROJECT_ROOT, "static_root")
                        )

TIME_ZONE = 'UTC'

# Login and logout urls override
LOGIN_URL = os.getenv('LOGIN_URL', '{}account/login/'.format(SITEURL))
LOGOUT_URL = os.getenv('LOGOUT_URL', '{}account/logout/'.format(SITEURL))

ACCOUNT_LOGIN_REDIRECT_URL = os.getenv('LOGIN_REDIRECT_URL', SITEURL)
ACCOUNT_LOGOUT_REDIRECT_URL =  os.getenv('LOGOUT_REDIRECT_URL', SITEURL)

AVATAR_GRAVATAR_SSL = ast.literal_eval(os.getenv('AVATAR_GRAVATAR_SSL', 'True'))

# Backend
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geonode',
        'USER': 'geonode',
        'PASSWORD': 'geonode',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 0,
        'CONN_TOUT': 5,
        'OPTIONS': {
            'connect_timeout': 5,
        }
    },
    # vector datastore for uploads
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': '', # Empty ENGINE name disables
        'NAME': 'geonode_data',
        'USER': 'geonode',
        'PASSWORD': 'geonode',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 0,
        'CONN_TOUT': 5,
        'OPTIONS': {
            'connect_timeout': 5,
        }
    }
}

GEOSERVER_LOCATION = os.getenv(
    'GEOSERVER_LOCATION', 'http://localhost:8080/geoserver/'
)

GEOSERVER_PUBLIC_HOST = os.getenv(
    'GEOSERVER_PUBLIC_HOST', SITE_HOST_NAME
)

GEOSERVER_PUBLIC_PORT = os.getenv(
    'GEOSERVER_PUBLIC_PORT', 8080
)

_default_public_location = 'http://{}:{}/geoserver/'.format(GEOSERVER_PUBLIC_HOST, GEOSERVER_PUBLIC_PORT) if GEOSERVER_PUBLIC_PORT else 'http://{}/geoserver/'.format(GEOSERVER_PUBLIC_HOST)

GEOSERVER_WEB_UI_LOCATION = os.getenv(
    'GEOSERVER_WEB_UI_LOCATION', GEOSERVER_LOCATION
)

GEOSERVER_PUBLIC_LOCATION = os.getenv(
    'GEOSERVER_PUBLIC_LOCATION', _default_public_location
)

OGC_SERVER_DEFAULT_USER = os.getenv(
    'GEOSERVER_ADMIN_USER', 'admin'
)

OGC_SERVER_DEFAULT_PASSWORD = os.getenv(
    'GEOSERVER_ADMIN_PASSWORD', 'geoserver'
)

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': GEOSERVER_LOCATION,
        'WEB_UI_LOCATION': GEOSERVER_WEB_UI_LOCATION,
        'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION': GEOSERVER_PUBLIC_LOCATION,
        'USER': OGC_SERVER_DEFAULT_USER,
        'PASSWORD': OGC_SERVER_DEFAULT_PASSWORD,
        'MAPFISH_PRINT_ENABLED': True,
        'PRINT_NG_ENABLED': True,
        'GEONODE_SECURITY_ENABLED': True,
        'GEOFENCE_SECURITY_ENABLED': True,
        'WMST_ENABLED': False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED': False,
        'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to dictionary identifier of database containing spatial data in DATABASES dictionary to enable
        'DATASTORE': 'datastore',
        'TIMEOUT': int(os.getenv('OGC_REQUEST_TIMEOUT', '60')),
        'MAX_RETRIES': int(os.getenv('OGC_REQUEST_MAX_RETRIES', '5')),
        'BACKOFF_FACTOR': float(os.getenv('OGC_REQUEST_BACKOFF_FACTOR', '0.3')),
        'POOL_MAXSIZE': int(os.getenv('OGC_REQUEST_POOL_MAXSIZE', '10')),
        'POOL_CONNECTIONS': int(os.getenv('OGC_REQUEST_POOL_CONNECTIONS', '10')),
    }
}

# If you want to enable Mosaics use the following configuration
UPLOADER = {
    # 'BACKEND': 'geonode.rest',
    'BACKEND': 'geonode.importer',
    'OPTIONS': {
        'TIME_ENABLED': True,
        'MOSAIC_ENABLED': False,
    },
    'SUPPORTED_CRS': [
        'EPSG:4326',
        'EPSG:3785',
        'EPSG:3857',
        'EPSG:32647',
        'EPSG:32736'
    ],
    'SUPPORTED_EXT': [
        '.shp',
        '.csv',
        '.kml',
        '.kmz',
        '.json',
        '.geojson',
        '.tif',
        '.tiff',
        '.geotiff',
        '.gml',
        '.xml'
    ]
}

# CSW settings
CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',
        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': urljoin(SITEURL, '/catalogue/csw'),
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',
        'USER': 'admin',
        'PASSWORD': 'admin',
        # 'ALTERNATES_ONLY': True,
    }
}

# pycsw settings
PYCSW = {
    # pycsw configuration
    'CONFIGURATION': {
        # uncomment / adjust to override server config system defaults
        # 'server': {
        #    'maxrecords': '10',
        #    'pretty_print': 'true',
        #    'federatedcatalogues': 'http://catalog.data.gov/csw'
        # },
        'server': {
            'home': '.',
            'url': CATALOGUE['default']['URL'],
            'encoding': 'UTF-8',
            'language': LANGUAGE_CODE,
            'maxrecords': '20',
            'pretty_print': 'true',
            # 'domainquerytype': 'range',
            'domaincounts': 'true',
            'profiles': 'apiso,ebrim',
        },
        'manager': {
            # authentication/authorization is handled by Django
            'transactions': 'false',
            'allowed_ips': '*',
            # 'csw_harvest_pagesize': '10',
        },
        'metadata:main': {
            'identification_title': 'GeoNode Catalogue',
            'identification_abstract': 'GeoNode is an open source platform' \
            ' that facilitates the creation, sharing, and collaborative use' \
            ' of geospatial data',
            'identification_keywords': 'sdi, catalogue, discovery, metadata,' \
            ' GeoNode',
            'identification_keywords_type': 'theme',
            'identification_fees': 'None',
            'identification_accessconstraints': 'None',
            'provider_name': 'Organization Name',
            'provider_url': SITEURL,
            'contact_name': 'Lastname, Firstname',
            'contact_position': 'Position Title',
            'contact_address': 'Mailing Address',
            'contact_city': 'City',
            'contact_stateorprovince': 'Administrative Area',
            'contact_postalcode': 'Zip or Postal Code',
            'contact_country': 'Country',
            'contact_phone': '+xx-xxx-xxx-xxxx',
            'contact_fax': '+xx-xxx-xxx-xxxx',
            'contact_email': 'Email Address',
            'contact_url': 'Contact URL',
            'contact_hours': 'Hours of Service',
            'contact_instructions': 'During hours of service. Off on ' \
            'weekends.',
            'contact_role': 'pointOfContact',
        },
        'metadata:inspire': {
            'enabled': 'true',
            'languages_supported': 'eng,gre',
            'default_language': 'eng',
            'date': 'YYYY-MM-DD',
            'gemet_keywords': 'Utility and governmental services',
            'conformity_service': 'notEvaluated',
            'contact_name': 'Organization Name',
            'contact_email': 'Email Address',
            'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD',
        }
    }
}

# -- START Client Hooksets Setup

# GeoNode javascript client configuration

# default map projection
# Note: If set to EPSG:4326, then only EPSG:4326 basemaps will work.
DEFAULT_MAP_CRS = os.environ.get('DEFAULT_MAP_CRS', "EPSG:3857")

DEFAULT_LAYER_FORMAT = os.environ.get('DEFAULT_LAYER_FORMAT', "image/png")

# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (os.environ.get('DEFAULT_MAP_CENTER_X', 0), os.environ.get('DEFAULT_MAP_CENTER_Y', 0))

# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
DEFAULT_MAP_ZOOM = int(os.environ.get('DEFAULT_MAP_ZOOM', 3))

MAPBOX_ACCESS_TOKEN = os.environ.get('MAPBOX_ACCESS_TOKEN', None)
BING_API_KEY = os.environ.get('BING_API_KEY', None)
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', None)

GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY = os.getenv('GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY', 'mapstore')

MAP_BASELAYERS = [{}]

"""
To enable the REACT based Client:
1. pip install pip install django-geonode-client==1.0.9
2. enable those:
"""

if GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY == 'react':
    GEONODE_CLIENT_HOOKSET = os.getenv('GEONODE_CLIENT_HOOKSET', 'geonode.client.hooksets.ReactHookSet')
    if 'geonode-client' not in INSTALLED_APPS:
        INSTALLED_APPS += ('geonode-client', )

"""
To enable the Leaflet based Client:
1. enable those:
"""
if GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY == 'leaflet':
    GEONODE_CLIENT_HOOKSET = os.getenv('GEONODE_CLIENT_HOOKSET', 'geonode.client.hooksets.LeafletHookSet')

    CORS_ORIGIN_WHITELIST = (SITEURL, )

    LEAFLET_CONFIG = {
        'TILES': [
            # Find tiles at:
            # http://leaflet-extras.github.io/leaflet-providers/preview/

            # Stamen toner lite.
            ('Watercolor',
                'http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.png',
                'Map tiles by <a href="http://stamen.com">Stamen Design</a>, \
                <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> \
                &mdash; Map data &copy; \
                <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
                <a href="http://creativecommons.org/licenses/by-sa/2.0/"> \
                CC-BY-SA</a>'),
            ('Toner Lite',
                'http://{s}.tile.stamen.com/toner-lite/{z}/{x}/{y}.png',
                'Map tiles by <a href="http://stamen.com">Stamen Design</a>, \
                <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> \
                &mdash; Map data &copy; \
                <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
                <a href="http://creativecommons.org/licenses/by-sa/2.0/"> \
                CC-BY-SA</a>'),
        ],
        'PLUGINS': {
            'esri-leaflet': {
                'js': 'lib/js/leaflet.js',
                'auto-include': True,
            },
            'leaflet-fullscreen': {
                'css': 'lib/css/leaflet.fullscreen.css',
                'js': 'lib/js/Leaflet.fullscreen.min.js',
                'auto-include': True,
            },
            'leaflet-opacity': {
                'css': 'lib/css/L.Control.Opacity.css',
                'js': 'lib/js/L.Control.Opacity.js',
                'auto-include': True,
            },
            'leaflet-navbar': {
                'css': 'lib/css/Leaflet.NavBar.css',
                'js': 'lib/js/index.js',
                'auto-include': True,
            },
            'leaflet-measure': {
                'css': 'lib/css/leaflet-measure.css',
                'js': 'lib/js/leaflet-measure.js',
                'auto-include': True,
            },
        },
        'SRID': 3857,
        'RESET_VIEW': False
    }

    if not DEBUG_STATIC:
        # if not DEBUG_STATIC, use minified css and js
        LEAFLET_CONFIG['PLUGINS'] = {
            'leaflet-plugins': {
                'js': 'lib/js/leaflet-plugins.min.js',
                'css': 'lib/css/leaflet-plugins.min.css',
                'auto-include': True,
            }
        }

"""
To enable the MapStore2 REACT based Client:
1. pip install pip install django-geonode-mapstore-client==1.0
2. enable those:
"""
if GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY == 'mapstore':
    GEONODE_CLIENT_HOOKSET = os.getenv('GEONODE_CLIENT_HOOKSET', 'geonode_mapstore_client.hooksets.MapStoreHookSet')

    if 'geonode_mapstore_client' not in INSTALLED_APPS:
        INSTALLED_APPS += (
            'mapstore2_adapter',
            'geonode_mapstore_client',)

    def get_geonode_catalogue_service():
        if PYCSW:
            pycsw_config = PYCSW["CONFIGURATION"]
            if pycsw_config:
                    pycsw_catalogue = {
                        ("%s" % pycsw_config['metadata:main']['identification_title']): {
                            "url": CATALOGUE['default']['URL'],
                            "type": "csw",
                            "title": pycsw_config['metadata:main']['identification_title'],
                            "autoload": True
                         }
                    }
                    return pycsw_catalogue
        return None

    GEONODE_CATALOGUE_SERVICE = get_geonode_catalogue_service()

    MAPSTORE_CATALOGUE_SERVICES = {
        "Demo WMS Service": {
            "url": "https://demo.geo-solutions.it/geoserver/wms",
            "type": "wms",
            "title": "Demo WMS Service",
            "autoload": False
         },
        "Demo WMTS Service": {
            "url": "https://demo.geo-solutions.it/geoserver/gwc/service/wmts",
            "type": "wmts",
            "title": "Demo WMTS Service",
            "autoload": False
        }
    }

    MAPSTORE_CATALOGUE_SELECTED_SERVICE = "Demo WMS Service"

    if GEONODE_CATALOGUE_SERVICE:
        MAPSTORE_CATALOGUE_SERVICES[list(GEONODE_CATALOGUE_SERVICE.keys())[0]] = GEONODE_CATALOGUE_SERVICE[list(GEONODE_CATALOGUE_SERVICE.keys())[0]]
        MAPSTORE_CATALOGUE_SELECTED_SERVICE = list(GEONODE_CATALOGUE_SERVICE.keys())[0]

    DEFAULT_MS2_BACKGROUNDS = [
        {
            "type": "tileprovider",
            "title": "Stamen Watercolor",
            "provider": "Stamen.Watercolor",
            "name": "Stamen.Watercolor",
            "source": "Stamen",
            "group": "background",
            "thumbURL": "https://stamen-tiles-c.a.ssl.fastly.net/watercolor/0/0/0.jpg",
            "visibility": False
        },
        {
            "type": "tileprovider",
            "title": "Stamen Terrain",
            "provider": "Stamen.Terrain",
            "name": "Stamen.Terrain",
            "source": "Stamen",
            "group": "background",
            "thumbURL": "https://stamen-tiles-d.a.ssl.fastly.net/terrain/0/0/0.png",
            "visibility": False
        },
        {
            "type": "tileprovider",
            "title": "Stamen Toner",
            "provider": "Stamen.Toner",
            "name": "Stamen.Toner",
            "source": "Stamen",
            "group": "background",
            "thumbURL": "https://stamen-tiles-d.a.ssl.fastly.net/toner/0/0/0.png",
            "visibility": False
        },
        {
            "type": "osm",
            "title": "Open Street Map",
            "name": "mapnik",
            "source": "osm",
            "group": "background",
            "visibility": True
        },
        {
            "type": "tileprovider",
            "title": "OpenTopoMap",
            "provider": "OpenTopoMap",
            "name": "OpenTopoMap",
            "source": "OpenTopoMap",
            "group": "background",
            "visibility": False
        },
        {
            "type": "wms",
            "title": "Sentinel-2 cloudless - https://s2maps.eu",
            "format": "image/jpeg",
            "id": "s2cloudless",
            "name": "s2cloudless:s2cloudless",
            "url": "https://maps.geo-solutions.it/geoserver/wms",
            "group": "background",
            "thumbURL": "%sstatic/mapstorestyle/img/s2cloudless-s2cloudless.png" % SITEURL,
            "visibility": False
        },
        {
            "source": "ol",
            "group": "background",
            "id": "none",
            "name": "empty",
            "title": "Empty Background",
            "type": "empty",
            "visibility": False,
            "args": ["Empty Background", {"visibility": False}]
        }
    ]

    if MAPBOX_ACCESS_TOKEN:
        MAPBOX_BASEMAPS = {
            "type": "tileprovider",
            "title": "MapBox streets-v11",
            "provider": "MapBoxStyle",
            "name": "MapBox streets-v11",
            "accessToken": "%s" % MAPBOX_ACCESS_TOKEN,
            "source": "streets-v11",
            "thumbURL": "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/256/6/33/23?access_token=%s" % MAPBOX_ACCESS_TOKEN,
            "group": "background",
            "visibility": True
        }
        DEFAULT_MS2_BACKGROUNDS = [MAPBOX_BASEMAPS,] + DEFAULT_MS2_BACKGROUNDS

    if BING_API_KEY:
        BING_BASEMAPS = [
            {
                "type": "bing",
                "title": "Bing Aerial",
                "name": "AerialWithLabels",
                "source": "bing",
                "group": "background",
                "apiKey": "{{apiKey}}",
                "visibility": True
            },
            {
                "type": "bing",
                "title": "Bing RoadOnDemand",
                "name": "RoadOnDemand",
                "source": "bing",
                "group": "background",
                "apiKey": "{{apiKey}}",
                "thumbURL": "%sstatic/mapstorestyle/img/bing_road_on_demand.png" % SITEURL,
                "visibility": False
            },
            {
                "type": "bing",
                "title": "Bing AerialWithLabelsOnDemand",
                "name": "AerialWithLabelsOnDemand",
                "source": "bing",
                "group": "background",
                "apiKey": "{{apiKey}}",
                "thumbURL": "%sstatic/mapstorestyle/img/bing_aerial_w_labels.png" % SITEURL,
                "visibility": False
            },
            {
                "type": "bing",
                "title": "Bing CanvasDark",
                "name": "CanvasDark",
                "source": "bing",
                "group": "background",
                "apiKey": "{{apiKey}}",
                "thumbURL": "%sstatic/mapstorestyle/img/bing_canvas_dark.png" % SITEURL,
                "visibility": False
            }
        ]
        DEFAULT_MS2_BACKGROUNDS = [BING_BASEMAPS, ] + DEFAULT_MS2_BACKGROUNDS

    MAPSTORE_BASELAYERS = DEFAULT_MS2_BACKGROUNDS

# -- END Client Hooksets Setup

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d '
                      '%(thread)d %(message)s'
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"], "level": "ERROR", },
        "geonode": {
            "handlers": ["console"], "level": "INFO", },
        "geoserver-restconfig.catalog": {
            "handlers": ["console"], "level": "ERROR", },
        "owslib": {
            "handlers": ["console"], "level": "ERROR", },
        "pycsw": {
            "handlers": ["console"], "level": "INFO", },
        "celery": {
            'handlers': ["console"], 'level': 'ERROR', },
    },
}

# Additional settings
X_FRAME_OPTIONS = 'ALLOW-FROM %s' % SITEURL
CORS_ORIGIN_ALLOW_ALL = True

GEOIP_PATH = "/usr/local/share/GeoIP"
