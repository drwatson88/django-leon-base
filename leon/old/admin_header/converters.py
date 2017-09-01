# -*- coding: utf-8 -*-


import os


class HeaderConverterMixin(object):

    class MainMenuNode(object):
        """
        Class for MainMenu objects-nodes
        """
        def __init__(self, node_obj):
            self.name = node_obj.title
            if node_obj.Options.native:
                self.link = {'href': '/{}/'.format(node_obj.link)}
            else:
                self.link = {'href': '/{}/'.format('/'.join(node_obj.Options.url_path +
                                                            [node_obj.slug_title]))}
            self.options = {}
            self.children = []
            self.options.update({'board': False})

    def _format(self):
        """
        Method for format data from Django ORM format to widget format
        :return:
        """
        self.header.update({
            'logo': self.header_settings.logo if self.header_settings else None,
            'phone': self.header_settings.phone if self.header_settings else None
        })