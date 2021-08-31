# Cristian Aurelio Ramirez Anzaldo
# A01066337

# Heapify
def heapify(heap, n, i):
    largest = i  # Largest as root
    left = 2 * i + 1  # left => 2*i + 1
    right = 2 * i + 2  # right => 2*i + 2

    # Left child? && LC > Root
    if left < n and heap[i] < heap[left]:
        largest = left

    # Right child? && RC > Root
    if right < n and heap[largest] < heap[right]:
        largest = right

    # Change root if needed
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]  # swap

        # Heapify the root.
        heapify(heap, n, largest)


# Create and sort a heap
def heapSort(heap):

    # Building a maxheap.
    for i in range(int(len(heap) / 2) - 1, -1, -1):
        heapify(heap, len(heap), i) # Creates a max heap

    # Extracting elements one by one
    for i in range(len(heap) - 1, 0, -1):
        # swap
        aux = heap[0]
        heap[0] = heap[i]
        heap[i] = aux

        heapify(heap, i, 0)


heap = [4, 10, 3, 5, 1]
print("Original heap:")
print(heap)

heapSort(heap)

print("Sorted heap: ")

print(heap)
