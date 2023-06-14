class ReadOnlyRouter:
    route_app_labels = ["integrations"]
    DATABASE = None

    def db_for_write(self, model, **hints):
        return None

    def db_for_read(self, model, **hints):
        return self.DATABASE


class M2Router(ReadOnlyRouter):
    DATABASE = 'm2'


class RMRouter:
    DATABASE = 'rm'
