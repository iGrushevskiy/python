def shut_down(s):
    if len(s) != 0: 
        if  s.isalpha():
            if s=='yes' or s=='Yes' or first=='YES':
                return 'Shutting down...'
            else:
                if s=='no' or s=='No' or s=='NO':
                    return 'Shutdown aborted!'
                else:
                    return 'Sorry, I didn\'t understand you.'
        else:
            return 'Sorry, I didn\'t understand you.'
    else:
        return 'Sorry, I didn\'t understand you.'
