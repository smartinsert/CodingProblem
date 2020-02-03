"""
Given a remote having 0-9 digits, plus button (to increase channel), minus (to decrease) and previous channel button
(to go to the previous channel). We were given 2 numbers stating the start and end channel number and an array having
various channel numbers. The task was to go to all channel numbers given in array with a minimum number of clicks.
"""
from typing import List, Tuple
import math


class Channel:
    def __init__(self, number, visited=False):
        self.number = number
        self.visited = visited

    def __eq__(self, other):
        return self.number == other.number

    def channel_difference(self, other):
        return abs(self.number - other.number)

    def __str__(self):
        return f'{self.number}'


class ViewChannels:
    def __init__(self, channel_list: List[int], start_channel: int, end_channel: int):
        self.channel_list = channel_list
        self.start_channel = Channel(start_channel)
        self.end_channel = Channel(end_channel)
        self.channels = self.__map_to_channel()
        self.channels.sort(key=lambda channel: channel.number)  # O(NLogN)
        self.previous_channel = None
        self.total_clicks = 0

    @property
    def get_total_clicks(self):
        return self.total_clicks

    def __map_to_channel(self):
        return [Channel(number=channel) for channel in self.channel_list
                if channel != self.start_channel.number and channel != self.end_channel.number]

    def find_the_closest_channel(self, target: Channel) -> Tuple[Channel, int]:
        low, high = 0, len(self.channels) - 1
        closest_number = None
        closest_index = None
        min_diff = math.inf
        if not self.channels:
            return Channel(-1), len(self.channels) + 1
        if len(self.channels) == 1:
            return self.channels[0].number
        while low <= high:
            mid = (low + high) // 2
            if mid + 1 < len(self.channels):
                min_diff_right = abs(self.channels[mid + 1].number - target.number)
                if min_diff_right < min_diff:
                    min_diff = min_diff_right
                    closest_number = self.channels[mid + 1]
                    closest_index = mid + 1
            if mid > 0:
                min_diff_left = abs(self.channels[mid - 1].number - target.number)
                if min_diff_left < min_diff:
                    min_diff = min_diff_left
                    closest_number = self.channels[mid - 1]
                    closest_index = mid - 1
            if self.channels[mid].number < target.number:
                low = mid + 1
            elif self.channels[mid].number > target.number:
                high = mid - 1
            else:
                return self.channels[mid], mid
        return closest_number, closest_index

    def minimum_number_of_clicks_to_go_from(self, source_channel: Channel, destination_channel: Channel) -> int:
        if destination_channel == source_channel:
            return 0
        elif self.previous_channel and destination_channel == self.previous_channel:
            return 1
        elif destination_channel != source_channel:
            return min(source_channel.channel_difference(destination_channel),
                       len(str(destination_channel.number)))

    def surf_channels(self):
        current_channel = self.start_channel
        self.total_clicks += len(str(current_channel.number))
        current_channel.visited = True
        while len(self.channels) > 1:
            closest_channel, channel_index = self.find_the_closest_channel(current_channel)
            self.total_clicks += self.minimum_number_of_clicks_to_go_from(current_channel, closest_channel)
            closest_channel.visited = True
            current_channel = closest_channel
            self.previous_channel = current_channel
            self.channels.pop(channel_index)
        self.total_clicks += self.minimum_number_of_clicks_to_go_from(current_channel, self.end_channel)


if __name__ == '__main__':
    view_channels = ViewChannels(channel_list=[2, 4, 600, 60, 100, 10, 50, 10, 50], start_channel=60, end_channel=100)
    view_channels.surf_channels()
    print(f'Minimum clicks needed is {view_channels.get_total_clicks}')
