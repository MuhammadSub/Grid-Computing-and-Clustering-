# Grid-Computing-and-Clustering-
Grid Computing and Clustering: 
    It seems that you have written the methodology for a grid computing project, which aims to improve the efficiency of grid computing by automatically distributing tasks and aggregating results from multiple computers on a local network. The project's objectives include implementing a method to acquire a list of all computers on the local network, gather information about each computer's CPU and memory, execute tasks on worker computers, aggregate results, and return the aggregated results to the main computer for printing.
    
Methodology: The Step-by-Step Guide to Grid Computing:
  In grid computing, several computers are linked together and functions as a single entity to complete a
  job. When a job is sent to the grid, it is broken into smaller sub-tasks and transferred to a separate
  computer in the grid to be handled. The findings from each computer are then pooled to provide the task's
  outcome. Grid computing is what I do. Methodology for the Project Code:
    1. To acquire a list of all the computers on the local network, use the get_computers() method. It
    scans the network with the nmap library and returns a list of all accessible hosts.
    2. The main() function iterates through the list of computers and calls the get_info() function for each
    computer. This function returns a dictionary containing information about the CPU and memory of
    the computer. The information for each computer is added to a dictionary info, with the
    computer's name as the key.
    3. The main() function then prompts the user to enter numbers for the fibonacci(), add(), and
    quadratic() functions, and stores the user's input in variables fb_nb, add_1, add_2, quad_1,
    quad_2, and quad_3 respectively.
    4. As inputs, the run_tasks() function is called using the fibonacci() function and the user-entered
    value for fb nb. This results in the creation of a pool of worker processes, the number of which is
    equal to the number of computers on the local network. The user-entered value is then sent to the
    fibonacci() method, which is subsequently executed on the worker processes. The function's
    output is returned and saved in the variable result.
    5. The run_tasks() function is called again, this time with the add() function and the user-entered
    values for add_1 and add_2 as arguments. The add() function is run on the worker processes and
    the result is returned and stored in the variable result.
    6. The quadratic() function and the user-entered values for quad_1, quad_2, and quad_3 are sent as
    arguments to the run_tasks() function a third time. The quadratic() function is called on the worker
    processes, and the result is returned and saved in the result variable.
    7. The output of the fibonacci(), add(), and quadratic() functions is printed.
    
The final step involves aggregating the results from each computer and returning the aggregated results to the main computer for printing. The code is developed in Python and tested to demonstrate its efficiency and effectiveness in grid computing.
