## Executar nas maquinas
```
worker$ cd ~ && git clone https://github.com/fabiosammy/python_redis_multiprocess.git
worker$ sudo apt-get update
worker$ sudo apt-get install python-pip python-redis
worker$ sudo pip install rq
worker$ cd ~/python_redis_multiprocess/
```

#### Verifiquem se o redis esta rodando
```
master$ docker run --rm --network="host" -p 6379:6379 redis
```

#### Agora alterem o arquivo `redis_worker` para apontar o serviço redis da sua máquina (processo master)
```
worker$ python redis_worker.py
```

#### E por fim, rodem o processo master em sua máquina
```
master$ python redis_master.py
```
#### Resultado
```
A =
[[908   7 619 914 463]
 [338  89 816  53 157]
 [740 415 394  80 855]
 [938 394 449 542 948]
 [742 241 944 568 834]]
B =
[[692 814 220  53 834]
 [ 18 653 850 187 948]
 [167 428  86 940  41]
 [  5 774  86 500 997]
 [608 567  25 810 274]]
Initializing redis master
O trabalho 974ce48f-7e68-4566-aa8f-47bcfd208e97 ainda nao foi concluido
C =
[[1017909 1978572  349123 1463323 1827407]
 [ 467491  812538  228669  955267  495579]
 [1105588 1588692  577689 1219735 1340764]
 [1310265 2170010  650186 1584332 1974339]
 [1185362 2077903  518972 1931293 1680812]]

real	0m2,275s
user	0m0,335s
sys	0m0,193s


