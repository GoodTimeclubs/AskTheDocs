from unittest import result

import pytest

from errors import  ollamaError
from embedChunks import embedChunks
from unittest.mock import patch, MagicMock

@patch("embedChunks.load_dotenv")
@patch("embedChunks.requests.post")
def test_embedChunks(mock_requests, mock_load_dotenv,monkeypatch):
    monkeypatch.setenv("OLLAMA_EMB_MODEL","bge-m3:latest")
    monkeypatch.setenv("OLLAMA_BASE_URL", "http://test:11434")
    mock_requests.return_value.json.return_value = {"embeddings": [["test"]]}
    mock_requests.return_value.status_code = 200

    result = embedChunks("input")

    payload = mock_requests.call_args.kwargs["json"]

    assert payload["model"] == "bge-m3:latest"
    assert payload["input"] == "input"
    assert result== ["test"]


@patch("embedChunks.load_dotenv")
@patch("embedChunks.requests.post")
def test_embedChunksollama_404(mock_post,mock_load_dotenv, monkeypatch):
    mock_post.return_value.status_code = 404
    mock_post.return_value.json.return_value = {"error": "model not found"}

    with pytest.raises(ollamaError, match="model not found"):
        embedChunks("input")