
# MISSION 3 - UNDERSTAND THE OPERATING SYSTEM

## Task 3.1 - Explore Your Operating System

### Commands Used

| Command | Purpose |
|---|---|
| sw_vers | Displays macOS version details |
| uname -s | Displays operating system kernel |
| whoami | Displays the current account name |
| df -h / | Displays available and used storage |
| top -l 1 -n 10 | Displays a snapshot of system activity |

### Observations

| Information Explored | What It Tells You | Privacy-Safe Observation |
|---|---|---|
| Operating system / system details | Identifies the operating system and version | macOS operating system |
| Current account identity | Identifies the currently active account | A local user account is active; identity redacted |
| Available and used storage | Shows disk space usage and available space | Checked using df -h / |
| System activity snapshot | Shows running processes and resource activity | Running processes were observed using Terminal |


---

## Task 3.2 - Understand Processes

### What is a process?

A process is a program or application that is currently
running on a computer. Each running process uses system
resources such as CPU time and memory.

### What does the PID column represent?

PID stands for Process Identifier. It is a unique
number assigned to each running process so that
the operating system can identify and manage it.

### Two examples of processes

1. Web browser process - Runs a web browser and
   handles browsing activities.
2. Terminal process - Runs commands entered by
   the user in the Terminal.

### Command Used

ps -Ao pid,comm | head -n 12

This command displays process identifiers and
their associated command names.

---

## Task 3.3 - Understand Paths and Permissions

### Absolute Path

An absolute path gives the complete location of a
file or directory starting from the root directory.

Example:
 /Users/[redacted]/Desktop/digital-detective-8033/

### Relative Path

A relative path specifies a location in relation
to the current working directory.

Example:
 mission-03-operating-system/README.md

### Commands Used

| Command | Purpose |
|---|---|
| pwd | Displays the current directory |
| cd | Changes the current directory |
| ls -l | Displays detailed file information and permissions |

### File Permissions

| Permission | Meaning | Example |
|---|---|---|
| r - Read | Allows reading file contents | Opening a text file |
| w - Write | Allows modifying a file | Editing a text file |
| x - Execute | Allows executing a file or accessing a directory | Running a script |

The detailed listing uses permission letters
to show what the file owner, group and others
are allowed to do.

No system permissions were changed.

---

## Task 3.4 - Operating System Responsibilities

| OS Responsibility | Explanation | Example |
|---|---|---|
| Process management | Manages running programs and allocates CPU time | Running a browser and Terminal together |
| Memory management | Allocates and manages RAM for applications | Giving memory to a browser |
| Device management | Controls connected hardware devices | Managing keyboard, mouse and printer |
| File management | Organises files and directories | Creating, saving and deleting files |
| User interface / shell | Allows users to interact with the computer | Using Terminal to enter commands |
| Security and permissions | Controls access to files and system resources | Allowing only authorised users to modify files |

---

## Conclusion

Through this mission, I learned about operating
systems and their responsibilities.

I explored system information, running processes,
storage, file paths and file permissions using
macOS Terminal commands.

I also understood how an operating system manages
memory, processes, hardware devices, files and
security to ensure that the computer works properly.

