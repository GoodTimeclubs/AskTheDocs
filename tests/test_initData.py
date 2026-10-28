from unittest.mock import patch

import pytest
from errors import qdrantError
from initData import  initData

@patch("initData.createCollection")
@patch("initData.upsertEmbed")
@patch("initData.embedChunks")
@patch("initData.createChunks")
def test_initData(mock_createChunks,mock_embedChunks,mock_upsertEmbed,mock_createCollection):
        mock_createChunks.return_value = ["h1\nh2\nh3\ntest\n","h1\nh2\nh3\ntest\n"]
        mock_createCollection.return_value = True

        initData()

        assert mock_upsertEmbed.call_args.args[0] == "h1\nh2\nh3\ntest\n"
        assert mock_upsertEmbed.call_count == 2
        assert mock_embedChunks.call_count == 2


@patch("initData.createCollection")
@patch("initData.upsertEmbed")
@patch("initData.embedChunks")
@patch("initData.createChunks")
def test_initData_alreadyCreated(mock_createChunks,mock_embedChunks,mock_upsertEmbed,mock_createCollection):
        mock_createChunks.return_value = ["h1\nh2\nh3\ntest\n","h1\nh2\nh3\ntest\n"]
        mock_createCollection.side_effect = Exception("already exists")

        with pytest.raises(qdrantError, match="already initialized"):
            initData()

        assert mock_upsertEmbed.call_count == 0
        assert mock_embedChunks.call_count == 0