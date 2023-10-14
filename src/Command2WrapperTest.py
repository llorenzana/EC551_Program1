import os

from blif_to_tt import blif_file_to_tt_file

# Change the working directory to the directory where your script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    # Specify the directory path
    folder_path = "blif"

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

   # Print the list of files
    iter = 0
    print(f"Select a file to use:")
    for index, file in enumerate(files):
        print(f"{index + 1}: {file}")

    # Get and error check user choice (DOES NOT CHECK IF FILE IS BLIF)
    while True:
        choice = int(input("Enter your selection: "))

        #Error check user choice
        choice = choice - 1 #Set choice to python indexing

        if (choice >= 0 and choice < len(files)):
            break
        else:
            print("Please select a valid file.")

    # Get the truth table for the selected file
    filename = "blif/" + files[choice]
    outputFilename = files[choice] + ".text"
    blif_file_to_tt_file(filename, outputFilename)

    # PARSE the output file
    # Open a file in read mode ('r')
    with open(outputFilename, 'r') as file:
        for line in file:
            # if ()
            print(line, end='')

    #Clean up files
    # os.remove(outputFilename)

if __name__ == "__main__":
    main()

