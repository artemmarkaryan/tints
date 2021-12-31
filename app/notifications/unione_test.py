import unittest
import unione


class SmokeTest(unittest.TestCase):
    def test_sending(self):
        api = unione.API("695e163x51m969qm4unpwd8bx6jr7zoi1zp9cjfe")
        api.send_mail(
            to="artemandriy@gmail.com",
            subj="test",
            text="test"
        )


if __name__ == '__main__':
    unittest.main()
