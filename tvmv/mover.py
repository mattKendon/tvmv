import os
import shutil
from tvmv.tvshow import TVShow, InvalidFilenameException


class Mover(object):

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.files = []
        self.ignored = 0
        self.moved = 0

        if not os.path.isdir(self.source) or not os.path.isdir(self.destination):
            raise NotADirectoryError

    def find_sources(self):
        for f in os.listdir(self.source):
            try:
                f = TVShow(f)
            except InvalidFilenameException:
                self.ignored += 1
            else:
                self.files.append(f)

    def move(self):
        self.find_sources()
        for tv_show in self.files:
            self.move_file(tv_show)

    def move_file(self, file):
        destination_folder = self.prepare(file.name, file.season)
        source = os.path.join(self.source, file.filename)
        destination = os.path.join(destination_folder, str(file))
        shutil.copy(source, destination)
        self.moved += 1

    def prepare(self, name, season):
        name_folder = os.path.join(self.destination, name.replace(' ', '_'))
        season_folder = os.path.join(self.destination, name.replace(' ', '_'), 'season_' + str(season).zfill(2))
        if not os.path.exists(name_folder):
            os.mkdir(name_folder)
        if not os.path.exists(season_folder):
            os.mkdir(season_folder)
        return season_folder
