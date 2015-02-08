import os
from unittest import TestCase
from click.testing import CliRunner
import shutil
from tvmv import cli
from tvmv.mover import Mover


class TestMover(TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.source = 'source'
        self.destination = 'destination'
        os.mkdir(self.source)
        os.mkdir(self.destination)
        for i in range(1, 5):
            file_name = 'tv show - 1{e} - episode name.mp4'
            open(os.path.join(self.source, file_name.format(e=str(i).zfill(2))), 'a').close()

    def tearDown(self):
        shutil.rmtree(self.source)
        shutil.rmtree(self.destination)

    def test_it_lists_all_files_in_source_directory(self):
        mover = Mover(self.source, self.destination)
        mover.find_sources()

        result = self.runner.invoke(cli.ls, [self.source])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, "\n".join([f.filename for f in mover.files])+"\n")

    def test_it_moves_all_files_from_source_directory_to_destination_directory(self):
        result = self.runner.invoke(cli.move, [self.source, self.destination])
        destination_folder = os.path.join(self.destination, 'tv_show', 'season_01')
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(len([f for f in os.listdir(destination_folder)]), 4)