import threading
import time
import logging
import random
import Banco

## Inicializando lock, semaforo e criando um banco numa variável chamada banco ##
lock = threading.Lock()
semaphore = threading.Semaphore(5)
banco = Banco.Banco()

## Criando o número de contas, utilizando uma função dentro do arquivo Banco ##
banco.cria_conta(6)

## Função onde as operações funcionam ##

## Aqui, com a biblioteca random, escolhemos umas das operações, que estão definidas dentro do arquivo Banco, e, após,
## selecionamos uma conta aleatória para essa operação ser executada.
## com isso, dentro de um match case, as operações serão executadas e os threads selecionados para entrar dentro de 
## um lock (no caso da operação depositar e sacar), ou dentro de um semáforo (no caso da operação consultar).
##no caso da operação depoistar e sacar, ele depositará ou sacará um valor aleatório dentro de 1 e 100 da conta.
def operacao_thread(id):
    while True:
        operacao_escolhida = random.choice(['depositar', 'sacar', 'consultar'])
        conta_aleatoria = random.choice(banco.chaves)
        match (operacao_escolhida):
            case 'depositar':
                lock.acquire()
                logging.info("Thread %d: depositando", id)
                banco.depositar(conta_aleatoria, random.randint(1, 100))
                logging.info("Thread %d: depositou", id)
                lock.release()
                time.sleep(1)
            case 'sacar':
                lock.acquire()
                logging.info("Thread %d: sacando", id)
                banco.sacar(conta_aleatoria, random.randint(1, 100))
                logging.info("Thread %d: sacou", id)
                lock.release()
                time.sleep(1)
            case 'consultar':
                semaphore.acquire()
                logging.info("Thread %d: consultando", id)
                print("Thread %d: saldo: %d" % (id, banco.consultar_saldo(conta_aleatoria)))
                semaphore.release()
                logging.info("Thread %d: consultou", id)
                time.sleep(1)

if __name__ == "__main__":
    threads = []
    
    ## formatação para o logging
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    ## threads inicializadas
    for id in range(5):
        t = threading.Thread(target=operacao_thread, args=(id,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    
