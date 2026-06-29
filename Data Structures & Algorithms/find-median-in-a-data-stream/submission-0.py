class MedianFinder:

    def __init__(self):
       self.arr=[] 

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()


    def findMedian(self) -> float:
        t=len(self.arr)
        

        if t%2 :
            return float(self.arr[t//2])
        
        else:
            return float((self.arr[t//2] + self.arr[(t//2)-1])/2)
        
        