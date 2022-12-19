import PyIO
import PyPluMA

class CSVColumnsPlugin:
    def input(self, infile):
       self.parameters = PyIO.readParameters(infile)
       self.csvfile = open(PyPluMA.prefix()+"/"+self.parameters["csvfile"], 'r')
       self.columnfile = open(PyPluMA.prefix()+"/"+self.parameters["columnsfile"], 'r')
    def run(self):
       self.mycolumns = self.csvfile.readline().strip().split(',')
       self.keep = [0]
       for line in self.columnfile:
          self.keep.append(self.mycolumns.index(line.strip()))
    def output(self, myoutfile):
       outfile = open(myoutfile, 'w')
       for i in range(len(self.keep)):
           outfile.write(self.mycolumns[self.keep[i]])
           if (i == len(self.keep)-1):
               outfile.write("\n")
           else:
               outfile.write(",")
       for line in self.csvfile:
          myline = line.strip().split(',')
          for i in range(len(self.keep)):
           outfile.write(myline[self.keep[i]])
           if (i == len(self.keep)-1):
               outfile.write("\n")
           else:
               outfile.write(",")
            

