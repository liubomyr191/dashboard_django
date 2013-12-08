from dash.base import plugin_widget_registry
from dash.base import plugin_widget_registry
from dash.factory import plugin_widget_factory
from dash.contrib.plugins.dummy.dash_widgets import BaseDummyWidget
from dash.contrib.plugins.image.dash_widgets import BaseImageWidget
from dash.contrib.plugins.memo.dash_widgets import BaseMemoWidget, BaseTinyMCEMemoWidget
#from dash.contrib.plugins.news.dash_widgets import BaseNewsWidget
from dash.contrib.plugins.rss_feed.dash_widgets import BaseReadRSSFeedWidget
from dash.contrib.plugins.video.dash_widgets import BaseVideoWidget
#from dash.contrib.plugins.weather.dash_widgets import BaseWeatherWidget
from dash.contrib.layouts.windows8.dash_widgets import (
    URL1x1Windows8MainWidget, URL1x1Windows8SidebarWidget,
    )

# **************************************************************************
# **************************************************************************
# **************************************************************************
# ************************* Registering the widgets ************************
# **************************************************************************
# **************************************************************************
# **************************************************************************

# **************************************************************************
# ******************* Registering widgets for Dummy plugin *****************
# **************************************************************************

main_sizes = (
    (1, 1),
)
sidebar_sizes = (
    (1, 1),
)
plugin_widget_factory(BaseDummyWidget, 'windows8', 'main', 'dummy', main_sizes)
plugin_widget_factory(BaseDummyWidget, 'windows8', 'sidebar', 'dummy', sidebar_sizes)

# **************************************************************************
# ******************* Registering widgets for Image plugin *****************
# **************************************************************************

main_sizes = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)
sidebar_sizes = (
    (1, 1),
    (2, 2),
)
plugin_widget_factory(BaseImageWidget, 'windows8', 'main', 'image', main_sizes)
plugin_widget_factory(BaseImageWidget, 'windows8', 'sidebar', 'image', sidebar_sizes)

# **************************************************************************
# ******************* Registering widgets for Memo plugin ******************
# **************************************************************************

main_sizes = (
    (2, 2),
    (3, 3),
)
sidebar_sizes = (
    (2, 2),
)
plugin_widget_factory(BaseMemoWidget, 'windows8', 'main', 'memo', main_sizes)
plugin_widget_factory(BaseMemoWidget, 'windows8', 'sidebar', 'memo', sidebar_sizes)

# **************************************************************************
# ******************* Registering widgets for RSS plugin *******************
# **************************************************************************

main_sizes = (
    (2, 3),
)
sidebar_sizes = (
    (2, 3),
)
plugin_widget_factory(BaseReadRSSFeedWidget, 'windows8', 'main', 'read_rss_feed', main_sizes)
plugin_widget_factory(BaseReadRSSFeedWidget, 'windows8', 'sidebar', 'read_rss_feed', sidebar_sizes)

# **************************************************************************
# ******************* Registering the widgets for URL plugin ***************
# **************************************************************************

plugin_widget_registry.register(URL1x1Windows8MainWidget)
plugin_widget_registry.register(URL1x1Windows8SidebarWidget)

# **************************************************************************
# ***************** Registering the widgets for Video plugin ***************
# **************************************************************************

main_sizes = (
    (2, 2),
)
sidebar_sizes = (
    (2, 3),
)
plugin_widget_factory(BaseVideoWidget, 'windows8', 'main', 'video', main_sizes)
plugin_widget_factory(BaseVideoWidget, 'windows8', 'sidebar', 'video', sidebar_sizes)
