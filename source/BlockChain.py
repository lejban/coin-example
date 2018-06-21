import Block

class BlockChain:
    diff     = 10
    maxNonce = 2**32
    target   = 2 ** (256-diff)
    block    = Block.Block("Genesis")
    head     = block
    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block: Block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                break
            else:
                block.nonce += 1