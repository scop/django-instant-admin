# Copyright 2019 Ville Skyttä
# SPDX-License-Identifier: BSD-3-Clause


class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'inspected':
            return model._meta.app_label
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        if any(x._meta.app_label == 'inspected' for x in (obj1, obj2)):
            return obj1._meta.app_label == obj2._meta.app_label
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'inspected':
            return False
        return None
