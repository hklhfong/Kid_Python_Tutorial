def gcdOfStrings( str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        x = ""
        max_length = max(len(str1), len(str2))

        for i in range(max_length):
            if i < len(str1) and i < len(str2):
                if str1[i] == str2[i]: 
                    x += str1[i]
                else:
                    return ""
            else:
                if i+1 == len(str1):
                    return x
                if x[i % len(x)] == str1[i % len(x)]:
                    continue
                else:
                    return ""
                
result = gcdOfStrings("ABCABC", "ABC")
print(result)
