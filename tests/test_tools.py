import unittest

from mcp_server.server import list_roadmaps, get_lesson


class TestRoadmapTools(unittest.TestCase):

    def test_list_roadmaps(self):
        result = list_roadmaps()

        self.assertEqual(
            result.roadmaps[0].id,
            "guitar-theory"
        )

    def test_existing_lesson(self):
        result = get_lesson(
            "guitar-theory",
            "1.1"
        )

        self.assertTrue(result.ok)
        self.assertEqual(
            result.lesson.title,
            "Musical Intervals"
        )

    def test_missing_lesson(self):
        result = get_lesson(
            "guitar-theory",
            "9.9"
        )

        self.assertFalse(result.ok)
        self.assertEqual(
            result.error,
            "LESSON_NOT_FOUND"
        )

    def test_missing_roadmap(self):
        result = get_lesson(
            "unknown-roadmap",
            "1.1"
        )

        self.assertFalse(result.ok)
        self.assertEqual(
            result.error,
            "ROADMAP_NOT_FOUND"
        )


if __name__ == "__main__":
    unittest.main()
