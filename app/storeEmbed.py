from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import uuid
import os
from dotenv import load_dotenv

#read .env file
load_dotenv()

host = os.getenv("QDRANT_HOST")
port = os.getenv("QDRANT_PORT")


client = QdrantClient(host=host, port=port)


def createCollection():
    client.create_collection(
        collection_name="testing",
        vectors_config=VectorParams(size=1024, distance=Distance.EUCLID)
    )

def upsertEmbed(data,embed):
    client.upsert(
        collection_name="testing",
        wait=True,
        points=[
            PointStruct(id=uuid.uuid5(uuid.NAMESPACE_DNS, data), 
                        vector=embed,
                        payload={"Text" : data}
                        )
        ]
    )