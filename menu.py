"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
	ADMIN_TOOLS_MENU = 'automation.menu.CustomMenu'
"""

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu
from admin_tools.menu.models import *


class CustomMenu(Menu):
	"""
	Custom Menu for automation admin site.
	"""
	def __init__(self, **kwargs):
		Menu.__init__(self, **kwargs)
		self.children += [
			items.MenuItem(_('Dashboard'), reverse('admin:index')),
			items.Bookmarks(),
			items.AppList(
				_('Applications'),
				exclude=('django.contrib.*',)
			),
			items.AppList(
				_('Administration'),
				models=('django.contrib.*',)
			)
		]

	def init_with_context(self, context):
		"""
		Use this method if you need to access the request context.
		"""
		return super(CustomMenu, self).init_with_context(context)
	
class HistoryMenuItem(MenuItem):
    def init_with_context(self, context):
        self.title = 'History'
        request = context['request']
        # we use sessions to store the visited pages stack
        history = request.session.get('history', [])
        for item in history:
            self.children.append(MenuItem(
                title=item['title'],
                url=item['url']
            ))
        # add the current page to the history
        history.insert(0, {
            'title': context['title'],
            'url': request.META['PATH_INFO']
        })
        if len(history) > 10:
            history = history[:10]
        request.session['history'] = history
		


class MyMenu(Menu):
    def __init__(self, **kwargs):
        super(MyMenu, self).__init__(**kwargs)
        self.children.append(
            MenuItem(title='Home', url=reverse('admin:index'))
        )
        self.children.append(
            AppListMenuItem(title='Applications')
        )
        self.children.append(
            MenuItem(
                title='Multi level menu item',
                children=[
                    MenuItem('Child 1'),
                    MenuItem('Child 2'),
                ]
            ),
        )                                                         
                                                  
