import threading
import time
import logging
import random
import Banco

def cria_contas(num_contas):
    for i in range(num_contas):
        banco.contas.append(Banco.Conta(random.randint(1, num_contas), random.randrange(0, 500)))

def operacao_thread(id):
    operacao_escolhida = random.choice(Banco.Banco.depositar(), Banco.Banco.sacar(), Banco.Banco.consultar_saldo())
    
    while True:
        semaphore.acquire()
        lock.acquire()
        logging.info("Thread %s pegou o lock e o semáforo", id)
        banco.depositar(Banco.contas[id], random.randrange(0, 100))
        logging.info("Thread %s depositou", id)
        lock.release()
        logging.info("Thread %s liberou o lock", id)
        semaphore.release()
        logging.info("Thread %s liberou o semáforo", id)
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

lock = threading.Lock()
semaphore = threading.Semaphore(5)
banco = Banco.Banco()
