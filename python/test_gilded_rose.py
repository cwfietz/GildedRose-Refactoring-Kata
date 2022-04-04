# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # self.assertEquals("foo", items[0].name)
        self.assertEqual("foo", items[0].name)

    def test_quality_degrades_by_two(self):
        items = [Item("foo", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_degrades_by_one(self):
        items = [Item("foo", 1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_quality_is_never_negative(self):
        items = [Item("foo", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_quality_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
    
    def test_sulfuras_sellin_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)

    def test_backstage_passes_increase_in_quality_as_sell_in_day_approaches_11_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_backstage_passes_increase_in_quality_as_sell_in_day_approaches_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
    
    def test_backstage_passes_increase_in_quality_as_sell_in_day_approaches_6_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
    
    def test_backstage_passes_increase_in_quality_as_sell_in_day_approaches_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_backstage_passes_quality_drops_to_zero_after_sell_in_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)



        
if __name__ == '__main__':
    unittest.main()
