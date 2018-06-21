import Block, BlockChain
import json

blockchain = BlockChain.BlockChain()

for n in range(5):
    data = ["Data for Block " + str(n+1)]
    data_str = json.dumps(data)
    block = Block.Block(data_str)
    blockchain.mine(block)

output = []
while blockchain.head != None:
    output.append(blockchain.head.out())
    blockchain.head = blockchain.head.next
print(json.dumps(output, sort_keys=True, indent=4))