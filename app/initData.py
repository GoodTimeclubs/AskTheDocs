from storeEmbed import client
from createChunks import createChunks
from embedChunks import embedChunks
from storeEmbed import upsertEmbed
from storeEmbed import createCollection



def initData():

    chunks = createChunks()

    if not client.collection_exists("testing"):
        createCollection()

    for c in chunks:
        upsertEmbed(c,embedChunks(c))

if __name__ == "__main__":
    initData()
