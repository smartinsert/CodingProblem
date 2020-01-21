group_of_two = [1, 1]
group_of_four = [1, 1, 1, 1]


class Seats:
    def __init__(self, number_of_rows):
        self.seat_configurations = [group_of_two, group_of_four, group_of_two] * number_of_rows

    def get_index_of(self, size):
        for idx, group in self.seat_configurations:
            if len(group) == size:
                return idx

    def assign(self, number_of_seats):
        if number_of_seats == 2:
            idx = self.get_index_of(2)
        elif number_of_seats == 3:
            idx = self.get_index_of(4)
        elif number_of_seats == 4:
            two_idx = self.get_index_of(2)
            four_idx = self.get_index_of(4)
            if sum(self.seat_configurations[two_idx]) == 2:
                idx = two_idx
            else:
                idx = four_idx
        group = self.seat_configurations.pop(idx)
        if sum(group) < number_of_seats:
            return -1
        current_idx = 0
        while number_of_seats > 0:
            if group[current_idx] == 1:
                group[current_idx] = 0
            current_idx += 1
            number_of_seats -= 1
        self.seat_configurations.append(group)


