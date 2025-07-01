class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        # reverse_list = list()
        # for i in range(len(s_list)-1, -1, -1):
        #     reverse_list.append(s_list[i])
        # can be directly replaced with:
        reverse_list = s_list[::-1]
        return " ".join(reverse_list)