def add_it_up_example():
    return "Happy Hacking!"

def create_buffer_with_total(buffer_contents):
    total_of_values = sum([int(row) for row in buffer_contents])
    total_rows = ['=================', 'Total: {}'.format(total_of_values)]
    new_buffer = buffer_contents + total_rows
    return new_buffer
