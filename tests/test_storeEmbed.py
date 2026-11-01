from storeEmbed import createCollection, upsertEmbed
from unittest.mock import patch
from qdrant_client.models import PointStruct
import uuid


@patch('storeEmbed.client')
def test_createCollection(mock_client):
    createCollection()
    assert mock_client.create_collection.call_count == 1


@patch('storeEmbed.client')
def test_upsertEmbed(mock_client):
    data = "This is a test"
    embed = [0.1] * 1024

    upsertEmbed(data, embed)
    mock_client.upsert.assert_called_once_with(
        collection_name="testing",
        wait=True,
        points=[PointStruct(id=uuid.uuid5(uuid.NAMESPACE_DNS, data),
                            vector=embed, payload={"Text": data})]
    )
