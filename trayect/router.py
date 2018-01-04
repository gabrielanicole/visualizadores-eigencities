class TrayectDatabaseRouter(object):
    """
    Determine how to route database calls for an app's models (in this case, for an app named Example).
    All other models will be routed to the next router in the DATABASE_ROUTERS setting if applicable,
    or otherwise to the default database.
    """

    def db_for_read(self, model, **hints):
        """Send all read operations on trayect app models to `trayactoria_db`."""
        if model._meta.app_label == 'trayect':
            return 'trayactoria_db'
        return 'default'


    def db_for_write(self, model, **hints):
        """Send all write operations on trayect app models to `trayactoria_db`."""
        if model._meta.app_label == 'trayect':
            return 'trayactoria_db'
        return 'default'


    def allow_relation(self, obj1, obj2, **hints):
        """Determine if relationship is allowed between two objects."""

        # Allow any relation between two models that are both in the Example app.
        if obj1._meta.app_label == 'trayect' and obj2._meta.app_label == 'trayect':
            return True
        #  # Allow if neither is chinook app.
        elif 'trayect' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True

        #  # Allow if neither is chinook app //Block relationship if one object is in the trayect app and the other isn't.
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the trayect app's models get created on the right database."""
        if app_label == 'trayect':
            # The trayect app should be migrated only on the trayactoria_db database.
            return db == 'trayactoria_db'
        elif db == 'trayactoria_db':
            # Ensure that all other apps don't get migrated on the trayactoria_db database.
            return False

        # No opinion for all other scenarios
        return True