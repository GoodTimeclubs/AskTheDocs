from createChunks import createChunks
from embedChunks import embedChunks
import time
i = 0
starttime = time.time()

chunks = createChunks()

afterChunking = time.time()

for c in chunks:
    print(c)
    print(embedChunks(c))
    i += 1

afterEmbed = time.time()

print(f"Total time: {afterEmbed-starttime:.2f} seconds.")
print(f"Chunking time: {afterChunking-starttime:.2f} seconds.")
print(f"Embedding time: {afterEmbed-afterChunking:.2f} seconds.")
print(i)