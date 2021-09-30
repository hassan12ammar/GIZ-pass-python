

class Solution:

    @staticmethod
    def longest_palindromic(string_input: str) -> str:
        # make new string to store the palindromic in
        longest_palind = ""
        input_length = len(string_input)
        # loop on our input tow times first from 0-length
        # second loop from the length to first index
        for latter_index in range(input_length):
            for inverse_latter_index in range(input_length, latter_index, -1): # start, end, step
                # check the length to make sure we have the longest palindromic
                current_length = inverse_latter_index - latter_index
                if len(longest_palind) > current_length:
                    break
                else:
                    # check if the string we have is palindromic
                    current_string = string_input[latter_index:inverse_latter_index][::]
                    inverse_string = string_input[latter_index:inverse_latter_index][::-1]
                    if inverse_string == current_string:
                        longest_palind = string_input[latter_index:inverse_latter_index]
                        break
        # return the result we stored in the "longest_palind" string
        return longest_palind

# test the functio
print(Solution.longest_palindromic("babad"))                       # aba
print(Solution.longest_palindromic("aaasaippuakivikauppiasbbbb"))  # saippuakivikauppias
print(Solution.longest_palindromic("HHabacefec"))  # cefec
