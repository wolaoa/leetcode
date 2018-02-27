class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        totalCnt = len(words)
        avlLen = maxWidth
        currList = []
        currWordLen = 0
        currCnt = 0
        for word in words:   
            # exceed, not the last line
            wordLen = len(word)
            if wordLen > avlLen:
                # can't be the last word
                slots = len(currList) - 1
                if slots == 0:
                    currTerm = ' '.join(currList)
                    currTerm = ('%-' + str(maxWidth) + 's') % (currTerm)
                else:
                    emptyCnt  = maxWidth - currWordLen
                    gap = emptyCnt / slots
                    extra = emptyCnt % slots
                    gapEmpty = ' ' * gap
                    if extra == 0:
                        currTerm = gapEmpty . join(currList)
                    else:
                        moreGap = gapEmpty + ' '
                        currTerm = moreGap . join(currList[:extra])
                        currTerm += moreGap + (gapEmpty . join(currList[extra:]))
                res.append(currTerm)
                currList = []
                currList.append(word)
                currWordLen = wordLen
                avlLen = maxWidth - wordLen - 1
            elif wordLen == avlLen:
                # meet the end of current line, print it
                currList.append(word)
                currTerm = ' ' . join(currList)
                res.append(currTerm)
                currList = []
                avlLen = maxWidth
                currWordLen = 0
            else:
                # keep and word to the current line
                currList.append(word)
                avlLen -= wordLen + 1
                currWordLen += wordLen
            currCnt += 1
        # add last line to the res
        if len(currList) > 0:
            currTerm = ' '.join(currList)
            currTerm = ('%-' + str(maxWidth) + 's') % (currTerm)
            res.append(currTerm)
        
        return res


                

