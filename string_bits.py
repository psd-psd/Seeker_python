# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'

def string_bits(str):
        i=-1
        x=''
        for ch in str:
            i+=1
            if i%2==0:
                x=ch+x
        return x[::-1]
