print("\n\n=====================\nCREATINY - IKA TESTER\n=====================\n")

while True:
    print("1-Solo Image Test\n2-Multi Image Test\n3-RealTime Test\nq-Exit\n\n")

    opt = input("-> ")
    if opt == "1":
        with open("src/yolo_soloimage.py", encoding="utf-8") as f:
            exec(f.read())
    elif opt == "2":
        with open("src/yolo_multiimage.py", encoding="utf-8") as f:
            exec(f.read())
    elif opt == "3":
        with open("src/yolo_realtime_test1.py", encoding="utf-8") as f:
            print("press 'q' to stop")
            exec(f.read())
    elif opt == "q":
        exit()

    print("\n\n")

