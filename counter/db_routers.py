class CounterRouter:
    route_app_labels = ["counter"]
    DATABASE = 'default'

    def db_for_write(self, model, **hints):
        return self.DATABASE

    def db_for_read(self, model, **hints):
        return self.DATABASE
