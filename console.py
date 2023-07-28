from crud_notes import notes_worker
def printManual():
    print("""Type 1 for read all notes
Type 2 for read 1 note
Type 3 for write note
Type 4 for update note
Type 5 for delete note
Type 'exit' for exit program""")

def userTalk(num_command: str) -> None:
    worker = notes_worker()
    match num_command:
        # read all
        case "1":
            worker.readAll()
        # read one note
        case "2":
            worker.readNote(int(input("Select note for read: ")))
        # write row
        case "3":
            worker.addNote(input("Write your note: "))
        # update note
        case "4":
            num_note = int(input("Select updatable note: "))
            new_note = input("Write new data for note: ")
            worker.updateNote(num_note, new_note)
        # delete note
        case "5":
            worker.deleteNote(int(input("Select node for delete: ")))
    print("----------------------------------")
    printManual()
