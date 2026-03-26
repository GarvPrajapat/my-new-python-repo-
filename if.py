def main()->None:
    age=int(input("Enter your age:"))

    if age>50:
        print("you are 50+ year old.")
        print("you are a seiner citzien")
    elif age>=18:
        print("you are 18+")
    else:
        print("you are 18-")


if __name__ == "__main__": 
    main()