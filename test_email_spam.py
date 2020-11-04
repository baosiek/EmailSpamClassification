import unittest


def _print_success_message():
    print("Test passed!")
    
class TestEmailSpams(unittest.TestCase):

    def test_sizes(self):    
        with open("./data/contents.txt", "rb") as fp:   # Deserializing contents
            contents = pickle.load(fp)
            self.assertEqual(len(contents), 517401)
            _print_success_message()
               
    
if __name__ == '__main__':
    unittest.main()    

# unittest.main(argv=['first-arg-is-ignored'], exit=False)