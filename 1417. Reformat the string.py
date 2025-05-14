class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters=[]
        digits=[]

        for i in s:
            if i.isdigit():
                digits.append(i)
            else:
                letters.append(i)
        
        if abs(len(letters)-len(digits))>1:
            return ""

        result=[]
        
        if len(letters)>len(digits):
            first,second=letters,digits
        else:
            first,second=digits,letters
        
        while first or second:
            if first:
                result.append(first.pop(0))
            if second:
                result.append(second.pop(0))
        return "".join(result)

