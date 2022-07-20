import threading
import time
import logging
import random
import Banco

lock = threading.Lock()
semaphore = threading.Semaphore(5)
banco = Banco.Banco()

banco.cria_conta(6)

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

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    for id in range(5):
        t = threading.Thread(target=operacao_thread, args=(id,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    