from unittest.mock import patch
import pytest
from askModel import askModel
from askModel import ollamaError

@patch("askModel.load_dotenv")
@patch("askModel.requests.post")
@patch("askModel.findCloseEmbed")
def test_askModel(mock_findCloseEmbed, mock_post,mock_load_dotenv,monkeypatch):
    monkeypatch.setenv("OLLAMA_CHAT_MODEL", "gemma4:e2b")
    monkeypatch.setenv("OLLAMA_BASE_URL", "http://test:11434")

    mock_findCloseEmbed.return_value = "This is a mock test"
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"response": "working"}

    result = askModel("question")
    payload = mock_post.call_args.kwargs["json"]

    #checking if args are passed correctly to ollama
    assert result == "working"
    assert payload["prompt"] == "question"
    assert "This is a mock test" in payload["system"]
    assert payload["model"] == "gemma4:e2b"
    assert "options" in payload
    assert payload["stream"] == False



@patch("askModel.load_dotenv")
@patch("askModel.requests.post")
@patch("askModel.findCloseEmbed")
def test_askModel_uses_env_values(mock_findCloseEmbed, mock_post,mock_load_dotenv,monkeypatch):
    monkeypatch.setenv("OLLAMA_CHAT_MODEL", "gemma4:e2b")
    monkeypatch.setenv("OLLAMA_BASE_URL", "http://test:11434")
    mock_post.return_value.status_code = 200

    askModel("question")

    url = mock_post.call_args.args[0]

    #test .env usage
    assert url == "http://test:11434/api/generate"
    mock_load_dotenv.assert_called()



@patch("askModel.load_dotenv")
@patch("askModel.requests.post")
@patch("askModel.findCloseEmbed")
def test_askModel_default_url(mock_findCloseEmbed, mock_post,mock_load_dotenv, monkeypatch):
    monkeypatch.delenv("OLLAMA_BASE_URL", raising=False)
    mock_post.return_value.status_code = 200

    askModel("question")

    #test env fallback url
    url = mock_post.call_args.args[0]
    assert url == "http://localhost:11434/api/generate"

@patch("askModel.load_dotenv")
@patch("askModel.requests.post")
@patch("askModel.findCloseEmbed")
def test_askModel_ollama_404(mock_findCloseEmbed, mock_post,mock_load_dotenv, monkeypatch):
    mock_post.return_value.status_code = 404
    mock_post.return_value.json.return_value = {"error": "model not found"}

    with pytest.raises(ollamaError, match="model not found"):
        askModel("question")