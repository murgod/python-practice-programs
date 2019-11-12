def lexSmallest(a, n):
  
    # Sort strings using above compare()
    a.sort(reverse = True)

    # Concatenating sorted strings
    answer = ""
    for i in range( n):
        answer += a[i]

    return answer

# Driver code
if __name__ == "__main__":

    a = [ "super", "tower" ]
    n = len(a)
    print(lexSmallest(a, n))
