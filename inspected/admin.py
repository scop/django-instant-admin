# Copyright 2019 Ville Skyttä
# SPDX-License-Identifier: BSD-3-Clause

from django.apps import apps
from django.contrib import admin


for model in apps.get_app_config('inspected').get_models():
    admin.site.register(model)
