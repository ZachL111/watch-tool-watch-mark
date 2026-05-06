import unittest

from src.watch_tool_watch_mark.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(43, 41, 32, 92)
        self.assertEqual(review_score(item), 123)
        self.assertEqual(review_lane(item), "watch")


if __name__ == "__main__":
    unittest.main()
