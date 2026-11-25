The Digital Detective

This is my submission for the Diwali Independent Learning Assignment called "The Digital Detective: Explore Your Computer, Build a Mini System Report".

The assignment had nine missions. In each one I explored one part of my Mac, wrote down what I saw, and committed the work. The missions go from setting up a GitHub repository, to Terminal practice, to the operating system, to how Python runs, to number systems, to Git branches, and finally to networks.

Mission index

Mission	Topic	Link
0	Repository and workspace setup	mission-00-setup
1	Computer fundamentals and IPOS	mission-01-computer-basics
2	Terminal and file management	mission-02-terminal
3	Operating system, processes and permissions	mission-03-operating-system
4	How programs run	mission-04-programs
5	Number systems, Python and text encoding	mission-05-numbers-data
6	Git, GitHub, branches and Pull Requests	mission-06-git-github
7	Computer networks	mission-07-networking
8	Final review and submission	mission-08-final-report
Folder layout

digital-detective-8019/
├── README.md
├── mission-00-setup/
├── mission-01-computer-basics/
├── mission-02-terminal/
├── mission-03-operating-system/
├── mission-04-programs/
│   ├── README.md
│   └── hello.py
├── mission-05-numbers-data/
│   ├── README.md
│   └── number_converter.py
├── mission-06-git-github/
├── mission-07-networking/
├── mission-08-final-report/
└── evidence/
Every mission folder has its own README. The evidence folder keeps short saved outputs so the observations in the READMEs can be checked. I removed my account name, device name and IP address from those files before saving them, so my account just shows as student.

What I learned

The biggest thing I learned is that most of what a computer does is a small number of simple steps repeated very fast. Input, processing, output and storage sounds like a school diagram, but I could point at each stage while typing.

I also stopped seeing the Terminal as a scary black window. Almost every command I used was just a verb, an optional flag and a target, and pwd was enough to find out why a command did nothing.

The part that surprised me most was that Python is not purely interpreted. It compiles the file to bytecode first, and I could see the .pyc file sitting in __pycache__. C gave me one 33 KB executable and no cache, which made the difference clear in a way that reading about it did not.

What the missions cover

How a computer takes input, processes it, produces output and stores results
Terminal commands for looking at and changing files, plus flags and pipes
The operating system, running processes, storage, paths and file permissions
How Python runs a program, and how compilers differ from interpreters
Binary, decimal and hexadecimal conversions, and how text is encoded
Git commits, branches and Pull Requests on GitHub
Local networks, DNS, routers, protocols and what happens when a page loads
Running the number converter

The converter is in mission-05-numbers-data. Run it from inside that folder:

cd mission-05-numbers-data
python3 number_converter.py
It asks for a decimal number and prints the binary and hexadecimal forms:

Enter a decimal number: 25
Decimal: 25
Binary: 0b11001
Hexadecimal: 0x33
About the commits

Each mission was finished, documented, committed and pushed on its own. The commit messages say which mission they belong to, so the history can be read one mission at a time instead of one big upload at the end.

Tools I used

Terminal (zsh shell)
Git and GitHub
Python 3
VS Code as the text editor
