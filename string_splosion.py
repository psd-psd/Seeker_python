# Given a non-empty string like "Code" return a string like "CCoCodCode".


# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
    x=''
    for i in range(0,len(str)+1):
        x=x+str[0:i]
    return x
