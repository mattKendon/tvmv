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
        new_files = [f for f in os.listdir(self.source) if os.path.isfile(os.path.join(self.source, f))]
        self.assertEqual(len(new_files), 4)