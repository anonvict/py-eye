'''
 Bahasa campuran 😸 (eng/id)
 Created by: anonvict 🐬✨ || Inspired by: (Dennis Hoelscher) FluxGarage/Roboeyes 💌

 ”idea like this? (Because I don't have OLED 0.96 😸)”
'''

import time,os,curses,random,threading
def main(stdscr):
    try:
        curses.use_default_colors()
        curses.curs_set(0)
        stdscr.nodelay(True)
        biru = 1
        curses.init_pair(biru, curses.COLOR_BLUE, -1)
    except curses.error as e:
        print(f"{e}")
        return
    def normal():
        return [
            "                    ",
            "                    ",
            "   █████  █████     ",
            "   █████  █████     ",
            "   █████  █████     "
        ]
    def kedipnormal():
        return [
            "                    ",
            "                    ",
            "                    ",
            "   █████  █████     ",
            "                    "
        ]
    def kiri():
        return [
            "                    ",
            "                    ",
            " █████  █████       ",
            " █████  █████       ",
            "                    "
        ]
    def kedipkiri():
        return [
            "                    ",
            "                    ",
            "                    ",
            " █████  █████       ",
            "                    "
        ]
    def kanan():
        return [
            "                    ",
            "                    ",
            "                    ",
            "     █████  █████   ",
            "     █████  █████   "
        ]
    def kedipkanan():
        return [
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "     █████  █████   "
        ]
    def heran1():
        return [
            "                    ",
            "                    ",
            "  █████            ",
            "  █████  █████     ",
            "                    "
        ]
    def heran2():
        return [
            "                    ",
            "                    ",
            "         █████      ",
            "  █████  █████      ",
            "                    "
        ]
    def tidur1():
        return [
            "                    ",
            "                    ",
            "               z    ",
            "  —————  —————      ",
            "                    "
        ]

    def tidur2():
        return [
            "                    ",
            "                    ",
            "               zZ   ",
            "  —————  —————      ",
            "                    "
        ]
    def tidur3():
        return [
            "                    ",
            "                    ",
            "               zZz  ",
            "  —————  —————      ",
            "                    "
        ]
    def malas():
        return [
            "                    ",
            "                    ",
            "   █████  █████     ",
            "                    ",
            "                    "
        ]
    def ukuran(ek):
        tinggi = len(ek)
        lebar = max(len(b) for b in ek)
        return tinggi, lebar
    def clear_area(tinggi, lebar):
        for i in range(tinggi):
            stdscr.addstr(i, 0, " " * lebar)
    def tampil(ek, warna):
        for i, baris in enumerate(ek):
            stdscr.addstr(i, 0, baris, curses.color_pair(warna))
    layar_kotor = False
    def clear_all():
        nonlocal layar_kotor
        stdscr.erase()
        layar_kotor = False

    ekspresi_list = [normal, kiri, kanan, heran1, heran2, malas];
    tidur_list = [tidur1, tidur2, tidur3]
    timeout_list = [30, 60, 120]
    timeout_index = 0
    last_activity = time.time()
    '''
    Feedback suara aku memakai play-audio (sesuaikan!)
    '''
    def play_sound():
        os.system(
            'play-audio "sound/robot-notif.wav" '
            '> /dev/null 2>&1 &'
        )
    def sleep_for(duration):
        end_time = time.time() + duration
        idx = 0
        while time.time() < end_time:
            ek = tidur_list[idx % len(tidur_list)]
            h, w = ukuran(normal())
            if layar_kotor:
                clear_all()
            else:
                clear_area(h, w)
            tampil(ek(), biru)
            stdscr.refresh()
            frame_end = time.time() + 1
            while time.time() < frame_end:
                if stdscr.getch() != curses.ERR:
                    return True
                time.sleep(0.1)
            idx += 1
        return False
    def sleep_infinite():
        idx = 0
        while True:
            ek = tidur_list[idx % len(tidur_list)]
            h, w = ukuran(normal())
            if layar_kotor:
                clear_all()
            else:
                clear_area(h, w)
            tampil(ek(), biru)
            stdscr.refresh()

            frame_end = time.time() + 1
            while time.time() < frame_end:
                if stdscr.getch() != curses.ERR:
                    return
                time.sleep(0.1)

            idx += 1

    try:
        while True:
            now = time.time()
            idle = now - last_activity
            thresh = timeout_list[timeout_index]
            if 0 <= timeout_index < len(timeout_list) - 1 and idle >= thresh:
                woke = sleep_for(thresh)
                h, w = ukuran(tidur3())
                if layar_kotor:
                    clear_all()
                else:
                    clear_area(h, w)
                threading.Thread(target=play_sound).start()
                tampil(normal(), biru)
                stdscr.refresh()
                time.sleep(1)
                if woke:
                    timeout_index = min(timeout_index + 1, len(timeout_list) - 1)
                else:
                    timeout_index = min(timeout_index + 1, len(timeout_list) - 1)
                last_activity = time.time()
            elif timeout_index == len(timeout_list) - 1 and idle >= thresh:
                sleep_infinite()
                h, w = ukuran(tidur3())
                if layar_kotor:
                    clear_all()
                else:
                    clear_area(h, w)
                threading.Thread(target=play_sound).start()
                tampil(normal(), biru)
                stdscr.refresh()
                time.sleep(1)
                timeout_index = 0
                last_activity = time.time()
            else:
                ek = random.choice(ekspresi_list)
                h, w = ukuran(normal())
                if layar_kotor:
                    clear_all()
                else:
                    clear_area(h, w)
                tampil(ek(), biru)
                stdscr.refresh()
                time.sleep(random.uniform(1, 3))
                do_blink = random.choice([True, False])
                if ek == kiri and do_blink:
                    clear_all() if layar_kotor else clear_area(h, w)
                    tampil(kedipkiri(), biru)
                    stdscr.refresh()
                    time.sleep(0.05)
                    clear_all() if layar_kotor else clear_area(h, w)
                    tampil(kiri(), biru)
                    stdscr.refresh()
                    time.sleep(random.uniform(1, 3))
                elif ek == kanan and do_blink:
                    clear_all() if layar_kotor else clear_area(h, w)
                    tampil(kedipkanan(), biru)
                    stdscr.refresh()
                    time.sleep(0.05)
                    clear_all() if layar_kotor else clear_area(h, w)
                    tampil(kanan(), biru)
                    stdscr.refresh()
                    time.sleep(random.uniform(1, 3))
                elif ek == normal and do_blink:
                    clear_all() if layar_kotor else clear_area(h, w)
                    tampil(kedipnormal(), biru)
                    stdscr.refresh()
                    time.sleep(0.05)
                    clear_all() if layar_kotor else clear_area(h, w)
                    tampil(normal(), biru)
                    stdscr.refresh()
                    time.sleep(random.uniform(1, 3))
            key = stdscr.getch()
            if key != curses.ERR:
                last_activity = time.time()
                timeout_index = 0
                if key == curses.KEY_CLEAR:
                    layar_kotor = True
                else:
                    h, w = ukuran(normal())
                    if layar_kotor:
                        clear_all()
                    else:
                        clear_area(h, w)
                    tampil(heran1(), biru)
                    stdscr.refresh()
                    threading.Thread(target=play_sound).start()
                    time.sleep(1)

    except KeyboardInterrupt:
        pass

curses.wrapper(main)
