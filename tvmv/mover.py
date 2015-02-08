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
            destination_folder = self.prepare(tv_show.name, tv_show.season)
            source = os.path.join(self.source, tv_show.filename)
            destination = os.path.join(destination_folder, str(tv_show))
            shutil.copyfile(source, destination)

    def prepare(self, name, season):
        name_folder = os.path.join(self.destination, name.replace(' ', '_'))
        season_folder = os.path.join(self.destination, name.replace(' ', '_'), 'season_' + str(season).zfill(2))
        if not os.path.exists(name_folder):
            os.mkdir(name_folder)
        if not os.path.exists(season_folder):
            os.mkdir(season_folder)
        return season_folder
