# -*- coding: utf-8 -*-


class SidebarConverterMixin(object):

    class SidebarMenuNode(object):
        """
        Class for SidebarMenu objects-nodes
        """
        def __init__(self, node_obj, fa_icon):
            self.name = node_obj.title
            self.fa_icon = fa_icon
            if node_obj.Options.native:
                self.link = '/{}/'.format(node_obj.link).replace('//', '/')
            else:
                self.link = '/{}/'.format('/'.join(node_obj.Options.url_path +
                                                   [node_obj.slug_title])).replace('//', '/')
            self.options = {}
            self.children = []
            self.options.update({'board': False})

    def _format(self):
        """
        Method for format data from Django ORM format to widget format
        :return:
        """
        for section in self.SECTIONS:
            sidebar_menu_storage = []
            for item in self.sidebar_item_s:
                if item.type == section['key']:
                    self.__recursive_node_append(item.item_content_object,
                                                 sidebar_menu_storage, item.fa_icon)

            section['children'] = sidebar_menu_storage if sidebar_menu_storage else []
            self.menu_sidebar.update({
                section['key']: section
            })

    def __recursive_node_append(self, node_obj, storage, fa_icon):
        node = self.SidebarMenuNode(node_obj, fa_icon)
        storage.append(node)
        for item in node_obj.get_show_children():
            self.__recursive_node_append(item, node.children, None)
