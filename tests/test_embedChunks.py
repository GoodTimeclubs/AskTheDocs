from unittest import result

from embedChunks import embedChunks
from unittest.mock import patch, MagicMock

@patch("askModel.load_dotenv")
@patch("askModel.requests.post")
def test_embedChunks(mock_requests, mock_load_dotenv,monkeypatch):
    monkeypatch.setenv("OLLAMA_EMB_MODEL","bge-m3:latest")
    monkeypatch.setenv("OLLAMA_BASE_URL", "http://test:11434")
    mock_requests.return_value.json.return_value = {"embeddings": [["test"]]}

    result = embedChunks("input")

    payload = mock_requests.call_args.kwargs["json"]

    assert payload["model"] == "bge-m3:latest"
    assert payload["input"] == "input"
    assert result== ["test"]