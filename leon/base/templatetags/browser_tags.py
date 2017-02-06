# -*- coding: utf-8 -*-


import os
import settings
import json
from django import template

register = template.Library()


@register.simple_tag
def get_assets_css(path):

    assets_path = os.path.join(settings.PROJECT_ROOT, settings.STORAGE_PATH, path, 'assets.json')
    with open(assets_path, 'r') as f:
        assets_content = f.read()
    return json.loads(assets_content).get('css') if assets_content else []


@register.simple_tag
def get_assets_js(path):

    assets_path = os.path.join(settings.PROJECT_ROOT, settings.STORAGE_PATH, path, 'assets.json')
    with open(assets_path, 'r') as f:
        assets_content = f.read()
    return json.loads(assets_content).get('js') if assets_content else []


@register.simple_tag
def get_widget_path(*args):

    return '/'.join(args)


@register.simple_tag
def get_widget_folder(*args):

    return '_'.join(args)


@register.simple_tag
def get_widget_files(path, widget_type, file_type):

    assembly_path = os.path.join(settings.PROJECT_ROOT, settings.STORAGE_PATH,
                                 path, '{}.json'.format(widget_type))
    with open(assembly_path, 'r') as f:
        assembly_content = f.read()
    return json.loads(assembly_content).get(file_type) if assembly_content else []
