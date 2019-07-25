class Tools(object):
    def prefix_byte_count_to_hex_string(hex_str):
        length = len(hex_str)
        if length == 0:
            return '00'
        if length % 2 == 1:
            hex_str = '0' + hex_str
            length += 1
        byte_count = format(int(length / 2), 'x')
        if len(byte_count) % 2 == 1:
            byte_count = '0' + byte_count

        return byte_count + hex_str
