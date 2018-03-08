class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        depth = path.split('/')
        newDepth = []
        normPath = '/'
        for curDir in depth:
            if curDir == '.' or curDir == '':
                continue
            elif curDir == '..':
                if len(newDepth) > 0:
                    newDepth.pop()
            else:
                newDepth.append(curDir)
        normPath += '/'.join(newDepth)
        return normPath        

