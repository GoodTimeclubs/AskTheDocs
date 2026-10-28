from unittest.mock import patch
from findCloseEmbed import findCloseEmbed
from qdrant_client.models import ScoredPoint

@patch("findCloseEmbed.embedChunks")
@patch("findCloseEmbed.client")
def test_findCloseEmbed(mock_client,mock_embedChunks):
    mock_client.query_points.return_value.points = [
        ScoredPoint(id=i, version=0, score=1.0, payload={"Text": t})
        for i, t in enumerate(["t1", "t2", "t3", "t4", "t5"])
    ]

    result = findCloseEmbed("query")

    assert result == "t1t2t3t4t5"