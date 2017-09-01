# -*- coding: utf-8 -*-


import os


class ConverterMixin(object):

    class MainMenuNode(object):
        """
        Class for MainMenu objects-nodes
        """
        def __init__(self, node_obj):
            self.name = node_obj.title
            if node_obj.Options.native:
                self.link = {'href': '/{}/'.format(node_obj.link)}
            else:
                self.link = {'href': '/{}/'.format('/'.join(node_obj.Options.url_path + [node_obj.slug_title]))}
            self.options = {}
            self.children = []
            self.options.update({'board': False})

    def _format(self):
        """
        Method for format data from Django ORM format to widget format
        :return:
        """
        main_menu_storage = []
        for item in self.menu_item_s:
            self.__recursive_node_append(item.item_content_object, main_menu_storage)
        self.header.update({
            'main_menu': main_menu_storage,
            'logo': self.header_settings.logo,
            'phone': self.header_settings.phone
        })

    def __recursive_node_append(self, node_obj, storage):
        node = self.MainMenuNode(node_obj)
        storage.append(node)
        for item in node_obj.get_show_children():
            self.__recursive_node_append(item, node.children)
