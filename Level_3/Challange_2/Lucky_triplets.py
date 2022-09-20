def solution(l):

    trippels = 0
    x_y_pairs = [0 for _ in l]

    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                x_y_pairs[i] += 1
                trippels += x_y_pairs[j]
    return trippels


#print solution([1,2,3,4,5,6,7,8])


def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    print(nums1)

    if len(nums1) % 2:
        return nums1[len(nums1) // 2]
    else:
        print (nums1[len(nums1) / 2], nums1[(len(nums1) / 2) - 1]), ((nums1[len(nums1) / 2] + nums1[(len(nums1) / 2) - 1]))/2
        return (float(nums1[len(nums1) / 2]) + float(nums1[(len(nums1) / 2) - 1])) / 2

print findMedianSortedArrays([1,2,3,4],[5,6,7,8])

print (18/7)