def main():
    while(True):
        file_object=open('./data/data.txt', 'a+') #map this ./data folder location to 
        input_data=input('Enter data to be written into the file.\n')
        file_object.write(input_data +"\n")
        print()
        choice=input("Do you want to continue? (y/n)\n")
        if (choice.lower()=="n"):
            file_object.close()
            break
        elif(choice.lower()=="y"):
            continue
        else:
            print("You entered invalid choice. Program continued.")

if(__name__=='__main__'):
    main()