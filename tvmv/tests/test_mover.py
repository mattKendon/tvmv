import os
from unittest import TestCase
import shutil
from tvmv.mover import Mover
from tvmv.tvshow import TVShow


class TestMover(TestCase):

    def setUp(self):
        self.source = 'source'
        self.destination = 'destination'
        os.mkdir(self.source)
        os.mkdir(self.destination)
        for i in range(1, 5):
            file_name = 'tv show - 1{e} - episode name.mp4'
            open(os.path.join(self.source, file_name.format(e=str(i).zfill(2))), 'a').close()
        self.out = Mover(self.source, self.destination)

    def tearDown(self):
        shutil.rmtree(self.source)
        shutil.rmtree(self.destination)

    def test_it_takes_source_and_destination_when_initialised(self):
        Mover(self.source, self.destination)

    def test_it_raises_not_directory_error_if_source_is_not_directory(self):
        self.assertRaises(NotADirectoryError, Mover, 'foo', self.destination)

    def test_it_raises_not_directory_error_if_destination_is_not_a_directory(self):
        self.assertRaises(NotADirectoryError, Mover, self.source, 'food')

    def test_it_creates_a_list_TVShow_objects_from_a_directory(self):
        self.out.find_sources()
        self.assertEqual(len(self.out.files), 4)
        self.assertIsInstance(self.out.files[0], TVShow)

    def test_it_copies_the_files_from_source_to_destination(self):
        self.out.move()
        destination_folder = os.path.join(self.destination, 'tv_show', 'season_01')
        new_files = [f for f in os.listdir(destination_folder) if os.path.isfile(os.path.join(destination_folder, f))]
        self.assertEqual(len(new_files), 4)

    def test_it_prepares_a_show_folder_and_a_season_folder(self):
        self.out.prepare('tv show', 1)
        self.assertTrue(os.path.isdir(os.path.join(self.destination, 'tv_show')))
        self.assertTrue(os.path.isdir(os.path.join(self.destination, 'tv_show', 'season_01')))