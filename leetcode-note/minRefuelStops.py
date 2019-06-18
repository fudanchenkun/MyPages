class Status(object):
    def __init__(self, steps, fuel):
        self.steps = steps
        self.fuel = fuel

    def __lt__(self, other):
        return self.steps < other.steps


# 找到上一个能一步到达target且已行走步数最小的站点，再往前递归。但只通过了47个测试用例，还没发现原因，期待大神指教
class DPSolution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """

        def minStatus(target, stations):
            if startFuel >= target:
                return [Status(0, startFuel)]

            if len(stations) == 0:
                return [Status(0, startFuel)] if startFuel >= target else []
            elif len(stations) == 1:
                if startFuel >= target:
                    return [Status(0, startFuel)]
                elif startFuel >= stations[0][0] and startFuel + stations[0][1] >= target:
                    return [Status(1, startFuel + stations[0][1])]
                else:
                    return []

            status_list = []
            for i in range(len(stations)):
                for tmp in minStatus(stations[i][0], stations[:i]):
                    if tmp.fuel + stations[i][1] >= target:
                        tmp.steps += 1
                        tmp.fuel += stations[i][1]
                        status_list.append(tmp)
            if len(status_list) > 0:
                min_steps = min(status_list).steps
                return filter(lambda x:x.steps==min_steps, status_list)
            else:
                return []

        ans = minStatus(target, stations)
        if len(ans) > 0:
            return min(ans).steps
        return -1



# 贪心策略，算step最小，不管fuel多大，step只会加1，很显然用贪心算法，方法就是优先队列或者最大堆，python只有最小堆也是醉了
import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        if startFuel >= target:
            return 0

        heap = []
        fuel = startFuel
        steps = 0
        stations.append([target, 0])
        for i in range(len(stations)):
            print i, fuel
            if fuel < stations[i][0]:
                print fuel
                while len(heap) > 0:
                    tmp_fuel = heapq.heappop(heap) * -1
                    fuel += tmp_fuel
                    steps += 1
                    if fuel >= stations[i][0]:
                        break
                print fuel
                if fuel < stations[i][0]:
                    return -1
            heapq.heappush(heap, stations[i][1] * -1)
        if fuel >= target:
            return steps
        return -1