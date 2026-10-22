from initData import initData
from findCloseEmbed import findCloseEmbed

initData()

results = findCloseEmbed("Wann kommt mein Lumen 5 Roboter?")

for result in results:
    print(result.payload["Text"])