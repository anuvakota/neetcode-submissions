class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #create a member variable with min heap
        self.minHeap,self.k = nums,k #rn its an array need to make a heap
        heapq.heapify(self.minHeap)
       
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) 
            #what if it has less than k elements     

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
