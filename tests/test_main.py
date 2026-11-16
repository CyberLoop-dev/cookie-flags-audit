import unittest
from main import audit


class CookieAuditTests(unittest.TestCase):
    def test_reports_missing_flags(self):
        result = audit(["Set-Cookie: session=abc; Path=/"])
        messages = [item[2] for item in result]
        self.assertTrue(any("missing secure" in m for m in messages))
        self.assertTrue(any("missing httponly" in m for m in messages))

    def test_host_prefix_requirements(self):
        result = audit(["__Host-id=1; Path=/; Secure; HttpOnly; SameSite=Lax"])
        self.assertEqual(result, [])

    def test_none_requires_secure(self):
        result = audit(["sid=1; SameSite=None"])
        self.assertTrue(any("requires Secure" in item[2] for item in result))


if __name__ == "__main__":
    unittest.main()
