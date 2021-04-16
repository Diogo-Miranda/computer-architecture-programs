def sort(array):
    n = len(array)
    i = 0
    array_tmp = [None] * (len(array) + 1)
    for i in range(len(array)):
        array_tmp[i+1] = array[i]
    
    array = array_tmp

    heap_length = 2
    while(heap_length <= n):
        build(heap_length, array)
        heap_length = heap_length + 1
       
    heap_length = n
    while(heap_length > 1):
        swap(1, heap_length, array)
        heap_length = heap_length - 1
        rebuild(heap_length, array)

    array_tmp = [None] * (len(array) - 1)

    for i in range(len(array_tmp)):
        array_tmp[i] = array[i+1]

    return array_tmp

def build(heap_length, array):
    i = heap_length
    index_child = int(i/2)
    while(i > 1 and array[i] > array[index_child]):
        swap(i, index_child, array)
        i = int(i / 2)
        index_child = int(i/2)

def rebuild(heap_length, array):
    i = 1
    while(i <= (heap_length/2)):
        child = get_greater_children(i, heap_length, array)
        if(array[i] < array[child]):
            swap(i, child, array)
            i = child
        else:
            i = heap_length    

def get_greater_children(i, heap_length, array):
    child = 1

    if(2*i == heap_length or array[2*i] > array[2*i+1]):
        child = 2*i
    else:
        child = 2*i + 1

    return child

def swap(i, j, array):
    print(f'ANTES DO SWAP = TROCANDO {i} por {j} array = {array}')
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    print(f'DEPOIS DO SWAP = TROCANDO {i} por {j} array = {array}')

array = [4,10,3,5,1]

array = sort(array)

print(array)