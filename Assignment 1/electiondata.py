class ElectionResults:
  
  def __init__(self, filename):
    self.filename = filename

  def load(self):
    self.file = open(self.filename, 'r')
    self.file.readline()
    self.all_lines = self.file.readlines()

  def states(self):
    all_names = []
    for line in self.all_lines:
      columns = line.split(',')
      all_names.append(columns[1])
    return all_names

  def ObamaVotes(self):
    #self.file.readline()
    all_names = []
    for line in self.all_lines:
      columns = line.split(',')
      totalVotes = 0
      totalVotes += int(columns[3], base=10)
    return totalVotes

  def RoVotes(self):
    #self.file.readline()
    all_names = []
    for line in self.all_lines:
      columns = line.split(',')
      totalVotes = 0
      totalVotes += int(columns[5], base=10)
    return totalVotes
    
    


  def state_count(self):
    return len(self.all_lines)