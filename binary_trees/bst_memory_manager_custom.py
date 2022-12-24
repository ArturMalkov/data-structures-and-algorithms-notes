def init_memory(max_size):
    memory = []
    for i in range(max_size):
        memory.append([0, i + 1, 0])  # key, left node, right node
    return [memory, 0]  # memory structure and pointer to the first available memory segment


def new_node(memory_structure):  # memory allocation
    memory, first_free = memory_structure
    memory_structure[1] = memory[first_free][1]
    return first_free


def delete_node(memory_structure, index):
    memory, first_free = memory_structure
    memory[index][1] = first_free
    memory_structure[1] = index
