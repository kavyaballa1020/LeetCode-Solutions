class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ls=[]
        ls.append(celsius+273.15)
        ls.append(celsius*1.80+32)
        return ls