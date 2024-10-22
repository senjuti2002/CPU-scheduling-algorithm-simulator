import tkinter as tk
from tkinter import ttk, messagebox

class CPUSchedulingAlgorithms:
    @staticmethod
    def fcfs(processes):
        current_time = 0
        waiting_times = []
        turnaround_times = []
        result = []

        for pid, arrival, burst, priority in sorted(processes, key=lambda x: x[1]):
            if current_time < arrival:
                current_time = arrival
            start_time = current_time
            finish_time = start_time + burst
            turnaround_time = finish_time - arrival
            waiting_time = start_time - arrival

            waiting_times.append(waiting_time)
            turnaround_times.append(turnaround_time)
            result.append((pid, start_time, turnaround_time, waiting_time))

            current_time += burst

        avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
        avg_waiting_time = sum(waiting_times) / len(waiting_times)

        return result, avg_turnaround_time, avg_waiting_time

    @staticmethod
    def sjf(processes):
        processes_sorted = sorted(processes, key=lambda x: (x[1], x[2]))  
        current_time = 0
        waiting_times = []
        turnaround_times = []
        result = []

        while processes_sorted:
            available_processes = [p for p in processes_sorted if p[1] <= current_time]
            if available_processes:
                pid, arrival, burst, priority = min(available_processes, key=lambda x: x[2])
                processes_sorted.remove((pid, arrival, burst, priority))
                start_time = current_time
                finish_time = start_time + burst
                turnaround_time = finish_time - arrival
                waiting_time = start_time - arrival

                waiting_times.append(waiting_time)
                turnaround_times.append(turnaround_time)
                result.append((pid, start_time, turnaround_time, waiting_time))

                current_time += burst
            else:
                current_time += 1 

        avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
        avg_waiting_time = sum(waiting_times) / len(waiting_times)

        return result, avg_turnaround_time, avg_waiting_time

    @staticmethod
    def sjf_preemptive(processes):
        n = len(processes)
        remaining_time = [process[2] for process in processes] 
        complete = 0
        current_time = 0
        min_burst_time = float('inf')
        shortest = -1
        check = False
        waiting_time = [0] * n
        turnaround_time = [0] * n
        finish_time = [0] * n
        start_time = [-1] * n
        arrival_times = [process[1] for process in processes]  
        burst_times = [process[2] for process in processes]

    
        while complete != n:
           min_burst_time = float('inf')  
           for j in range(n):
            if (processes[j][1] <= current_time and remaining_time[j] < min_burst_time and remaining_time[j] > 0):
                min_burst_time = remaining_time[j]
                shortest = j
                check = True

           if not check:  
            current_time += 1
            continue

      
           if start_time[shortest] == -1:
            start_time[shortest] = current_time

        
           remaining_time[shortest] -= 1

        
           if remaining_time[shortest] == 0:
            complete += 1
            check = False
            finish_time[shortest] = current_time + 1

            
            turnaround_time[shortest] = finish_time[shortest] - arrival_times[shortest]
            waiting_time[shortest] = turnaround_time[shortest] - burst_times[shortest]

            
            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0

        
           current_time += 1

    
        avg_turnaround_time = sum(turnaround_time) / n
        avg_waiting_time = sum(waiting_time) / n

    
        result = []
        for i in range(n):
          result.append((processes[i][0], start_time[i], turnaround_time[i], waiting_time[i]))

        return result, avg_turnaround_time, avg_waiting_time

    @staticmethod
    def priority_scheduling(processes):
        
        processes_sorted = sorted(processes, key=lambda x: (x[3], x[1]))

        current_time = 0
        waiting_times = []
        turnaround_times = []
        result = []

        for pid, arrival, burst, priority in processes_sorted:
            if current_time < arrival:
                current_time = arrival
            start_time = current_time
            finish_time = start_time + burst
            turnaround_time = finish_time - arrival
            waiting_time = start_time - arrival

            waiting_times.append(waiting_time)
            turnaround_times.append(turnaround_time)
            result.append((pid, start_time, turnaround_time, waiting_time))

            current_time += burst

        avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
        avg_waiting_time = sum(waiting_times) / len(waiting_times)

        return result, avg_turnaround_time, avg_waiting_time
    
    @staticmethod
    def priority_preemptive(processes):
        n = len(processes)
        remaining_time = [process[2] for process in processes]  
        complete = 0
        current_time = 0
        min_priority = float('inf')
        highest_priority_index = -1
        check = False
        waiting_time = [0] * n
        turnaround_time = [0] * n
        finish_time = [0] * n
        start_time = [-1] * n
        arrival_times = [process[1] for process in processes] 
        burst_times = [process[2] for process in processes]  
        priorities = [process[3] for process in processes]   

        
        while complete != n:
            min_priority = float('inf')  
            for j in range(n):
                
                if (processes[j][1] <= current_time and priorities[j] < min_priority and remaining_time[j] > 0):
                    min_priority = priorities[j]
                    highest_priority_index = j
                    check = True

            if not check:  
                current_time += 1
                continue

          
            if start_time[highest_priority_index] == -1:
                start_time[highest_priority_index] = current_time

            
            remaining_time[highest_priority_index] -= 1

  
            if remaining_time[highest_priority_index] == 0:
                complete += 1
                check = False
                finish_time[highest_priority_index] = current_time + 1

        
                turnaround_time[highest_priority_index] = finish_time[highest_priority_index] - arrival_times[highest_priority_index]
                waiting_time[highest_priority_index] = turnaround_time[highest_priority_index] - burst_times[highest_priority_index]

                
                if waiting_time[highest_priority_index] < 0:
                    waiting_time[highest_priority_index] = 0

            
            current_time += 1

        
        avg_turnaround_time = sum(turnaround_time) / n
        avg_waiting_time = sum(waiting_time) / n

        
        result = []
        for i in range(n):
            result.append((processes[i][0], start_time[i], turnaround_time[i], waiting_time[i]))

        return result, avg_turnaround_time, avg_waiting_time

    
    
    
    
    @staticmethod
    def round_robin(processes, quantum):
        n = len(processes)
        burst_times = {p[0]: p[2] for p in processes}  
        remaining_time = {p[0]: p[2] for p in processes}  
        waiting_time = {p[0]: 0 for p in processes}
        turnaround_time = {p[0]: 0 for p in processes}
        start_time = {}
        completion_time = {}
        
        current_time = 0
        queue = []  # Queue of processes
        mark = {p[0]: False for p in processes}  
        processes_sorted = sorted(processes, key=lambda x: x[1])  

        queue.append(processes_sorted[0])
        mark[processes_sorted[0][0]] = True

        completed = 0

        while completed != n:
            if queue:
                pid, arrival, burst, priority = queue.pop(0)

            
                if pid not in start_time:
                    start_time[pid] = max(current_time, arrival)
                    current_time = start_time[pid]

                
                if remaining_time[pid] > quantum:
                    remaining_time[pid] -= quantum
                    current_time += quantum
                else:
                    current_time += remaining_time[pid]
                    remaining_time[pid] = 0
                    completion_time[pid] = current_time

                
                    turnaround_time[pid] = completion_time[pid] - arrival
                    waiting_time[pid] = turnaround_time[pid] - burst
                    completed += 1

                
                for process in processes_sorted:
                    process_pid, process_arrival, _, _ = process
                    if process_pid != pid and process_arrival <= current_time and not mark[process_pid]:
                        queue.append(process)
                        mark[process_pid] = True

                
                if remaining_time[pid] > 0:
                    queue.append((pid, arrival, burst, priority))
            else:
                current_time += 1  

        
        avg_turnaround_time = sum(turnaround_time.values()) / n
        avg_waiting_time = sum(waiting_time.values()) / n

        
        result = [(pid, start_time[pid], turnaround_time[pid], waiting_time[pid]) for pid in start_time]
        return result, avg_turnaround_time, avg_waiting_time


class CPUSchedulerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CPU Scheduling Simulator")
        self.geometry("700x500")

        
        self.process_table = ttk.Treeview(self, columns=("Process ID", "Arrival Time", "Burst Time", "Priority"), show='headings')
        self.process_table.heading("Process ID", text="Process ID")
        self.process_table.heading("Arrival Time", text="Arrival Time")
        self.process_table.heading("Burst Time", text="Burst Time")
        self.process_table.heading("Priority", text="Priority")
        self.process_table.pack(side=tk.TOP, fill=tk.X)

      
        self.process_table.bind("<ButtonRelease-1>", self.on_process_select)

        
        input_frame = tk.Frame(self)
        input_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        tk.Label(input_frame, text="Process ID:").grid(row=0, column=0)
        self.pid_entry = tk.Entry(input_frame)
        self.pid_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Arrival Time:").grid(row=1, column=0)
        self.arrival_entry = tk.Entry(input_frame)
        self.arrival_entry.grid(row=1, column=1)

        tk.Label(input_frame, text="Burst Time:").grid(row=2, column=0)
        self.burst_entry = tk.Entry(input_frame)
        self.burst_entry.grid(row=2, column=1)

        tk.Label(input_frame, text="Priority:").grid(row=3, column=0)
        self.priority_entry = tk.Entry(input_frame)
        self.priority_entry.grid(row=3, column=1)

        
        btn_frame = tk.Frame(self)
        btn_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.add_btn = tk.Button(btn_frame, text="Add Process", command=self.add_process)
        self.add_btn.grid(row=0, column=0)

        self.edit_btn = tk.Button(btn_frame, text="Edit Process", command=self.edit_process)
        self.edit_btn.grid(row=0, column=1)

        self.delete_btn = tk.Button(btn_frame, text="Delete Process", command=self.delete_process)
        self.delete_btn.grid(row=0, column=2)

        self.run_btn = tk.Button(btn_frame, text="Run Algorithm", command=self.run_algorithm)
        self.run_btn.grid(row=0, column=3)

        
        self.algo_label = tk.Label(self, text="Select Algorithm:")
        self.algo_label.pack(side=tk.TOP)

        self.algo_combobox = ttk.Combobox(self, values=["FCFS", "SJF Non-Preemptive", "SJF Preemptive", "Priority", "Preemptive Priority", "Round Robin"])

        self.algo_combobox.pack(side=tk.TOP)

        
        self.quantum_label = tk.Label(self, text="Quantum (for Round Robin):")
        self.quantum_label.pack(side=tk.TOP)

        self.quantum_entry = tk.Entry(self)
        self.quantum_entry.pack(side=tk.TOP)

      
        self.processes = []
        self.selected_process = None

    def on_process_select(self, event):
        item = self.process_table.selection()[0]
        self.selected_process = self.process_table.item(item, "values")
        self.pid_entry.delete(0, tk.END)
        self.pid_entry.insert(tk.END, self.selected_process[0])
        self.arrival_entry.delete(0, tk.END)
        self.arrival_entry.insert(tk.END, self.selected_process[1])
        self.burst_entry.delete(0, tk.END)
        self.burst_entry.insert(tk.END, self.selected_process[2])
        self.priority_entry.delete(0, tk.END)
        self.priority_entry.insert(tk.END, self.selected_process[3])

    def add_process(self):
        pid = self.pid_entry.get()
        arrival = int(self.arrival_entry.get())
        burst = int(self.burst_entry.get())
        priority = int(self.priority_entry.get())

        self.processes.append((pid, arrival, burst, priority))
        self.process_table.insert('', 'end', values=(pid, arrival, burst, priority))
        self.clear_entries()

    def edit_process(self):
        if not self.selected_process:
            messagebox.showerror("Error", "No process selected!")
            return

        pid = self.selected_process[0]
        for i, p in enumerate(self.processes):
            if p[0] == pid:
                self.processes[i] = (pid, int(self.arrival_entry.get()), int(self.burst_entry.get()), int(self.priority_entry.get()))
                break

        selected_item = self.process_table.selection()[0]
        self.process_table.item(selected_item, values=(pid, self.arrival_entry.get(), self.burst_entry.get(), self.priority_entry.get()))
        self.clear_entries()

    def delete_process(self):
        if not self.selected_process:
            messagebox.showerror("Error", "No process selected!")
            return

        pid = self.selected_process[0]
        self.processes = [p for p in self.processes if p[0] != pid]
        selected_item = self.process_table.selection()[0]
        self.process_table.delete(selected_item)
        self.clear_entries()

    def clear_entries(self):
        self.pid_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.selected_process = None

    def run_algorithm(self):
        selected_algo = self.algo_combobox.get()

        if selected_algo == "FCFS":
            result, avg_turnaround_time, avg_waiting_time = CPUSchedulingAlgorithms.fcfs(self.processes)
        elif selected_algo == "SJF Non-Preemptive":
            result, avg_turnaround_time, avg_waiting_time = CPUSchedulingAlgorithms.sjf(self.processes)
        elif selected_algo == "SJF Preemptive":
            result, avg_turnaround_time, avg_waiting_time = CPUSchedulingAlgorithms.sjf_preemptive(self.processes)
        elif selected_algo == "Preemptive Priority":
            result, avg_turnaround_time, avg_waiting_time = CPUSchedulingAlgorithms.priority_preemptive(self.processes)

        
        elif selected_algo == "Priority":
            result, avg_turnaround_time, avg_waiting_time = CPUSchedulingAlgorithms.priority_scheduling(self.processes)
        elif selected_algo == "Round Robin":
            try:
                quantum = int(self.quantum_entry.get())
                result, avg_turnaround_time, avg_waiting_time = CPUSchedulingAlgorithms.round_robin(self.processes, quantum)
            except ValueError:
                messagebox.showerror("Error", "Invalid quantum value!")
                return
        else:
            messagebox.showerror("Error", "No algorithm selected!")
            return

        self.show_results(result, avg_turnaround_time, avg_waiting_time)

    def show_results(self, result, avg_turnaround_time, avg_waiting_time):
        result_window = tk.Toplevel(self)
        result_window.title("Results")
        result_window.geometry("500x300")

        result_table = ttk.Treeview(result_window, columns=("Process ID", "Start Time", "Turnaround Time", "Waiting Time"), show='headings')
        result_table.heading("Process ID", text="Process ID")
        result_table.heading("Start Time", text="Start Time")
        result_table.heading("Turnaround Time", text="Turnaround Time")
        result_table.heading("Waiting Time", text="Waiting Time")

        result_table.pack(fill=tk.BOTH, expand=True)

        for pid, start_time, turnaround_time, waiting_time in result:
            result_table.insert('', 'end', values=(pid, start_time, turnaround_time, waiting_time))

        avg_frame = tk.Frame(result_window)
        avg_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        tk.Label(avg_frame, text=f"Average Turnaround Time: {avg_turnaround_time:.2f}").pack(side=tk.LEFT, padx=10)
        tk.Label(avg_frame, text=f"Average Waiting Time: {avg_waiting_time:.2f}").pack(side=tk.LEFT, padx=10)

if __name__ == "__main__":
    app = CPUSchedulerApp()
    app.mainloop()
