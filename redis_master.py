import numpy
from time import sleep
from redis import Redis
from rq import Queue
from redis_modules import calc_as_function
from redis_modules import create_matrix
from redis_modules import populate_matrix

LINES = 5

COLUNS = 5

matrixA = create_matrix(LINES, COLUNS)

matrixB = create_matrix(LINES, COLUNS)
print "A ="
print numpy.asmatrix(matrixA)
print "B ="
print numpy.asmatrix(matrixB)

matrixC = numpy.zeros(shape=(LINES, COLUNS))

if __name__ == "__main__":
  print "Initializing redis master"
  redis_conn = Redis(host='127.0.0.1',port=6379)
  queue_jobs = Queue('my_queue', connection=redis_conn)
  jobs = []
  for i in range(len(matrixA)):

    for j in range(len(matrixA[0])):
      line = []
      colun = []

      for k in range(len(matrixB)):
        line = line + [matrixA[i][k]]
        colun = colun + [matrixB[k][j]]

      job = queue_jobs.enqueue(calc_as_function, line, colun)
      jobs.append(job)
  results = []

  for job in jobs:
    while job.result is None:
      print "O trabalho {0} ainda nao foi concluido".format(job.id)
      sleep(2)
    results = results + [job.result]

print "C ="
print numpy.asmatrix(populate_matrix(LINES, COLUNS, results))
