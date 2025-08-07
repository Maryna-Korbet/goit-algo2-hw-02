# Task 1: 3D Printer Queue Optimization

This project implements a greedy algorithm to optimize the queue of 3D printing jobs in a university laboratory setting. The goal is to manage the print jobs efficiently based on their priorities and the technical constraints of the 3D printer.


## Problem Description

You are given a list of 3D print jobs, each with the following attributes:

- **ID**: Unique identifier of the print job.
- **Volume**: The volume of the model in cubic centimeters.
- **Priority**: The priority of the job, where:
  - 1 = Highest priority (e.g., theses)
  - 2 = Medium priority (e.g., laboratory works)
  - 3 = Lowest priority (e.g., personal projects)
- **Print time**: Estimated printing time in minutes.

The 3D printer has constraints:

- Maximum total volume printable in one batch.
- Maximum number of models printable simultaneously.


## Objective

Develop a function `optimize_printing` that:

- Processes print jobs respecting their priorities (higher priority jobs are printed first).
- Groups models for simultaneous printing without exceeding volume or item count limits.
- Calculates the total printing time, where the print time for a batch equals the maximum print time among grouped jobs.
- Returns the optimal print order and the total time required to complete all jobs.


## Technologies Used

- Python 3.8+
- `dataclasses` module for structured data representation
- Type hinting for better code clarity


## How It Works

1. Input jobs are converted into `PrintJob` dataclass instances.
2. Jobs are sorted by priority (ascending) and then by ID.
3. Jobs are greedily grouped into batches such that:
   - The total volume of the batch does not exceed the printer's maximum volume.
   - The number of items in the batch does not exceed the printer's maximum items.
4. Each batch's printing time equals the longest print time among its jobs.
5. The total print time is the sum of all batch print times.
6. The function returns the concatenated list of job IDs in print order and the total print time.


## Usage

Run the `test_printing_optimization` function to see example outputs for different scenarios, including:

- Jobs with the same priority
- Jobs with different priorities
- Jobs exceeding the printer constraints

```bash
python optimize_printing.py

```
---