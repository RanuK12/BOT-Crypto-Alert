import schedule
import time
from alerts import generate_alerts

def job():
    generate_alerts('bitcoin')

# Configura el trabajo para que se ejecute cada 10 minutos
schedule.every(10).minutes.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
