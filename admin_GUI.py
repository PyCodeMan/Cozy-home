import multiprocessing
import tkinter as tk
from tkinter import ttk
from time import sleep


def create_gui(data_queue):
    root = tk.Tk()
    frame = ttk.Frame(root, padding=10)
    frame.grig()
    ttk.Label(frame, text='DEBUG TEST').grid(column=0, row=0)
    ttk.Button(frame, text='Quit', command=root.destroy).grid(column=1, row=0)

    def check_queue():
        if not data_queue.empty():
            data = data_queue.get()
            print(data)
        root.after(100, check_queue)
    
    check_queue()
    root.mainloop()


def server(requested_data, data_queue):
    while True:
        sleep(1)
        data = 'DEBUG_TEST'
        data_queue.put(data)


def create_process(target):
    process = multiprocessing.Process(target=target)
    process.start()
    return process


def main():

    data_queue = multiprocessing.Queue()
    manager = multiprocessing.Manager()
    shared_data = manager.dict()

    gui_process = create_process(lambda: create_gui(data_queue))
    server_process = create_process(lambda: server(None, data_queue, shared_data))

# I feel exhausted now, I will continue later...