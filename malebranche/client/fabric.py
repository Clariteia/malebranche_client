from .importers import SystemImporter


class Fabric(object):

    def system(self):
        return SystemImporter()
