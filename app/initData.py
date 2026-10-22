from createChunks import createChunks
from embedChunks import embedChunks
from storeEmbed import upsertEmbed
from storeEmbed import createCollection


def initData():

    chunks = createChunks()

    try:
        createCollection()
    except:
        print("Info : using existing collection")

    for c in chunks:
        upsertEmbed(c,embedChunks(c))
