class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        """
        label explain:
            0:  nothing
            1:  /*
        """
        label = 0
        current_line = ''
        rtype = []
        for line in source:
            if len(line) == 0:
                continue
            # stack is empty 
            if label == 0:
                current_line = line
            else:
                close_index = line.find("*/")
                if close_index == -1:
                    continue
                label = 0
                print close_index
                current_line = current_line + line[close_index + 2:]
            print "CURR_LINE: " + current_line
            one_index   = current_line.find("//")
            multi_index = current_line.find("/*")
            print one_index, multi_index
            if one_index == multi_index:
                #one_index == multi_index == -1
                rtype.append(current_line)
                current_line = ''
                continue
            elif multi_index == -1:
                if one_index > 0:
                    rtype.append(current_line[0: one_index])
                current_line = ''
            elif one_index == -1 or multi_index < one_index:
                # one_index not find , multi_index exists 
                label = 1
                if multi_index == 0:
                    prefix = ''
                else:
                    prefix = current_line[0: multi_index]
                close_index = current_line.find("*/")
                if close_index == -1:
                    subfix = ''
                    label = 0
                else:
                    subfix = current_line[close_index + 2:]
                current_line = prefix + subfix
                print current_line
            else:
                if one_index > 0:
                    rtype.append(current_line[0: one_index])
                current_line = ''
            
        if current_line != '':
            rtype.append(current_line)
        
        return rtype





                
