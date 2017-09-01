# -*- coding: utf-8 -*-


import os
import json


class MainMenuConverterMixin(object):

    main_menu_item_s = None


    class MainMenuNode(object):
        """
        Class for MainMenu objects-nodes
        """
        def __init__(self, node_obj):
            self.name = node_obj.title
            if node_obj.Options.native:
                self.link = {
                    'href': node_obj.link
                }
            else:
                self.link = {
                    'href': '/{}/'.format('/'.join(node_obj.Options.url_path + [node_obj.slug_title]))
                }
            self.options = {}
            self.children = []
            self.options.update({'board': False})

    def _format(self):
        """
        Method for format data from Django ORM format to widget format
        :return:
        """
        main_menu_storage = []
        for item in self.main_menu_item_s:
            self.__recursive_node_append(item.item_content_object, main_menu_storage)
        self.header.update({
            'main_menu': main_menu_storage,
            'logo': {
                'title': self.header_settings.title,
                'short': self.header_settings.short,
                'logo': self.header_settings.logo
            },
            'phone': {
                'active': True,
                'key': self.header_settings.phone
            }
        })
        self.extra = json.loads(self.header_settings.extra.extra_field) \
            if hasattr(self.header_settings, 'extra') else {}
        for k, v in self.extra.items():
            self.header.update({k: v})

    def __recursive_node_append(self, node_obj, storage):
        node = self.MainMenuNode(node_obj)
        storage.append(node)
        for item in node_obj.get_show_children():
            self.__recursive_node_append(item, node.children)
