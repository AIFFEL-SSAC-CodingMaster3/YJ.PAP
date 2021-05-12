import collections
from typing import List
from heapq import *


# 1236
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result

a = Solution()
a.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)

'''
#360
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())

        # count total with max_freq
        max_freq_ele_count = 0
        for val in list(freq.values()):
            if val == max_freq:
                max_freq_ele_count += 1

        ans = ((max_freq - 1) * (n + 1)) + max_freq_ele_count

        return max(ans, len(tasks))
'''

'''
# 376
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        f = collections.Counter(tasks)
        max_freq = max(f.values())
        f = list(f.values())
        max_freq_ele_count = 0
        i = 0
        while (i < len(f)):
            if f[i] == max_freq:
                max_freq_ele_count += 1
            i += 1

        a = (max_freq - 1) * (n + 1) + max_freq_ele_count

        return max(a, len(tasks))

# 408
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())

        max_freq_ele_count = 0  # total_elements_with_max_freq, last row element
        # count total with max_freq
        for i in range(len(freq)):
            if freq[i] == max_freq:
                max_freq_ele_count += 1

        ans = ((max_freq - 1) * (n + 1)) + max_freq_ele_count

        return max(ans, len(tasks))

# 416
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        jobs, time, tot_max_len = {}, 0, 0
        for task in tasks:
            if task in jobs:
                jobs[task] += 1
            else:
                jobs[task] = 1
        max_len = max(jobs.values())
        for job in jobs:
            if jobs[job] == max_len:
                tot_max_len += 1
        return max((max_len-1)*(n+1)+tot_max_len, len(tasks))

# 426
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.defaultdict(int)
        for task in tasks:
            freq[task] += 1

        maximum = -1
        # find most frequent
        for task in freq:
            maximum = max(maximum, freq[task])

        # find number of most frequent tasks
        numOfFreqTasks = 0
        for task in freq:
            if freq[task] == maximum:
                numOfFreqTasks += 1

        return max(len(tasks), n * (maximum - 1) + maximum + numOfFreqTasks - 1)

'''

'''
# 640
from heapq import *

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        min_len = 999999
        dict_ = dict()

        counts = collections.Counter(tasks)
        h, res = [], 0
        for key, value in counts.items():
            heappush(h, (-value, key))

        while h:

            i, temp = 0, []
            while i <= n:
                res += 1
                # update h
                if h:
                    curr_val, curr_key = heappop(h)
                    if curr_val + 1 < 0:
                        heappush(temp, (curr_val + 1, curr_key))

                # stop boundary
                if not temp and not h:
                    break
                else:
                    i += 1

            while temp:
                heappush(h, heappop(temp))

        return res
'''

'''
# 660
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1

        idle = {}
        heap = []
        for task in count:
            heapq.heappush(heap, (-count[task], task))

        t = 0
        while heap or idle:
            if heap:
                neg_c, task = heapq.heappop(heap)
                c = -neg_c
                c -= 1
                if c > 0:
                    neg_c = -c
                    idle[t] = (neg_c, task)

            if t - n in idle:
                heapq.heappush(heap, idle[t - n])
                del idle[t - n]

            t += 1

        return t
'''

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 값이 오르는 경우 매 번 그리디 계산
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        return result

a = Solution()
a.maxProfit(prices = [7,1,5,3,6,4])
'''

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans+=prices[i]-prices[i-1]
        return ans
a = Solution()
a.maxProfit(prices = [7,1,5,3,6,4])
'''

'''
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        people.sort(key=lambda x: (-x[0], x[1]))

        for p in people:
            queue.insert(p[1], p)

        return queue

a = Solution()
a.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
'''