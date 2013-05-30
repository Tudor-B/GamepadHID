import unittest
import remapper

class Test(unittest.TestCase):


    def testremapper(self):
        #Make a remapper object and reads the buttonmap
        rem = remapper.remapper("testcontroller")
        #Writes the current buttonmap to the file
        rem.writeButtons('testcontroller')
        #Tests if the square buttons is mapped to ID 2 
        Test.assertEqual(self, rem.buttons['square'], 2, "Square button was not mapped to ID 2")
        #remapping square button to button ID 6
        rem.mapButton('square', 6)
        #checks if the square button has been succesfully moved to ID 6
        Test.assertEqual(self, rem.buttons['square'], 6, "Square button was not mapped to ID 6")
        #sets square button to tab action
        rem.mapAction('square', 'tab')
        #tests if tab is mapped to square
        Test.assertEqual(self, rem.actions['square'], 'tab', "Tab was not mapped to square")
        #write the action mapping to a file
        rem.writeActions('default')
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testremapper']
    unittest.main()