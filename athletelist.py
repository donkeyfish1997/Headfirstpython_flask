def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            data = data.strip().split(',')
            return AthleteList(data.pop(0),data.pop(0),data)


    except IOError as err:
        print('file error', err)
        return 0


class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    @property
    def top3(self):
        return sorted(set([sanitize(tmp) for tmp in self]))[:3]
    @property
    def clean_data(self):
        return sorted(set([sanitize(tmp) for tmp in self]))

if __name__ == '__main__':
    pass