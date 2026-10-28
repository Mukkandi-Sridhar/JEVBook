import pytest
from triage import parse_ticket, BadReply


def test_valid_reply():
    t = parse_ticket('{"category": "delivery", "urgent": false}')
    assert t.category == "delivery"


def test_reply_that_is_not_json():
    with pytest.raises(BadReply):
        parse_ticket("Sure! This looks like a delivery issue.")


def test_unknown_category():
    with pytest.raises(BadReply):
        parse_ticket('{"category": "Refund request", "urgent": true}')
