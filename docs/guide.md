# User guide

To run the most up to date version of this program. Clone the git repository and
run the run.sh script.  
```
./run.sh
```
If you don't want to generate the pruning tables set the environment variable
`NO_TABLES` to any value.  
For example:
```
NO_TABLES=1 ./run.sh
```

### Run a binary (not updated)
The latest x86_64 executable binaries for macOS and Linux can be found in the 
[releases](https://github.com/Valokoodari/CubeSolver/releases) tab of this 
repository.  

The binary can be executed from the command line with ```./cubesolver-mac``` on macOS and ```./cubesolver-linux``` on Linux.  


## Requirements
- Linux or macOS (Should also work on Windows with WSL)  
- Python 3.8.2 or newer (Tested with 3.8.2 on macOS and 3.9.5 on Arch Linux and Cubbli 18)  

---

## Cubbli without sudo access
The python version installed on Cubbli 18 (used on Melkki for example) is Python
3.6.9 which doesn't work properly (or at all) with this project.  
Fortunately you can install Python 3.9.5 for yourself even without sudo.
```
$ wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tar.xz
$ tar -xf Python-3.9.5.tar.xz
$ cd Python-3.9.5
$ ./configure --prefix=$HOME/.local
$ make
$ make install
```
Now you need to add the Python 3.9.5 to your path with the following command  
`export PATH="$HOME/.local/bin:$PATH"`  
You may also add the command to the end of your `~/.profile` (or similar file) 
to use the custom Python version as the default one.  
