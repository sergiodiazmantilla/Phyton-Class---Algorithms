from multiprocessing import Pool

def partial_sum(sub_list):
    return sum(sub_list)

if __name__ == '__name__':
    data = [i for i in range(1000000)]
    num_chunks = 4
    chunk_size = len(data) // num_chunks

    with Pool(num_chunks) as pool:
        result = pool.map(partial_sum, [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)])
    
    print("Suma total:", sum(result))