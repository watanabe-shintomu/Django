import unittest

from ..personal_member import PersonalMember


class TestExample(unittest.TestCase):
    def setUp(self) -> None:
        self.personal_member = PersonalMember.objects.create(
            name_kana="テスト",
            name_kanji="テスト",
        )

    def test_example(self):
        self.assertEqual(self.personal_member.name_kana, "テスト")
        self.assertEqual(self.personal_member.name_kanji, "テスト")
