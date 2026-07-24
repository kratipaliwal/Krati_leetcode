from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequencies = Counter(tasks)

        max_frequency = max(frequencies.values())
        max_frequency_count = sum(
            frequency == max_frequency
            for frequency in frequencies.values()
        )

        required_cycles = (
            (max_frequency - 1) * (n + 1)
            + max_frequency_count
        )

        return max(len(tasks), required_cycles)