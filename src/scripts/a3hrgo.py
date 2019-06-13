from src.autofichaje.autofichaje import AutoFichaje
from datetime import datetime, timedelta
import time
from random import randint
import click


def login_and_mark_entrada(hold=False):
    print('Checking last action...')
    af = AutoFichaje()
    af.login()
    a, t = af.get_status()
    print(f'Last accion: {a}, {t}')
    if a != 'Entrada':
        print('Marking Entrada...')
        entrada = False
        while not entrada:
            af.mark()
            time.sleep(3)
            a, t = af.get_status()
            print(f'Current status: {a}, {t}')
            if a == 'Entrada':
                entrada = True
                print(f'Entrada marked successfully {a}, {t}')
    else:
        print(f'Last acction: {a}, {t}. Entrada already marked!')
    if not hold:
        af.driver.close()
    return t


def login_and_mark_salida(hold=False):
    print('Checking last action...')
    af = AutoFichaje()
    af.login()
    a, t = af.get_status()
    print(f'Last accion: {a}, {t}')
    if a != 'Salida':
        print('Marking Salida...')
        salida = False
        while not salida:
            af.mark()
            time.sleep(3)
            a, t = af.get_status()
            print(f'Current status: {a}, {t}')
            if a == 'Salida':
                salida = True
                print(f'Salida marked successfully {a}, {t}')
    else:
        print(f'Last acction: {a}, {t}. Salida already marked!')
    if not hold:
        af.driver.close()
    return t

@click.command()
@click.option('--hours', '-h', default=8, type=click.INT)
def main(hours):
    print(f'----- Mark {hours} hours -----')
    ent_time = login_and_mark_entrada()
    target_time = ent_time + timedelta(hours=hours, minutes=randint(1, 5), seconds=randint(0, 60))
    print(f'Setting exit time to {target_time}')

    now = datetime.now()
    diff = (target_time - now).seconds
    sleep_time = int(diff / 10)
    while now < target_time:
        print(f'{diff/60:05.1f}m away from marking exit - '
              f'{now.hour:02}:{now.minute:02}:{now.second:02} / {target_time.hour:02}:{target_time.minute:02}:{target_time.second:02}')
        time.sleep(sleep_time)
        now = datetime.now()
    else:
        ext_time = login_and_mark_salida()

    print('Work done today, see you tomorrow :)')



if __name__ == '__main__':
    main()
