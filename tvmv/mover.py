import os
import shutil
from tvmv.tvshow import TVShow


class Mover(object):

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.files = []

        if not os.path.isdir(self.source) or not os.path.isdir(self.destination):
            raise NotADirectoryError

    def find_sources(self):
        self.files = [TVShow(f) for f in os.listdir(self.source) if os.path.isfile(os.path.join(self.source, f))]

    def move(self):
        self.find_sources()
        for tv_show in self.files:
            source = os.path.join(self.source, tv_show.filename)
            destination = os.path.join(self.destination, str(tv_show))
            shutil.copyfile(source, destination)
