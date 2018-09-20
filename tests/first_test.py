import unittest
import sys
sys.path.insert(0,'/home/vagrant/dev/moon/project')
from project import app

class FirstTestCase(unittest.TestCase):
    def setUp(self):
         self.app=app.test_client()

    def login(self,uname,pwd):
        rv= self.app.post('/login',
                             data=dict(username=uname,password=pwd),
                             follow_redirects=True)
        return rv

    def test_first(self):
        rv=self.login('admin','default')
        assert b'login successful' in rv.data


if __name__=='__main__':
    unittest.main()
