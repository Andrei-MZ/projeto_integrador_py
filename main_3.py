

  InsertionSort(arr[])
      for j = 1 to arr.length
         key = arr[j]
         i = j - 1
         while i >= 0 and arr[i] > key
            arr[i+1] = arr[i]
            i = i - 1
         arr[i+1] = key