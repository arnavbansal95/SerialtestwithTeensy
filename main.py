import comm

if __name__ == "__main__":
    CommObj = comm.CommModule()
    CommObj.setUp()
    CommObj.write(b"Hello World!")
    print(CommObj.read())
    CommObj.tearDown()