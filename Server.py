import socket
import threading
import dframe as df
from threading import Thread
from dframe import *

lock = threading.Lock()


def client_thread(connection):
    try:
        data = connection.recv(1024).decode().strip()  # Step 1
        log = data.split(' ')

        # Ensure the data is valid
        if len(log) != 2 or not log[0].isdigit():
            print(f"[ERROR] Invalid login format received: '{data}'")
            connection.send("InvalidVoter".encode())
            connection.close()
            return

        log[0] = int(log[0])  # Now safe to convert

        if df.verify(log[0], log[1]):
            if df.isEligible(log[0]):
                print('Voter Logged in... ID:' + str(log[0]))
                print(f"[LOGIN RECEIVED] {log}")
                print(f"[VERIFY] {df.verify(log[0], log[1])}, [Eligible] {df.isEligible(log[0])}")
                connection.send("Authenticate".encode())  # Step 2: tell client login success
            else:
                print('Vote Already Cast by ID:' + str(log[0]))
                connection.send("VoteCasted".encode())  # Step 2: inform already voted
                connection.close()
                return
        else:
            print('Invalid Voter')
            connection.send("InvalidVoter".encode())  # Step 2: inform invalid
            connection.close()
            return

        # --- Wait for client to vote only AFTER successful login ---
        data = connection.recv(1024)  # Step 3: client sends vote ONLY after pressing button
        print("Vote Received from ID: " + str(log[0]) + "  Processing...")

        lock.acquire()
        if df.vote_update(data.decode(), log[0]):
            print("Vote Casted Successfully by voter ID = " + str(log[0]))
            connection.send("Successful".encode())
        else:
            print("Vote Update Failed by voter ID = " + str(log[0]))
            connection.send("Vote Update Failed".encode())
        lock.release()
        connection.close()

    except Exception as e:
        print(f"[ERROR] {e}")
        connection.send("Server Error".encode())
        connection.close()



def voting_Server():

    serversocket = socket.socket()
    host = "127.0.0.1"
    port = 4001

    ThreadCount = 0

    try :
        serversocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    print("Waiting for the connection")

    serversocket.listen(10)

    print( "Listening on " + str(host) + ":" + str(port))

    while True :
        client, address = serversocket.accept()

        print('Connected to :', address)

        t = Thread(target = client_thread,args = (client,))
        t.start()
        ThreadCount+=1
        # break

    serversocket.close()

if __name__ == '__main__':
    voting_Server()
