# def shaker_sort(values):
#     if not values:
#         return
#     left = 0
#     right = len(values) - 1
#     while left <= right:
#         for i in range(right, left, -1):
#             if values[i - 1] > values[i]:
#                 values[i - 1], values[i] = values[i], values[i - 1]
#         left += 1
#         for i in range(left, right):
#             if values[i] > values[i + 1]:
#                 values[i], values[i + 1] = values[i + 1], values[i]
#         right -= 1


# if __name__ == "__main__":
#     values = [5, 2, 9, 11, 5, 6]
#     print("Before sorting:", values)
#     shaker_sort(values)
#     print("After sorting:", values)


# def merge_sort_impl(values, buffer, l, r):
#     if l < r:
#         m = (l + r) // 2
#         merge_sort_impl(values, buffer, l, m)
#         merge_sort_impl(values, buffer, m + 1, r)

#         k = l
#         i, j = l, m + 1
#         while i <= m or j <= r:
#             if j > r or (i <= m and values[i] < values[j]):
#                 buffer[k] = values[i]
#                 i += 1
#             else:
#                 buffer[k] = values[j]
#                 j += 1
#             k += 1

#         for i in range(l, r + 1):
#             values[i] = buffer[i]


# def merge_sort(values):
#     if values:
#         buffer = [0] * len(values)
#         merge_sort_impl(values, buffer, 0, len(values) - 1)

# # Пример использования функции
# if __name__ == "__main__":
#     values = [5, 2, 9, 1, 5, 6]
#     print("Before sorting:", values)
#     merge_sort(values)
#     print("After sorting:", values)

# def partition(values, l, r):
#     x = values[r]
#     less = l

#     for i in range(l, r):
#         if values[i] <= x:
#             values[i], values[less] = values[less], values[i]
#             less += 1

#     values[less], values[r] = values[r], values[less]     
#     return less

# def quick_sort_impl(values, l, r):
#     if l < r:
#         q = partition(values, l, r)
#         quick_sort_impl(values, l, q - 1)
#         quick_sort_impl(values, q + 1, r)

# def quick_sort(values):
#     if values:
#         quick_sort_impl(values, 0, len(values) - 1)

# # быстрая сортировка
# if __name__ == "__main__":
#     values = [5, 2, 9, 1,  6]
#     print("Before sorting:", values)
#     quick_sort(values)
#     print("After sorting:", values)

class Solution:
    def longestCommonPrefix(self,strs: list[str])->str:
        pref = strs[0]
        pref_len = len(pref)
        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ''
                pref = pref[0:pref_len]
            return preff
        
main = 'hello'