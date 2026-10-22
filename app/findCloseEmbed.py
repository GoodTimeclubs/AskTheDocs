from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from storeEmbed import client
from embedChunks import embedChunks

def findCloseEmbed(Query):
    results = client.query_points(
        collection_name="testing",
        query=embedChunks(Query),
        with_payload=True,
        limit=5
    )

    return results.points