from unittest import TestCase
from tvmv.tvshow import TVShow, InvalidFilenameException


class TestTVShow(TestCase):

    def test_it_is_constructed_with_a_filename_string(self):
        TVShow('24 - 301 - 2pm-3pm.mp4')

    def test_it_allows_access_to_the_filename_it_was_constructed_with(self):
        tv_24 = TVShow('24 - 301 - 2pm-3pm.mp4')
        self.assertEqual(tv_24.filename, '24 - 301 - 2pm-3pm.mp4')

    def test_it_parses_a_filename_into_a_tv_show_name(self):
        tv_24 = TVShow('24 - 301 - 2pm-3pm.mp4')
        tv_archer = TVShow('Archer - 301 - A new archer episode.mpeg')
        self.assertEqual(tv_24.name, '24')
        self.assertEqual(tv_archer.name, 'archer')

    def test_it_parses_a_filename_into_a_season_number(self):
        tv_24 = TVShow('24 - 301 - 2pm-3pm.mp4')
        tv_archer = TVShow('Archer - 1001 - A new archer episode.mpeg')
        self.assertEqual(tv_24.season, 3)
        self.assertEqual(tv_archer.season, 10)

    def test_it_parses_a_filename_into_an_episode_number(self):
        tv_24 = TVShow('24 - 301 - 2pm-3pm.mp4')
        tv_archer = TVShow('Archer - 1024 - A new archer episode.mpeg')
        self.assertEqual(tv_24.episode, 1)
        self.assertEqual(tv_archer.episode, 24)

    def test_it_parses_a_filename_into_an_episode_name(self):
        tv_24 = TVShow('24 - 301 - 2pm-3pm.mp4')
        tv_archer = TVShow('Archer - 1024 - A new archer episode.mpeg')
        self.assertEqual(tv_24.episode_name, '2pm-3pm')
        self.assertEqual(tv_archer.episode_name, 'a new archer episode')

    def test_it_parses_a_filename_into_a_file_type(self):
        tv_24 = TVShow('24 - 301 - 2pm-3pm.mp4')
        tv_archer = TVShow('Archer - 1024 - A new archer episode.mpeg')
        self.assertEqual(tv_24.file_type, 'mp4')
        self.assertEqual(tv_archer.file_type, 'mpeg')

    def test_it_casts_to_a_string(self):
        tv_24 = TVShow('24 - 301 - 2pm-3pm.mp4')
        tv_archer = TVShow('Archer - 1024 - A new archer episode.mpeg')
        tv_bbt = TVShow('Big Bang Theory - 210 - a theory episode.mpeg')
        tv_no_episode_name = TVShow('Show - 210.mp4')
        self.assertEqual(str(tv_24), '24.s03.e01.2pm-3pm.mp4')
        self.assertEqual(str(tv_archer), 'archer.s10.e24.a_new_archer_episode.mpeg')
        self.assertEqual(str(tv_bbt), 'big.bang.theory.s02.e10.a_theory_episode.mpeg')
        self.assertEqual(str(tv_no_episode_name), 'show.s02.e10.mp4')

    def test_it_raises_invalid_filename_exception_when_it_cannot_parse_a_tv_show_name(self):
        self.assertRaises(InvalidFilenameException, TVShow, '')
        self.assertRaises(InvalidFilenameException, TVShow, None)
        self.assertRaises(InvalidFilenameException, TVShow, 1)

    def test_it_raises_invalid_filename_exception_when_it_cannot_parse_a_season(self):
        self.assertRaises(InvalidFilenameException, TVShow, 'Something')
        self.assertRaises(InvalidFilenameException, TVShow, 'Something - abcd')

    def test_it_raises_invalid_filename_exception_it_cannot_parse_an_episode(self):
        self.assertRaises(InvalidFilenameException, TVShow, 'Something - 10 - ')
        self.assertRaises(InvalidFilenameException, TVShow, 'Something - 1 - ')

    def test_it_does_not_raise_invalid_filename_exception_if_it_cannot_parse_an_episode_name(self):
        TVShow('Something - 103.mp4')

    def test_it_raises_invalid_filename_exception_if_it_cannot_parse_file_type(self):
        self.assertRaises(InvalidFilenameException, TVShow, 'Something - 103 - A name')