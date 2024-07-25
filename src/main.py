import schedule
import time
from alerts import monitor_price, monitor_initial_price

def job():
    monitor_price()

# Configura el trabajo para que se ejecute cada 30 minutos
schedule.every(30).minutes.do(job)

if __name__ == "__main__":
    monitor_initial_price()  # Monitorear el precio inicial al iniciar
    while True:
        schedule.run_pending()
        time.sleep(1)

