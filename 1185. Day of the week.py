class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        date=datetime.date(year,month,day)
        d=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

        return d[date.weekday()]