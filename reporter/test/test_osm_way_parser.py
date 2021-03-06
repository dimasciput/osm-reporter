# coding=utf-8
"""Test cases for the OSM Way Parser module.
:copyright: (c) 2013 by Tim Sutton
:license: GPLv3, see LICENSE for more details.
"""
import xml
import unittest

from reporter.test.logged_unittest import LoggedTestCase
from reporter.osm_way_parser import OsmParser
from reporter.test.helpers import FIXTURE_PATH


class OsmParserTestCase(LoggedTestCase):
    """Test the sax parser for OSM data."""

    def test_parse(self):
        """Test that we can parse a predefined osm file."""
        myParser = OsmParser(tagName="building")
        source = open(FIXTURE_PATH)
        xml.sax.parse(source, myParser)
        myExpectedWayDict = {u'Babsie': 37,
                             u'Firefishy': 12,
                             u'Jacoline': 3}
        myExpectedNodeDict = {u'Babsie': 306,
                              u'Firefishy': 104,
                              u'Jacoline': 17}
        myExpectedTimelineDict = {
            u'Babsie': {
                u'2012-12-08': 15,
                u'2012-12-10': 22
            },
            u'Burger': {
                u'2010-05-16': 1
            },
            u'Firefishy': {
                u'2012-09-26': 10,
                u'2012-12-08': 15,
                u'2012-12-09': 5,
                u'2012-12-10': 1
            },
            u'Jacoline': {
                u'2012-12-08': 1,
                u'2012-12-10': 2
            },
            u'thomasF': {
                u'2012-08-22': 5
            },
            u'timlinux': {
                u'2010-12-09': 1,
                u'2012-07-10': 1
            }
        }

        # OsmParser way count test
        self.assertDictEqual(myExpectedWayDict,
                             myParser.wayCountDict)

        # OsmParser node count test
        self.assertDictEqual(myExpectedNodeDict,
                             myParser.nodeCountDict)

        # OsmParser timeline test
        self.assertDictEqual(myExpectedTimelineDict,
                             myParser.userDayCountDict)


if __name__ == '__main__':
    unittest.main()
