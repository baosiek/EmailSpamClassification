import unittest


def porra(self, caralho):
    print(caralho)
    
    
def _print_success_message():
    print("Test passed!")
    
class Tests(unittest.TestCase):

    def test_sizess(self):    
        with open("./data/contents.txt", "rb") as fp:   # Deserializing contents
            contents = pickle.load(fp)
            self.assertEqual(len(contents), 517401)
            _print_success_message()
               
    
if __name__ == '__main__':
    unittest.main()    

# unittest.main(argv=['first-arg-is-ignored'], exit=False)