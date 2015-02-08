class TVShow(object):
    def __init__(self, filename):
        self.filename = filename
        try:
            name = self.filename.rsplit('.', 1)
            self.name = self.parse_name(name[0])
            self.season = self.parse_season(name[0])
            self.episode = self.parse_episode(name[0])
            self.episode_name = self.parse_episode_name(name[0])
            self.file_type = self.parse_file_type(self.filename)
        except IndexError:
            raise InvalidFilenameException
        except AttributeError:
            raise InvalidFilenameException
        except ValueError:
            raise InvalidFilenameException

    @staticmethod
    def parse_name(filename):
        return filename.split(' - ')[0].lower()

    @staticmethod
    def parse_season(filename):
        return int(filename.split(' - ')[1][0:-2])

    @staticmethod
    def parse_episode(filename):
        return int(filename.split(' - ')[1][-2:])

    @staticmethod
    def parse_episode_name(filename):
        try:
            return filename.split(' - ')[2].lower()
        except IndexError:
            return None

    @staticmethod
    def parse_file_type(filename):
        filename_split = filename.rsplit('.', 1)
        if len(filename_split) != 2:
            raise InvalidFilenameException
        return filename_split[-1]

    def __str__(self, *args, **kwargs):
        if self.episode_name is None:
            episode_name = ''
        else:
            episode_name = '.' + str(self.episode_name).replace(' ', '_')

        to_string = "{name}.s{season}.e{episode}{episode_name}.{type}"
        return to_string.format(name=self.name.replace(' ', '.'),
                                season=str(self.season).zfill(2),
                                episode=str(self.episode).zfill(2),
                                episode_name=episode_name,
                                type=self.file_type)


class InvalidFilenameException(Exception):
    pass

