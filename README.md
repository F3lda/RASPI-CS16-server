# RASPI-CS16-server
Run Counter-Strike 1.6 server on Raspberry Pi

## Installation
1. Install **Pi-Apps** on Raspberry Pi
2. From Pi-Apps install **Box86** and **Wine**
3. Move Windows version of Counter-Strike 1.6 to the Raspberry Pi
4. Copy files from this repository to the folder with file `hlds.exe`

## Run
- run `./start_game.sh` to start the game
- run `./start_server.sh` to start the server
- run `./start_server.sh` to start the server
- run `./start_server_py_background.sh` to start the server on background
-- to stop the server send `exit` command over RCON or kill its main process

## Notes
- PHP RCON for CS 1.6: [https://github.com/F3lda/PHP-CS16-RCON](https://github.com/F3lda/PHP-CS16-RCON)
- `netstat --listen`
-  `ps -eF`
- I was unsuccessful to run the Linux version of Counter-Strike 1.6 server on Raspberry Pi
