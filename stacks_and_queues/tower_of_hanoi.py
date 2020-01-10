class Tower:
    def __init__(self, index):
        self.disks = list()
        self.index = index

    def add(self, disk):
        if self.disks and self.disks[-1] <= disk:
            print('Cant add !!')
        else:
            self.disks.append(disk)

    def move_top_to(self, tower):
        top = self.disks.pop()
        tower.add(top)
        print(f'Moved disk {top} from {self.index} to {tower.index}')

    def move_disks(self, number_of_disks, destination, buffer):
        if number_of_disks > 0:
            self.move_disks(number_of_disks-1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(number_of_disks - 1, destination, self)


if __name__ == '__main__':
    towers = [Tower(i) for i in range(3)]
    for i in range(5, 0, -1):
        towers[0].add(i)
    towers[0].move_disks(5, towers[2], towers[1])
    print(towers[2].disks)
