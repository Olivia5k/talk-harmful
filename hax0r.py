class StringFilter(object):
    def cummings_filter(self, string):
        return string.lower()

class StringFilterTests(unittest.TestType):
    def test_cummings_filter(self):
        sf = StringFilter()
        result = sf.cummings_filter('TeSt StrInG heHE')

        self.assertEqual(result, 'test string hehe')
