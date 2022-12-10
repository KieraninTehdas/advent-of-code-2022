import sys


def find_first_packet_marker_index(datastream_buffer):
    packet_length = 4

    for idx in range(0, len(datastream_buffer)):
        end_idx = idx + packet_length

        if len(set(datastream_buffer[idx:end_idx])) == packet_length:
            return end_idx


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        buffer = f.read()
        print(find_first_packet_marker_index(buffer))
