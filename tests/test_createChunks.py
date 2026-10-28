from _pytest import monkeypatch
import createChunks as cc
from unittest.mock import patch, MagicMock
from createChunks import createChunks, docFolder
from createChunks import appendBlock
from createChunks import blockToText
from createChunks import blocksToChunks
from pathlib import Path


def test_appendBlock(monkeypatch):
    monkeypatch.setattr(cc, "blocks",[])
    monkeypatch.setattr(cc, "text", ["test"])

    appendBlock("h1","h2","h3")


    assert cc.blocks == [["h1","h2","h3",["test"]]]
    assert cc.text == []


def test_appendBlock_withStoredBlocks(monkeypatch):
    monkeypatch.setattr(cc, "blocks",[["h1","h2","h3",["before"]]])
    monkeypatch.setattr(cc, "text", ["test"])

    appendBlock("h1","h2","h3")


    assert cc.blocks == [["h1","h2","h3",["before"]],["h1","h2","h3",["test"]]]
    assert cc.text == []

def test_blockToText():
    block = ["h1","h2","h3",["test"]]
    result = blockToText(block)

    assert result == "h1\nh2\nh3\ntest\n"

def test_blockToText_emptyBlock():
    block = []
    result = blockToText(block)

    assert result == None

@patch("createChunks.blockToText")
def test_blocksToChunks(mock_blockToText:MagicMock, monkeypatch):
    monkeypatch.setattr(cc, "blocks", [["h1", "h2", "h3", ["test"]]])
    mock_blockToText.return_value = "h1\nh2\nh3\ntest\n"
    result = blocksToChunks()

    assert mock_blockToText.call_count == 1
    assert result == ["h1\nh2\nh3\ntest\n"]


@patch("createChunks.blockToText")
def test_blocksToChunks_noBlocks(mock_blockToText, monkeypatch):
    monkeypatch.setattr(cc, "blocks", [])
    mock_blockToText.return_value = None
    result = blocksToChunks()

    assert mock_blockToText.call_count == 0
    assert result == []


@patch("createChunks.blocksToChunks")
@patch("createChunks.appendBlock")
def test_createChunks(mock_appendBlock,mock_blocksToChunks,monkeypatch):
    monkeypatch.setattr(cc,"docFolder", Path(__file__).parent / ".." / "tests" / "testData")

    createChunks()

    assert mock_appendBlock.call_count == 13
    mock_blocksToChunks.assert_called()


