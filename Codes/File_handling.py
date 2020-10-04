#!/usr/bin/python3

class txtfile:
    def __init__(self, input_file):
        self.input_file = input_file

    def read_data(self):
        r = open(self.input_file, 'r')
        return r.readline()

    def write_data(self, write_content):
        self.write_content = write_content
        w = open(self.input_file, 'w')
        w.write(self.write_content)
        w.close()

    def append(self, append_conent):
        self.append_conent = append_conent
        a = open(self.input_file, 'a+')
        a.writelines(self.append_conent)
        a.writelines("\n")
        a.close()


reading = txtfile('/tmp/1234')

#reading.write_data('Hi')
reading.append("Hello")
for i in reading.read_data():
    print(i)