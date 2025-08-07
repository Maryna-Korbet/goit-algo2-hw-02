from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimizes the 3D printing job queue based on job priorities and printer constraints.

    Args:
        print_jobs (List[Dict]): List of print jobs, each containing:
            - id (str): Unique identifier of the job.
            - volume (float): Volume of the model in cm³ (> 0).
            - priority (int): Priority level (1 - highest, 2, or 3 - lowest).
            - print_time (int): Printing time in minutes (> 0).
        constraints (Dict): Printer constraints containing:
            - max_volume (float): Maximum total volume printable at once.
            - max_items (int): Maximum number of models printable at once.

    Returns:
        Dict: A dictionary with:
            - "print_order": List of job IDs in the optimized print order.
            - "total_time": Total printing time in minutes.
    """
    # Convert input dictionaries to dataclass instances
    jobs = [PrintJob(**job) for job in print_jobs]
    cons = PrinterConstraints(**constraints)
    
    # Sort jobs by priority ascending (1 = highest), then by id for stable order
    jobs.sort(key=lambda x: (x.priority, x.id))
    
    print_order = []
    total_time = 0
    
    i = 0
    n = len(jobs)
    
    # Greedily group jobs without exceeding constraints
    while i < n:
        current_volume = 0
        current_count = 0
        group = []
        max_print_time = 0
        
        # Формуємо групу жадібно
        while i < n:
            job = jobs[i]
            if (current_volume + job.volume <= cons.max_volume) and (current_count + 1 <= cons.max_items):
                group.append(job)
                current_volume += job.volume
                current_count += 1
                if job.print_time > max_print_time:
                    max_print_time = job.print_time
                i += 1
            else:
                # Current job doesn't fit, break to print current group
                break
        
        # Add job ids of current group to print order
        print_order.extend([job.id for job in group])
        # Add max print time of group to total time
        total_time += max_print_time
    
    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Тестування
def test_printing_optimization():
    """
    Runs predefined tests to verify the optimize_printing function.
    Prints the print order and total time for each test case.
    """
    # Test 1: Jobs with the same priority
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Test 2: Jobs with different priorities
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # laboratory works
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # theses
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}  # personal projects
    ]

    # Test 3: Jobs exceeding printer constraints
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1 (same priority):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Print order: {result1['print_order']}")
    print(f"Total time: {result1['total_time']}  minutes\n")

    print("\nТест 2 (different priorities):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Print order: {result2['print_order']}")
    print(f"Total time: {result2['total_time']}  minutes\n")

    print("\nТест 3 (exceeding constraints):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Print order: {result3['print_order']}")
    print(f"Total time: {result3['total_time']}  minutes\n")

if __name__ == "__main__":
    test_printing_optimization()
