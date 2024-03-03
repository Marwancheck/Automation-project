import unittest

import HtmlTestRunner

from test_log_in_log_out_valid_credentials import  Log_in_out
from test_log_in_invalid_credentials import Log_in_invalid
from test_add_remove_item_cart import Add_remove_item_cart
from test_service_and_garantii import Check_service_garantii
from test_filter_laptop_by_price import Filter_laptop_price
from test_search_site import Search_site
from test_socialmedia_redirect import Social_media_redirect



class TestSuite(unittest.TestCase):

		def test_suite(self):
				teste_de_rulat = unittest.TestSuite()
				teste_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Log_in_invalid),
                unittest.defaultTestLoader.loadTestsFromTestCase(Log_in_out),
				unittest.defaultTestLoader.loadTestsFromTestCase(Add_remove_item_cart),
				unittest.defaultTestLoader.loadTestsFromTestCase(Check_service_garantii),
				unittest.defaultTestLoader.loadTestsFromTestCase(Filter_laptop_price),
				unittest.defaultTestLoader.loadTestsFromTestCase(Search_site),
				unittest.defaultTestLoader.loadTestsFromTestCase(Social_media_redirect)])


				runner = HtmlTestRunner.HTMLTestRunner\
								(
				combine_reports=True,
				report_title = "Test execution report",
				report_name = "Test results"
		)

				runner.run(teste_de_rulat)