#! /usr/bin/env python3


class GetLogData():
    def __init__(self, orient):
        self.data = []
        self.filename = 'log.txt'
        self.orientation = orient

    def getData(self, length):
        self.data = []
        self.length = length
        with open(self.filename, 'r') as f:
            self.lines = f.readlines()
            if self.orientation == 'Start':
                self.reduced_lines = self.lines[:self.length]
            elif self.orientation == 'End':
                self.length = len(self.lines) - self.length
                self.reduced_lines = self.lines[self.length:]

            for x in self.reduced_lines:
                self.words = x.split()
                self.data.append(float(self.words[1]))

        return self.data

    def getLogLength(self):
        with open('log.txt', 'r') as f:
            self.lines = f.readlines()
            self.length = len(self.lines)
        return self.length
